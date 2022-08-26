from django.shortcuts import render,redirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.conf import settings
from django.utils import translation

from aadhaar_kiosk.formSessions import forms as enrolForms
from aadhaar_kiosk.formSessions.models import enrolForm


def index(request):
    return render(request, "kiosk/home.html")

def set_language(request, slug):
    language = slug
    print("Changing language to ", language)
    translation.activate(language)
    response = redirect('formSessions:index')
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
    return response


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
            if (request.GET.get('edit') == 'true'):
                try:
                    uuid = request.session.get('uuid')
                    print("UUID: ", uuid)
                except enrolForm.DoesNotExist:
                    print("Enrolment form does not exist, redirecting to step 1")
                    return redirect(reverse('formSessions:enrol1'))

                update_field = {
                    'firstname': request.POST.get('firstname'),
                    'middlename': request.POST.get('middlename'),
                    'lastname': request.POST.get('lastname'),
                    'gender': request.POST.get('gender'),
                }

                enrolForm.objects.filter(uuid=uuid).update(**update_field)

                return redirect(reverse('formSessions:enrolPreview'))
                
            else:
                f = form.save()
                # Save the uuid to session 
                request.session['uuid'] = str(f.uuid)

                print("UUID: ", request.session.get('uuid'))
                return redirect(reverse('formSessions:enrol_dob'))


            

            # redirect to a new URL:
        return render(request, "kiosk/enrol/step1.html", {'form': form})
    else:
        # Check if request is for edit form
        print("test")
        if request.GET.get('edit'):
            print("EDIT FORM")
            try:
                uuid = request.session.get('uuid')
                print("UUID: ", uuid)
                instance = enrolForm.objects.get(uuid=request.session.get('uuid'))
            except enrolForm.DoesNotExist:
                print("Enrolment form does not exist, redirecting to step 1")
                return redirect(reverse('formSessions:enrol1'))
                
            form = enrolForms.enrol1Form(instance=instance)
            return render(request, "kiosk/enrol/step1.html", {'form': form, 'instance': instance, 'edit': True})
        else:
            print("NEW FORM")
            form = enrolForms.enrol1Form()
            return render(request, "kiosk/enrol/step1.html", {'form': form})


def enrol_dob(request):
    if request.session.get('uuid') is None:
        return redirect(reverse('formSessions:enrol1'))
    else:
        try:
            enrolForm.objects.get(uuid=request.session.get('uuid'))
        except enrolForm.DoesNotExist:
            print("Enrolment form does not exist, redirecting to step 1")
            return redirect(reverse('formSessions:enrol1'))

    uuid = request.session.get('uuid')
    print("UUID: ", uuid)
    if request.method == 'POST':
        print("Post: ", request.POST)
        # Check if the form is valid:
        instance = get_object_or_404(enrolForm, uuid=uuid)
        form = enrolForms.enrolDOBForm(request.POST, instance=instance)
        if form.is_valid():

            print("VALID FORM")

            # Save the data to the database.
            f = form.save()

            # Save the uuid to session 
            request.session['uuid'] = str(f.uuid)

            print("UUID: ", request.session.get('uuid'))
            return redirect(reverse('formSessions:enrol2',kwargs={'slug': 'address_co'}))

            # redirect to a new URL:
        return render(request, "kiosk/enrol/step_dob.html", {'form': form})
    else:
        form = enrolForms.enrol1Form()
        return render(request, "kiosk/enrol/step_dob.html")


def enrol2(request, slug):
    # Verify uuid is set in session, if not redirect to step 1
    if request.session.get('uuid') is None:
        return redirect(reverse('formSessions:enrol1'))
    else:
        try:
            enrolForm.objects.get(uuid=request.session.get('uuid'))
        except enrolForm.DoesNotExist:
            print("Enrolment form does not exist, redirecting to step 1")
            return redirect(reverse('formSessions:enrol1'))
    uuid = request.session.get('uuid')

    # Address fields list
    address_fields = {
        'address_co': "C/o",
        'address_no': "House Number",
        'address_2': "Street / Road",
        'address_landmark': "Landmark",
        'address_area': "Area",
        'address_city': "Village / Town / City",
        'address_postoffice': "Post Office",
        'address_district': "District",
        'address_subdistrict': "Sub-District",
        'address_state': "State",
    }

    

    # Handle POST request
    if request.method == 'POST':
        # instance = enrolForm.objects.get(uuid=uuid)
        instance = get_object_or_404(enrolForm, uuid=uuid)
        form = enrolForms.enrol2Form(request.POST, instance=instance)
        print("Processing POST request")
        print("Post request data: ", request.POST)
        print("Form data: ", form.data)
        # Check if the form is valid:
        if form.is_valid():
            print("VALID FORM")

            # Manually update database
            update_field = {
                slug: request.POST.get(slug),
            }

            enrolForm.objects.filter(uuid=uuid).update(**update_field)

            # Save the data to the database.
            # form.save(commit=False)

            # Get the next field in the address_fields list
            try:
                next_field = list(address_fields.keys())[list(address_fields.keys()).index(slug)+1]
                return redirect(reverse('formSessions:enrol2',kwargs={'slug': next_field}))
            except IndexError:
                return redirect(reverse('formSessions:enrol3'))
        else:
            print("INVALID FORM")
            print(form.errors)

            # redirect to a new URL:
        return render(request, "kiosk/enrol/step2.html", {'label': address_fields[slug], 'name': slug})

    # Handle GET request
    else:
        # Decide which field to load
        if slug in address_fields:
            return render(request, "kiosk/enrol/step2.html", {'label': address_fields[slug], 'name': slug})
        else:
            return HttpResponse("Invalid URL")

