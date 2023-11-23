from django.db import models

class RandomUser(models.Model):
    gender = models.CharField(verbose_name='pol', max_length=55, null=True, blank=True)
    first_name = models.CharField(verbose_name='name', max_length=255, null=True, blank=True)
    last_name = models.CharField(verbose_name='soname', max_length=55, null=True, blank=True)
    street_number = models.IntegerField(verbose_name='номкр дома', null=True, blank=True)
    street_name = models.CharField(verbose_name='улица', max_length=100, null=True, blank=True)
    city = models.CharField(verbose_name='город проживания', max_length=100, null=True, blank=True)
    country = models.CharField(verbose_name='страна проживания', max_length=100, null=True, blank=True)
    postcode = models.CharField(verbose_name='почтовый индекс', max_length=100, null=True, blank=True)
    login = models.CharField(verbose_name='никнейм', blank=True, null=True, max_length=100)
    password = models.CharField(verbose_name='пароль пользователя', max_length=100, null=True, blank=True)
    born_data = models.CharField(verbose_name='дата рождения',max_length=55, blank=True, null=True)
    age = models.IntegerField(verbose_name='возраст', null=True, blank=True)