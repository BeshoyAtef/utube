from django import template
import requests

register = template.Library()

@register.simple_tag
def get_size(url):
    vid = requests.head(url)
    size = vid.headers['content-length']
    return size