
from django.urls import path

from . import views

urlpatterns = [

    path('', views.store, name='store'),

    path('product/<slug:slug>', views.product_page, name='product_page'),

]
