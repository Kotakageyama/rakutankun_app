import hashlib
from mysite.settings import DEBUG
import os
from time import sleep

from django.conf import settings
from django.http import Http404, HttpResponse, FileResponse, StreamingHttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from zipfile import ZipFile

from .forms import LoginForm
from .forms import ProfileDataForm, UserUpdateForm
from .models import User, CreditsData

import sys
from pathlib import Path
import os
import io
import glob
import json
import time


def user_update(request):
    params = {'student_id': '', 'user_credits': [], 'credits_list':CreditsData.objects.all(), 'form' : None}
    if request.method == 'POST':
        print(request.POST)
        datas_list = User.objects.filter(student_id=request.POST['student_id'],passwd=request.POST['passwd']).first()
        params['student_id'] = datas_list.student_id
        params['user_credits'] = [int(x.strip()) for x in datas_list.credits_list.split(',')]
        form = UserUpdateForm(request.POST)
        choicelist = []
        for i in (CreditsData.objects.all()).values():
            choicelist.append((i['Number'],i['ClassName']))
            #print(i['Number'])
        ulist = []
        for i,j in enumerate(params['user_credits']):
            if j == 1:
                ulist.append(i+1)
        form.fields['choicelist'].choices = choicelist
        form.fields['choicelist'].initial = ulist
        print(form.fields['choicelist'])
        print(ulist)
        params['form'] = form
    return render(request, 'dashboard/userupdate.html', params)

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

def getUpdateCreditList(stid, pswd, aalist):
    datas_list = User.objects.filter(student_id=stid,passwd=pswd).first()
    clist = [int(x.strip()) for x in datas_list.credits_list.split(',')]
    for b in range(len(clist)):
        clist[b] = 0
    for i in aalist:
        print(i)
        clist[int(i)-1] = 1
    return clist

def user_profile(request):
    params = {'student_id': '', 'user_credits': [], 'credits_list':CreditsData.objects.all(),'form':None}
    if request.method == 'POST':
        print(request.POST)
        form = ProfileDataForm(request.POST)
        if 'choicelist' in request.POST:
            print(request.POST.getlist('choicelist'))
            print(getUpdateCreditList(request.POST['student_id'], request.POST['passwd'], request.POST.getlist('choicelist')))
            gucl = getUpdateCreditList(request.POST['student_id'], request.POST['passwd'], request.POST.getlist('choicelist'))
            userUpdate = User.objects.get(student_id = request.POST['student_id'], passwd = request.POST['passwd'])
            userUpdate.credits_list =  ",".join([str(_) for _ in gucl])
            print(userUpdate)
            userUpdate.save()
        if(User.objects.filter(student_id=request.POST['student_id'],passwd=request.POST['passwd']).count() != 1):
            user = User()
            user.student_id = request.POST['student_id']
            user.passwd = request.POST['passwd']
            user.save()
        datas_list = User.objects.filter(student_id=request.POST['student_id'],passwd=request.POST['passwd']).first()
        params['student_id'] = datas_list.student_id
        params['user_credits'] = [int(x.strip()) for x in datas_list.credits_list.split(',')]
        params['form'] = form
    return render(request, 'dashboard/userprofile.html', params)
