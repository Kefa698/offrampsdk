from django.urls import path
from . import views

urlpatterns = [
    path('tofiat/',views.ConvertToFiat.as_view(),name='tofiat'),
     path('tocrypto/',views.ConvertToCrypto.as_view(),name='tocrypto'),
]