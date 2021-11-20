from currency.models import ContactUs, Rate

from django.http.response import HttpResponse


# from django.shortcuts import render


def rate_list(request):
    results = []
    rates = Rate.objects.all()
    for rate in rates:
        results.append(
            f'ID: {rate.id}, sale: {rate.sale}, buy: {rate.buy}, '
            f'created: {rate.created}, source: {rate.source}<br>'
        )
    return HttpResponse(str(results))


def contact_us(request):
    results = []
    messages = ContactUs.objects.all()
    for message in messages:
        results.append(
            f'ID: {message.id}, Email: {message.email_from}, Subject: {message.subject}, '
            f'Message: {message.message}'
        )
    return HttpResponse(str(results))
