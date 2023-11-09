from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model


UserModel = get_user_model()

def custom_validation(data):
    email = data.get('email', '')
    first_name = data.get('first_name', '')
    password = data.get('password', '')

    if not email or UserModel.objects.filter(email=email).exists():
        raise ValidationError('Please choose another email.')

    if not password or len(password) < 8:
        raise ValidationError('Please choose another password with a minimum of 8 characters.')

    if not first_name:
        raise ValidationError('Please choose another firstName.')

    return data



def validate_email(data):
    email = data.get('email', '')
    if not email:
        raise ValidationError('An email is needed.')
    return True


def validate_username(data):
    first_name = data.get('first_name', '')
    if not first_name:
        raise ValidationError('Please choose another firstName.')
    return True

def validate_password(data):
    password = data.get('password', '')
    if not password:
        raise ValidationError('A password is needed.')
    return True