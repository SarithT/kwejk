from django.core.exceptions import ObjectDoesNotExist
from django.db import models
import os
from django.contrib.auth.models import User
# Create your models here.
from Spmag import settings

SQUAD_TO_CHOOSE = ((1,'SPMAGIC'), (2,'FALCON'))

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    squad = models.CharField(choices=SQUAD_TO_CHOOSE, max_length=20)

class Image(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    description = models.TextField(max_length=50, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    addedBy = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    isOnGifMonitor = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.isOnGifMonitor:
            try:
                gifImage = Image.objects.filter(isOnGifMonitor=True).get()
                gifImage.isOnGifMonitor = False
                gifImage.save()
            except ObjectDoesNotExist:
                print("Gif monitor is currently empty")
        super().save(*args, **kwargs)

    def delete(self, using=None, keep_parents=False):
        if self.image:
            print("deleting " + str(self.image.path))
            os.remove(self.image.path)
        super().delete()

class ProntoTimer(models.Model):
    lastProntoDate = models.DateField(auto_now_add=True)
    duration = models.DurationField()