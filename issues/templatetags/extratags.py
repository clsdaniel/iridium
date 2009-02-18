from django import template

register = template.Library()

@register.filter
def lookup(value, arg):
    return arg[value]
