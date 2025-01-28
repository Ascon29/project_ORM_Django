from django.core.management import BaseCommand
from library.models import Autor, Book


class Command(BaseCommand):
    help = 'Add books'

    def handle(self, *args, **kwargs):
        author, _ = Autor.objects.get_or_create(first_name='Антон', last_name='Чехов', birth_date='1860-01-29')

        books = [
            {'title': 'Вишневый сад', 'publication_date': '1904-01-01', 'author': author},
            {'title': 'Три сестры', 'publication_date': '1901-01-01', 'author': author},
        ]

        for book_data in books:
            book, created = Book.objects.get_or_create(**book_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Book succesfully created: {book}'))
            else:
                self.stdout.write(self.style.WARNING(f'Book already exists: {book}'))
