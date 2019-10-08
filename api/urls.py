from django.urls import path, include

from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('feed', views.UserProfileFeedViewSet)
router.register('profile/student', views.UserProfileViewSet_Student)
router.register('profile/teacher', views.UserProfileViewSet_Teacher)
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    path('login/', views.UserLoginApiView.as_view()),
    path('', include(router.urls)),
]

