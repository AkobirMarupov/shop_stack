from django.contrib.auth.base_user import BaseUserManager



class UserManager(BaseUserManager):
    use_in_migrations = True


    def _create_user(self, email, password, **extra_fields):
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user



    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuserda is_staff=True bo‘lishi kerak.')

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuserda is_superuser=True bo‘lishi kerak.')

        return self._create_user(email, password, **extra_fields)
