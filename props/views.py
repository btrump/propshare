from props.models import Prop
from django.contrib.auth.models import User
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

def index(request, *args, **kwargs):
  props = Prop.objects.all()
  context = RequestContext(request, {'props':props})
  return render_to_response('props/index.html', context)

def detail(request, *args, **kwargs):
  owner = get_object_or_404(User, username=kwargs['owner'])
  prop = get_object_or_404(Prop, slug=kwargs['slug'], owner=owner.id)
  context = RequestContext(request, {'prop':prop})
  return render_to_response('props/detail.html', context)
