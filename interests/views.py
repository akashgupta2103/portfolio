from django.shortcuts import render
from .models import Interest
# Create your views here.
def interest(request):
    interests = Interest.objects
    return render(request, 'interest/interest.html',{'interests':interests})