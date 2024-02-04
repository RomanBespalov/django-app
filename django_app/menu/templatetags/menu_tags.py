# templatetags/menu_tags.py
from django import template
from menu.models import MenuItem

register = template.Library()


@register.simple_tag
def draw_menu(menu_items, current_path):
    return {'menu_items': menu_items, 'current_path': current_path}


@register.inclusion_tag('menu_item.html', takes_context=True)
def draw_menu_item(context, item):
    context['item'] = item
    context['children'] = item.children.all()
    return context
