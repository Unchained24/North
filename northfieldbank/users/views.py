from django.shortcuts import render, redirect
from .models import Reg
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required



from .forms import ProfileForm

# Create your views here.

def logoutUser(request):
    logout(request)

    return redirect ("home")
    # return render(request, "webpage/home.html")

@login_required(login_url='home')
def dashboard(request):
   
    return render(request, "users/dashboard.html")


@login_required(login_url='home')
def accountsummary(request):
   
    return render (request, "users/accountsummary.html")

@login_required(login_url='home')
def accountdetails(request):
   
    return render (request, "users/accountdetails.html")

@login_required(login_url='home')
def creditcards(request):
    return render (request, "users/creditcards.html")

@login_required(login_url='home')
def contactus(request):
    return render (request, "users/contactus.html")

@login_required(login_url='home')
def billpaycenter(request):

    return render(request, "users/billpaycenter.html")

@login_required(login_url='home')
def deletepaytoaccount(request):

    return render (request, "users/deletepaytoaccount.html")

@login_required(login_url='home')
def paynow(request):

    return render (request, "users/paynow.html")

@login_required(login_url='home')
def paynowc(request):

    return render (request, "users/paynowc.html")

@login_required(login_url='home')
def searchpaytolist(request):

    return render (request, "users/searchpaytolist.html")

@login_required(login_url='home')
def beneficiary(request):

    return render (request, "users/beneficiary.html")

@login_required(login_url='home')
def addbeneficiery(request):

    return render (request, "users/add-beneficiery.html")

def profile(request):
    
    reg = request.user.reg
    form = ProfileForm(instance=reg)

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=reg)
        if form.is_valid():
            form.save()

    context ={'form':form}
    return render (request, "users/profile.html", context)

def changepin(request):

    return render(request, "users/pin.html")

def changepassword(request):

    
    return render(request, "users/changepassword.html")

def transfer(request):

    messages.warning(request, "This account is RESTRICTED and cannot perfom this operation!")
    
    return redirect('dashboard')

    