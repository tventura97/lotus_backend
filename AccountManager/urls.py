from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'challenges', views.ChallengeViewSet)
router.register (r'accounts', views.AccountsViewSet)
router.register(r'OwnedChallenges', views.OwnedChallengeViewSet)
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]