from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='base'),
    path('add_product/', views.add_product, name='add_product'),
    path('view_inventory/', views.view_inventory, name='view_inventory'),
    path('record_sale/', views.record_sale, name='record_sale'),
    path('customer/', views.customer, name='customer'),
    path('add_customer/', add_customer_view, name='add_customerID'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)