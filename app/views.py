from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import data
from django.core.paginator import Paginator

def home(request):
    view_data = data.objects.all()
    paginator = Paginator(view_data, 25) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'home.html',context = {'videos':view_data, 'page_obj': page_obj})

def search(request):        
    if request.method == 'GET': # this will be GET now
        name = request.GET.get('search')    # do some research what it does
        status = data.objects.filter(name__icontains=name) | data.objects.filter(language__icontains=name) | data.objects.filter(actor__icontains=name)| data.objects.filter(genre__icontains=name)|data.objects.filter(actor__icontains=name)|data.objects.filter(actor__icontains=name)
        return render(request, "search.html", {"songs": status})
    else:
        return render(request, "search.html", {})

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('details')
    messages.warning(request, 'Please check your credentials and try again')
    return render(request,'login.html')

@login_required
def adddetails(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        language = request.POST.get('language')
        actor = request.POST.get('actor')
        actress = request.POST.get('actress')
        released = request.POST.get('released')

        link = request.POST.get('link')
        duration = request.POST.get('duration')
        genre = request.POST.get('genre')
        result = data(name = name,language = language,actor = actor,actress = actress,released = released,link = link,duration = duration,genre = genre)
        if result:
            result.save()
            messages.info(request, 'Added Successfully')
        else:
            messages.warning(request, 'Something went wrong.. Try again')
        
    return render(request,'adddetails.html')

@login_required
def list_data(request):
    view_data = data.objects.all()
    return render(request,'list.html',context = {'videos':view_data})

def edit(request, id):  
    movielist = data.objects.get(id=id)  
    return render(request,'edit.html', {'employee':movielist})  

def update(request, id):  
    employee = Employee.objects.get(id=id)  
    form = EmployeeForm(request.POST, instance = employee)
    
    if form.is_valid():  
        form.save()  
        return redirect("/details")  

    return render(request, 'edit.html', {'employee': employee})  
def destroy(request, id):  
    movielist = data.objects.get(id=id)  
    movielist.delete()  
    return redirect("/details")  

@login_required
def exit(request):
    logout(request)
    return render(request,'login.html')

    