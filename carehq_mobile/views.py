# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from django.template.context import RequestContext

@login_required
def carehq_mobile(request, template='carehq_mobile/shine-ui.html'):
    if not request.user:
        return HttpResponseRedirect("/")
    if not request.user.api_key:
        return Http404()
    context = dict()
    context['key'] = request.user.api_key.key
    return render_to_response(template, context, context_instance=RequestContext(request))