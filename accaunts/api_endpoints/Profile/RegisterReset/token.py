from django.core.signing import TimestampSigner, BadSignature, SignatureExpired

signer = TimestampSigner(salt='email-verification')
EMAIL_TOKEN_EXPIRY_SECONDS = 3600  

def generate_email_verification_token(user):
    return signer.sign(user.pk)

def verify_email_verification_token(token):
    try:
        unsigned = signer.unsign(token, max_age=EMAIL_TOKEN_EXPIRY_SECONDS)
        return int(unsigned)
    except (BadSignature, SignatureExpired):
        return None
