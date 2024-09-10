from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm 
from .models import Record
 
def home(request):
    #grabs every item in the databse table and assigns it to this variable
    records = Record.objects.all()

    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        #Authenticate
        user = authenticate(request, username=username, password =password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('home')
        else:
            messages.success(request, "There was an error logging in, please enter the correct etails and try again")
            return redirect('home')
    else:
        return render(request, 'home.html', {'records':records}) #empty context dictionary{}

# def login_user(request):
#     pass

#logout functionality
def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and Login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been successfully registered')
            return redirect('home')   
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form   })
    return render(request, 'register.html', {'form': form  })

def customer_records(request, pk):
    if request.user.is_authenticated:
        #look up records
        customer_records = Record.objects.get(id=pk)
        