from django.shortcuts import render
from .models import Inflation, MPR

# Create your views here.


def inflation_view(request):
    inflation = Inflation.objects.all()

    context = {
        'inflation': inflation,
    }
    return render(request, 'inflation.html', context)


def mpr_view(request):
    mprs = MPR.objects.all()

    context = {
        'mprs': mprs,
    }
    return render(request, 'mpr.html', context)

