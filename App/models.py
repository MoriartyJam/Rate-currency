from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings
# from django.core.urlresolvers import reverse
from django.urls import reverse
from django.utils import timezone
import pytz


class Post(models.Model):
    currency = models.TextField(max_length=3, default='SOME STRING')
    period1 = models.DateTimeField(max_length=10)
    period2 = models.DateTimeField(max_length=10)
