from django.shortcuts import render,HttpResponse
from .models import Message

def homePageLogic(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        Message.objects.create(name=name, email=email, message=message)
        return HttpResponse("Thank you for your message! We will get back to you soon.")
    return render(request, "index.html")
