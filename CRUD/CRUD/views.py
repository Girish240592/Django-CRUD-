from django.shortcuts import render,redirect
from app.models import Employees

def INDEX(request):
    data = Employees.objects.all()
    
    context = {
        'd' : data,
        }
    return render(request, 'index.html', context)

    

def ADD(request):
    if request.method == 'POST':
        n = request.POST.get('name')
        e = request.POST.get('email')
        a = request.POST.get('address')
        p = request.POST.get('phone')
        
        d=Employees(name=n,email=e,address=a,phone=p)
        d.save()
        return redirect('read')
    return redirect(request, 'index.html')

def EDIT(request):
    emp=Employees.objects.all()
    context ={'emp':emp}
    return redirect(request, 'index.html',context)