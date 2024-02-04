from django.urls import path

from menu.views import render_menu

urlpatterns = [
    path('menu/', render_menu, name='render_menu'),
]
