from django.urls import path
from .views import inflation_view, mpr_view

urlpatterns = [
    path('inflation/', inflation_view, name='inflation'),
    path('mpr/', mpr_view, name='mpr'),
]