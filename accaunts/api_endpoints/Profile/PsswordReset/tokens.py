from django.utils import timezone
from django.core.signing import TimestampSigner, BadSignature, SignatureExpired
from django.conf import settings


signer = TimestampSigner(salt='password-reset')

TOKEN_EPIRY_SECONDS = 3600

def generate_password_reset_token(user):
    return signer.sign(user.pk)

def verify_password_reset_token(token):
    try:
        unsigned = signer.unsign(token, max_age=TOKEN_EPIRY_SECONDS)
        return int(unsigned)
    except (BadSignature, SignatureExpired):
        return None