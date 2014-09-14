from django.db import models


class Music(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.name


class Vote(models.Model):
    ip = models.GenericIPAddressField(primary_key=True)
    reverse = models.CharField(max_length=200, blank=True, null=True)
    point = models.SmallIntegerField(default=1) # +1 means "want to skip the current song"
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        p = str(self.point)
        if self.point >= 0:
            p = '+' + p

        return '%s : %s' % (self.ip, p)
