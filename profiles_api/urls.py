from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view())
]

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename='hello-viewset')
router.register('profiles', views.UserProfileViewSet)
urlpatterns += router.urls