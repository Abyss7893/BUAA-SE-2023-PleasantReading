from django import forms
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
import json

from api.admin import validateAccessToken, sendVerificationEmail
from api.models import UserInfo

TOKEN = False