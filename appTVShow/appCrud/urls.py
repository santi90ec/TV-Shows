from django.contrib import admin
from django.shortcuts import redirect
from django.urls import path
from django.urls.conf import include
from . import views
urlpatterns = [
    path('',views.index),
    path('shows',views.shows),
    path('shows/new',views.new),
    path('shows/new/created',views.created),
    path('shows/<int:number>',views.showinfo),
    path('shows/<int:number>/edit',views.edit),
    path('shows/<int:number>/edit/success',views.editSucc),
    path('shows/<int:number>/delete',views.delete)
]
