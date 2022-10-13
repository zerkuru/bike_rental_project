from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .filters import TransportFilter
from .models import TransportModel, TransportTypeModel, ManufacturerModel
from .permissions import IsTransportOwnerOrAdmin
from .serializers import TransportSerializer, TransportTypeSerializer, ManufacturerSerializer


class TransportViewSet(ModelViewSet):
    serializer_class = TransportSerializer
    queryset = TransportModel.objects.all()
    parser_classes = [MultiPartParser, FormParser]
    filterset_class = TransportFilter

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsTransportOwnerOrAdmin]
        return [permission() for permission in permission_classes]


class MyTransportViewSet(ModelViewSet):
    serializer_class = TransportSerializer

    def get_queryset(self):
        return TransportModel.objects.filter(transport_owner=self.request.user)

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsTransportOwnerOrAdmin]
        return [permission() for permission in permission_classes]


class TransportTypeViewSet(ModelViewSet):
    serializer_class = TransportTypeSerializer
    queryset = TransportTypeModel.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]


class ManufacturerViewSet(TransportTypeViewSet):
    serializer_class = ManufacturerSerializer
    queryset = ManufacturerModel.objects.all()
