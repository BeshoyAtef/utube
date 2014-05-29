from django import template
import requests
from django.template.defaultfilters import filesizeformat
import time

register = template.Library()

@register.simple_tag
def get_size(url):
    vid = requests.head(url)
    size = vid.headers['Content-Length']
    return filesizeformat(int(size))

@register.simple_tag 
def get_name(str_name):
    name_array=str_name.split('x')     
    try:         
        name=name_array[1]     
    except:
        name_array=str_name.split(' ')         
        try:             
            name = name_array[2]
            formated = name_array[3]             
            return name + '<span class="label label-danger">'+str(formated)+'</span>'         
        except:             
            name = str_name
            return name     
    return name+str('p')

@register.simple_tag 
def dur(dur_sec):
    return time.strftime('%H:%M:%S', time.gmtime(dur_sec))


