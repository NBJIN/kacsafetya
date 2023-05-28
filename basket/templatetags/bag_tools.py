from django import template


register = template.Library()


@register.filter(name='calc_total')


def calc_total(fee, quantity):
    return fee * quantity
