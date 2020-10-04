from django.urls import path

from users.views import TestPage

urlpatterns = [
    path('', TestPage.as_view(), name='test'),
]
