from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm,TransferCreationForm
from django.contrib.auth import login,logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Bank_Account,Transfer
from django.contrib.auth.decorators import login_required
from django.contrib import messages
def index(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('home')

    else:
        form=AuthenticationForm()
        if request.user.is_authenticated:
            return redirect('home')

    context={
        'form':form
        }
    return render(request,'index.html',context)


def register(request):
    if request.method=='POST':
        form=CustomUserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request,user)
            New_Balance_Account=Bank_Account(owner=user,balance=500)
            New_Balance_Account.save()
            return redirect('home')

    else:
        form=CustomUserCreationForm()
    context={
        'form':form
    }
    return render(request,'register.html',context)


@login_required
def home(request):

    context={
        'user':request.user
    }
    return render(request,'home.html',context)


def logout_user(request):
    logout(request)
    return redirect('index')


def status(request):
    Usser_Account=Bank_Account.objects.get(owner=request.user)
    Movements=Usser_Account.movements.all().order_by('-Date')
    
    
    context={
        'user':Usser_Account,
        'movements':Movements,
        
    }
    return render(request,'status.html',context)

def withdraw(request):
    User_Account=Bank_Account.objects.get(owner=request.user)
    if request.method=='POST':
        Money=request.POST['amount']
        if int(Money)<=User_Account.balance and int(Money)>0:
            User_Account.balance-=int(Money)
            movement=User_Account.movements.create(money=int(Money),Type_Movement="Withdraw")
            User_Account.movements.add(movement)
            User_Account.save()
            return redirect('status')
        else:
            messages.error(request,'You dont have enough money')
            return redirect('withdraw')
        
    context={
        'user':User_Account,
    }
    return render(request,'withdraw.html',context)

def deposit(request):
    User_Account=Bank_Account.objects.get(owner=request.user)
    if request.method=='POST':
        Money=request.POST['money']
        if int(Money)<=0:
            messages.error(request,'You cant deposit negative numbers or zero')
            return redirect('deposit')
        
        else:
            User_Account.balance+=int(Money)
            movement=User_Account.movements.create(money=int(Money),Type_Movement="Deposit")
            User_Account.movements.add(movement)
            User_Account.save()
            return redirect('status')
    context={
        'user':User_Account,
    }
    return render(request,'deposit.html',context)

def inf_movement(request,pk):
    user=Bank_Account.objects.get(owner=request.user)
    Movement=user.movements.get(id=pk)
    print(Movement.id)
    if Movement.Type_Movement=="Transfer":
        Movement=Transfer.objects.get(id=pk)
        print(Movement.id)
    context={
        'movement':Movement,
    }
    return render(request,'inf_mov.html',context)


def transfer(request):
    user=Bank_Account.objects.get(owner=request.user)
    if request.method=='POST':
        Money=request.POST['money']
        if int(Money)>user.balance:
            messages.error(request,'You dont have enough money')
            return redirect('transfer')
        
        elif int(Money)<=0:
            messages.error(request,'You cant transfer negative numbers or zero')
            return redirect('transfer')
        
        else:
            form=TransferCreationForm(request.POST)
            if form.is_valid():
                transfer=form.save(commit=False)
                transfer.transmitter=user
                transfer.Type_Movement="Transfer"
                transfer.save()
                transfer.receiver.balance+=int(Money)
                user.balance-=int(Money)
                user.movements.add(transfer)
                transfer.receiver.movements.add(transfer)
                transfer.receiver.save()
                user.save()
                
                return redirect('status')
        
        

    else:
        form=TransferCreationForm()
        

    context={
        'form':form,
        'user':user,
    }

    return render(request,'transfer.html',context)

