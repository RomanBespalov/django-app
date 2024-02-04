from django.shortcuts import render

from .models import MenuItem


def render_menu(request):
    main_items = MenuItem.objects.filter(parent__isnull=True)
    return render(request, 'recursive_menu.html', {'main_items': main_items})
