from django.db import models

class Event(models.Model):
    """
    A simple model to demonstrate a nullable DateTimeField.
    """
    name = models.CharField(
        max_length=200,
        help_text="The name of the event."
    )
    event_date = models.DateTimeField(
        null=True, 
        blank=True,
        help_text="The date and time of the event (optional)."
    )
    foo = models.CharField(
        max_length=200,
        unique=True,
        help_text="foo",
        blank=True,
        null=True,
    )
