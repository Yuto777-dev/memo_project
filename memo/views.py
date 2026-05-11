from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Memo
from .form import MemoForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

class MemoListView(LoginRequiredMixin,ListView):
    model = Memo
    template_name = 'memo/memo_list.html'
    def get_queryset(self):
        return Memo.objects.filter(user=self.request.user)

class MemoCreateView(LoginRequiredMixin,CreateView):
    model = Memo
    form_class = MemoForm
    template_name = 'memo/memo_form.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MemoUpdateView(LoginRequiredMixin,UpdateView):
    model = Memo
    form_class = MemoForm
    template_name = 'memo/memo_form.html'
    success_url = reverse_lazy('index')
    def get_queryset(self):
        return Memo.objects.filter(user=self.request.user)


class MemoDeleteView(LoginRequiredMixin,DeleteView):
    model = Memo
    template_name = 'memo/memo_confirm_delete.html'
    success_url = reverse_lazy('index')
    def get_queryset(self):
        return Memo.objects.filter(user=self.request.user)

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'auth/signup.html'
    success_url = reverse_lazy('login')
