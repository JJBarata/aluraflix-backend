from rest_framework import serializers
from aluraflix_api.videos import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = '__all__'

