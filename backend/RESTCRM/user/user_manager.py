from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations: True
    
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return username
    
    