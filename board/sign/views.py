from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from .forms import  SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from .token import TokenGenerator
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.contrib.auth import get_user_model


class BaseRegisterView(CreateView):
    model = User
    form_class = SignupForm
    success_url = '/sign/login/'
    


def signup(request):
    if request.method == 'POST':
        account_activation_token = TokenGenerator()
        form = SignupForm(request.POST)
        if form.is_valid():
            # save form in the memory not in database
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            # to get the domain of the current site
            current_site = get_current_site(request)
            mail_subject = 'Activation link has been sent to your email id'
            message = render_to_string('sign/activate.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignupForm()
    return render(request, 'sign/signup.html', {'form': form})

def activate(request, uidb64, token): 
    User = get_user_model() 
    try: 
        uid = force_text(urlsafe_base64_decode(uidb64)) 
        user = User.objects.get(pk=uid) 
    except(TypeError, ValueError, OverflowError, User.DoesNotExist): 
        user = None 
    if user is not None and account_activation_token.check_token(user, token): 
        user.is_active = True 
        user.save() 
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.') 
    else: 
        return HttpResponse('Activation link is invalid!') 