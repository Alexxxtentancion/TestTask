import factory.django

from .models import Person


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    date_of_birth = factory.Faker('date_of_birth')



# for _ in range(200):
#     PersonFactory._create()
