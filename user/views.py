from django.contrib.auth import authenticate, login
from django.shortcuts import render,redirect
from django.contrib import messages
from user.forms import UserForm
from user.models import User,Seller,Bidder
from django.http import HttpResponse
from datetime import datetime
import mysql.connector as sql

# Global Variables
un = ''
pwd = ''

# Create your views here.
def index(request):
    return render(request, 'index.html')

def seller(request):
    if request.method=="POST":
        sc = request.POST.get('category')
        simg = request.FILES.get('image')
        ain = request.POST.get('bid_name')
        aip = request.POST.get('bid_value')
        aid = request.POST.get('bid_description')
        st = request.POST.get('actiontime')
        et = request.POST.get('endtime')
        fn = request.POST.get('fname')
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        bd = request.POST.get('bdate')
        gen = request.POST.get('optradio')
        street = request.POST.get('stadd')
        lnk = request.POST.get('lnk')
        cty = request.POST.get('city')
        stat = request.POST.get('state')
        pin = request.POST.get('post')
        aadh = request.POST.get('aadhar')
        pan = request.POST.get('pan')
        UPI = request.POST.get('upi')
        bank = request.POST.get('bank')
        POA = request.POST.get('poa')
        en = Seller(sc=sc,simg=simg,ain=ain,aip=aip,aid=aid,st=st,et=et,fn=fn,em=em,ph=ph,bd=bd,gen=gen,street=street,lnk=lnk,cty=cty,stat=stat,pin=pin,aadh=aadh,pan=pan,UPI=UPI,bank=bank,POA=POA)
        en.save()
        data1 = Seller.objects.all()
        return render(request, 'dashboard.html',{'datas':data1})
    return render(request, 'seller.html')

# def product(request):

def bidder(request):
    if request.method=="POST":
        fn = request.POST.get('fname')
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        bd = request.POST.get('bdate')
        gen = request.POST.get('optradio')
        street = request.POST.get('stadd')
        lnk = request.POST.get('lnk')
        cty = request.POST.get('city')
        stat = request.POST.get('state')
        pin = request.POST.get('post')
        aadh = request.POST.get('aadhar')
        pan = request.POST.get('pan')
        UPI = request.POST.get('upi')
        bank = request.POST.get('bank')
        en = Bidder(fn=fn,em=em,ph=ph,bd=bd,gen=gen,street=street,lnk=lnk,cty=cty,stat=stat,pin=pin,aadh=aadh,pan=pan,UPI=UPI,bank=bank)
        en.save()
        data2 = Bidder.objects.all()
        return render(request, 'productpage.html',{'datas':data2})
    return render(request, 'bidder.html')

def data(request):
    data1 = Seller.objects.all()
    return render(request, "dashboard.html",{'datas':data1})

def userlogin(request):
    return render(request,"signin.html")

def signin(request):
    global un,pwd
    if request.method == 'POST':
        m = sql.connect(host="localhost", user="root", password="root", database="djangopy")
        cursor = m.cursor()
        d = request.POST
        for key, value in d.items():
            if key == "uname":
                un = value
            if key == "upass":
                pwd = value
        c = "select * from user where username='{}' and password='{}'".format(un, pwd)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            messages.error(request, "User does not Exists!")
            return render(request, 'signin.html')
        else:
            data1 = Seller.objects.all()
            return render(request, 'dashboard.html',{'datas':data1})

    return render(request, 'signin.html')

def usr(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = UserForm()
    return render(request,'usr.html',{'form':form})

# register
def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            try:
                form.save()
            except:
                messages.error(request, "User Already Exists!")
                form = UserForm()
                return render(request, 'register.html',{'form':form})
        return render(request,"signin.html",{'form':form})
    else:
        form = UserForm()
    return render(request, 'register.html',{'form':form})

# view records
def show(request):
    users = User.objects.all()
    return render(request, "show.html",{'users':users})

def profile(request):
    return render(request, "profile.html")

def product(request,id):
    seller = Seller.objects.get(id=id)
    print(seller)
    return render(request, "productpage.html",{'data':seller})