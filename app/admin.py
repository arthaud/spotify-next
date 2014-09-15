from django.contrib import admin
from app.models import Music, Vote, Client


class VoteAdmin(admin.ModelAdmin):
    list_display = ('ip', 'reverse', 'point', 'date')
    readonly_fields = ('date',)

admin.site.register(Music)
admin.site.register(Vote, VoteAdmin)
admin.site.register(Client)
