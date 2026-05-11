from django.urls import path
from .views import MemoListView,MemoCreateView,MemoUpdateView

urlpatterns = [
    path('', MemoListView.as_view(), name = 'index'),
    path('new/', MemoCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', MemoUpdateView.as_view(), name='memo-edit')
]