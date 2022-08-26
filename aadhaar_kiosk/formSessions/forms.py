import datetime
from django import forms
from django.utils import translation
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from aadhaar_kiosk.formSessions.models import enrolForm

class enrol1Form(forms.ModelForm):
    """
    Step 1 of enrolment form
    Fields:
    - Name
    - Gender
    """
    firstname = forms.CharField(label=_("First Name"), max_length=100, min_length=3, widget=forms.widgets.TextInput(
        attrs={
            'minlength': '3',
            'data-parsley-minlength': '3',
            }
        ),)
    middlename = forms.CharField(label=_('Middle Name'), max_length=100, widget=forms.widgets.TextInput(
        attrs={
            'minlength': '3',
            'required': False,
            }
        ),)
    lastname = forms.CharField(label=_('Last Name'), max_length=100, widget=forms.widgets.TextInput(
        attrs={
            'minlength': '3',
            }
        ),)
    # dob = forms.DateField(label="Date of Birth", widget=forms.widgets.DateInput(
    #     attrs={
    #         'type': 'date',
    #         'data-kioskboard-type': 'all',
    #         'data-kioskboard-placement': 'top',
    #         'data-kioskboard-specialcharacters': 'true',
    #         'class': 'onkeyboard'
    #         }
    #     ),)
    def __init__(self, *args, **kwargs):
        super(enrol1Form, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.field_class = "onkeyboard"
        self.fields['middlename'].required = False



        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'Submit', css_class='btn-lg btn-block button-5 fs-1', style=""))

    class Meta:
        model = enrolForm                                 
        fields = ['firstname', 'middlename', 'lastname', 'gender']
        labels = {
            'gender': _('Gender'),
            'middle_name': _('Middle Name'),
        }


class enrolDOBForm(forms.ModelForm):
    """
    Step 1 of enrolment form
    Fields:
    - DOB
    """
    def __init__(self, *args, **kwargs):
        super(enrolDOBForm, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.field_class = "onkeyboard"


        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'Submit', css_class='btn-lg btn-block submitBtnBottom fs-1', style=""))
    class Meta:
        model = enrolForm                                 
        fields = ['dob']

class enrol2Form(forms.ModelForm):
    """
    Step 2 of enrolment form
    Fields:
    - address_co
    - address_no
    - address_2
    - address_landmark
    - address_area
    - address_city
    - address_postoffice
    - address_district
    - address_subdistrict
    - address_state
    """

    class Meta:
        model = enrolForm
        fields = ['address_co', 'address_no', 'address_2', 'address_landmark', 'address_area', 'address_city', 'address_postoffice', 'address_district', 'address_subdistrict', 'address_state']

class enrol3Form(forms.ModelForm):
    """
    Step 3 of enrolment form
    Fields:
    - email
    """
    email = forms.EmailField(label="", help_text="asd", widget=forms.widgets.EmailInput(
        attrs={
            'data-kioskboard-specialcharacters': 'true',
            }
        ),)
    def __init__(self, *args, **kwargs):
        super(enrol3Form, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.field_class = "onkeyboard"


        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'Submit', css_class='btn-lg btn-block button-5 fs-1', style=""))

    class Meta:
        model = enrolForm
        fields = ['email']

class enrol4Form(forms.ModelForm):
    """
    Step 3 of enrolment form
    Fields:
    - email
    - phone
    """
    phone = forms.IntegerField(label="", 
        validators=[
            RegexValidator(
                '^(\w+\d+|\d+\w+)+$',
                message="Password should be a combination of Alphabets and Numbers"
            )
        ],
        widget=forms.widgets.NumberInput(
        attrs={
            'type': 'tel',
            'pattern': '[0-9]{10}',
            'data-kioskboard-type': 'numpad',
            }
        ),)
    def __init__(self, *args, **kwargs):
        super(enrol4Form, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.field_class = "onkeyboard"


        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'Submit', css_class='btn-lg btn-block button-5 fs-1', style=""))

    class Meta:
        model = enrolForm
        fields = ['phone']



################
# Update Form #
################


class update1Form(forms.ModelForm):
    """
    Step 1 of enrolment form
    Fields:
    - Name
    - Gender
    """
    # aadhaar = forms.CharField(label=_("First Name"), max_length=100, widget=forms.widgets.TextInput(
    #     attrs={
    #         'minlength': '3',
    #         }
    #     ),)
    # dob = forms.DateField(label="Date of Birth", widget=forms.widgets.DateInput(
    #     attrs={
    #         'type': 'date',
    #         'data-kioskboard-type': 'all',
    #         'data-kioskboard-placement': 'top',
    #         'data-kioskboard-specialcharacters': 'true',
    #         'class': 'onkeyboard'
    #         }
    #     ),)
    def __init__(self, *args, **kwargs):
        super(enrol1Form, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)
        self.helper.field_class = "onkeyboard"
        self.fields['middlename'].required = False


        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'Submit', css_class='btn-lg btn-block button-5 fs-1', style=""))

    class Meta:
        model = enrolForm                                 
        fields = ['firstname', 'middlename', 'lastname', 'gender']
        labels = {
            'firstname': _('First Name'),
        }

