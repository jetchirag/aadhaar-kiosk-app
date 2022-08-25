import datetime
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from aadhaar_kiosk.formSessions.models import enrolForm


class enrol1Form(forms.ModelForm):
    """
    Step 1 of enrolment form
    Fields:
    - Name
    - Gender
    - Date of Birth
    """
    # username = forms.CharField(label='Your Name', max_length=100)
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


        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'Submit', css_class='btn-lg btn-block submitBtnBottom fs-1', style=""))

    class Meta:
        model = enrolForm                                 
        fields = ['fullname', 'gender', 'dob']

class enrol2Form(forms.ModelForm):
    """
    Step 2 of enrolment form
    Fields:
    - Address 1
    """
    def __init__(self, field, *args, **kwargs):
        super(enrol2Form, self).__init__(*args, **kwargs)

        # If you pass FormHelper constructor a form instance
        # It builds a default layout with all its fields
        self.helper = FormHelper(self)

        self.fields["address_no"] = forms.CharField()


        # You can dynamically adjust your layout
        self.helper.layout.append(Submit('save', 'Submit', css_class='btn-lg btn-block submitBtnBottom fs-1', style=""))

    class Meta:
        model = enrolForm                                 
        fields = ['address_co']