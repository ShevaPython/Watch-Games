from django import template
from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    """Вернуть количество постов"""
    return Post.published.count()

@register.simple_tag(name='post_tags_all')
def return_all_tags():
    """Вернуть все теги поста"""
    return Post.tags.all()