from django import template

register = template.Library()

@register.simple_tag
def percentage(lower, upper):
    return lower / upper * 100