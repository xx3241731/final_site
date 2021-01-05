from django.shortcuts import render

import json
import csv
from django.http import HttpResponse
from datetime import datetime
def homepage(request):
    now = datetime.now()
    f = open(r'D:\Downloads\world.csv','rt',encoding='utf-8')
    reader = csv.DictReader(f)
    dict_list = []
    for data in reader:

        dict_list.append(data)

    return render(request, 'world.html', locals())
def data(request):

    f = open(r'D:\Downloads\world.csv','rt',encoding='utf-8')
    reader = csv.DictReader(f)
    dict_list = []
    for data in reader:

        dict_list.append(data)

    return render(request, 'data.html', locals())

def ind(request):
    
    f = open(r'D:\Downloads\ind.csv','rt',encoding='utf-8')
    reader1 = csv.DictReader(f)
    dict_list1 = []
    for data in reader1:

        dict_list1.append(data)

    return render(request, 'ind.html', locals())
    
def us(request):

    f = open(r'D:\Downloads\us.csv','rt',encoding='utf-8')
    reader2 = csv.DictReader(f)
    dict_list2 = []
    for data in reader2:

        dict_list2.append(data)

    return render(request, 'us.html', locals())

def phi(request):

    f = open(r'D:\Downloads\phi.csv','rt',encoding='utf-8')
    reader3 = csv.DictReader(f)
    dict_list3 = []
    for data in reader3:

        dict_list3.append(data)

    return render(request, 'phi.html', locals())

def chi(request):

    f = open(r'D:\Downloads\chi.csv','rt',encoding='utf-8')
    reader4 = csv.DictReader(f)
    dict_list4 = []
    for data in reader4:

        dict_list4.append(data)

    return render(request, 'chi.html', locals())

def jap(request):

    f = open(r'D:\Downloads\jap.csv','rt',encoding='utf-8')
    reader5 = csv.DictReader(f)
    dict_list5 = []
    for data in reader5:

        dict_list5.append(data)

    return render(request, 'jap.html', locals())

