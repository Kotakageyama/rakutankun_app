import hashlib
from mysite.settings import DEBUG
import os
from time import sleep

from django.conf import settings
from django.http import Http404, HttpResponse, FileResponse, StreamingHttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from zipfile import ZipFile

from .forms import DownloadForm, LoginForm, DownloadCheckForm
from .models import User, CreditsData

from sshtunnel import SSHTunnelForwarder
from pymongo import MongoClient

import sys
from pathlib import Path
import os
import io
import glob
import json
import time

def getPrefixList():
    prefixList = PREFIXLIST
    temp = []
    for i in prefixList:
        temp.append((i,i))
    prefixList = temp
    print(prefixList)
    return prefixList

def user_update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print('post')
        print(data.get('prefix'))
        print(data.get('fromFrameNumber'))
    print(data.get('prefix'))
    filenamebr = getFilenameFilebr(data.get('prefix'),int(data.get('fromFrameNumber')),int(data.get('toFrameNumber')))
    # return HttpResponse(json.dumps(filenamebr),content_type="application/json")
    for fn, fb in filenamebr.items():
        filenamebr[fn] = base64.b64encode(fb).decode()
    return JsonResponse(filenamebr)

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
    params = {'student_id': '', 'username':'', 'credits_list': '', 'form': None}
    if request.method == 'POST':
        params['student_id'] = request.POST['student_id']
        params['fromFrameNumber'] = request.POST['fromFrameNumber']
        datas_list = User.objects.filter(student_id=request.POST['student_id'],passwd=request.POST['passwd']) 
    else:
        form = DownloadCheckForm()
        params['form'] = form
    return render(request, 'dashboard/userprofile.html', params)
