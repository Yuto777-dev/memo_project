from django.urls import path
from .views import MemoListView

urlpatterns = [
    path('',MemoListView.as_view(), name = 'index'),
]