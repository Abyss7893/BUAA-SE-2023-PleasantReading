from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import json
import os

from api.admin import validateAccessToken, sendVerificationEmail, getUserFromToken
from api.models import UserInfo

TOKEN = True

SERVER_URL= "http://154.8.183.51"
# Create your views here.
def image_gallery(request):
    if TOKEN:
        print(request.headers.get('Authorization'))
        accessToken = request.headers.get('Authorization').split(' ')[1]
        decodedToken = validateAccessToken(accessToken)
        if decodedToken:
            print(getUserFromToken(accessToken))
            users = UserInfo.objects.all()
            return render(request, 'image_gallery.html', {'users': users})
        else:
            return JsonResponse({'message': 'please login first'})
    else:
        users = UserInfo.objects.all()
        return render(request, 'image_gallery.html', {'users': users})


class UserForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ['userID', 'passwd', 'email', 'img']
        widgets = {
            'passwd': forms.PasswordInput(),
            'img': forms.FileInput()
        }


def my_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form)
            image = request.FILES['img']
            ID = form.cleaned_data['userID']
            passwd = form.cleaned_data['passwd']
            email = form.cleaned_data['email']
            userObj = UserInfo(userID=ID, passwd=passwd, email=email, img=image)
            userObj.save()
            url = userObj.img.url
            return render(request, 'success.html', {'image_url': url})
            # 其他处理...
    else:
        form = UserForm()

    return render(request, 'test.html', {'form': form})


def changePwd(request):
    data = json.loads(request.body)
    userID = data.get('ID')
    oldPwd = data.get('oldpwd')
    newPwd = data.get('newpwd')

    accessToken = request.headers.get('Authorization').split(' ')[1]
    decodedToken = validateAccessToken(accessToken)
    if decodedToken is None:
        return JsonResponse({'message': 'fail', 'error': 'not the login user'}, status=400)
    obj = UserInfo.objects.filter(userID=userID)
    print(obj.get().passwd)
    if obj.count() == 0:
        return JsonResponse({'message': 'fail', 'error': 'ID error'}, status=400)
    else:
        if obj.get().passwd != oldPwd:
            return JsonResponse({'message': 'fail', 'error': 'old password error'}, status=400)
        else:
            UserInfo.objects.filter(userID=userID).update(passwd=newPwd)
            user = User.objects.get(username=userID)
            user.set_password(newPwd)
            user.save()
            return JsonResponse({'message': 'success'}, status=200)


def getInfo(request, ID):
    if request.method != 'GET':
        return JsonResponse({'message': 'fail', 'error': 'request method error'}, status=400)
    try:
        data = UserInfo.objects.filter(userID=ID)
        if data.count() == 0:
            return JsonResponse({"message": "failed", "error": "id error"})
        else:
            email = data.get().email
            gender = data.get().gender
            nickname = data.get().nickname
            motto = data.get().motto
            birthday = data.get().birth
            VIP = data.get().VIPDate
            responseData = {
                'username': ID,
                'email': email,
                'gender': gender,
                'nickname': nickname,
                'motto': motto,
                'birthday': birthday,
                'VIPDate': VIP,
                'message': 'login success'
            }
            return JsonResponse(responseData, status=200)
    except:
        return JsonResponse({'message': 'fail', 'error': 'ID error'}, status=400)
    

def changeInfo(request):
    accessToken = request.headers.get('Authorization').split(' ')[1]
    decodedToken = validateAccessToken(accessToken)
    if decodedToken is None:
        return JsonResponse({'message': 'fail', 'error': 'not the login user'}, status=404)

    data = json.loads(request.body)
    ID = getUserFromToken(accessToken).username
    gender = data.get('gender')
    nickname = data.get('nickname')
    birthday = data.get('birthday')
    motto = data.get('motto')

    if gender:
        UserInfo.objects.filter(userID=ID).update(gender=gender)
    if nickname:
        UserInfo.objects.filter(userID=ID).update(nickname=nickname)
    if birthday:
        UserInfo.objects.filter(userID=ID).update(birth=birthday)
    if motto:
        UserInfo.objects.filter(userID=ID).update(motto=motto)
    return JsonResponse({"message": "success"})


def login(request):
    print('Yes')
    data = json.loads(request.body)
    username = data.get('id')
    password = data.get('pwd')
    print("username = {0}, pwd = {1}".format(username, password))
    user = authenticate(request, username=username, password=password)
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


def register(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    try:
        print(username)
        cnt = UserInfo.objects.filter(userID=username).count()
        if cnt != 0:
            return JsonResponse({'message': 'fail', 'error': 'username exists'})
        # verificationCode = sendVerificationEmail(email)
        User.objects.create_user(username=username, password=password, email=email)
        UserInfo.objects.create(userID=username, passwd=password, email=email, nickname=username)
        return JsonResponse({'message': 'success'})
    except Exception as e:
        return JsonResponse({'message': 'fail', 'error': str(e)})


def setAvatar(request):
    accessToken = request.headers.get('Authorization').split(' ')[1]
    decodedToken = validateAccessToken(accessToken)
    if decodedToken is None:
        return JsonResponse({'message': 'fail', 'error': 'not the login user'}, status=404)

    ID = getUserFromToken(accessToken).username
    image = request.FILES['img']
    print(image)
    if image is None:
        return JsonResponse({'message': 'fail', 'error': 'get avatar fail'}, status=403)

    obj = UserInfo.objects.get(userID=ID)
    var = obj.img.name
    if var != "UserImg/user_img.jpg" and os.path.exists(SERVER_URL + var):
        os.remove(SERVER_URL + var)
    image.name = ID + ".jpg"
    obj.img = image
    obj.save()
    obj = UserInfo.objects.get(userID=ID)
    avatar = obj.img
    return JsonResponse({'message': 'success', 'avatarUrl': SERVER_URL + avatar.url})


def getAvatar(request, ID):
    if request.method != 'GET':
        return JsonResponse({'message': 'fail', 'error': 'request method error'}, status=400)
    try:
        obj = UserInfo.objects.get(userID=ID)
        avatar = obj.img
        return JsonResponse({'message': 'success', 'url': SERVER_URL + avatar.url})
    except:
        return JsonResponse({'message': 'fail', 'error': 'ID error'}, status=400)
