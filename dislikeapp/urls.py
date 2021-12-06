from django.urls import path

from dislikeapp.views import DislikeView, DislikeListView

app_name = 'dislikeapp'

urlpatterns = [
    path('list/', DislikeListView.as_view(), name='list'),
    path('dislike/', DislikeView.as_view(), name='dislike')
]