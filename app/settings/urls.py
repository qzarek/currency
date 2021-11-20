from currency.views import rate_list, contact_us

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('rate/', rate_list),
    path('contact-us/', contact_us),

]
