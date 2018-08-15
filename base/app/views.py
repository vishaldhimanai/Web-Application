from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def index(request):
	"""The home page for Vishal Dhiman AI"""
	return render(request, 'app/index.html')