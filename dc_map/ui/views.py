from django import http
from django.shortcuts import render
from ui import models


def home(request):
    return render(
        request,
        template_name='home.html',
    )


def datacenters(request):
    dcs = models.Datacenter.objects\
        .order_by('provider__name')\
        .values()
    return http.JsonResponse(
        data=list(dcs),
        safe=False,
    )
