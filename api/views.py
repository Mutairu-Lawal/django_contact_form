from .serializers import UsersSerializer
from users.models import Users
from rest_framework import generics, mixins


# Create your views here


class User(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserDetail(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer
    lookup_field = 'id'

    def get(self, resquest, id):
        return self.retrieve(resquest, id)

    def put(self, resquest, id):
        return self.update(resquest, id)

    def delete(self, resquest, id):
        return self.destroy(resquest, id)
