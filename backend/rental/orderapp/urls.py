from django.urls import path, include, re_path
from orderapp.views import OrderView, MyTransportOrderView

app_name = 'change_status'
urlpatterns = [
    path('<int:pk>/<str:status>/', OrderView.change_status, name='change_status'),
]
