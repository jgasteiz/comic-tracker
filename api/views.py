from django.contrib.auth.models import User
from rest_framework import viewsets, mixins
from rest_framework.response import Response

from dashboard.models import Comic
from .serializers import ComicSerializer, UserSerializer


class Comics(viewsets.ModelViewSet):
    model = Comic
    queryset = Comic.objects.all()
    serializer_class = ComicSerializer

    def update(self, request, *args, **kwargs):
        try:
            comic = Comic.objects.get(external_id=kwargs.get('pk'))
            tracked = self.request.data.get('tracked')
            if tracked:
                comic.tracked_by.add(self.request.user)
            else:
                comic.tracked_by.remove(self.request.user)
            comic.save()
            return Response(ComicSerializer(instance=comic, context=self.get_serializer_context()).data)
        except Comic.DoesNotExist as e:
            pass
        return Response("NO")


class NewReleases(viewsets.ModelViewSet):
    queryset = Comic.objects.nearest_wednesday_comics()
    serializer_class = ComicSerializer

    def get_queryset(self):
        return Comic.objects.nearest_wednesday_comics(
            date=self.request.GET.get('date'),
        )


class TrackedComics(viewsets.ModelViewSet):
    queryset = Comic.objects.nearest_wednesday_comics()
    serializer_class = ComicSerializer

    def get_queryset(self):
        return Comic.objects.tracked_by_user(
            user=self.request.user,
            date=self.request.GET.get('date'),
        )


class Users(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        return self.get_user(request)

    def list(self, request, *args, **kwargs):
        return self.get_user(request)

    def get_user(self, request):
        if request.user is not None and not request.user.is_anonymous():
            return Response(self.serializer_class(request.user).data)
        return Response({})
