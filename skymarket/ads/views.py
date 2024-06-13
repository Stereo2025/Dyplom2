from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated

from ads.models import Ad, Comment
from ads.permissions import IsOwner, IsAdmin
from ads.serializers import AdSerializer, AdListSerializer, \
    CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 10


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    http_method_names = ["get", "post", "patch", "delete"]

    def get_serializer_class(self):
        if self.action in ("me", "list"):
            self.serializer_class = AdListSerializer
        else:
            self.serializer_class = AdSerializer

        return super().get_serializer_class()

    def get_permissions(self):
        if self.action == "list":
            self.permission_classes = [AllowAny]
        elif self.action == "update":
            self.permission_classes = [IsAuthenticated & IsOwner | IsAdmin]
        elif self.action == "destroy":
            self.permission_classes = [IsAuthenticated & IsOwner | IsAdmin]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(author_id=self.request.user.pk)

    @action(detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = self.get_queryset().filter(author_id=self.request.user.pk)
        return self.list(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'
    http_method_names = ["get", "post", "patch", "delete"]

    def get_queryset(self):
        self.queryset = self.queryset.filter(ad_id=self.kwargs.get('ad_id'))
        return super().get_queryset()

    def get_permissions(self):
        if self.action == "update":
            self.permission_classes = [IsAuthenticated & IsOwner | IsAdmin]
        elif self.action == "destroy":
            self.permission_classes = [IsAuthenticated & IsOwner | IsAdmin]
        else:
            self.permission_classes = [IsAuthenticated]

        return super().get_permissions()

    def perform_create(self, serializer):
        serializer.save(ad_id=self.kwargs.get("ad_id"), author_id=self.request.user.pk)
