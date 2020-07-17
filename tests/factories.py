from factory import SubFactory
from factory.django import DjangoModelFactory
from faker import Factory

from .models import OneModel, ChildModel


faker = Factory.create()


class OneModelFactory(DjangoModelFactory):
    name = faker.name()
    decimal_value = faker.random_digit()

    class Meta:
        model = OneModel


class ModelWithFileFactory(OneModelFactory):
    document = faker.file_path()


class ChildModelFactory(DjangoModelFactory):
    one = SubFactory(OneModelFactory)
    name = faker.name()

    class Meta:
        model = ChildModel
