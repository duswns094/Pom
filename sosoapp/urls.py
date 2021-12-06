from django.urls import path

from sosoapp.views import SosoView, SosoListView

app_name = 'sosoapp'

urlpatterns = [
    path('list/', SosoListView.as_view(), name='list'),
    path('soso/', SosoView.as_view(), name='soso')
]