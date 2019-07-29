from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

# Create your views here.
class HomePageView(TemplateView):
	template_name = 'teenagers/home.html'