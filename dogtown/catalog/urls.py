from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('akita', views.akita, name='akita'),
    path('store', views.store, name='store'),
    path('kelpi', views.kelpi, name='kelpi'),
    path('beagle', views.beagle, name='beagle'),
    path('bobtail', views.bobtail, name='bobtail'),
    path('pitbull', views.pitbull, name='pitbull'),
    path('bulldog', views.bulldog, name='bulldog'),
    path('dalmatian', views.dalmatian, name='dalmatian'),
    path('cocker', views.cocker, name='cocker'),
    path('place_order/<str:item_name>', views.place_order, name='place_order'),
]