from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import json
from datetime import date

from api.admin import validateAccessToken, sendVerificationEmail, getUserFromToken
from api.models import UserInfo, BookBasicInfo, Collections, BookContext, Bookmark

def notAnonymous(request):
    if len(request.headers.get('Authorization').split(' ')) > 1:
        accessToken = request.headers.get('Authorization').split(' ')[1]
        decodedToken = validateAccessToken(accessToken)
        if decodedToken:
            return True
        else:
            return False
    else:
        return False

def getUsername(request):
    return getUserFromToken(request.headers.get('Authorization').split(' ')[1]).username

def isVIP(request):
    dt = UserInfo.objects.get(userID=getUsername(request)).VIPDate
    if dt is not None:
        if dt < date.today():
            return False
        else:
            return True
    else:
        return False

def getBookInfo(request, bookid):
    res = BookBasicInfo.objects.filter(bookID=bookid, onShelf=True)
    if res.count() == 0:
        return JsonResponse({"message": "failed"}, status=400)
    else:
        book = res.first()
        favcnt = 0
        if notAnonymous(request):
            favcnt = Collections.objects.filter(bookID=bookid, userID=UserInfo.objects.get(userID=getUsername(request))).count()
        data = {
            'id': book.bookID,
            'title': book.name,
            'author': book.author,
            'category': book.category,
            'status': book.status,
            'brief': book.profile,
            'score': book.totScore / book.rateNumber if book.rateNumber > 0 else 0,
            'cnt': book.wordsCnt,
            'cover': book.img.url,
            'favorcnt': book.collections,
            'vip': book.isVIP,
            'fav': True if favcnt>0 else False,
        }
        return JsonResponse(data)

def getBookOutline(request, bookid):
    res = BookBasicInfo.objects.filter(bookID=bookid, onShelf=True)
    if res.count() == 0:
        return JsonResponse({"message": "failed"}, status=400)
    else:
        outline = list(BookContext.objects.filter(bookID=bookid).order_by('chapter').values_list('title'))
        return JsonResponse({"outline": outline})

def getBookContent(request, bookid, chapter):
    res = BookBasicInfo.objects.filter(bookID=bookid, onShelf=True)
    if res.count() == 0:
        return JsonResponse({"message": "failed"}, 400)
    else:
        book = res.first()
        content = BookContext.objects.filter(bookID=bookid, chapter=chapter)
        if content.count() == 0:
            return JsonResponse({"message": "failed"}, status=400)
        is_marked = False
        if notAnonymous(request):
            is_marked = Bookmark.objects.filter(bookID_id=bookid, chapter=chapter, userID=getUsername(request)).count() > 0
        if book.isVIP:
            if notAnonymous(request):
                if isVIP(request):
                    return JsonResponse({"content": content.first().text, "marked": is_marked})
                else:
                    return JsonResponse({"message": "vip only"}, status=403)
            else:
                return JsonResponse({"message": "login please"}, status=401)
        else:
            return JsonResponse({"content": content.first().text, "marked": is_marked})
