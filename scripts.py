from django.db import models
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation
from dotenv import load_dotenv
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
import os
load_dotenv()


try:
    schoolkid = get_object_or_404(Schoolkid, full_name=os.getenv("KID_NAME", "Фролов Иван Григорьевич"))
except ObjectDoesNotExist:
    print 'Does Not Exist!'

def fix_marks():
    Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3]).update(points=5)

def remove_chastisements():
    chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
    chastisements.delete()
    
def create_commendation(subject__title):
    lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter, subject__title=subject__title).first()
    if lesson:
        Commendation.objects.create(text="Хвалю!", created=lesson.date, schoolkid=schoolkid, subject=lesson.subject, teacher=lesson.teacher)
    else:
        print("урок не найден")


