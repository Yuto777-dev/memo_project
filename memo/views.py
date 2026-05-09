from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from .models import Memo

class MemoListView(ListView):
    model = Memo
    temlate_name = 'memo/memo_list.html'

class MemoCreateView(CreateView):
    model = Memo
    tempate_name = 'memo/memo_form.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('index')