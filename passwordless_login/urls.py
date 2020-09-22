from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/login/generate', views.generate, name='generate'),
    path('auth/login/validate', views.validate, name='validate')
]
