from django.db import models


class CalendarData(models.Model):
    calendar_status = models.JSONField()
