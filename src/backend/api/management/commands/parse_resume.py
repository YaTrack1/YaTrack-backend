import os
import csv
import logging

from django.conf import settings
from django.core.management import BaseCommand

from api.management.logger import init_logger
from user.models import User
from resume.models import Resume

# from vacancy.models import Skill

init_logger("parse_resume")
logger = logging.getLogger("parse_resume")

file_name = "resume.csv"


class Command(BaseCommand):

    help = settings.HELP_TEXT_PARSER.format(file_name)

    def add_arguments(self, parser):

        delet = settings.DELETE_TEXT_PARSER.format(file_name)

        parser.add_argument(
            "--delete",
            action="store_true",
            help=delet,
        )

    def handle(self, *args, **options):

        models = [
            Resume,
        ]

        if options[settings.OPTIONS_DELETE]:
            for model in models:
                model.objects.all().delete()
                logger.info(settings.DATA_DELETE.format(model))

        if not options[settings.OPTIONS_DELETE]:
            for model in models:
                if model.objects.exists():
                    logger.info(settings.DATA_UPLOADED.format(model))
                    return

            with open(
                os.path.join(
                    settings.BASE_DIR / settings.DATA_DIR.format(file_name)
                ),
                encoding="utf-8",
            ) as csv_file:

                reader = csv.reader(csv_file, delimiter=",")
                next(reader)

                for row in reader:
                    candidate = User.objects.get(username=row[1])
                    # city = City.objects.get_or_create(name=row[3])
                    # skills = Skill.objects.get_or_create(name=row[9])
                    Resume.objects.get_or_create(
                        title=row[0],
                        candidate=candidate,
                        gender=row[2],
                        # city=city,
                        city=row[3],
                        telegram=row[4],
                        github=row[5],
                        about_me=row[6],
                        birthday=row[7],
                        status_type_work=row[8],
                        status_finded=row[9],
                    )
            logger.info(settings.DATA_LOAD_IN_FILE.format(file_name))
