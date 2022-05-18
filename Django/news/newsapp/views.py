from django.shortcuts import render
from newsapp import models
import math

page1 = 1  

def index(request, pageindex=None):
    global page1  
    pagesize = 8  
    newsall = models.NewsUnit.objects.all().order_by('-id')  
    datasize = len(newsall) 
    totpage = math.ceil(datasize / pagesize)  
    if pageindex==None:  
        page1 = 1
        newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[:pagesize]
    elif pageindex=='1': 
        start = (page1-2)*pagesize 
        if start >= 0:  
            newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
            page1 -= 1
    elif pageindex=='2':  
        start = page1*pagesize  
        if start < datasize:  
            newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]
            page1 += 1
    elif pageindex=='3':  
        start = (page1-1)*pagesize 
        newsunits = models.NewsUnit.objects.filter(enabled=True).order_by('-id')[start:(start+pagesize)]

    currentpage = page1  
    return render(request, "index.html", locals())

def detail(request, detailid=None):
	unit = models.NewsUnit.objects.get(id=detailid)  
	category = unit.catego
	title = unit.title
	pubtime = unit.pubtime
	nickname = unit.nickname
	message = unit.message
	unit.press += 1  
	unit.save()  
	
	return render(request, "detail.html", locals())
