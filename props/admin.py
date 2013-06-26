from props.models import Prop
from django.contrib import admin

class PropAdmin(admin.ModelAdmin):
#     fieldsets = [
#                  (None, {'fields': ['video_url', 'title', 'is_votable', 'contest', 'status', 'user', 'thumbnail_url']}),
#                  (u'Description', {'fields': ['text',]}),
#                  (u'Categories', {'fields': ['categories',]}),
#                  (u'Date Information', {'fields': ['publish_start',]}),
#                  (u"""Advanced Data (don't change unless you know what you're doing!)""", {'fields': ['provider_url', 'author_name', 'author_url', 'video_code', 'duration'], 'classes':['collapse']}),
#                  ]
    list_display = ('name', 'owner', 'status')
    list_filter = ['date_created', 'status']
    date_hierarchy = 'date_created'
    search_fields = ['name']
    
admin.site.register(Prop, PropAdmin)