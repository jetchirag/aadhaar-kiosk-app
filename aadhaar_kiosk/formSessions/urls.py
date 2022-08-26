from django.urls import path
import aadhaar_kiosk.formSessions.views as sessionsViews

app_name = "formSessions" 
urlpatterns = [
    path("", view=sessionsViews.index, name="index"),
    path("set_language/<slug:slug>", view=sessionsViews.set_language, name="set_language"),

    # Enrol Form
    path("enrol/step1", view=sessionsViews.enrol1, name="enrol1"),
    path("enrol/step2/<slug:slug>", view=sessionsViews.enrol2, name="enrol2"),
    path("enrol/step_dob", view=sessionsViews.enrol_dob, name="enrol_dob"),
    path("enrol/step3", view=sessionsViews.enrol3, name="enrol3"),
    path("enrol/step4", view=sessionsViews.enrol4, name="enrol4"),

    path("enrol/fingerprint", view=sessionsViews.enrolFingerPrint, name="enrolFingerPrint"),
    path("enrol/iris", view=sessionsViews.enrolIris, name="enrolIris"),

    path("enrol/preview", view=sessionsViews.enrolPreview, name="enrolPreview"),

    ## Update URLS
    path("update/step1", view=sessionsViews.update1, name="update1"),
]
