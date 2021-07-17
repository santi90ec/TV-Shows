from django.shortcuts import redirect, render
from .models import Show
from django.contrib import messages
# Create your views here.
def index(request):
    return redirect("/shows")
def shows(request):
    if request.method=="GET":
        context={
            'allshows': Show.objects.all()
        }
        return render(request,"shows.html",context)
def new(request):
    if request.method=="GET":
        return render(request,"newshow.html")
def created(request):
    if request.method=="POST":
        errors=Show.objects.basic_validator(request.POST)
        if len(errors) >0:
            for key , values in errors.items():
                messages.error(request, values)
            return redirect('/shows/new')

        else:
            newshow=Show.objects.create(
                title=request.POST['title'],
                network=request.POST['network'],
                releaseDate=request.POST['date'],
                description=request.POST['desc']
            )
            return redirect(f'/shows/{newshow.id}')
    
def edit(request,number):
    if request.method=='GET':
        showupdate=Show.objects.get(id=number)
        context={
            'show': showupdate
        }
        context['date']= str(context['show'].releaseDate)
        request.session['showEdit']=showupdate.id
        return render(request,"updateshow.html",context)
def editSucc(request,number):
    if request.method=='POST':
        errors=Show.objects.basic_validator(request.POST)
        if len(errors) >0:
            for key , values in errors.items():
                messages.error(request, values)
            return redirect(f'/shows/{number}/edit')

        else:
            updatedShow=Show.objects.get(id=number)
            updatedShow.title=request.POST['title']
            updatedShow.network=request.POST['network']
            updatedShow.releaseDate=request.POST['date']
            updatedShow.description=request.POST['desc']
            updatedShow.save()
            return redirect(f'/shows/{updatedShow.id}')
def showinfo(request,number):
    info=Show.objects.get(id=number)
    context={
        'infoShow': info
    }
    return render(request,"showinfo.html",context)
def delete(request, number):
    showDelet=Show.objects.get(id=number)
    showDelet.delete()
    return redirect('/shows')