from django.db import models
from guid.models import Language, City


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(null=True)
    contact_link = models.CharField(max_length=255)
    city = models.ForeignKey(City, models.CASCADE, related_name='contact')
    check_in_time = models.DateTimeField()
    check_out_time = models.DateTimeField()
    language = models.ForeignKey(Language, models.CASCADE, related_name='contact')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

