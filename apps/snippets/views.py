import time

from rest_framework.viewsets import ModelViewSet

from apps.snippets.models import Snippet
from apps.snippets.serializers import SnippetSerializer


class SnippetViewSet(ModelViewSet):
    serializer_class = SnippetSerializer
    queryset = Snippet.objects.all()

    # def list(self, request, *args, **kwargs):
    #     time.sleep(10)
    #     return super().list(request, *args, **kwargs)