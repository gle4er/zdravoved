from django.views.generic import TemplateView

from users.celery import debug_task

class TestPage(TemplateView):
    template_name = 'main.html'

    def get_context_data(self, **kwargs):
        debug_task.delay()
