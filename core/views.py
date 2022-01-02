from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from rates.models import Inflation, MPR
from .models import Sector, Tag, CompanyProfile, Market, Chairman, ShareDetail, SharePrice, Indices, Report, MarketReport

# Create your views here.


def index_view(request):
    inflation = Inflation.objects.last()
    mpr = MPR.objects.last()
    sectors = Sector.objects.all()
    markets = Market.objects.all()
    indices = Indices.objects.all()[:10]
    market_reports = MarketReport.objects.all().order_by('session_number')

    context = {
        'inflation': inflation,
        'mpr': mpr,
        'sectors': sectors,
        'markets': markets,
        'indices': indices,
        'market_reports': market_reports,
    }

    return render(request, 'index.html', context)


def listed_companies(request):
    companies = CompanyProfile.objects.all().order_by('company_id')

    context = {
        'companies': companies
    }
    return render(request, 'companies.html', context)


def company_details(request, company_id):
    chairman = Chairman.objects.filter(company_id=company_id)
    company = get_object_or_404(CompanyProfile, id=company_id)
    share = ShareDetail.objects.filter(company_id=company_id)
    share_price = SharePrice.objects.filter(company_id=company_id)
    reports = Report.objects.filter(company_id=company_id)
    context = {
        'company': company,
        'chairman': chairman,
        'share': share,
        'share_price': share_price,
        'reports': reports,
    }
    return render(request, 'company_details.html', context)


def sector(request, sector_slug):
    sector = get_object_or_404(Sector, slug=sector_slug)
    companies = CompanyProfile.objects.filter(sector=sector).order_by('name')
    paginator = Paginator(companies, 50)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'sector': sector,
    }
    return render(request, 'sectors.html', context)


def market(request, market_slug):
    market = get_object_or_404(Market, slug=market_slug)
    companies = CompanyProfile.objects.filter(market=market).order_by('name')
    paginator = Paginator(companies, 50)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'market': market,
    }
    return render(request, 'market.html', context)



def about_view(request):
    return render(request, 'about.html')