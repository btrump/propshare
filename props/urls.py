from django.conf.urls import patterns, url
from props.models import Prop

urlpatterns = patterns('props.views',
    url(r'^(?P<owner>[-\w]+)/(?P<slug>[-\w]+)/$',
        'detail',
        name='prop_detail'),
    url(r'^$',
        'index',
        name='prop_list'),
)
