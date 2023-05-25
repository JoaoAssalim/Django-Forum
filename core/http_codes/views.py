from django.http import HttpResponse
from django.template import loader


def handler403(request, *args, **argv):
    context = {}
    html_template = loader.get_template('http_codes/page-403.html')

    return HttpResponse(html_template.render(context, request), status=403)


def handler404(request, *args, **argv):
    context = {}
    html_template = loader.get_template('http_codes/page-404.html')

    return HttpResponse(html_template.render(context, request), status=404)


def handler500(request, *args, **argv):
    context = {}
    html_template = loader.get_template('http_codes/page-500.html')

    return HttpResponse(html_template.render(context, request), status=500)