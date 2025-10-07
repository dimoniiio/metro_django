from django.db import models


class User(models.Model):
    full_name = models.CharField("ФИО", max_length=255)
    email = models.EmailField("Email")
    address = models.TextField("Адрес", blank=True, null=True)
    photo = models.ImageField("Фото",
                              upload_to='user_photos/',
                              blank=True,
                              null=True)

    def __str__(self):
        return self.full_name
