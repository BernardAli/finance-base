from django.contrib import admin
from .models import Tag, Sector, CompanyProfile, Market, Chairman, ChiefExecutiveOfficer, \
    ShareDetail, SharePrice, Indices, FinancialPeriod, Report, MarketReport

# Register your models here.

admin.site.register(Sector)
admin.site.register(CompanyProfile)
admin.site.register(Tag)
admin.site.register(Market)
admin.site.register(Chairman)
admin.site.register(ChiefExecutiveOfficer)
admin.site.register(ShareDetail)
admin.site.register(SharePrice)
admin.site.register(Indices)
admin.site.register(FinancialPeriod)
admin.site.register(Report)
admin.site.register(MarketReport)
