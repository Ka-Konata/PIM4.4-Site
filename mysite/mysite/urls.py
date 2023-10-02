"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from dotenv import load_dotenv
import os

# Setando as minhas próprias variáveis de ambiente
load_dotenv()
print(os.environ["API_URL"])

urlpatterns = [
    path('admin/', admin.site.urls),
    path("login/", include("login.urls")),
    path("area_do_analistarh/", include("area_do_analistarh.urls"))
]