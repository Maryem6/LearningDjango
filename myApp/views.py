from django.shortcuts import render, redirect
from .models import Feature
from django.contrib.auth.models import User 
from django.contrib import messages, auth
# Create your views here.
def logout (request):
    auth.logout(request)
    return redirect('/')
def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect ('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repeatedPassword = request.POST["repeatedPassword"]

        if password == repeatedPassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used!')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('login')
        else:
            messages.info(request, 'The passwords do not match!')
            return redirect('register')
    else:
        return render(request, 'register.html')

def index (request):
    #feature1 = Feature()
    #feature1.id = 0
    #feature1.name = 'Fast'
    #feature1.is_true = True
    #feature1.details = 'Our service is very quick '

    #feature2 = Feature()
    #feature2.id = 1
    #feature2.name = 'Reliable'
    #feature2.is_true = True
    #feature2.details = 'Our service is very reliable '

    #feature3 = Feature()
    #feature3.id = 2
    #feature3.name = 'Easy to use'
    #feature3.is_true = False
    #feature3.details = 'Our service is easy to use '

    #feature4 = Feature()
    #feature4.id = 3
    #feature4.name = 'Affordable'
    #feature4.is_true = True
    #feature4.details = 'Our service is very affordable '

    #feature5 = Feature()
    #feature5.id = 4
    #feature5.name = 'Trustworthy'
    #feature5.is_true = False
    #feature5.details = 'Our service is filled with trust '

    #return render(request, 'index.html', {'feature1' : feature1, 'feature2' : feature2, 'feature3' : feature3, 'feature4': feature4})

    #features = [feature1, feature2, feature3, feature4, feature5]
    
    features = Feature.objects.all()
    return render(request, 'index.html', {'features' : features})