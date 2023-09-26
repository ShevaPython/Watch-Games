from django import template
from django.utils.safestring import mark_safe
import markdown
from ..models import Post

register = template.Library()


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))


@register.simple_tag
def total_posts():
    """Вернуть количество постов"""
    return Post.published.count()


@register.simple_tag(name='post_tags_all')
def return_all_tags():
    """Вернуть все теги поста"""
    return Post.tags.all()


@register.inclusion_tag('blog/latest_posts.html')
def show_latest_posts(count=3):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}
