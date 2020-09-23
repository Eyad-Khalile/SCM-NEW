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
from django.forms import formset_factory, modelformset_factory, inlineformset_factory


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
    if request.user.is_authenticated:
        return redirect('home')
    else:

        users = User.objects.all()
        emails = []
        for user in users:
            # emails += user.email,
            emails.append(user.email)
            print('emails ======== :', emails)

        if request.method == 'POST':
            user_form = UserRegistrationForm(request.POST or None)
            user_email = request.POST.get('email')

            if user_email not in emails:

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
                    mail_subject = 'Activate your SCM account.'
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
                    # return HttpResponse('Please confirm your email address to complete the registration')
                    messages.success(request, _(
                        'لقد تم أرسال بريد الكتروني يتضمن رابط لتأكيد التسجيل , يرجى التحقق من البريد لتتمكن من  تسجيل الدخول'))
                    return redirect('home')

                    # return render(request,
                    #               'registration/register_done.html',
                    #               {'new_user': new_user})

            else:
                if user_email in emails:
                    messages.warning(
                        request, f'رحاءً , انشئ حساب باستخدام بريد الكتروني آخر, هذا البريد الاكتروني {user_email} مستخدم ')
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

        # return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
        messages.success(request, _(
            'شكرا لتأكيد بريدك الالكتروني , اﻵن يمكنك تسجيل الدخول'))
        return redirect('login')
    else:
        # return HttpResponse('Activation link is invalid!')
        messages.warning(request, _('رابط التحقق غير فعال'))
        return redirect('home')


# ::::::::::: LOGIN :::::::::
def user_login(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
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
@login_required(login_url='login')
def app_media_act(request, user_id):

    ExFormset = modelformset_factory(
        WorkDetail, form=ExperForm, extra=11, can_delete=True)
    VioFormset = modelformset_factory(
        Violation, form=ViolationForm, extra=11, can_delete=True)

    if request.method == 'POST':
        registerForm = MediaActForm(request.POST or None)
        # expForm = ExFormset(request.POST or None, queryset=WorkDetail.objects.filter(worker__id=user_id))
        # vioForm = VioFormset(request.POST or None, queryset=Violation.objects.filter(victim__id=user_id))
        expForm = ExFormset(request.POST or None,
                            queryset=WorkDetail.objects.none())
        vioForm = VioFormset(request.POST or None,
                             queryset=WorkDetail.objects.none())
        upForm = UploadForm(request.POST or None, request.FILES or None)

        if registerForm.is_valid() and expForm.is_valid() and vioForm.is_valid() and upForm.is_valid():
            reg_user = registerForm.save(commit=False)
            reg_user.user = request.user
            reg_user.profile = request.user.profile
            reg_user.save()
            registerForm = MediaActForm()

            instances = expForm.save(commit=False)
            for instance in instances:
                instance.registration_media_act = reg_user
                # instance.worker_id = request.user.id
                instance.save()

            inst_vio = vioForm.save(commit=False)
            for inst in inst_vio:
                inst.violation = reg_user
                # inst.victim_id = request.user.id
                inst.save()

            for field in request.FILES.keys():
                print('field  ==== : ', field)
                filename = request.FILES[field]
                print('filename  ==== : ', filename)
                for formfile in request.FILES.getlist(field):
                    print('formfile  ==== : ',  formfile)
                    doc = docs(docs=reg_user, doc=formfile)
                    doc.save()
                    upForm = UploadForm()

            messages.success(request, _('لقد تم تقديم الطلب بنجاح'))

            mail_subject = 'تأكيد استلام طلب'
            message = 'لقد تم استلام الطلب و ستتم معالجته باقرب وقت ممكن و إعلامكم بالنتجية'
            to_email = request.user.email
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()

            return redirect('app_media_act', user_id)
        else:
            messages.error(request, _('نرحو التحقق من كافة الحقول المطلوبة'))

    else:
        registerForm = MediaActForm()
        # expForm = ExFormset(
        #     queryset=WorkDetail.objects.filter(worker__id=user_id))
        # vioForm = VioFormset(
        #     queryset=Violation.objects.filter(victim__id=user_id))
        expForm = ExFormset(queryset=WorkDetail.objects.none())
        vioForm = VioFormset(queryset=WorkDetail.objects.none())
        upForm = UploadForm()

    context = {
        'registerForm': registerForm,
        'expForm': expForm,
        'vioForm': vioForm,
        'upForm': upForm,
    }

    return render(request, 'formula/app_media_act.html', context)


def faq(request):

    return render(request, 'account/faq.html')
