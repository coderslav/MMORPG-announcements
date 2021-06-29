from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import AnnForm, CommentForm
from .models import *
from django.contrib.auth.mixins import LoginRequiredMixin


class MainPageView(ListView):
    model = Announcement
    template_name = 'main.html'
    ordering = ['-ann_time_in']


class AnnDetails(LoginRequiredMixin, DetailView):
    model = Announcement
    template_name = 'details.html'

    def post(self, request, pk):
        comment_for_change = Comment.objects.get(id=request.POST.get('a_c_n_c_id'))
        comment_for_change.com_confirmed = True
        comment_for_change.save(update_fields=['com_confirmed'])
        return redirect('ann_details', pk)


class AnnCreate(LoginRequiredMixin, CreateView):
    template_name = 'create.html'
    form_class = AnnForm


class AnnDelete(LoginRequiredMixin, DeleteView):
    template_name = 'delete.html'
    success_url = '/'  # TODO avoid HardCodding
    queryset = Announcement.objects.all()  # TODO try change with model = Announcement


class AnnEdit(LoginRequiredMixin, UpdateView):
    template_name = 'edit.html'
    form_class = AnnForm
    queryset = Announcement.objects.all()  # TODO try change with model = Announcement


class CommentCreate(LoginRequiredMixin, CreateView):
    template_name = 'comment_create.html'
    form_class = CommentForm


class CommentDetails(LoginRequiredMixin, DetailView):
    model = Comment
    template_name = 'comment_details.html'


class CommentList(LoginRequiredMixin, ListView):
    model = Comment
    template_name = 'comment_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_comments'] = Comment.objects.filter(com_author=self.request.user).order_by('-com_time_in')
        return context


class CommentDelete(LoginRequiredMixin, DeleteView):
    template_name = 'comment_delete.html'
    success_url = '/comments/'  # TODO avoid HardCodding
    queryset = Comment.objects.all()  # TODO try change with model = Comment


class CommentEdit(LoginRequiredMixin, UpdateView):
    template_name = 'comment_edit.html'
    form_class = CommentForm
    queryset = Comment.objects.all()  # TODO try change with model = Comment


class PrivateAccount(LoginRequiredMixin, ListView):
    model = Announcement
    template_name = 'private_account.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['anns'] = Announcement.objects.filter(ann_author=self.request.user).order_by('-ann_time_in')
        return context

    def post(self, request):
        comment_for_change = Comment.objects.get(id=request.POST.get('comment_id'))
        comment_for_change.com_confirmed = True
        comment_for_change.save(update_fields=['com_confirmed'])
        return redirect('private_account')


class CommentDeleteByAnnAuthor(LoginRequiredMixin, DeleteView):
    template_name = 'comment_delete_by_ann_author.html'
    success_url = '/private/'  # TODO avoid HardCodding
    queryset = Comment.objects.all()  # TODO try change with model = Comment

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ann'] = Announcement.objects.get(comment=context['comment'])
        return context
