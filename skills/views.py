from django.shortcuts import render
from .models import Skill
# Create your views here.
def skill(request):
	skills = Skill.objects
	return render(request, 'skill/skill.html',{'skills':skills})