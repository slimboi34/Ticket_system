from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket_list, name='ticket_list'),
    path('create/', views.create_ticket, name='create_ticket'),  # This is the target URL
    path('update/<int:ticket_id>/', views.update_ticket, name='update_ticket'),
]