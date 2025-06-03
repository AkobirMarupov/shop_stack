from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes


def send_verification_email(user, token):
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    verify_url = f"{settings.FRONTEND_URL}/verify-email/{uid}/{token}/"

    context = {
        'user': user,
        'email': user.email,
        'verify_url': verify_url,
    }

    subject = "Email manzilingizni tasdiqlang"
    html_message = render_to_string('register.html', context)

    email = EmailMessage(subject, html_message, to=[user.email])
    email.content_subtype = 'html'
    email.send()
