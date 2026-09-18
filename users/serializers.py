from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate_email(self, value):

        if not value.endswith("@gmail.com"):
            raise serializers.ValidationError(
                "Email must be from the domain @gmail.com"
            )

        query = User.objects.filter(email=value)

        if self.instance:
            query = query.exclude(pk=self.instance.pk)

        if query.exists():
            raise serializers.ValidationError("Email already exists")

        return value

    def validate_mobile(self, value):

        if len(value) != 10:
            raise serializers.ValidationError("Mobile number must be 10 digits long")


        if not value.isdigit():
            raise serializers.ValidationError("Mobile Number Must Contain only the digit")

        return value
        