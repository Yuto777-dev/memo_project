from django.urls import path
from .views import MemoListView,MemoCreateView,MemoUpdateView,MemoDeleteView

urlpatterns = [
    path('', MemoListView.as_view(), name = 'index'),
    path('new/', MemoCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', MemoUpdateView.as_view(), name='memo-edit'),
    path('<int:pk>/delete/', MemoDeleteView.as_view(), name='memo-delete')
]