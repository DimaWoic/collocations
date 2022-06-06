from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DeleteView
from .models import Category, Collocation

# Create your views here.


class UserLoginView(LoginView):
    template_name = 'collocations/login.html'
    redirect_authenticated_user = True
    error_css_class = 'errors'
    set_expiry = 86200

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['next'] = reverse_lazy('index')
        return context


class UserLogoutView(LoginRequiredMixin, LogoutView):
    next_page = 'login'


class CollocationsIndexView(LoginRequiredMixin, CreateView):
    model = Collocation
    template_name = 'collocations/collocations_index.html'
    template_name_suffix = '_index'
    login_url = reverse_lazy('login')
    fields = ['phrase', 'translation', 'category']
    success_url = reverse_lazy('index')

    def get_login_url(self, **kwargs):
        super().get_login_url(**kwargs)
        login_url = reverse_lazy('login')
        return login_url

    def get_context_data(self, **kwargs):
        context = super(CollocationsIndexView, self).get_context_data()
        context['records'] = self.model.objects.all()
        return context

