from django.contrib import admin
from aluraflix_api.models import Video

class Videos(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descricao', 'url')
    list_display_links = ('id', 'titulo', 'descricao', 'url')
    search_fields = ('titulo',)
    list_per_page = 10

admin.site.register(Video, Videos)
