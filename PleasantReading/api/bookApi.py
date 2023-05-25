from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from django.db.models import Q, F, FloatField, Case, When, Value, CharField, OuterRef, Subquery, Count, Max
from rest_framework import serializers
from django.db.models.functions import Concat
import json
from datetime import date, datetime, timedelta

from api.admin import validateAccessToken, sendVerificationEmail, getUserFromToken
from api.models import UserInfo, BookBasicInfo, Collections, BookContext, Bookmark, Comments, Score, History, Author

SERVER_URL = "http://154.8.183.51"
BK2PG = 10
CM2PG = 5
NT2PG = 5


def getPages(pages, num):
    return max((pages + num - 1) // num, 1)


def notAnonymous(request):
    if 'Authorization' not in request.headers:
        return False
    if len(request.headers.get('Authorization')) == 0:
        return False
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
    res = BookBasicInfo.objects.filter(bookID=bookid)
    if res.count() == 0:
        return JsonResponse({"message": "failed"}, status=400)
    else:
        book = res.first()
        favcnt = 0
        if notAnonymous(request):
            favcnt = Collections.objects.filter(bookID=bookid, userID=getUsername(request)).count()
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
            'fav': True if favcnt > 0 else False,
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
            userid = getUsername(request)
            is_marked = Bookmark.objects.filter(bookID=bookid, chapter=chapter, userID=userid).count() > 0
            History.objects.create(bookID=bookid, userID=userid, chapter=chapter, timestamp=date.today())
        if book.isVIP:
            if notAnonymous(request):
                if isVIP(request):
                    return JsonResponse(
                        {"content": content.first().text.split('\n'), "chaptertitle": content.first().title,
                         "marked": is_marked})
                else:
                    return JsonResponse({"message": "vip only"}, status=403)
            else:
                return JsonResponse({"message": "login please"}, status=401)
        else:
            return JsonResponse({"content": content.first().text.split('\n'), "chaptertitle": content.first().title,
                                 "marked": is_marked})


def updateBookmark(request, bookid, chapter):
    if not notAnonymous(request):
        return JsonResponse({'message': 'login please'}, status=401)
    userid = getUsername(request)
    mark = Bookmark.objects.filter(bookID=bookid, userID=userid, chapter=chapter)
    if request.method == 'POST':
        if mark.count() > 0:
            return JsonResponse({'message': 'bookmark exists'}, status=400)
        Bookmark.objects.create(bookID=bookid, userID=userid, chapter=chapter)
        return JsonResponse({'message': 'success'})
    elif request.method == 'DELETE':
        if mark.count() == 0:
            return JsonResponse({'message': 'no bookmark'}, status=400)
        mark.delete()
        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': 'invalid request'}, status=400)

def bookFilter(request, perm=True):
    if request.method != 'GET':
        return JsonResponse({'message': 'invalid request'}, status=400)
    if perm:
        books = BookBasicInfo.objects.filter(onShelf=True)
    else:
        books = BookBasicInfo.objects.all()
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
        elif method == 'weekpop' or method == 'monthpop' or method == 'yearpop':
            if method == 'weekpop':
                days = 7
            elif method == 'monthpop':
                days = 30
            else:
                days = 365
            stamp = date.today() - timedelta(days=days)
            history_within_month = History.objects.filter(timestamp__gte=stamp, bookID=OuterRef('bookID'))
            books = books.annotate(num_reads=Subquery(
                history_within_month.values('bookID').annotate(count=Count('bookID')).values('count'))).order_by(
                '-num_reads')
    if request.GET.get('page'):
        page = eval(request.GET.get('page'))
        books = books[(page - 1) * BK2PG:page * BK2PG]
    books = list(books.values_list('bookID', flat=True))
    return JsonResponse({'books': books, 'pages': getPages(num, BK2PG)})


def bookSearch(request):
    if request.method != 'GET':
        return JsonResponse({'message': 'invalid request'}, status=400)
    books = BookBasicInfo.objects.filter(onShelf=True)
    if request.GET.get('keyword'):
        books = books.filter(
            Q(name__icontains=request.GET.get('keyword')) | Q(author__icontains=request.GET.get('keyword')))
        num = books.count()
        if request.GET.get('page'):
            page = eval(request.GET.get('page'))
            books = books[(page - 1) * BK2PG:page * BK2PG]
        books = list(books.values_list('bookID', flat=True))
        return JsonResponse({'books': books, 'pages': getPages(num, BK2PG)})
    else:
        return JsonResponse({'message': 'blank content'}, status=400)


def getBookNotes(request, bookid, chapter, page):
    if request.method != 'GET':
        return JsonResponse({'message': 'invalid request'}, status=400)
    if not notAnonymous(request):
        return JsonResponse({'notes': [], 'pages': 1})
    userid = getUsername(request)
    comments = Comments.objects.filter(bookID=bookid, userID=userid, chapter=chapter, visible=False)
    num = comments.count()
    comments = comments[(page - 1) * NT2PG:page * NT2PG]
    return JsonResponse({'notes': list(comments.values_list('text', flat=True)), 'pages': getPages(num, NT2PG)})


def getAllNotes(request):
    if request.method != 'GET':
        return JsonResponse({'message': 'invalid request'}, status=400)
    if not notAnonymous(request):
        return JsonResponse({'notes': [], 'pages': 1})
    userid = getUsername(request)
    notes = Comments.objects.filter(userID=userid, visible=False)
    subquery = BookBasicInfo.objects.filter(bookID=OuterRef('bookID')).values('name')[:1]
    notes = notes.annotate(
        name=Subquery(subquery.values('name'))
    )
    notes = notes.values('bookID', 'name', 'chapter', 'text')
    return JsonResponse({'notes': list(notes)})


def getComments(request, bookid, chapter, page):
    if request.method != 'GET':
        return JsonResponse({'message': 'invalid request'}, status=400)
    comments = Comments.objects.filter(bookID=bookid, chapter=chapter, visible=True)
    num = comments.count()
    subquery = UserInfo.objects.filter(userID=OuterRef('userID')).values('nickname', 'img')[:1]
    comments = comments.annotate(
        nickname=Subquery(subquery.values('nickname')),
        img=Concat(Value(SERVER_URL + '/media/'), Subquery(subquery.values('img')), output_field=CharField())
    )
    comments = comments.values('userID', 'nickname', 'img', 'text', 'timestamp')
    comments = comments[(page - 1) * CM2PG:page * CM2PG]
    return JsonResponse({'comments': list(comments), 'pages': getPages(num, CM2PG)})


class FavorBookSerializer(serializers.ModelSerializer):
    bookid = serializers.CharField(source='bookID')
    name = serializers.CharField()
    cover = serializers.ImageField(source='img')

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        avatar_url = SERVER_URL + ret['cover']
        ret['cover'] = avatar_url
        return ret

    class Meta:
        model = BookBasicInfo
        fields = ['bookid', 'name', 'cover']


def getFavor(request):
    if request.method != 'GET':
        return JsonResponse({'message': 'invalid request'}, status=400)
    if not notAnonymous(request):
        return JsonResponse({'message': 'login please'}, status=401)
    userid = getUsername(request)
    collections = Collections.objects.filter(userID=userid)
    book_ids = [collection.bookID for collection in collections]
    books = BookBasicInfo.objects.filter(onShelf=True, bookID__in=book_ids)
    serializer = FavorBookSerializer(books, many=True)
    return JsonResponse({'books': serializer.data})


def updateFavor(request, bookid):
    if not notAnonymous(request):
        return JsonResponse({'message': 'login please'}, status=401)
    userid = getUsername(request)
    if request.method == 'PUT':
        Collections.objects.create(userID=userid, bookID=bookid)
    elif request.method == 'DELETE':
        favs = Collections.objects.filter(userID=userid, bookID=bookid)
        favs.delete()
    return JsonResponse({'message': 'success'})


def submitNotes(request, bookid, chapter):
    if request.method != 'POST':
        return JsonResponse({'message': 'error'}, status=400)
    if not notAnonymous(request):
        return JsonResponse({'message': 'login please'}, status=401)
    data = json.loads(request.body)
    userid = getUsername(request)
    Comments.objects.create(userID=userid, bookID=bookid, chapter=chapter, text=data.get('text'), visible=False,
                            timestamp=date.today())
    return JsonResponse({'message': 'success'})


def submitComments(request, bookid, chapter):
    if request.method != 'POST':
        return JsonResponse({'message': 'error'}, status=400)
    if not notAnonymous(request):
        return JsonResponse({'message': 'login please'}, status=401)
    data = json.loads(request.body)
    userid = getUsername(request)
    Comments.objects.create(userID=userid, bookID=bookid, chapter=chapter, text=data.get('text'), visible=True,
                            timestamp=date.today())
    return JsonResponse({'message': 'success'})


def getScore(request, bookid):
    if not notAnonymous(request):
        return JsonResponse({'message': 'login please'}, status=401)
    userid = getUsername(request)
    ret = Score.objects.filter(userID=userid, bookID=bookid)
    if ret.count() == 0:
        return JsonResponse({'message': 'no score'}, status=404)
    else:
        return JsonResponse({'message': 'success', 'score': ret.first().score})


def putScore(request, bookid, score):
    if not notAnonymous(request):
        return JsonResponse({'message': 'login please'}, status=401)
    userid = getUsername(request)
    ret = Score.objects.filter(userID=userid, bookID=bookid)
    if ret.count() > 0:
        return JsonResponse({'message': 'score exist'}, status=400)
    Score.objects.create(userID=userid, bookID=bookid, score=eval(score))
    return JsonResponse({'message': 'success'})


def getMarks(request):
    if not notAnonymous(request):
        return JsonResponse({'message': 'login please'}, status=401)
    userid = getUsername(request)
    marks = Bookmark.objects.filter(userID=userid)
    subquery = BookBasicInfo.objects.filter(bookID=OuterRef('bookID')).values('name')[:1]
    marks = marks.annotate(name=Subquery(subquery.values('name')))
    marks = marks.values('bookID', 'name', 'chapter')
    return JsonResponse({'marks': list(marks)})


def getLastVisit(request):
    if not notAnonymous(request):
        return JsonResponse({'message': 'login please'}, status=401)
    userid = getUsername(request)
    ret = History.objects.filter(userID=userid)
    if ret.count() == 0:
        return JsonResponse({'message': 'no record'}, status=400)
    ret = ret.last()
    return JsonResponse({'bookid': ret.bookID,
                         'name': BookBasicInfo.objects.get(bookID=ret.bookID).name,
                         'chapter': ret.chapter})

def getRecentHistory(request):
    if not notAnonymous(request):
        return JsonResponse({'message': 'login please'}, status=201)
    userid = getUsername(request)

    latest_history = History.objects.filter(bookID=OuterRef('bookID')).order_by('-timestamp')
    result = History.objects.filter(id=Subquery(latest_history.values('id')[:1]))
    print(result.values('bookID', 'chapter'))

    latest_chapters = result[:8]
    subquery = BookBasicInfo.objects.filter(bookID=OuterRef('bookID')).values('name', 'img')[:1]
    latest_chapters = latest_chapters.annotate(
        name=Subquery(subquery.values('name')), img=Subquery(subquery.values('img'))
    )
    subquery = BookContext.objects.filter(bookID=OuterRef('bookID'), chapter=OuterRef('chapter')).values('title')[:1]
    latest_chapters = latest_chapters.annotate(
        title=Subquery(subquery.values('title'))
    )
    latest_chapters = latest_chapters.values('name', 'img', 'bookID', 'chapter', 'title')
    return JsonResponse({'list': list(latest_chapters)})

def getAuthor(request, name):
    res = Author.objects.filter(name=name)
    works = BookBasicInfo.objects.filter(author=name, onShelf=True).values('bookID', 'name', 'profile', 'img')
    if res.count() == 0:
        return JsonResponse({'profile': '暂无有关详细信息', 'img': 'AuthorImg/default.jpg', 'works': list(works)})
    return {'profile': res.first().profile, 'img': res.first().img, 'works': list(works)}
