from django.shortcuts import render,redirect
from django.urls import reverse
from django.http import HttpResponse

from aadhaar_kiosk.formSessions import forms as enrolForms
from aadhaar_kiosk.formSessions.models import enrolForm


def index(request):
    return render(request, "kiosk/home.html")


#####################
### ENROL VIEWS #####
#####################

def enrol1(request):
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = enrolForms.enrol1Form(request.POST)

        # Check if the form is valid:
        if form.is_valid():

            print("VALID FORM")

            # Save the data to the database.
            f = form.save()

            # Save the uuid to session 
            request.session['uuid'] = str(f.uuid)

            print("UUID: ", request.session.get('uuid'))
            return redirect(reverse('formSessions:enrol2'))

            # redirect to a new URL:
        return render(request, "kiosk/enrol/step1.html", {'form': form})
    else:
        form = enrolForms.enrol1Form()
        return render(request, "kiosk/enrol/step1.html", {'form': form})

def enrol2(request):
    if request.method == 'POST':
        uuid = "8b4df4ec-75b0-48e7-8260-0bb42519d714"
        instance = enrolForm.objects.get(uuid=uuid)

        form = enrolForms.enrol1Form(request.POST, instance=instance)

        # Check if the form is valid:
        if form.is_valid():

            print("VALID FORM")

            # Save the data to the database.
            form.save()

            # redirect to a new URL:
        return render(request, "kiosk/enrol/step1.html", {'form': form})
    else:
        form = enrolForms.enrol2Form('address_co')
        return render(request, "kiosk/enrol/step1.html", {'form': form})