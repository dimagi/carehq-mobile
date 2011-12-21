# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template.context import RequestContext

@login_required
def carehq_mobile(request, template='carehq_mobile/shine-ui.html'):
    return render_to_response(template, {}, context_instance=RequestContext(request))