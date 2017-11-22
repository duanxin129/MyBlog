from django import template
from django.db.models import Count

from ..models import Post,Category,Tag

register = template.Library()

@register.assignment_tag
def get_recent_posts(num=5):
 return Post.objects.all().order_by('-create_time')[:num]

@register.assignment_tag
def archives():
 return Post.objects.dates('create_time', 'month', order='DESC')

@register.assignment_tag
def get_categories():
 return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.assignment_tag
def get_categories():
 return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)

@register.assignment_tag
def get_tags():
 # 记得在顶部引入 Tag model
 return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)