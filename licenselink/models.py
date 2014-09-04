import random
import string
from django.db import models


class License(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()

    def __str__(self):
        return self.name


class UserLicense(models.Model):
    license_type = models.ForeignKey(License)
    author = models.CharField(max_length=500)
    year = models.IntegerField(max_length=4)
    organisation = models.CharField(max_length=500)
    short_url = models.CharField(max_length=6, blank=True, unique=True, editable=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.pk is None:
            char_set = string.ascii_lowercase + string.digits
            self.short_url = ''.join(random.sample(char_set * 6, 6))
            super(UserLicense, self).save(force_insert, force_update, using, update_fields)

    def display_license(self):
        conditional = {1: (self.year, self.author),
                       2: (self.year, self.author),
                       3: (self.year, self.author),
                       4: (self.year, self.author)}
        return self.license_type.text.format(*conditional[self.license_type.id])