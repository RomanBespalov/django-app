from django import template


register = template.Library()


@register.inclusion_tag('recursive_menu.html', takes_context=True)
def draw_menu(context, parent_item=None):
    main_items = parent_item.children.all()
    return {'main_items': main_items, 'request': context['request']}
