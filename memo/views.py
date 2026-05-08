from django.views.generic import ListView
from .models import Memo

class MemoListView(ListView):
    model = Memo
    temlate_name = 'memo/memo_list.html'