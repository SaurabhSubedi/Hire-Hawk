from django import template

register = template.Library()

@register.filter
def period_split(value):
    return value.split('.')