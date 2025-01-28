from django.core.management import BaseCommand
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    def handle(self, *args, **options):
        User = get_user_model()
        user = User.objects.create(
            email='testmail@mail.ru',
            first_name='admin',
            last_name='admin',
        )

        user.set_password('1234')

        user.is_staff = True
        user.is_superuser = True

        user.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully created admin user with {user.email}'))
