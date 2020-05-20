from django.test import TestCase

from .factories import OneModelFactory
from .models import OneModel


class OneModelTests(TestCase):

    def test_model(self):
        NUM_RECORDS = 100
        OneModelFactory.create_batch(size=NUM_RECORDS)

        self.assertEqual(OneModel.objects.all().count(), NUM_RECORDS)
