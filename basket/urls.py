from django.urls import path

from . import views

app_name = 'basket'

urlpatterns = [
    path('summary', views.basket_summary, name='basket_summary'),
    path('add/', views.BasketAdd.as_view(), name='basket_add'),
    path('delete/', views.BasketDelete.as_view(), name='basket_delete'),
    path('update/', views.BasketUpdate.as_view(), name='basket_update'),
]