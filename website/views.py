from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record
 
def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You are now logged in")
            return redirect('home')
        else:
            messages.error(request, "Invalid login details. Please try again.")
            return redirect('home')
    return render(request, 'home.html', {'records': records})
 #empty context dictionary{}

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
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'You have been successfully registered')
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def customer_records(request, pk):
    if request.user.is_authenticated:
        #look up records
        customer_records = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_records': customer_records})
    else:
        messages.success(request, 'Must be logged in to view this page ')
        return redirect('home')  

def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk) 
        delete_it.delete()
        messages.success(request, 'Record Deleted Successfully ')
        return redirect('home') 
    else:
        messages.success(request, 'You must be logged in before you can perform this action')
        return redirect('home')

def add_record(request):
    if request.user.is_authenticated:
        form = AddRecordForm(request.POST or None)
        if request.method == 'POST':
            if form.is_valid():
                form.save()
                messages.success(request, 'Record added successfully')
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.error(request, 'You must be logged in to add a record')
        return redirect('home')
