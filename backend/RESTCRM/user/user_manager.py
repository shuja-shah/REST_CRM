from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migrations: True
    
    def create_user(self, username, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return username
    
    def create_superuser(self, username, email, password, **extra_fields):
        user = self.create_user(
            username=username,
            email=email,
            password=password,
            **extra_fields
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
    def delete_user(self, username):
        user = self.get(username=username)
        if user:
            user.delete()
            return str('deleted!')
        return str('No User Found!')
    
    def get_user(self,username):
        user = self.get(username=username)
        if user:
            return user
        return str('no such user exists')