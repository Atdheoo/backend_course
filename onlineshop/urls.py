from django.urls import path, re_path
from onlineshop.views import OrderView

urlpatterns = [
    re_path(r'^order/?$', OrderView.as_view(), name='order'),
]