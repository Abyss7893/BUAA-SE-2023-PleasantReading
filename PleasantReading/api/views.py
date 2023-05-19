from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
import json

from api.admin import validateAccessToken
from api.models import UserInfo


# Create your views here.
def image_gallery(request):
    accessToken = request.headers.get('Authorization').split(' ')[1]
    decodedToken = validateAccessToken(accessToken)
    if decodedToken:
        print(request.user)
        users = UserInfo.objects.all()
        return render(request, 'image_gallery.html', {'users': users})
    else:
        return JsonResponse({'message': '请登录'})

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
            userObj = UserInfo(userID=ID, passwd=passwd, email=email,img=image)
            userObj.save()
            url = userObj.img.url
            return render(request, 'success.html', {'image_url': url})
            # 其他处理...
    else:
        form = UserForm()

    return render(request, 'test.html', {'form': form})


@csrf_exempt
def login(request):
    print('Yes')
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    print("username = {0}, pwd = {1}".format(username, password))
    user = authenticate(request, username=username, password=password)
    if user is not None:
        refresh = RefreshToken.for_user(user)
        accessToken = refresh.access_token
        responseData = {
            'refresh': str(refresh),
            'access': str(accessToken),
            'message': 'login success'
        }
        return JsonResponse(responseData, status=200)
    else:
        return JsonResponse({'message': '登录失败'}, status=400)



@csrf_exempt
def register(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')
    try:
        print(username)
        cnt = UserInfo.objects.filter(userID=username).count()
        if cnt != 0:
            return JsonResponse({'message': 'failed', 'error': '用户名重复'})

        User.objects.create_user(username=username, password=password, email=email)
        UserInfo.objects.create(userID=username, passwd=password, email=email)
        return JsonResponse({'message': 'successful'})
    except Exception as e:
        return JsonResponse({'message': 'failed', 'error': str(e)})
