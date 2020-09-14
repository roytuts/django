from django import template

register = template.Library()

@register.filter(name='split')
def split(str, key):
    return str.split(key)

@register.filter
def get_by_index(a, i):
    return a[i]