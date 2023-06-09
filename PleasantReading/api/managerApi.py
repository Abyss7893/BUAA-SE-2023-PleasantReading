from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.utils.crypto import get_random_string
from rest_framework_simplejwt.tokens import RefreshToken
import json
import os

from api.admin import getUserFromToken, validateAccessToken
from api.models import *
from api.userApi import login
from api.bookApi import bookFilter

SERVER_URL= "http://154.8.183.51"

def checkManager(request):
    if 'Authorization' not in request.headers:
        return False
    accessToken = request.headers.get('Authorization').split(' ')[1]
    decodedToken = validateAccessToken(accessToken)
    if decodedToken is None:
        return False
    ID = getUserFromToken(accessToken).username
    cnt = Manager.objects.filter(userID=ID)
    return cnt.count() != 0


def getAllBooks(request):
    if not checkManager(request):
        return JsonResponse({'message': 'fail', 'error': 'not the login manager'}, status=400)
    return bookFilter(request, perm=False)

def managerRegister(request):
    data = json.loads(request.body)
    ID = data.get('id')
    pwd = data.get('pwd')
    email = data.get('email')
    cnt = Manager.objects.filter(userID=ID).count() + \
          UserInfo.objects.filter(userID=ID).count()
    if cnt != 0:
        return JsonResponse({'message': 'fail', 'error': 'ID exists'})
    Manager.objects.create(userID=ID, passwd=pwd, email=email)
    User.objects.create_user(username=ID, password=pwd, email=email)
    return JsonResponse({'message': 'success'})

