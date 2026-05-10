from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from .models import Memo
from .form import MemoForm

class MemoListView(ListView):
    model = Memo
    temlate_name = 'memo/memo_list.html'

class MemoCreateView(CreateView):
    model = Memo
    form_class = MemoForm
    tempate_name = 'memo/memo_form.html'
    success_url = reverse_lazy('index')