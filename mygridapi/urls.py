from django.urls import path
from .views import PersonView
from rest_framework.routers import DefaultRouter
app_name = 'mygridapi'
router = DefaultRouter()
router.register(r'persons',PersonView)
urlpatterns = router.urls