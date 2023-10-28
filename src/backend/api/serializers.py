from django.db.transaction import atomic
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, relations

from user.models import User
from core.models import City, Skill
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
        fields = (
            "first_name",
            "last_name",
            "email",
            "last_login",
            "is_active",
        )


class CandidateInTrackerSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя как <Кандидат> для трекекра."""

    class Meta:
        model = User
        fields = (
            "first_name",
            "last_name",
            # "last_login",
        )


# class OrganizationSerializer(serializers.ModelSerializer):
#     """Сериализатор модели организации."""

#     name = serializers.PrimaryKeyRelatedField(
#         source="organization",
#         read_only=True,
#     )
#     itn = serializers.SlugRelatedField(
#         source="organization", read_only=True, slug_field="itn"
#     )

#     class Meta:
#         model = Organization
#         fields = "__all__"


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


class ResumeInTrackerSerializer(serializers.ModelSerializer):
    candidate = CandidateInTrackerSerializer(read_only=True)
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
    skill_list = relations.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), many=True
    )

    class Meta:
        model = Resume
        fields = (
            "title",
            "candidate",
            "photo",
            "birthday",
            "city",
            "skill_list",
            "gender",
            "telegram",
            "github",
            "about_me",
            "status_type_work",
            "status_finded",
        )
        read_only_fields = ("author",)

    @atomic
    def creating_skills(self, resume, skills_data):
        for skill in skills_data:
            SkillInResume.objects.get_or_create(
                resume=resume,
                skill=skill["id"],
            )

    @atomic
    def create(self, validated_data):
        skills_data = validated_data.pop("skills")
        candidate = self.context.get("request").user
        resume = Resume.objects.create(candidate=candidate, **validated_data)
        self.creating_skills(resume, skills_data)

        return resume

    @atomic
    def update(self, instance, validated_data):
        skills_data = validated_data.pop("skills")
        SkillInResume.objects.filter(resume=instance).delete()
        self.creating_skills(instance, skills_data)

        return super().update(instance, validated_data)


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
    author = EmployerSerializer(read_only=True)
    city = CitySerializer(read_only=True)
    skill_list = relations.PrimaryKeyRelatedField(
        queryset=Skill.objects.all(), many=True
    )

    class Meta:
        model = Vacancy
        fields = (
            "position",
            "author",
            "specialty",
            "description",
            "duties",
            "city",
            "conditions",
            "stages",
            "skill_list",
        )
        read_only_fields = ("author",)

    @atomic
    def creating_skills(self, vacancy, skills_data):
        for skill in skills_data:
            SkillInVacancy.objects.get_or_create(
                vacancy=vacancy,
                skill=skill["id"],
            )

    @atomic
    def create(self, validated_data):
        skills_data = validated_data.pop("skills")
        author = self.context.get("request").user
        vacancy = Vacancy.objects.create(author=author, **validated_data)
        self.creating_skills(vacancy, skills_data)

        return vacancy

    @atomic
    def update(self, instance, validated_data):
        skills_data = validated_data.pop("skills")
        SkillInVacancy.objects.filter(vacancy=instance).delete()
        self.creating_skills(instance, skills_data)

        return super().update(instance, validated_data)


class TrackerSerializer(serializers.ModelSerializer):
    """Сериализатор модели всех резюме кандидатов."""

    resume = ResumeInTrackerSerializer()

    class Meta:
        model = Tracker
        fields = ("resume",)


class ComparisonSerializer(serializers.ModelSerializer):
    """Сериализатор модели подходящих кандидатов."""

    resume = ResumeInTrackerSerializer()
    # vacancy = VacancySerializer()

    class Meta:
        model = Comparison
        fields = (
            "resume",
            "vacancy",
        )


class FavoriteSerializer(serializers.ModelSerializer):
    """Сериализатор модели избранных кандидатов."""

    resume = ResumeInTrackerSerializer()
    # vacancy = VacancySerializer()

    class Meta:
        model = Favorite
        fields = (
            "resume",
            "vacancy",
        )


class InvitationSerializer(serializers.ModelSerializer):
    """Сериализатор модели приглашенных кандидатов."""

    resume = ResumeInTrackerSerializer()
    # vacancy = VacancySerializer()

    class Meta:
        model = Invitation
        fields = (
            "resume",
            "vacancy",
        )


# class ResumeSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Resume
#         fields = (
#             "id",
#             "title",
#             "candidate",
#             "gender",
#         )
