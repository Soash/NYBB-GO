# decorators.py

from django.http import HttpResponseRedirect
from django.urls import reverse
from datetime import datetime
from .models import CompetitionSettings

def competition_active(view_func):
    def wrapper(request, *args, **kwargs):
        try:
            competition_settings = CompetitionSettings.objects.first()
            if competition_settings:
                start_time = competition_settings.start_time
                over_time = competition_settings.over_time

                if datetime.now() < start_time or datetime.now() > over_time:
                    return HttpResponseRedirect(reverse('countdown'))
        except CompetitionSettings.DoesNotExist:
            pass

        return view_func(request, *args, **kwargs)
    return wrapper
