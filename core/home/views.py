from django.views import View
from django.views.generic.base import TemplateView, RedirectView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseNotFound


class FeedView(LoginRequiredMixin, TemplateView):
    login_url = 'login'
    template_name = 'dash/home/index.html'


class RedirectFeedView(LoginRequiredMixin, RedirectView):
    login_url = 'login'
    pattern_name = 'feed'


def page_404(request):
    return HttpResponseNotFound()