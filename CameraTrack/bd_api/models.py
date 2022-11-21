from django.db import models



class AllowedNumbers(models.Model):
    number = models.CharField(max_length=7, unique=True, primary_key=True)
    vin_code = models.CharField(max_length=17, unique=True)
    car_model = models.TextField()

    def __str__(self):
        return self.number


class NumbersLogs(models.Model):
    number = models.CharField(max_length=7)
    log_date = models.DateField()
    status = models.TextField()
    media_path = models.TextField()

    def __str__(self):
        return self.number


class Users(models.Model):
    login = models.TextField(primary_key=True)
    full_name = models.TextField()
    password = models.TextField()
    salt = models.CharField(max_length=5)
    last_login = models.DateField()
    role = models.TextField()

    def __str__(self):
        self.full_name
