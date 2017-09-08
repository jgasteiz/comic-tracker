from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import TemplateView, FormView

from dashboard.forms import FetchComicsForm
from .models import Comic
from .scrapers import NewComicsParser


class DashboardHomeView(TemplateView):
    template_name = 'dashboard/index.html'


class DashboardLoginView(LoginView):
    template_name = 'dashboard/login.html'

    def get_success_url(self):
        return reverse('dashboard:home')


class FetchComics(FormView):
    form_class = FetchComicsForm
    template_name = 'dashboard/fetch_comics.html'

    def get_context_data(self, **kwargs):
        ctx = super(FetchComics, self).get_context_data(**kwargs)
        date = self.request.GET.get('date')
        ctx['comic_list'] = Comic.objects.nearest_wednesday_comics(date)
        return ctx

    def form_valid(self, form):
        date = form.cleaned_data.get('date')
        parser = NewComicsParser()
        parser.parse(date=date)
        messages.add_message(self.request, messages.INFO, 'Comics have been fetched for the `{}`'.format(date))
        return redirect('{url}?date={date}'.format(url=reverse('dashboard:fetch_comics'), date=date))


fetch_comics = FetchComics.as_view()
login = DashboardLoginView.as_view()
home = DashboardHomeView.as_view()
