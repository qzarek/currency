from currency.views import contact_us, rate_list, source_create, source_delete, source_list, source_update, status_code

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('rate/list/', rate_list),
    path('contact-us/', contact_us),
    path('cs2/', status_code),
    path('source-list/', source_list),
    path('source-list/create/', source_create),
    path('source-list/update/<int:pk>/', source_update),
    path('source-list/delete/<int:pk>/', source_delete),

]
