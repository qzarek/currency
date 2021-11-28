from currency.views import contact_us, rate_list, status_code

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('rate/list/', rate_list),
    path('contact-us/', contact_us),
    path('cs2/', status_code),

]
