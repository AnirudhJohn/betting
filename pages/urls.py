from django.urls import path

from .views import StagingAreaView, NewHome

urlpatterns = [
    path('', StagingAreaView.as_view(), name='stage'),
    path('newhome/', NewHome.as_view(), name='newhome')
]