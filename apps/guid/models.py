from django.db import models
from django.conf import settings


class Language(models.Model):
    contraction = models.CharField(max_length=5)
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='languages')

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        return f"{settings.SITE_URL}{self.image.url}"


class City(models.Model):
    name = models.CharField(max_length=355)
    description = models.TextField()

    def __str__(self):
        return self.name


class CityImage(models.Model):
    city = models.ForeignKey(City, models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cities')

    @property
    def get_image(self):
        return f"{settings.SITE_URL}{self.image.url}"


class Guid(models.Model):
    name = models.CharField(max_length=350)
    image = models.ImageField(upload_to='guids')
    bio = models.TextField()
    rating = models.FloatField(null=True, blank=True)
    language = models.ManyToManyField(Language, related_name='guids')
    city = models.ManyToManyField(City, related_name='guids')

    @property
    def get_rating(self):
        count = self.rate.count()
        summa = sum([i.rate for i in self.rate.all()])
        if count == 0:
            return self.rating
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
    image = models.ImageField(upload_to='guid_works', null=True, blank=True)
    video = models.FileField(null=True, blank=True)

    @property
    def get_image(self):
        if self.image:
            return f"{settings.SITE_URL}{self.image.url}"
        return None

    @property
    def get_video(self):
        if self.video:
            return f"{settings.SITE_URL}{self.video.url}"
        return None

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
    comment = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.guid.name


class Booking(models.Model):
    guid = models.ForeignKey(Guid, models.CASCADE, related_name='booking')
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    city = models.ForeignKey(City, models.CASCADE, related_name='booking')
    language = models.ForeignKey(Language, models.SET_NULL, null=True, related_name='booking')
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()
    contact_link = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    is_checked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
