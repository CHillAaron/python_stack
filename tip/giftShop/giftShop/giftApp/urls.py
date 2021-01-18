from django.urls import path
from . import views

urlpatterns = [
    # @app.route("/")
    path("", views.index), #localhost:8000
    path("sendBlessings", views.processGiftSubmission)
]
