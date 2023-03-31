from django.shortcuts import render
from django.core.mail import send_mail


# Create your views here.
def home(request):
    return render(request,'home.html',{})

def contact(request):
    if request.method == "POST":
       name = request.POST['name']
       emailname = request.POST['emailname']
       mobilename = request.POST['mobilename']
       Message = request.POST['Message']
       send_mail(
           name,
           Message,
           emailname,
           ['aagrata1@gmail.com'],
           
       )
       
       return render(request,'contact.html',{ 'name': name})

    else:
        return render(request,'contact.html',{})
