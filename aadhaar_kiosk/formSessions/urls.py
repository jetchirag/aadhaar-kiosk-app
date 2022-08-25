from django.urls import path
import aadhaar_kiosk.formSessions.views as sessionsViews

app_name = "formSessions" 
urlpatterns = [
    path("", view=sessionsViews.index, name="index"),
    path("enrol/step1", view=sessionsViews.enrol1, name="enrol1"),
    path("enrol/step2", view=sessionsViews.enrol2, name="enrol2"),
]
