from django.conf.urls import include, url
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'infos', views.InfoViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