def managerLogin(request):
    data = json.loads(request.body)
    ID = data.get('id')
    if Manager.objects.filter(userID=ID).count() == 0:
        return JsonResponse({'message': 'fail', 'error': 'not manager'}, status=400)
    password = data.get('pwd')
    user = authenticate(request, username=ID, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        accessToken = refresh.access_token
        responseData = {
            'refresh': str(refresh),
            'access': str(accessToken),
            'message': 'success'
        }
        return JsonResponse(responseData, status=200)
    else:
        return JsonResponse({'message': 'fail'}, status=400)

def newBook(request):
    if not checkManager(request):
        return JsonResponse({'message': 'fail', 'error': 'not the login manager'}, status=400)

    data = json.loads(request.body)
    name = data.get('title')
    author = data.get('author')
    status = data.get('status')
    category = data.get('category')
    profile = data.get('brief')
    isVIP = data.get('vip')
    onShelf = data.get('onshelf')
    if name is None:
        return JsonResponse({"message": "fail", "error": "name is None"}, status=400)
    if category is None:
        return JsonResponse({"message": "fail", "error": "category is None"}, status=400)
    if profile is None:
        return JsonResponse({"message": "fail", "error": "brief is None"}, status=400)
    obj = BookBasicInfo.objects.filter(name=name)
    if obj.count() == 0:
        BookBasicInfo.objects.create(
            name=name,
            author=author if author is not None else '匿名',
            status=status if status is not None else "连载",
            category=category,
            profile=profile,
            isVIP=isVIP if isVIP is not None else False,
            onShelf=onShelf if onShelf is not None else True,
            collections=0
        )
        return JsonResponse({'message': 'create success'})
    else:
        obj = BookBasicInfo.objects.get(name=name)
        if author is not None:
            obj.author = author
        if status is not None:
            obj.status = status
        if onShelf is not None:
            obj.onShelf = onShelf
        if isVIP is not None:
            obj.isVIP = isVIP
        if category is not None:
            obj.category = category
        if profile is not None:
            obj.profile = profile
        obj.save()
        return JsonResponse({'message': 'update status success'})


def newBook2(request):
    if not checkManager(request):
        return JsonResponse({'message': 'fail', 'error': 'not the login manager'}, status=400)

    data = json.loads(request.body)
    name = data.get('title')
    author = data.get('author')
    status = data.get('status')
    category = data.get('category')
    profile = data.get('brief')
    isVIP = data.get('vip')
    onShelf = data.get('onshelf')
    if name is None:
        return JsonResponse({"message": "fail", "error": "name is None"}, status=400)
    if category is None:
        return JsonResponse({"message": "fail", "error": "category is None"}, status=400)
    if profile is None:
        return JsonResponse({"message": "fail", "error": "brief is None"}, status=400)
    BookBasicInfo.objects.create(
        name=name,
        author=author if author is not None else '匿名',
        status=status if status is not None else "连载",
        category=category,
        profile=profile,
        isVIP=isVIP if isVIP is not None else False,
        onShelf=onShelf if onShelf is not None else True,
        collections=0
    )
    return JsonResponse({'message': 'create success'})

def setBookCover(request):
    if not checkManager(request):
        return JsonResponse({'message': 'fail', 'error': 'not the login manager'}, status=400)

    ID = int(request.POST.get('bookid'))
    image = request.FILES['img']
    if image is None:
        return JsonResponse({'message': 'fail', 'error': 'get cover fail'}, status=403)

    obj = BookBasicInfo.objects.get(bookID=ID)
    var = obj.img.name
    if var != "BookImg/default.jpg" and os.path.exists(SERVER_URL + var):
        os.remove(SERVER_URL + var)
    image.name = get_random_string(length=8) + ".jpg"
    obj.img = image
    obj.save()
    obj = BookBasicInfo.objects.get(bookID=ID)
    cover = obj.img
    return JsonResponse({'message': 'success', 'avatarUrl': SERVER_URL + cover.url})


def getCover(request, bookid):
    if request.method != 'GET':
        return JsonResponse({'message': 'fail', 'error': 'request method error'}, status=400)
    try:
        obj = BookBasicInfo.objects.get(bookID=bookid)
        return JsonResponse({'message': 'success', 'url': SERVER_URL + obj.img.url})
    except:
        return JsonResponse({'message': 'fail', 'error': "bookid error"}, status=400)


def uploadChapter(request):
    if not checkManager(request):
        return JsonResponse({'message': 'fail', 'error': 'not the login manager'}, status=400)

    data = json.loads(request.body)
    bookID = int(data.get('bookid'))
    chapter = int(data.get('chapter'))
    context = data.get('context')
    title = data.get('title')
    if BookBasicInfo.objects.filter(bookID=bookID).count() == 0:
        return JsonResponse({'message': 'fail', 'error': 'bookID error'}, status=400)
    if BookContext.objects.filter(bookID=bookID,chapter=chapter).count() != 0:
        obj = BookContext.objects.get(bookID=bookID, chapter=chapter)
        if title is not None:
            obj.title = title
        if context is not None:
            preLen = len(obj.text)
            nowLen = len(context)
            obj.text = context
            book = BookBasicInfo.objects.get(bookID=bookID)
            book.wordsCnt = book.wordsCnt + nowLen - preLen
            book.save()
        obj.save()
        return JsonResponse({"message": "reload success"})
    else:
        BookContext.objects.create(bookID=bookID, chapter=chapter, text=context, title=title)
        return JsonResponse({"message": "upload success"})


def updateAuthor(request):
    if not checkManager(request):
        return JsonResponse({'message': 'fail', 'error': 'not the login manager'}, status=400)

    try:
        name = request.POST.get('name')
        image = request.FILES.get('img', None)
        profile = request.POST.get('brief', None)
    except:
        return JsonResponse({"message": "accept data error"}, status=400)

    obj = Author.objects.filter(name=name)
    flag = True
    if obj.count() == 0:
        Author.objects.create(
            name=name,
            profile="这个人很懒，什么都没有留下~"
        )
        flag = False
    obj = Author.objects.get(name=name)
    if image is not None:
        var = obj.img.name
        if var != "AuthorImg/default.jpg" and os.path.exists(SERVER_URL + var):
            os.remove(SERVER_URL + var)
        image.name = get_random_string(length=8) + ".jpg"
        obj.img = image
    if profile:
        obj.profile = profile
    obj.save()
    print("pram = ", profile)
    print("profile = ", obj.profile)
    if flag:
        return JsonResponse({"message": "reload success"})
    else:
        return JsonResponse({"message": "upload success"})
