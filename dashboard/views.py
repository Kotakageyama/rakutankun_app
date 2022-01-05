import hashlib
from mysite.settings import DEBUG
import os
from time import sleep

from django.conf import settings
from django.http import Http404, HttpResponse, FileResponse, StreamingHttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from zipfile import ZipFile

from .forms import LoginForm
from .models import User, CreditsData

import sys
from pathlib import Path
import os
import io
import glob
import json
import time


def user_update(request):
    params = {'student_id': '', 'username':'', 'user_credits': [], 'credits_list':CreditsData.objects.all()}
    if request.method == 'POST':
        print(request.POST)
        if(User.objects.filter(student_id=request.POST['student_id'],passwd=request.POST['passwd']).count() != 1):
            user = User()
            user.student_id = request.POST['student_id']
            user.passwd = request.POST['passwd']
            user.save()
        datas_list = User.objects.filter(student_id=request.POST['student_id'],passwd=request.POST['passwd']).first()
        params['student_id'] = datas_list.student_id
        params['username'] = datas_list.username
        params['user_credits'] = [int(x.strip()) for x in datas_list.credits_list.split(',')]
    return render(request, 'dashboard/userprofile.html', params)

def index(request):
    params = {'student_id': '', 'passwd': '', 'form': None}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        params['student_id'] = request.POST['student_id']
        params['passwd'] = request.POST['passwd']
        params['form'] = form
    else:
        form = LoginForm()
        params['form'] = form
    return render(request, 'dashboard/index.html',params)

def user_profile(request):
    params = {'student_id': '', 'username':'', 'user_credits': [], 'credits_list':CreditsData.objects.all()}
    if request.method == 'POST':
        print(request.POST)
        if(User.objects.filter(student_id=request.POST['student_id'],passwd=request.POST['passwd']).count() != 1):
            user = User()
            user.student_id = request.POST['student_id']
            user.passwd = request.POST['passwd']
            user.save()
        datas_list = User.objects.filter(student_id=request.POST['student_id'],passwd=request.POST['passwd']).first()
        params['student_id'] = datas_list.student_id
        params['username'] = datas_list.username
        params['user_credits'] = [int(x.strip()) for x in datas_list.credits_list.split(',')]
    return render(request, 'dashboard/userprofile.html', params)
