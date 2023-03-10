from django.db import models
from django.conf import settings


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='cities')
    description = models.TextField()

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        return f"{settings.SITE_URL}{self.image.url}"


class Guid(models.Model):
    name = models.CharField(max_length=350)
    image = models.ImageField(upload_to='guids')
    bio = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    language = models.CharField(max_length=255)

    @property
    def get_rating(self):
        count = self.rate.count()
        summa = sum([i.rate for i in self.rate.all()])
        if count == 0:
            count = 1
        self.rating = summa / count
        self.save()
        return self.rating

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        return f"{settings.SITE_URL}{self.image.url}"


class WorkOfGuid(models.Model):
    guid = models.ForeignKey(Guid, models.CASCADE, related_name='works')
    image = models.ImageField(upload_to='guid_works')
    video = models.FileField(null=True, blank=True)

    @property
    def get_image(self):
        return f"{settings.SITE_URL}{self.image.url}"

    def __str__(self):
        return self.guid.name


class Rate(models.Model):
    RATE = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    )
    rate = models.PositiveIntegerField(choices=RATE, default=1)
    guid = models.ForeignKey(Guid, models.CASCADE, related_name='rate')

    def __str__(self):
        return self.guid.name


class Booking(models.Model):
    guid = models.ForeignKey(Guid, models.CASCADE, related_name='booking')
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    city = models.ForeignKey(City, models.SET('City deleted'), related_name='booking')
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()
    contact_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