def enrol3(request):
     # Verify uuid is set in session, if not redirect to step 1
    if request.session.get('uuid') is None:
        return redirect(reverse('formSessions:enrol1'))
    else:
        try:
            enrolForm.objects.get(uuid=request.session.get('uuid'))
        except enrolForm.DoesNotExist:
            print("Enrolment form does not exist, redirecting to step 1")
            return redirect(reverse('formSessions:enrol1'))
    uuid = request.session.get('uuid')
    print("UUID: ", uuid)
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        instance = get_object_or_404(enrolForm, uuid=uuid)
        form = enrolForms.enrol3Form(request.POST, instance=instance)

        # Check if the form is valid:
        if form.is_valid():

            print("VALID FORM")

            # Save the data to the database.
            f = form.save()
            return redirect(reverse('formSessions:enrol4'))

            # redirect to a new URL:
        return render(request, "kiosk/enrol/step3.html", {'form': form})
    else:
        form = enrolForms.enrol3Form()
        return render(request, "kiosk/enrol/step3.html", {'form': form})

def enrol4(request):
      # Verify uuid is set in session, if not redirect to step 1
    if request.session.get('uuid') is None:
        return redirect(reverse('formSessions:enrol1'))
    else:
        try:
            enrolForm.objects.get(uuid=request.session.get('uuid'))
        except enrolForm.DoesNotExist:
            print("Enrolment form does not exist, redirecting to step 1")
            return redirect(reverse('formSessions:enrol1'))
    uuid = request.session.get('uuid')
    print("UUID: ", uuid)
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        instance = get_object_or_404(enrolForm, uuid=uuid)
        form = enrolForms.enrol4Form(request.POST, instance=instance)

        # Check if the form is valid:
        if form.is_valid():

            print("VALID FORM")

            # Save the data to the database.
            f = form.save()
            return redirect(reverse('formSessions:enrolFingerPrint'))

            # redirect to a new URL:
        return render(request, "kiosk/enrol/step4.html", {'form': form})
    else:
        form = enrolForms.enrol4Form()
        return render(request, "kiosk/enrol/step4.html", {'form': form})

def enrolFingerPrint(request):
    # Verify uuid is set in session, if not redirect to step 1
    if request.session.get('uuid') is None:
        return redirect(reverse('formSessions:enrol1'))
    else:
        try:
            enrolForm.objects.get(uuid=request.session.get('uuid'))
        except enrolForm.DoesNotExist:
            print("Enrolment form does not exist, redirecting to step 1")
            return redirect(reverse('formSessions:enrol1'))
    uuid = request.session.get('uuid')
    print("UUID: ", uuid)
    
    return render(request, "kiosk/enrol/fingerprint.html")


def enrolIris(request):
    # Verify uuid is set in session, if not redirect to step 1
    if request.session.get('uuid') is None:
        return redirect(reverse('formSessions:enrol1'))
    else:
        try:
            enrolForm.objects.get(uuid=request.session.get('uuid'))
        except enrolForm.DoesNotExist:
            print("Enrolment form does not exist, redirecting to step 1")
            return redirect(reverse('formSessions:enrol1'))
    uuid = request.session.get('uuid')
    print("UUID: ", uuid)
    
    return render(request, "kiosk/enrol/iris.html")


def enrolPreview(request):
    # Verify uuid is set in session, if not redirect to step 1
    if request.session.get('uuid') is None:
        return redirect(reverse('formSessions:enrol1'))
    else:
        try:
            enrolForm.objects.get(uuid=request.session.get('uuid'))
        except enrolForm.DoesNotExist:
            print("Enrolment form does not exist, redirecting to step 1")
            return redirect(reverse('formSessions:enrol1'))

    uuid = request.session.get('uuid')
    instance = get_object_or_404(enrolForm, uuid=uuid)

    fields = {
        'First Name': {
            'value': instance.firstname,
            'edit': reverse('formSessions:enrol1'),
        },
        'Middle Name': {
            'value': instance.middlename,
            'edit': reverse('formSessions:enrol1'),
        },
        'Last Name': {
            'value': instance.lastname,
            'edit': reverse('formSessions:enrol1'),
        },
        'Gender': {
            'value': instance.get_gender_display,
            'edit': reverse('formSessions:enrol1'),
        },
        'Date of Birth': {
            'value': instance.dob,
            'edit': reverse('formSessions:enrol_dob'),
        },
    }
    address_fields = {
        'address_co': "C/o",
        'address_no': "House Number",
        'address_2': "Street / Road",
        'address_landmark': "Landmark",
        'address_area': "Area",
        'address_city': "Village / Town / City",
        'address_postoffice': "Post Office",
        'address_district': "District",
        'address_subdistrict': "Sub-District",
        'address_state': "State",
    }
    # Add address fields to fields dict
    for key, value in address_fields.items():
        fields[value] = {
            'value': getattr(instance, key),
            'edit': reverse('formSessions:enrol2', kwargs={'slug': key}),
        }

    fields['Email Address'] ={
            'value': instance.email,
            'edit': reverse('formSessions:enrol3'),
        }
    fields['Phone Number'] = {
            'value': instance.phone,
            'edit': reverse('formSessions:enrol3'),
        }
    
    
    return render(request, "kiosk/enrol/preview.html", {'fields': fields})


##################
# Updation Form #
##################

def update1(request):
    
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
            return redirect(reverse('formSessions:enrol_dob'))

            # redirect to a new URL:
        return render(request, "kiosk/enrol/step1.html", {'form': form})
    else:
        # Set language to get request
        

        form = enrolForms.enrol1Form()
        return render(request, "kiosk/update/step1.html", {'form': form})
