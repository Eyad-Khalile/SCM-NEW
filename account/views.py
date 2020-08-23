from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from .forms import *
from django.core.mail import send_mail, BadHeaderError
from django.utils.translation import gettext as _
from django.contrib import messages
from django.contrib.auth.models import User

from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.forms import formset_factory


# ::::::::::: HOME PAGE :::::::::
def home(request):
    context = {

    }
    return render(request, 'account/home.html', context)

# ::::::::::: ABOUT US :::::::::


def about(request):

    return render(request, 'account/about_as.html')

# :::::::::::::::::::: CONTACT US :::::::::::::::::::::


def contact(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST or None)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            print('subject ====== ', subject)
            print('from_email ====== ', from_email)
            print('message ====== ', message)
            try:
                send_mail(subject, message, from_email,
                          ['khalile.eyad@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalide header found. ')
            return redirect('contact_success')

    return render(request, 'account/contact_as.html', {'form': form})


def contact_success(request):
    return render(request, 'account/contact_success.html')


# ::::::::::: SIGN-UP / REGISTER :::::::::
def register(request):

    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST or None)
        user_email = request.POST.get('email')

        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            new_user.is_active = False
            # Set the chosen password
            new_user.set_password(
                user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            user_form = UserRegistrationForm()

            current_site = get_current_site(request)
            mail_subject = 'Activate your blog account.'
            message = render_to_string('registration/acc_active_email.html', {
                'user': new_user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(new_user.pk)),
                'token': account_activation_token.make_token(new_user),
            })
            to_email = user_email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

            # return render(request,
            #               'registration/register_done.html',
            #               {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()

    context = {
        'user_form': user_form,
    }

    return render(request,
                  'registration/register.html',
                  context)


# ::::::::::: REGISTER ACTIVATION BY E-MAIL :::::::::
def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


# ::::::::::: LOGIN :::::::::
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated '
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


# ::::::::::: USER PROFILE :::::::::
@login_required(login_url='login')
def user_profile(request, user_id):

    context = {

    }

    return render(request, 'registration/profile.html', context)


# ::::::::::: UPDATE USER PROFILE :::::::::

@login_required(login_url='login')
def update_user(request, user_id):

    if request.method == 'POST':
        u_update = UpdateUserForm(request.POST or None, instance=request.user)
        u_profile = ProfileForm(
            request.POST or None, request.FILES or None, instance=request.user.profile)

        if u_update.is_valid() and u_profile.is_valid():
            u_update.save()
            u_profile.save()

            messages.success(
                request, f'Your profile has been updated successfully ')
            return redirect('profile', user_id)

    else:
        u_update = UpdateUserForm(instance=request.user)
        u_profile = ProfileForm(instance=request.user.profile)

    context = {
        'u_update': u_update,
        'u_profile': u_profile,
    }

    return render(request, 'registration/update_profile.html', context)


# ::::::::::: DASHBOARD :::::::::
@login_required(login_url='login')
def dashboard(request):
    user_type = request.user.profile.who_are_you

    if request.method == 'POST':
        u_profile = ProfileForm(request.POST or None, request.FILES or None)
        if u_profile.is_valid():
            profile = u_profile.save(commit=False)
            profile.save()

    else:
        u_profile = ProfileForm()

    context = {
        'user_type': user_type,
        'u_profile': u_profile,
    }
    return render(request, 'account/dashboard.html', context)


# ///////////////////////////////////// FORMULA ////////////////////////////////////////////

# ::::::::::::: SETTINGS FOR EXPERIENCE ::::::::::::
# special field names
TOTAL_FORM_COUNT = 'TOTAL_FORMS'
INITIAL_FORM_COUNT = 'INITIAL_FORMS'
MIN_NUM_FORM_COUNT = 'MIN_NUM_FORMS'
MAX_NUM_FORM_COUNT = 'MAX_NUM_FORMS'
ORDERING_FIELD_NAME = 'ORDER'
DELETION_FIELD_NAME = 'DELETE'

# default minimum number of forms in a formset
DEFAULT_MIN_NUM = 0

# default maximum number of forms in a formset, to prevent memory exhaustion
DEFAULT_MAX_NUM = 1000


# ::::::::::::::::: APPLICATION FOR MEDIA ACTIVIST ::::::::::::::::::
def app_media_act(request, user_id):

    if request.method == 'POST':
        # u_update = UpdateUserForm(request.POST or None, instance=request.user)
        # u_profile = ProfileForm(
        #     request.POST or None, request.FILES or None, instance=request.user.profile)
        u_app = MediaActForm(request.POST or None)
        u_exper = formset_factory(request.POST or None, ExperForm, extra=1)
        # u_violation = ViolationForm(request.POST or None)

        if u_app.is_valid() and u_exper.is_valid():
            user_app = u_app.save(commit=False)
            user_app.user = request.user.id
            user_app.save()
            # u_violation.save()
            for form in u_exper:
                form.save()

            messages.success(
                request, _('لقد تم تقديم الطلب بنجاح'))
            return redirect('home')
    else:
        # u_update = UpdateUserForm(instance=request.user)
        # u_profile = ProfileForm(instance=request.user.profile)
        u_app = MediaActForm()
        u_exper = ExperForm()
        # u_violation = ViolationForm()

    context = {
        # 'u_update': u_update,
        # 'u_profile': u_profile,
        'u_app': u_app,
        'u_exper': u_exper,
    }

    return render(request, 'formula/app_media_act.html', context)
