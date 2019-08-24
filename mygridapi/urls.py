from django.urls import path
from .views import PersonView
from rest_framework.routers import DefaultRouter,SimpleRouter
from rest_framework import routers

class MyRouter(SimpleRouter):
    def __init__(self):
        self.trailing_slash = "/?"
        super(SimpleRouter,self).__init__()
app_name = 'mygridapi'
router = MyRouter()
router.register(r'persons',PersonView)
urlpatterns = router.urls