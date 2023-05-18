import requests
from django import forms
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from api.models import UserInfo


# Create your views here.
def image_gallery(request):
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
            userObj = UserInfo(userID=ID, passwd=passwd, email=email,img=image)
            userObj.save()
            url = userObj.img.url
            return render(request, 'success.html', {'image_url': url})
            # 其他处理...
    else:
        form = UserForm()

    return render(request, 'test.html', {'form': form})
