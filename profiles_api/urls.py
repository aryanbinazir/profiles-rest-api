from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('login/', views.UserLoginApiView.as_view())
]

router = DefaultRouter()
router.register("hello-viewset", views.HelloViewSet, basename='hello-viewset')
router.register('profiles', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
urlpatterns += router.urls