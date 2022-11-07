from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.utils import timezone


def stroke_validator(stroke):
    strokes = [
        'front crawl',
        'butterfly',
        'breast',
        'back',
        'freestyle'
    ]

    if stroke not in strokes:
        raise ValidationError(
            ('%(stroke)s is not a valid stroke'), params={'stroke':stroke},
        )

def date_validator(input_date):
    if input_date > timezone.now():
        raise ValidationError(
            (f"Can't set record in the future.")
        )

def record_broken_date_validator(input_date):
    if input_date < timezone.now():
        raise ValidationError(
            (f"Can't break record before record was set.")
        )


class SwimRecord(models.Model):
    # pass # delete me when you start writing in validations
    first_name = models.CharField(max_length=100, null=False, blank=False)
    last_name = models.CharField(max_length=100, null=False, blank=False)
    team_name = models.CharField(max_length=100, null=False, blank=False)
    relay = models.BooleanField(null=False, blank=False)
    stroke = models.CharField(max_length=100, validators=[stroke_validator])
    distance = models.IntegerField(validators=[MinValueValidator(50)])
    record_date = models.DateTimeField(validators=[date_validator])
    record_broken_date = models.DateTimeField(validators=[record_broken_date_validator])