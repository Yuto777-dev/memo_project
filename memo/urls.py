from django.urls import path
from .views import MemoListView,MemoCreateView

urlpatterns = [
    path('', MemoListView.as_view(), name = 'index'),
    path('new/', MemoCreateView.as_view(), name='create'),
]