"""
URL configuration for PleasantReading project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from PleasantReading import settings
from api import userApi, bookApi, managerApi

urlpatterns = [
    path('admin/', admin.site.urls),

    path('user/login', userApi.login),
    path('user/register', userApi.register),
    path('user/changepwd', userApi.changePwd),
    path('user/changeinfo', userApi.changeInfo),
    path('user/getinfo/<str:ID>', userApi.getInfo),
    path('user/setavatar', userApi.setAvatar),
    path('user/getavatar/<str:ID>', userApi.getAvatar),
    path('user/sendemail', userApi.userSendEmail),
    path('user/sending/<str:ID>/<str:pwd>', userApi.userCheck),

    path('book/info/<int:bookid>/', bookApi.getBookInfo),
    path('book/outline/<int:bookid>/', bookApi.getBookOutline),
    path('book/content/<int:bookid>/<int:chapter>/', bookApi.getBookContent),
    path('book/mark/<int:bookid>/<int:chapter>', bookApi.updateBookmark),
    path('book/filter/', bookApi.bookFilter),
    path('book/search/', bookApi.bookSearch),
    path('book/notes/<int:bookid>/<int:chapter>/<int:page>/', bookApi.getBookNotes),
    path('book/comments/<int:bookid>/<int:chapter>/<int:page>/', bookApi.getComments),
    path('book/favor/', bookApi.getFavor),
    path('book/favor/<int:bookid>', bookApi.updateFavor),
    path('book/notes/<int:bookid>/<int:chapter>', bookApi.submitNotes),
    path('book/comments/<int:bookid>/<int:chapter>', bookApi.submitComments),
    path('book/score/<int:bookid>/', bookApi.getScore),
    path('book/score/<int:bookid>/<str:score>', bookApi.putScore),
    path('book/marks/', bookApi.getMarks),
    path('book/lastVisit/', bookApi.getLastVisit),
    path('book/notes/', bookApi.getAllNotes),
    path('book/comments/', bookApi.getAllComments),
    path('book/recent/', bookApi.getRecentHistory),
    path('book/author/<str:name>', bookApi.getAuthor),

    path('manager/register', managerApi.managerRegister),
    path('manager/login', managerApi.managerLogin),
    path('manager/newbook', managerApi.newBook),
    path('manager/newbook2', managerApi.newBook2),
    path('manager/setcover', managerApi.setBookCover),
    path('manager/getcover/<int:bookid>', managerApi.getCover),
    path('manager/uploadchapter', managerApi.uploadChapter),
    path('manager/filter', managerApi.getAllBooks),
    path('manager/uploadauthor', managerApi.updateAuthor),

    path('submit/', userApi.my_view),
    path('gallery/', userApi.image_gallery),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
