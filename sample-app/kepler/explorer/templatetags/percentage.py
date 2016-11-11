from django import template

register = template.Library()

@register.simple_tag
def percentage(lower, upper):
    if not lower or not upper:
        return
    return lower / upper * 100