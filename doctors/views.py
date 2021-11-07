from django.shortcuts import render, redirect
from doctors.decorator import unauthenticated_user, allowed_users
from doctors.models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
import os
# Create your views here.


def index(request):
    # context = {}
    return render(request, "doctors/index.html")  # , context)


def about(request):
    return render(request, "doctors/about.html")


def maps(request):
    return render(request, "doctors/maps.html")


def project_requirement(request):
    return render(request, "doctors/requirement.html")



#ARTICLE

def healthblog(request):
    articles = Article.objects.all()
    context = {"articles": articles}
    return render(request, "doctors/healthblog.html", context)


def healthblog_content(request, pk):
    article = Article.objects.filter(id=pk).first()
    context = {"article": article}
    return render(request, "doctors/healthblog_one.html" ,context)


def deleteArticle(request, pk):
    article = Article.objects.get(id=pk)
    if request.method == "POST":
        os.remove(article.img.path)
        article.delete()
        return redirect("doctors:healthblog")


def addArticle(request):
    form = CreateArticleForm()
    if request.method == 'POST':
        createArticleForm = CreateArticleForm(request.POST, request.FILES)
        if createArticleForm.is_valid():
            createArticleForm.save()
            article = Article.objects.values('id').order_by('-id').first()
            id_last = article['id']
            return redirect("doctors:healthblog_content", pk=id_last)    #อยากให้ไดเรกไปหน้าที่พึ่ง
    return render(request, "doctors/addhealthblog.html", {"form": form})


def updateArticle(request, pk):
    article = Article.objects.get(id=pk)
    form = CreateArticleForm(instance=article)
    if request.method == 'POST':
        createNewsForm = CreateArticleForm(request.POST, instance=article)
        if createNewsForm.is_valid():
            createNewsForm.save()
            article = Article.objects.values('id').order_by('-id').first()
            id_last = article['id']
            return redirect("doctors:healthblog_content", pk=id_last)
    context = {"form": form, "article": article}    
    return render(request, "doctors/updatehealthblog.html", context)


#NEW
def news(request):
    news = New.objects.all()
    context = {"news": news}
    return render(request, "doctors/news.html", context)


def news_content(request, pk):
    new = New.objects.filter(id=pk).first()
    context = {"new": new}
    return render(request, "doctors/news_one.html" ,context)


def deleteNews(request, pk):
    new = New.objects.get(id=pk)
    if request.method == "POST":
        new.delete()
        os.remove(new.img.path)
        return redirect("doctors:news")


def addNews(request):
    form = CreateNewsForm()
    if request.method == 'POST':
        createNewsForm = CreateNewsForm(request.POST, request.FILES)
        if createNewsForm.is_valid():
            createNewsForm.save()
            news = New.objects.values('id').order_by('-id').first()
            id_last = news['id']
            return redirect("doctors:news_content", pk=id_last)    #อยากให้ไดเรกไปหน้าที่พึ่ง
    return render(request, "doctors/addnews.html", {"form": form})


def updateNew(request, pk):
    new = New.objects.get(id=pk)
    form = CreateNewsForm(instance=new)
    if request.method == 'POST':
        createNewsForm = CreateNewsForm(request.POST, instance=new)
        if createNewsForm.is_valid():
            createNewsForm.save()
            new = New.objects.values('id').order_by('-id').first()
            id_last = new['id']
            return redirect("doctors:news_content", pk=id_last)
    context = {"form": form, "new": new}
    return render(request, "doctors/updatenews.html", context)

#PACKAGE
def package(request):
    packages = Package.objects.all()
    return render(request, "doctors/package.html", {"packages": packages} )


def package_content(request, pk):
    pack = Package.objects.filter(id=pk).first()
    return render(request, "doctors/package_one.html", {'pack':pack})

def editpackage(request, pk):
    pack = Package.objects.get(id=pk)
    form = CreatePackageForm(instance=pack)
    if request.method == 'POST':
        createNewsForm = CreatePackageForm(request.POST, instance=pack)
        if createNewsForm.is_valid():
            createNewsForm.save()
            pack = Package.objects.values('id').order_by('-id').first()
            id_last = pack['id']
            return redirect("doctors:healthblog_content", pk=id_last)
    context = {"form": form, "pack":pack}    
    return render(request, "doctors/editpackage.html", context)

def deletePackage(request, pk):
    pack = Package.objects.filter(id=pk)
    if request.method == "POST":
        pack.delete()
        return redirect("doctors:package")

def addPackage(request):
    form = CreatePackageForm()
    if request.method == 'POST':
        newform = CreatePackageForm(request.POST, request.FILES)
        if newform.is_valid():
            newform.save()
            pack = Package.objects.values('id').order_by('-id').first()
            id_last = pack['id']
            return redirect("doctors:package_content", pk=id_last)  
    return render(request, "doctors/addpackage.html", {"form": form})

def buy(request ,pk):
	# pack = Package.objects.get(id=pk)
	# pat = Patient.objects.get(user=request.user.patient)
	# if request.method == 'POST':
    #     Buy.objects.add(patient=pat, package=pack,)
        return redirect('doctors:index')
    
def mypack(request):
    patient = request.user.patient.buy_set.all()

    return render(request, "doctors/mypack.html", {'patient':patient})      


def mdoctor(request):
    return render(request, "doctors/mdoctor.html")

#register / login / logout

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='patient')
            user.groups.add(group)
            Patient.objects.create(
                user=user
            )

            messages.success(request, 'Account was created for ' + username)
            return redirect('doctors:login')
    return render(request, 'doctors/register.html', {'form': form})

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('doctors:index')
        else:
            messages.info(request, 'Username or Password is invalid')
    return render(request, 'doctors/login.html')


def logoutPLS(request):
    logout(request)
    return redirect('doctors:login')

# @login_required(login_url='doctors:login') อยากให้ login ตรงไหนก็เอาไปใส่ช้างบน def นะ
# @allowed_users(allowed_roles=['xxxxx'])   กลุ่มของบท

def mcustomer(request):
    return render(request, "doctors/mcustomer.html")



@login_required(login_url='doctors:login')
def account(request):
    patient = request.user.patient
    form = accForm(instance=patient)

    if request.method == 'POST':
        form = accForm(request.POST, request.FILES, instance=patient)
        if form.is_valid():
            form.save()

    return render (request, 'doctors/acc.html', {'form': form})




def profile(request):
    return render(request, "doctors/profile.html")