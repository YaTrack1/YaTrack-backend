from rest_framework import serializers

from user.models import User, Candidate, Employer


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
        )


class EmployerSerializers(serializers.ModelSerializer):

    date_create = serializers.DateTimeField()

    class Meta:
        model = Employer
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "date_create",
        )


class CandidateSerializers(serializers.ModelSerializer):

    birthday = serializers.DateField()
    date_create = serializers.DateTimeField()

    class Meta:
        model = Candidate
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "birthday",
            "date_create",
        )
