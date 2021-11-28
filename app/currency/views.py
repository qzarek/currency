from currency.models import ContactUs, Rate

from django.http.response import HttpResponse
from django.shortcuts import render


def rate_list(request):
    rates = Rate.objects.all()
    context = {
        'rates': rates,
    }
    return render(request, 'rate_list.html', context)


def contact_us(request):
    messages = ContactUs.objects.all()
    context = {
        'messages': messages,
    }
    return render(request, 'contact_us.html', context)


def status_code(request):
    if True:
        response = HttpResponse(
            'User was created',
            status=201
        )
    else:
        response = HttpResponse(
            'Error. Invalid data',
            status=400
        )
    return response
