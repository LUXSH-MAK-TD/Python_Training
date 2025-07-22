from django.contrib import admin
from django.urls import path,include
from .views import registration_view, index_view, dashboard_view
from .views import send_message_view, inbox_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', registration_view, name='register'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('', index_view, name='index'),
    path('send-message/', send_message_view, name='send_message'),
    path('inbox/', inbox_view, name='inbox'),
]

admin.site.site_header = "Employee-System Admin Login "
admin.site.site_title = "Employee Admin Portal"
admin.site.index_title = "Welcome to Employee System Portal"