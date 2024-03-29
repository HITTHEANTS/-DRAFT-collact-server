from django.conf import settings
from django.contrib.auth import authenticate, login as django_login, logout as django_logout

from rest_framework import status, mixins, viewsets
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.views import RefreshJSONWebToken

from accounts.serializers import UserSerializer, ConfigSerializer
from accounts.models import User, Config
from api.views import DefaultViewSet


class ConfigViewSet(mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    permission_classes = (AllowAny,)
    serializer_class = ConfigSerializer
    http_method_naems = ['get']

    def get_queryset(self):
        return Config.objects.all()


class UserRegisterView(APIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserLoginView(ObtainJSONWebToken):
    def should_log(self, request, response):
        should_log_method = super().should_log(request, response)
        if not should_log_method:
            return False
        return status.is_success(response.status_code)

    def post(self, request, *args, **kwargs):
        # For Django-rest API View
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        user = authenticate(username=email, password=password)
        if user is None:
            return Response({'message': 'Email or password is wrong.'}, status=status.HTTP_403_FORBIDDEN)

        response = super().post(request, *args, **kwargs)
        if response.status_code != status.HTTP_200_OK:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if settings.DEBUG:
            django_login(request, user)

        # user.login()
        request.user = user
        return response


class UserActivateView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if not request.user.is_superuser:
            return Response({'message': 'Unauthorized.'}, status=status.HTTP_403_FORBIDDEN)

        email = request.data.get('email', None)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise AuthenticationFailed()

        user.is_active = True
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserMakeSuperuserView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        if not request.user.is_superuser:
            return Response({'message': 'Unauthorized.'}, status=status.HTTP_403_FORBIDDEN)

        email = request.data.get('email', None)
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise AuthenticationFailed()

        user.is_superuser = True
        user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserInfoView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        return Response(UserSerializer(request.user).data)


class TokenRefreshView(RefreshJSONWebToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code != status.HTTP_200_OK:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        return response


class UserViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  DefaultViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch', 'delete']
