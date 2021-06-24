from django.contrib import auth
from django.shortcuts import redirect
from django.views.generic import ListView, DetailView
from .models import *


def logout(request):
    auth.logout(request)
    return redirect('/')


class MainPageView(ListView):
    model = Announcement
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class PersonalAccount(DetailView):
    model = Announcement
    template_name = 'personal_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ann_comments'] = Comment.objects.filter(com_ann=context['announcement'], com_confirmed=True)
        context['ann_comments_not_confirmed'] = Comment.objects.filter(com_ann=context['announcement'],
                                                                       com_confirmed=False)
        context['user'] = self.request.user
        return context

    def post(self, request, pk):
        comment_for_change = Comment.objects.get(id=request.POST.get('a_c_n_c_id'))
        comment_for_change.com_confirmed = True
        comment_for_change.save()
        return redirect(f'/ann/{pk}')
