from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Patient

class PatientSerializers(serializers.ModelSerializer):

    created_by = serializers.CharField(
    source='created_by.username',
    read_only=True
    )
    
    class Meta:
        model = Patient
        fields = '__all__'

        extra_kwargs = {
            "name": {"required": True},
            "age": {"required": True},
            "gender": {"required": True},
            "phone": {"required": True}
        }

    def validate_phone(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
            "Phone number must contain only digit"
        )
        if len(value) != 10:
            raise serializers.ValidationError(
                "Phone number must be exactly 10 digit"
            )

        return value
    
    def validate_age(self, value):
       if value<=0:
            raise serializers.ValidationError(
                "Age must be greater than 0"
            )
       return value