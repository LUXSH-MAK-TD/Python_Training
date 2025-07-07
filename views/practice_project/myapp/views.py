from django.shortcuts import render

def home(request):
    
    return render(request, 'myapp/home.html')

from django.views import View

class AboutView(View):
    def get(self, request):
        
        return render(request, 'myapp/about.html')
