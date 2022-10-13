import datetime
import json
import os
import random
import uuid

from django.contrib.auth.models import User
from mimesis.locales import Locale

from authusersapp.models import UsersModel
from django.core.management.base import BaseCommand

from transportapp.models import ManufacturerModel, TransportTypeModel, TransportModel
import mimesis

NUMBER_OF_STRINGS = 1000


class Command(BaseCommand):
    def handle(self, *args, **options):
        UsersModel.objects.all().delete()
        persona = mimesis.Person('ru')
        for _ in range(NUMBER_OF_STRINGS):
            new_user = UsersModel(
                username=persona.username(),
                first_name=persona.first_name(),
                last_name=persona.last_name(),
                full_name=persona.full_name(),
                email=persona.email(unique=True),
                password=persona.password(),
                is_staff=random.choice([True, False]),
                is_active=random.choice([True, False]),
                is_activated=random.choice([True, False]),
                is_superuser=random.choice([True, False]),
                address=mimesis.Address('ru').address(),
                tel_number=persona.telephone(),
            )

            new_user.save()
        print('new users added')
        types = ['Велосипед', 'Самокат', 'Электросамокат', 'Ролики']
        TransportTypeModel.objects.all().delete()
        for item in types:
            new_transport_type = TransportTypeModel(
                name=item,
            )
            new_transport_type.save()

        print('new transport type added')
        ManufacturerModel.objects.all().delete()

        for _ in range(NUMBER_OF_STRINGS):
            new_manufacturer = ManufacturerModel(
                name=mimesis.Text().word()
            )
            new_manufacturer.save()

        print('new manufacturer added')
        TransportModel.objects.all().delete()
        ids = TransportTypeModel.objects.values("id")
        for _ in range(NUMBER_OF_STRINGS):
            new_transport = TransportModel(
                age_limit=random.randint(0, 18),
                transport_owner=UsersModel.objects.filter(id=random.randint(1, NUMBER_OF_STRINGS)).first(),
                information=mimesis.Text('ru').text(),
                rental_price=random.randint(0, 50000),
                deposit=random.randint(0, 1000),
                year=random.randint(2000, datetime.datetime.now().year),
                transport_model=mimesis.Text('en').word(),
                transport_type=TransportTypeModel.objects.filter(
                    id=random.choice(ids)['id']).first(),
                manufacturer=ManufacturerModel.objects.filter(
                    id=random.randint(1, NUMBER_OF_STRINGS)).first(),
            )
            new_transport.save()

        print('new transport added')
        super_user = UsersModel.objects.create_superuser('adminrental', 'admin@mail.ru', 'AdminR12345')
        if super_user:
            print('All done')
