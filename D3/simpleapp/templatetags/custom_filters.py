from django import template

register = template.Library()


@register.filter(name='censor')
def cut(value):
    Mat = ["сука", "блять"]
    sentence = ""

    for word in value.lower().split():
        if word in Mat:
            sentence += '*** '
        else:
            sentence += word + ' '
    return sentence