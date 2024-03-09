from django.shortcuts import render
from .models import*

context = {
        'posts':Post.objects.all(),
        }
def home(request):
    return render(request,'app/home.html',context)

def about(request):
    return render(request, 'app/about.html', {'title': 'About page'})

