from django.db.transaction import atomic
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers

from user.models import User
from core.models import Organization, City, Skill
from tracker.models import Tracker, Comparison, Favorite, Invitation
from resume.models import Resume, SkillInResume
from vacancy.models import Vacancy, SkillInVacancy


class EmployerSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя как <Наниматель>."""

    class Meta:
        model = User
        fields = "__all__"


class CandidateSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя как <Кандидат>."""

    class Meta:
        model = User
        fields = "__all__"


class OrganizationSerializer(serializers.ModelSerializer):
    """Сериализатор модели организации."""

    name = serializers.PrimaryKeyRelatedField(
        source="organization",
        read_only=True,
    )
    itn = serializers.SlugRelatedField(
        source="organization", read_only=True, slug_field="itn"
    )

    class Meta:
        model = Organization
        fields = "__all__"


class CitySerializer(serializers.ModelSerializer):
    """Сериализатор модели города."""

    name = serializers.PrimaryKeyRelatedField(
        source="city",
        read_only=True,
    )

    class Meta:
        model = City
        fields = "__all__"


class SkillSerializer(serializers.ModelSerializer):
    """Сериализатор модели навыка."""

    name = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all())

    class Meta:
        model = Skill
        fields = "__all__"


class SkillInResumeSerializer(serializers.ModelSerializer):
    """Сериализатор модели навыка в резюме."""

    name = serializers.SlugRelatedField(
        source="skill", read_only=True, slug_field="name"
    )

    class Meta:
        model = SkillInResume
        fields = "__all__"


class ResumeSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializer(read_only=True)
    photo = Base64ImageField()
    skill_list = SkillInResumeSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = "__all__"


class ResumeReadListSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializer(read_only=True)
    photo = Base64ImageField(read_only=True)
    grade = serializers.CharField()
    skill_list = SkillInResumeSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = ("candidate", "photo", "grade", "skill_list")


class ResumeCreateSerializer(serializers.ModelSerializer):
    candidate = CandidateSerializer(read_only=True)
    photo = Base64ImageField(max_length=None, use_url=True)
    city = CitySerializer(read_only=True)
    skill_list = SkillInResumeSerializer(many=True, read_only=True)

    class Meta:
        model = Resume
        fields = "__all__"


class SkillInVacancySerializer(serializers.ModelSerializer):
    name = serializers.PrimaryKeyRelatedField(read_only=True, source="skill")

    class Meta:
        model = SkillInVacancy
        fields = "__all__"


class VacancySerializer(serializers.ModelSerializer):
    position = serializers.SlugRelatedField(
        source="vacancy", read_only=True, slug_field="position"
    )

    class Meta:
        model = Vacancy
        fields = ("position",)


class VacancyReadListSerializer(serializers.ModelSerializer):
    position = serializers.SlugRelatedField(
        source="vacancy", read_only=True, slug_field="position"
    )

    class Meta:
        model = Vacancy
        fields = ("position",)


class VacancyCreateSerializer(serializers.ModelSerializer):
    skill_list = SkillInVacancySerializer(many=True, read_only=True)

    class Meta:
        model = Vacancy
        fields = "__all__"

    @atomic
    def creating_ingredients(self, recipe, ingredients_data):
        for ingredient in ingredients_data:
            SkillInVacancy.objects.get_or_create(
                recipe=recipe,
                ingredient=ingredient["id"],
                amount=ingredient["amount"],
            )


class TrackerSerializer(serializers.ModelSerializer):
    resume = ResumeSerializer()

    class Meta:
        model = Tracker
        fields = "__all__"


class ComparisonSerializer(serializers.ModelSerializer):
    resume = ResumeReadListSerializer()
    # vacancy = VacancySerializer()

    class Meta:
        model = Comparison
        fields = (
            "resume",
            "vacancy",
        )


class FavoriteSerializer(serializers.ModelSerializer):
    # resume = ResumeSerializer()
    # vacancy = VacancySerializer()

    class Meta:
        model = Favorite
        fields = (
            "resume",
            "vacancy",
        )


class InvitationSerializer(serializers.ModelSerializer):
    resume = ResumeSerializer()
    # vacancy = VacancySerializer()

    class Meta:
        model = Invitation
        fields = (
            "resume",
            "vacancy",
        )


class ResumeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Resume
        fields = (
            "id",
            "title",
            "candidate",
            "gender",
        )
