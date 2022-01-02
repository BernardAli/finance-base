from django.urls import path
from .views import index_view, about_view, listed_companies, company_details, sector, market


urlpatterns = [
    path('', index_view, name='index'),
    path('companies/', listed_companies, name='listed_companies'),
    path('companies/<uuid:company_id>', company_details, name='company_details'),
    path('sector/<sector_slug>', sector, name='sector'),
    path('market/<market_slug>', market, name='market'),
    path('about/', about_view, name='about'),
]