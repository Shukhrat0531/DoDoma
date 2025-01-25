from rest_framework import serializers
from .models import User1
from .utils import send_sms_via_smsc
from django.utils.timezone import now


class User1RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User1
        fields = ['phone_number', 'name']

    def create(self, validated_data):
        user, created = User1.objects.get_or_create(phone_number=validated_data['phone_number'])
        user.name = validated_data.get('name', user.name)
        user.generate_otp()
        message = f"Ваш код для авторизации: {user.otp}"
        send_sms_via_smsc(user.phone_number, message)
        return user


class User1VerificationSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User1.objects.get(phone_number=data['phone_number'])
            if not user.verify_otp(data['otp']):
                raise serializers.ValidationError("Неверный код или код истек")
            return data
        except User1.DoesNotExist:
            raise serializers.ValidationError("Номер телефона не найден")



class User1LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    otp = serializers.CharField(max_length=6)

    def validate(self, data):
        try:
            user = User1.objects.get(phone_number=data['phone_number'])
            if not user.is_verified:
                raise serializers.ValidationError("Ваш номер телефона не подтвержден.")
            if not user.verify_otp(data['otp']):
                raise serializers.ValidationError("Неверный код подтверждения или код истек.")
            return data
        except User1.DoesNotExist:
            raise serializers.ValidationError("Пользователь с таким номером телефона не найден.")
