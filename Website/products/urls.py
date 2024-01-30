from django.urls import path
from . import views
# all urls on this site start with /products
urlpatterns = [
    path('', views.index),
    path('new', views.new)
]
