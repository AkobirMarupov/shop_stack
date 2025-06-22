from django.dispatch import receiver
from django.db.models.signals import post_save
import json

from django_celery_beat.models import CrontabSchedule, PeriodicTask
from celery.schedules import timedelta

from datetime import datetime, timedelta

from accaunts.models import Story



@receiver(post_save, sender=Story)
def story_post_save(sender, instance, created, **kwargs):
    print("Signal is working!")
    if created:

        expire_time = instance.created_at + timedelta(minutes=1)

        args = [instance.id]
        print(expire_time, args)

        start_crontab, created = CrontabSchedule.objects.get_or_create(
            minute=expire_time.minute,
            hour=expire_time.hour,
            day_of_month=expire_time.day,
            month_of_year=expire_time.month,
            timezone=str(expire_time.tzinfo) if expire_time.tzinfo else 'UTC'
        )

        PeriodicTask.objects.create(
            crontab=start_crontab,
            name=f"task_expire_story_{instance.id}",
            task="accaunts.tasks.create_story_expirer_task",
            args=json.dumps(args),  # args ni json ko‘rinishda yozish kerak
            one_off=True
        )
