from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from mstudapp.models import course
from mstudapp.models import students
# Create your views here.
def home(request):
    return render(request,'home.html')
def signup(request):
    return render(request,'register.html')
def usercreate(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exists !!!!')
                return redirect('signup')
            else:
                user=User.objects.create_user(
                    first_name=first_name,
                    last_name=last_name,
                    username=username,
                    password=password,
                    email=email)
                user.save()
                print('Success....')
        else:
            messages.info(request,'Password doesnt match')
            print("Password is not matching...")
            return redirect('signup')
        return redirect('loginpage')
    else:
        return render(request,'register.html')

def loginpage(request):
    return render(request,'login.html')
def login1(request):
 if request.method == 'POST':
    username=request.POST['username']
    password=request.POST['password']
    user = auth.authenticate(username=username, password=password) 
    request.session["uid"]=user.id#session method part
    if user is not None:
        auth.login(request,user)
        messages.info(request,f'Welcome{username}')
        return redirect('login1')
    else:
        messages.info(request,'Invalid Username or Password. Try again.')
        return redirect('loginpage')
 else:
     return redirect('loginpage')
#@login_required(login_url='loginpage')#(login_required method part)
def logout(request):
    #if request.user.is_authenticated:(is authenticated method part)
    request.session["uid"] = ""#session method part
    auth.logout(request)
    return redirect('home')
#@login_required(login_url='loginpage')#(login_required method part)
def about(request):
    if 'uid' in request.session:#session method part
    #if request.user.is_authenticated:#(is authenticated method part)
        return render(request,'about.html') 
    return render(request,'login.html')#(is authenticated method part)&#session method part
#@login_required(login_url='loginpage')   
def addc(request):
    if 'uid' in request.session:
        if request.method=='POST':
            cname=request.POST['name']#in square bracket is form name
            price=request.POST['price']
            duration=request.POST['duration']
            c=course(name=cname,duration=duration,price=price)#in round barcket first one is any variable , second one after '=' isa variable given in previous steps(steps 10-13)
            c.save()
        return render(request,'addcourse.html')
    return render(request,'login.html')

#@login_required(login_url='loginpage')
def adds(request):
    if 'uid' in request.session:
        if request.method=='POST':
            sname=request.POST['name']#in square bracket is form name
            age=request.POST['age']
            courses=request.POST['courses']
            s=students(name=sname,age=age,courses=courses)#in round barcket first one is any variable , second one after '=' isa variable given in previous steps(steps 10-13)
            s.save()
        return render(request,'addstudent.html')
    return render(request,'login.html')
#@login_required(login_url='loginpage')
def show(request):
    if 'uid' in request.session:   
        student=students.objects.all()
        return render(request,'show.html',{'student':student})
    return render(request,'login.html')
    