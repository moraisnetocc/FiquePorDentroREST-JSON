from django.conf.urls import include, url
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'info', views.InfoViewSet)

urlpatterns = [
    # url(r'^home', views.home),
    url(r'^', include(router.urls)),
]
