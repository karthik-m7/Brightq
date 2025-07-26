from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    print('Hello World !')
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to database
        Contact.objects.create(name=name, phone=phone, email=email, message=message)

        return HttpResponse("Thanks for contacting us!")  # Or redirect, or show success
    return render(request,'index.html')
