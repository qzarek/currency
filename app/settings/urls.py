from currency.views import contact_us, rate_list

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('rate/', rate_list),
    path('contact-us/', contact_us),

]
