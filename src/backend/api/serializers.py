from django.db.transaction import atomic
from drf_extra_fields.fields import Base64ImageField
from rest_framework import serializers, relations
from django.conf import settings

from user.models import User
from core.models import City, Skill
from tracker.models import (
    Tracker,
    Comparison,
    Favorite,
    Interested,
    Invitation,
    UserViewedResume,
)
from resume.models import Resume, SkillInResume, Experience, Education
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


class InvitedSerializer(serializers.ModelSerializer):
    """Сериализатор модели просматривал пользователь резюме."""

    class Meta:
        model = UserViewedResume
        fields = ("id", "status")


class Vacancy2Serializer(serializers.ModelSerializer):
    """Сериализатор модели вакансии конкретного нанимателя."""

    title = serializers.CharField(source="position")
    newResumes = serializers.SerializerMethodField()
    favourites = serializers.SerializerMethodField()
    invited = serializers.SerializerMethodField()

    class Meta:
        model = Vacancy
        fields = (
            "title",
            "newResumes",
            "favourites",
            "invited",
        )

    def get_newResumes(
        self, vacancy
    ) -> list[int,]:
        """Получение ids резюме, которые наниматель ещё не смотрел."""
        resume_ids = UserViewedResume.objects.filter(
            employer=vacancy.author
        ).values_list("resume_id", flat=True)
        return Resume.objects.exclude(id__in=resume_ids).values_list(
            "id", flat=True
        )

    def get_favourites(
        self, vacancy
    ) -> list[int,]:
        """Получение ids резюме, которые наниматель отметили."""
        return Favorite.objects.filter(vacancy=vacancy).values_list(
            "resume_id", flat=True
        )

    def get_invited(
        self, vacancy
    ) -> list[dict,]:
        """Получение id резюме и его статус приглашения."""
        res = Invitation.objects.filter(vacancy=vacancy).values_list(
            "resume_id", "status"
        )
        return [
            {"id": item[0], "status": settings.STATUS_INVITATION[item[1]][1]}
            for item in res
        ]


class Resume2Serializer(serializers.ModelSerializer):
    """Сериализатор модели вакансии конкретного нанимателя."""

    name = serializers.CharField(source="candidate.username")
    lastVisited = serializers.DateTimeField(source="candidate.last_visited")
    interested = serializers.SerializerMethodField()
    mainSkills = serializers.SerializerMethodField()

    class Meta:
        model = Resume
        fields = (
            "name",
            "photo",
            "level",
            "lastVisited",
            "interested",
            "mainSkills",
        )

    def get_interested(
        self, resume
    ) -> list[int,]:
        """Получение ids резюме, которые наниматель отметили."""
        return Interested.objects.filter(resume=resume).values_list(
            "vacancy_id", flat=True
        )

    def get_mainSkills(
        self, resume
    ) -> list[(Skill, int),]:
        """Получение главных навыков резюме для данной вакансии."""
        vacancy_id = self.context["vacancy_id"]
        print(vacancy_id)
        return resume.get_main_skills(vacancy_id, settings.AMOUNT_MAIN_SKILLS)


class ExperienceSerializer(serializers.ModelSerializer):
    """Сериализатор опыт кандидата."""

    class Meta:
        model = Experience
        fields = (
            "position",
            "period",
            "duties",
        )


class DetailedResumeSerializer(serializers.ModelSerializer):
    """Сериализатор модели подробного резюме."""

    name = serializers.CharField(source="candidate.username")
    age = serializers.CharField(source="get_age")
    city = serializers.CharField(source="city.name")
    jobType = serializers.SerializerMethodField()
    contacts = serializers.CharField(source="telegram")
    about = serializers.CharField(source="about_me")
    skills = serializers.SerializerMethodField()
    experience = serializers.SerializerMethodField()
    education = serializers.SerializerMethodField()
    lastVisited = serializers.DateTimeField(source="candidate.last_visited")
    mainSkills = serializers.SerializerMethodField()

    class Meta:
        model = Resume
        fields = (
            "name",
            "photo",
            "level",
            "age",
            "city",
            "jobType",
            "portfolio",
            "contacts",
            "about",
            "skills",
            "experience",
            "education",
            "lastVisited",
            "mainSkills",
        )

    def get_jobType(self, resume):
        return settings.TYPE_WORK[resume.status_type_work][1]

    def get_skills(
        self, resume
    ) -> list[(Skill, int),]:
        return list(
            SkillInResume.objects.filter(resume=resume)
            .order_by("-rating")
            .values_list("skill__name", "rating")
        )

    def get_experience(self, resume) -> list[str]:
        return Experience.objects.filter(resume=resume).values(
            "position",
            "period",
            "duties",
        )

    def get_education(self, resume) -> list[str]:
        return Education.objects.filter(resume=resume).values(
            "grade",
            "institution",
            "period",
            "speciality",
        )

    def get_mainSkills(
        self, resume
    ) -> list[(Skill, int),]:
        """Получение главных навыков резюме для данной вакансии."""
        vacancy_id = self.context["vacancy_id"]
        print(vacancy_id)
        return resume.get_main_skills(vacancy_id, settings.AMOUNT_MAIN_SKILLS)
