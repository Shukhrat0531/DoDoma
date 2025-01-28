from django.db import models
import random
from rest_framework import serializers

from django.utils.timezone import now, timedelta

class User1(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)  # Поле для имени
    phone_number = models.CharField(max_length=15, unique=True)  # Номер телефона
    is_verified = models.BooleanField(default=False)  # Статус подтверждения
    otp = models.CharField(max_length=6, blank=True, null=True)  # Код подтверждения
    code_expiry = models.DateTimeField(blank=True, null=True)  # Время истечения кода
    reset_attempts = models.IntegerField(default=0)
    reset_attempts_time = models.DateTimeField(null=True, blank=True)

    def can_request_reset(self):
        """Проверяет, можно ли отправить новый код."""
        if self.reset_attempts >= 5 and self.reset_attempts_time and now() < self.reset_attempts_time + timedelta(minutes=10):
            return False  # Превышено количество попыток
        if self.reset_attempts_time and now() > self.reset_attempts_time + timedelta(minutes=10):
            self.reset_attempts = 0  # Сбрасываем попытки через 10 минут
        self.reset_attempts += 1
        self.reset_attempts_time = now()
        self.save()
        return True
    def generate_otp(self):
        self.otp = str(random.randint(100000, 999999))
        self.code_expiry = now() + timedelta(days=1000)
        self.save()

    def verify_otp(self, otp):
        if self.otp == otp and self.code_expiry >= now():
            self.is_verified = True
            self.save()  # Сохраняем изменения без удаления OTP
            return True
        return False
    
    
    
    def reset_password(self):
        if not self.can_request_reset():
            raise Exception("Превышено количество попыток сброса. Попробуйте позже.")
        self.otp = str(random.randint(100000, 999999))
        self.code_expiry = now() + timedelta(days=1000)
        self.save()    


    def __str__(self):
        return f"{self.name} ({self.phone_number})"


class Promocode(models.Model):
    name = models.CharField(max_length=200)
    discount = models.IntegerField(blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='upload', blank=True)

    def __str__(self):
        return self.name

class PromocodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promocode
        fields = ['name', 'discount', 'status']

class Unit(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='upload')
    price = models.IntegerField(default=0)
    compound = models.TextField(blank=True)
    storage = models.TextField(blank=True)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, blank=True,null=True)
    country = models.CharField(max_length=100,blank=True)
    discount = models.IntegerField(default=0)
    is_new = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Poster(models.Model):
    name = models.CharField(max_length=300, default='yozma hech narsa',blank=True)
    image = models.ImageField(upload_to='upload')

    def __str__(self):
        return self.name



