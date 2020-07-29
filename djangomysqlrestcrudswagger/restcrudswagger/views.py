from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from rest_framework import status
from rest_framework.response import Response
from restcrudswagger.serializers import UserSerializer
from restcrudswagger.models import User

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed/created/edited/deleted.
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    update_data_pk_field = 'id'
	
    def create(self, request, *args, **kwargs):
        kwarg_field: str = self.lookup_url_kwarg or self.lookup_field
        self.kwargs[kwarg_field] = request.data[self.update_data_pk_field]

        try:
            return self.update(request, *args, **kwargs)
        except Http404:
            return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
        except Http404:
            pass
        return Response(status=status.HTTP_204_NO_CONTENT)