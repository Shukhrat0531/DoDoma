from django.db import models
import random

from django.utils.timezone import now, timedelta

class User1(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)  # Поле для имени
    phone_number = models.CharField(max_length=15, unique=True)  # Номер телефона
    is_verified = models.BooleanField(default=False)  # Статус подтверждения
    otp = models.CharField(max_length=6, blank=True, null=True)  # Код подтверждения
    code_expiry = models.DateTimeField(blank=True, null=True)  # Время истечения кода

    def generate_otp(self):
        self.otp = str(random.randint(1000, 9999))
        self.code_expiry = now() + timedelta(days=100)
        self.save()

    def verify_otp(self, otp):
        if self.otp == otp and self.code_expiry >= now():
            self.is_verified = True
            self.save()  # Сохраняем изменения без удаления OTP
            return True
        return False


    def __str__(self):
        return f"{self.name} ({self.phone_number})"
