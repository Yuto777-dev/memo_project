from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Memo
from .form import MemoForm

class MemoListView(ListView):
    model = Memo
    template_name = 'memo/memo_list.html'

class MemoCreateView(CreateView):
    model = Memo
    form_class = MemoForm
    template_name = 'memo/memo_form.html'
    success_url = reverse_lazy('index')

class MemoUpdateView(UpdateView):
    model = Memo
    form_class = MemoForm
    template_name = 'memo/memo_form.html'
    success_url = reverse_lazy('index')

class MemoDeleteView(DeleteView):
    model = Memo
    template_name = 'memo/memo_confirm_delete.html'
    success_url = reverse_lazy('index')