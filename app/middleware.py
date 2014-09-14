from app.models import Music, Vote
import lib.spotify as spotify


class UpdateMusicMiddleware(object):
    def process_request(self, request):
        query = Music.objects.all()
        request.current_music = spotify.music_name()

        if not request.current_music:
            raise Exception('Unable to get current music name')

        if query.count() == 0 or query[0].name != request.current_music:
            # delete everything \o/
            Vote.objects.all().delete()
            Music.objects.all().delete()

            music = Music(name=request.current_music)
            music.save()
