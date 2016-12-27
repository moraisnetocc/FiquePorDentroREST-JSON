from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register(r'infos', views.InfoViewSet)
router.register(r'info_categories', views.InfoCategoryViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
