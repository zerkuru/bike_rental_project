from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import UsersModel
from .serializers import UserModelSerializer


class BaseUsersViewSet(ModelViewSet):
    queryset = UsersModel.objects.all()
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = UserModelSerializer

