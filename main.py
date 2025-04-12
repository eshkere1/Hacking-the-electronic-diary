from django.db import models
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
from dotenv import load_dotenv
load_dotenv()

SCHOOLKID = Schoolkid.objects.get(full_name=os.getenv(KID_NAME, "Фролов Иван Григорьевич"))


def fix_marks():
    bad_marks = Mark.objects.filter(schoolkid=schoolkid[0], points__in=[2, 3])
    for bad_mark in bad_marks:
        bad_mark.points=5
        bad_mark.save()

def remove_chastisements():
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()
    
def create_commendation(subject__title):
    lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject__title=subject__title)[0]
    Commendation.objects.create(text="Хвалю!", created=lesson.date, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher)


