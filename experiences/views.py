from django.shortcuts import render, get_object_or_404
from .models import Experience
# Create your views here.

def experience(request):
    experiences = Experience.objects
    return render(request, 'experience/experience.html',{'experiences':experiences})

	
def detail(request, exp_id):
    exp_detail = get_object_or_404(Experience, pk=exp_id)
    return render(request, 'experience/detail.html',{'experience':exp_detail})

	
	
	
