from django.urls import include, path
from rest_framework.routers import SimpleRouter
from ads.views import AdViewSet, CommentViewSet

# TODO настройка роутов для модели

ad_router = SimpleRouter()
ad_router.register(r'ads', AdViewSet)

ad_router.register("ads", AdViewSet, basename="users")


urlpatterns = [
    path('', include(ad_router.urls)),
    path("ads/<int:ad_id>/comments/",
         CommentViewSet.as_view({"get": "list", "post": 'create'})),

]
