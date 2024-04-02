# middleware.py

from django.http import HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import CompetitionSettings

class CompetitionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            competition_settings = CompetitionSettings.objects.first()
            if competition_settings:
                start_time = competition_settings.start_time
                over_time = competition_settings.over_time

                # Make datetime.now() timezone-aware
                current_time = timezone.now()

                if request.path != reverse('countdown') and not request.path.startswith('/admin'):  # Exclude admin and countdown page
                    if current_time < start_time:  # Before competition starts
                        return HttpResponseRedirect(reverse('countdown'))
                    elif current_time > over_time:  # After competition over time
                        return HttpResponseRedirect(reverse('competition_over'))
        except CompetitionSettings.DoesNotExist:
            pass

        response = self.get_response(request)
        return response
