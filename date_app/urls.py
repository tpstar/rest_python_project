from django.conf.urls import url
from date_app import views

urlpatterns = [
    url(r'^$', views.date),
]
