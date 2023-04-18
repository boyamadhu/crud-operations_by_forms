from django.shortcuts import render
from app1.models import *
from django.http import HttpResponse
# Create your views here.

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['topic']
        TO=topic.objects.get_or_create(topic_name=tn)[0]
        TO.save()
        return HttpResponse('submitted successfully')
    return render(request,'first.html')

def insert_webpage(request):
    WO=topic.objects.all()
    d={'webpage':WO}
    if request.method=='POST':
        tn=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        TO=topic.objects.get(topic_name=tn)
        WO=webpage.objects.get_or_create(topic_name=TO,name=name,url=url)[0]
        WO.save()
        return HttpResponse('submitted successfully')
    return render(request,'insert_webpage.html',d)


def insert_access(request):
    WP=webpage.objects.all()
    d={'webpage':WP}
    if request.method=='POST':
        tn=request.POST['name']
        author=request.POST['author']
        date=request.POST['date']
        TO=webpage.objects.get(name=tn)
        AO=access.objects.get_or_create(name=TO,author=author,date=date)[0]
        AO.save()
        return HttpResponse('submitted successfully')
    return render(request,'insert_access.html',d)


def retrieve_select_topic(request):
    LTO=topic.objects.all()
    d={'topics':LTO}
    return render(request,'retrieve_select_topic.html',d)


def retrieve_checkbox_topic(request):
    LTO=topic.objects.all()
    d={"topic":LTO}
    if request.method=='POST':
        tn=request.POST.getlist('topic')

        emptyquery=webpage.objects.none()

        for i in tn:
             emptyquery=emptyquery | webpage.objects.filter(topic_name=i)
        d1={'topics':emptyquery}

        return render(request,'display_webpage_topic.html',d1)
        
    return render(request,'checkbox_retrieve_topic.html',d)


def retrieve_access_select(request):
    WO=webpage.objects.all()
    d={'web':WO}

    if request.method=='POST':
        tn=request.POST.getlist('na')
        
        emptyquery=access.objects.none()
        for i in tn:
             emptyquery=emptyquery | access.objects.filter(name=i)
        d1={'names':emptyquery}
        return render(request,'display_access.html',d1)

    return render(request,'retrieve_access_select.html',d)


def update_webpage(request):
    LTO=webpage.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        new=request.POST['new']
        for i in tn:
            webpage.objects.filter(name=i).update(topic_name=new)
        d1={"topics":webpage.objects.all()}
        return render(request,'display_webpage_topic.html',d1)
    return render(request,'update_topic.html',d)

def update_access(request):
    LTO=access.objects.all()
    d={'key':LTO}
    if request.method=='POST':
        tn=request.POST.getlist('name')
        new=request.POST['new']
        for i in tn:
            access.objects.filter(author=i).update(name=new)
        d1={"names":access.objects.all()}
        return render(request,'display_access.html',d1)
    return render(request,'update_access.html',d)

def delete_topic(request):
    LTO=topic.objects.all()
    d={'topics':LTO}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        for i in tn:
            topic.objects.filter(topic_name=i).delete()
        d1={"topics":topic.objects.all()}
        return render(request,'display_topic.html',d1)
    return render(request,'delete_topic.html',d)


def delete_webpage(request):
    LTO=webpage.objects.all()
    d={'webpage':LTO}
    if request.method=='POST':
        tn=request.POST.getlist('topic')
        for i in tn:
            webpage.objects.filter(name=i).delete()
        d1={"topics":webpage.objects.all()}
        return render(request,'display_webpage_topic.html',d1)
    return render(request,'delete_webpage.html',d)