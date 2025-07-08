from django.urls import path
from .views import home_view, AboutView

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', AboutView.as_view(), name='about'),
]
