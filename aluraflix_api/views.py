from rest_framework import viewsets
from aluraflix_api.models import Video
from aluraflix_api.serializer import VideoSerializer

class VideosViewSet(viewsets.ModelViewSet):
    """Ëxibindo todos os vídeos"""
    queryset = Video.objects.all()
    serializer_class = VideoSerializer

