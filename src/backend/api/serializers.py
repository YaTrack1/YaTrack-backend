from rest_framework import serializers

from resume.models import Resume
from user.models import User


class EmployerSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )


class CandidateSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
        )

class ResumeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = (
            "id",
            "title",
        )
