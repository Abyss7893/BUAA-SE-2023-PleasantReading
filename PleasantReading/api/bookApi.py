from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q, F, FloatField, Case, When, Value
import json
from datetime import date

from api.admin import validateAccessToken, sendVerificationEmail, getUserFromToken
from api.models import UserInfo, BookBasicInfo, Collections, BookContext, Bookmark

SERVER_URL = "http://154.8.183.51"
BOOKS_IN_PAGE = 10

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
            'cover': SERVER_URL + book.img.url,
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
        outline = list(BookContext.objects.filter(bookID=bookid).order_by('chapter').values_list('title', flat=True))
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
                    return JsonResponse({"content": content.first().text, "chaptertitle": content.first().title, "marked": is_marked})
                else:
                    return JsonResponse({"message": "vip only"}, status=403)
            else:
                return JsonResponse({"message": "login please"}, status=401)
        else:
            return JsonResponse({"content": content.first().text, "chaptertitle": content.first().title, "marked": is_marked})

def updateBookmark(request, bookid, chapter):
    if not notAnonymous(request):
        return JsonResponse({'message': 'login please'}, status=401)
    userid=getUsername(request)
    mark = Bookmark.objects.filter(bookID=bookid, userID=userid, chapter=chapter)
    if request.method == 'POST':
        if mark.count() > 0:
            return JsonResponse({'message': 'bookmark exists'}, status=400)
        Bookmark.objects.create(bookID=BookBasicInfo.objects.get(bookID=bookid), userID=UserInfo.objects.get(userID=userid), chapter=chapter)
        return JsonResponse({'message': 'success'})
    elif request.method == 'DELETE':
        if mark.count() == 0:
            return JsonResponse({'message': 'no bookmark'}, status=400)
        mark.delete()
        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': 'invalid request'}, status=400)

def bookFilter(request):
    if request.method != 'GET':
        return JsonResponse({'message': 'invalid request'}, status=400)
    books=BookBasicInfo.objects.filter(onShelf=True)
    if request.GET.get('category'):
        books = books.filter(category__icontains=request.GET.get('category'))
    if request.GET.get('vip'):
        if request.GET.get('vip') == 'true':
            books = books.filter(isVIP=True)
        else:
            books = books.filter(isVIP=False)
    if request.GET.get('status'):
        books = books.filter(status=request.GET.get('status'))
    if request.GET.get('range'):
        rng = eval(request.GET.get('range'))
        if rng == 1:
            books = books.filter(wordsCnt__lte=300000)
        elif rng == 2:
            books = books.filter(Q(wordsCnt__lte=500000) & Q(wordsCnt__gt=300000))
        elif rng == 3:
            books = books.filter(Q(wordsCnt__lte=1000000) & Q(wordsCnt__gt=500000))
        elif rng == 4:
            books = books.filter(Q(wordsCnt__lte=2000000) & Q(wordsCnt__gt=1000000))
        elif rng == 5:
            books = books.filter(wordsCnt__gt=2000000)
    num = books.count()
    if request.GET.get('order'):
        method = request.GET.get('order')
        if method == 'score':
            books = books.annotate(
                cscore=F('totScore') / Case(
                    When(rateNumber__gt=0, then=F('rateNumber')),
                    default=Value(1),
                    output_field=FloatField()
                )
            ).order_by('-cscore')
        elif method == 'favorcnt':
            books = books.order_by('-collections')
        elif method == 'wordsinc':
            books = books.order_by('wordsCnt')
        elif method == 'wordsdec':
            books = books.order_by('-wordsCnt')
    if request.GET.get('page'):
        page = eval(request.GET.get('page'))
        books = books[(page-1)*BOOKS_IN_PAGE:page*BOOKS_IN_PAGE]
    books = list(books.values_list('bookID', flat=True))
    return JsonResponse({'books': books, 'pages': max(1, (num+BOOKS_IN_PAGE-1) // BOOKS_IN_PAGE)})

def bookSearch(request):
    if request.method != 'GET':
        return JsonResponse({'message': 'invalid request'}, status=400)
    books = BookBasicInfo.objects.filter(onShelf=True)
    if request.GET.get('keyword'):
        books = books.filter(Q(name__icontains=request.GET.get('keyword')) | Q(author__icontains=request.GET.get('keyword')))
        num = books.count()
        if request.GET.get('page'):
            page = eval(request.GET.get('page'))
            books = books[(page - 1) * BOOKS_IN_PAGE:page * BOOKS_IN_PAGE]
        books = list(books.values_list('bookID', flat=True))
        return JsonResponse({'books': books, 'pages': max(1, (num + BOOKS_IN_PAGE - 1) // BOOKS_IN_PAGE)})
    else:
        return JsonResponse({'message': 'blank content'}, status=400)

