from django.shortcuts import render,HttpResponse,redirect
from .models import feedback,fiup
from django.core.mail import send_mail, EmailMessage
from django.contrib.auth.models import User
from .forms import regist
from django.contrib.auth.decorators import login_required
# Create your views here.


def first(request):
    a='<h1>jklsdf</h1>'
    return HttpResponse(a)

def home(request):
    x=feedback.objects.all()
    return render(request,'home.html',{'data':x})

def con(request):
    x=feedback()
    if request.method=='POST':
        a=request.POST['nams']
        b=request.POST['num']
        c=request.POST['fed']
        x.User_Name=a
        x.Mobile=b
        x.FeedBack=c
        x.save()
        return redirect('ho')
    return render(request,'contact.html')

def ab(request):
    x=fiup()
    if request.POST:
        a=request.POST['nam']
        b=request.FILES['fi']
        fiup.objects.create(f_name=a,file=b).save()
        subject='This is Django'
        message = f'This is a test email sent from Django. Filename: {a}, File: {b}'
        from_email = 'stathamarun@gmail.com'
        recipient_list = ['meyyappan1301@gmail.com']
        email = EmailMessage(subject, message, from_email, recipient_list)
        email.attach(b.name, b.read(), b.content_type)

        # Send the email
        email.send()

    return render(request,'about.html')

def dele(request,id):
    a=feedback.objects.get(id=id)
    a.delete()
    return redirect('ho')

def upe(request,id):
    a=feedback.objects.get(id=id)
    if request.method=='POST':
        x=request.POST['nams']
        b=request.POST['num']
        c=request.POST['fed']
        a.User_Name=x
        a.Mobile=b
        a.FeedBack=c
        a.save()
        return redirect('ho')
    return render(request,'upda.html',{'single':a})


def regi(request):
    x=regist()
    if request.method=='POST':
        a=request.POST['username']
        b=request.POST['email']
        pas1=request.POST['password1']
        pas2=request.POST['password2']
        if pas1==pas2:
            user=User.objects.create_user(username=a,email=b,password=pas2)
            user.is_staff=True
            user.is_superuser=True
            user.save()
            return redirect('lo')
    return render(request,'register.html',{'auto':x})

@login_required
def dash(request):
    return render(request,'dashbo.html')