from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

# Function-Based View
def home_view(request):
    return render(request, 'home.html')

# Class-Based View
class AboutView(View):
    def get(self, request):
        return render(request, 'about.html')
