from django import template
from hello.models import *

register = template.Library()

'''
   10 popular tags for sidebar.
   Usage for: includes/menus.html

{% load globaltags %}
{% populartags as populartags_list %}
{% for tag in populartags_list %}
  <a href="{% url 'tag_posts_page' slug=tag.slug %}">
    {{ tag.title }} <span class="badge">{{ tag.total }}</span>
  </a>
{% empty %}
  <p>No tags yet!</p>
{% endfor %}
'''


@register.inclusion_tag('blog.html')
def populartags():
    tags_queryset = TagsforBlog.objects.all()
    mapping = [
        {
            'tag': tag,
            'total': Blog.objects.all().filter(tags__slug=tag.tagslug).count()
        } for tag in tags_queryset
    ]
    mapping.sort(key=lambda x: int(x['total']), reverse=True)
    print (mapping)
    return {'populartags':mapping[:5]}


@register.inclusion_tag('blog.html')
def recentposts():
    posts = Blog.objects.all()
    print (posts)
    return {'recentposts':posts[:4]}
