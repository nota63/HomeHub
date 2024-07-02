"""
URL configuration for home project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from xml.etree.ElementInclude import include

from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.home2, name='home2'),
    path("schedule_work/", views.schedule_work, name='schedule_work'),
    path("confirmation/", views.confirmation, name='confirmation'),
    path("summery/", views.summery, name='summery'),
    path("request_changes/", views.request_changes, name='request_changes'),
    path("charge/", views.charge, name='charge'),
    path("admin_password/", views.admin_password, name='admin_password'),
    path("admin_home/", views.admin_home, name='admin_home'),
    path("generate_bills/", views.generate_bills, name='generate_bills'),
    path("view_team/", views.view_team, name='view_team'),
    path("view_rates/", views.view_rates, name='view_rates'),
    path("special/", views.special, name='special'),
    path("cancel/", views.cancel, name='cancel'),
    path("manage_admin_passwords/", views.manage_admin_passwords, name='manage_admin_passwords'),
    path('feedback/', include('feedback.urls')),
    path('security', include('allauth.urls')),
    path('', include('security.urls')),
    path("what_we_are/",views.what_we_are,name='what_we_are'),
    path("about_owner/",views.about_owner,name='about_owner'),

]
