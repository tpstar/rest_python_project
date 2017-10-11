from django.conf.urls import url
from compute_app import views

urlpatterns = [
    url(r'^$', views.compute),
]
