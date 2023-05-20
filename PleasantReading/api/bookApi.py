from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import json

from api.admin import validateAccessToken, sendVerificationEmail, getUserFromToken
from api.models import UserInfo, BookBasicInfo, Collections, BookContext, Bookmark

def not_anonymous(request):
    if len(request.headers.get('Authorization').split(' ')) > 1:
        accessToken = request.headers.get('Authorization').split(' ')[1]
        decodedToken = validateAccessToken(accessToken)
        if decodedToken:
            return True
        else:
            return False
    else:
        return False

def get_username(request):
    return getUserFromToken(request.headers.get('Authorization').split(' ')[1]).username

def is_vip(request):
    id = get_username(request)
    return UserInfo.objects.get(userID=id).isVIP

def get_book_info(request, bookid):
    res = BookBasicInfo.objects.filter(bookID=bookid, onShelf=True)
    if res.count() == 0:
        return JsonResponse({"message": "failed"})
    else:
        book = res.first()
        favcnt = 0
        if not_anonymous(request):
            favcnt = Collections.objects.filter(bookID=bookid, userID=UserInfo.objects.get(userID=get_username(request))).count()
        data = {
            'id': book.bookID,
            'title': book.name,
            'author': book.author,
            'category': book.category,
            'status': book.status,
            'brief': book.profile,
            'score': book.totScore / book.rateNumber,
            'cnt': book.wordsCnt,
            'cover': book.img.url,
            'favorcnt': book.collections,
            'vip': book.isVIP,
            'fav': True if favcnt>0 else False,
        }
        return JsonResponse(data)

def get_book_outline(request, bookid):
    res = BookBasicInfo.objects.filter(bookID=bookid, onShelf=True)
    if res.count() == 0:
        return JsonResponse({"message": "failed"})
    else:
        outline = list(BookContext.objects.filter(bookID=bookid).order_by('chapter').values_list('title'))
        print(type(outline))
        print(outline)
        return JsonResponse({"message": "success", "outline": outline})

def get_book_content(request, bookid, chapter):
    res = BookBasicInfo.objects.filter(bookID=bookid, onShelf=True)
    if res.count() == 0:
        return JsonResponse({"message": "failed"})
    else:
        book = res.first()
        content = BookContext.objects.filter(bookID=bookid, chapter=chapter)
        if content.count() == 0:
            return JsonResponse({"message": "failed"})
        is_marked = False
        #...
        if book.isVIP:
            if not_anonymous(request):
                if is_vip(request):
                    return JsonResponse({"message": "success", "content": content.first().text, "marked": is_marked})
                else:
                    return JsonResponse({"message": "vip only"})
            else:
                return JsonResponse({"message": "login please"})
        else:
            if content.count() == 0:
                return JsonResponse({"message": "failed"})
            return JsonResponse({"message": "success", "content": content.first().text, "marked": is_marked})


# 进度：content未调试
