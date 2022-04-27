from django import template

from polls.models import Question

register = template.Library()

@register.simple_tag()
def get_categories():
    return Question.objects.all()

@register.inclusion_tag('book/list_categories.html')
def show_categories():
    cats = Question.objects.all()
    return {"cats2": cats}