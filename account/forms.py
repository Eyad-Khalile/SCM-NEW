from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(
        max_length=200, required=True, label=_('البريد اﻹلكتروني'))
    password = forms.CharField(
        label=_('كلمة السر'), widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=_('تأكيد كلمة السر'), widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


# class UserRegistrationForm(UserCreationForm):
#     first_name = forms.CharField(
#         max_length=30, required=False, help_text='Optional.', label=_('الاسم'))
#     last_name = forms.CharField(
#         max_length=30, required=False, help_text='Optional.', label=_('اسم العائلة'))
#     email = forms.EmailField(max_length=254,  required=True,
#                              help_text='Required. Inform a valid email address.', label=_('البريد الالكتروني'))

#     class Meta:
#         model = User
#         fields = ['username', 'first_name', 'last_name',
#                   'email', 'password1', 'password2']


class UpdateUserForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=100, required=True, label=_('الاسم اﻷول'))
    last_name = forms.CharField(
        max_length=100, required=True, label=_('اسم العائلة'))

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = ('gender', 'nickname', 'birth_date',
                  'birth_place', 'country', 'region', 'current_country', 'current_region', 'current_area', 'phone', 'facebook', 'who_are_you', 'image')
        labels = {
            'gender': _('الجنس'),
        }
        # exclude = ['user']


class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)

    class Meta:
        fields = [
            'from_email',
            'subject',
            "message",
        ]

        labels = {
            'from_email': _('بريدك الالكتروني'),
            'subject': _('الموضوع'),
            "message": _('نص الرسالة'),
        }


# :::::::::::::::: FORMULA :::::::::::::::::::::


class MediaActForm(forms.ModelForm):
    class Meta:
        model = RegisterMediaAct
        fields = [
            'family_state',
            'have_kids',
            'number_kids',
            'summary_family',
            'medical_state_q',
            'medical_state_des',
            'education_level',
            'job',
            'experience',
            'if_article_linke',
            'articls_link_1',
            'if_stop_work',
            'date_stop_work',
            'summary_of_your_state',
            'resource_prof',
            'recmond_1',
            'phon_1',
            'email_1',
            'recmond_2',
            'phon_2',
            'email_2',
            'org_memeber',
            'details',
            'violations',
            'relation_with_org',
            'summary_of_relations',
            'type_of_dmande',
            'resaon_for_help',
            'list_of_tools',
            'last_job_salary',
            'reason_stopping_job',
            'summary_of_help',
            'other_org_demand',
            'name_org',
            'date_of_demand_org',
            'type_of_demand_other_org',
            'result_of_demand_other_org',
            'know_support_programme',
            'training_media',
            'details_traning_media',
        ]

# :::::::::::: EXPERIENCE ::::::::::::


class ExperForm(forms.ModelForm):
    class Meta:
        model = WorkDetail
        fields = [
            'org_name',
            'job_title',
            'job_location',
            'start_date',
            'until_now',
            'end_date',
            'if_salary',
            'salary',
        ]

# :::::::::::::: VIOLATIONS :::::::::::::


class ViolationForm(forms.ModelForm):
    class Meta:
        model = Violation
        fields = [
            'violation_type',
            'date_of_violation',
            'responsibility',
        ]
