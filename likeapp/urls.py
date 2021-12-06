from django.urls import path

from likeapp.views import LikeListView, LikeView

app_name = 'likeapp'

urlpatterns = [
    path('list/', LikeListView.as_view(), name='list'),
    path('like/', LikeView.as_view(), name='like')
]