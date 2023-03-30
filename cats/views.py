from django.shortcuts import render
from .models import Cat

# Create your views here.
def cats(request):
    cats = Cat.objects.all()
    return render(request, 'cats.html',{'catss': cats})