from django.shortcuts import render,HttpResponse,redirect
from django.views import View
from ecomapp.models import Msg

# Create your views here.
def about(request):
    return HttpResponse("This is about page!")

def content(request):
    return HttpResponse("This is content page!")

def edit(request,rid):
    print("Id to be edited is:",rid)
    return HttpResponse("Id is to be edited is :"+ rid)

class SimpleView(View):
    def get(self,request):
        return HttpResponse("Hello from Simple View")

def hello(request):
    context={}
    context['name']="ABC"
    context['id']=123
    context['x']=20
    context['y']=100
    context['list']=[10,20,30,40,50]
    return render(request,'hello.html',context)

def create(request):
    #print("Request is:",request.method)
    if request.method=="GET":
        return render(request,'create.html')
    else:
        n=request.POST['uname']
        mail=request.POST['email']
        mob=request.POST['mob']
        msg=request.POST['msg']
        print("Name :",n, "E-mail:",mail, "Mob num:",mob, "Msgs:",msg)
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()

        return redirect("/dashboard")

def dashboard(request):
    m=Msg.objects.all()
    #print(m)
    context={}
    context['data']=m
    return render(request,'dashboard.html',context)

def delete(request,rid):
    m=Msg.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')

def edited(request,rid):
    if request.method=="GET":
        m=Msg.objects.get(id=rid)
        context={}
        context['data']=m
        return render(request,'edit.html',context)
    else:
        n=request.POST['uname']
        mail=request.POST['email']
        mob=request.POST['mob']
        msg=request.POST['msg']
        #print(n)
        #print(mail)
        m=Msg.objects.get(id=rid)
        m.delete()
        m=Msg.objects.create(name=n,email=mail,mobile=mob,msg=msg)
        m.save()
        return redirect('/dashboard')