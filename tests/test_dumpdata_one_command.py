from io import StringIO
import json

from django.core.management import call_command
from django.core.management.base import CommandError
from django.test import TestCase

from .factories import OneModelFactory


class DumpDataOneCallTests(TestCase):
    def setUp(self):
        self.APP_MODEL = 'tests.onemodel'
        self.COMMAND = 'dumpdata_one'
        self.NON_EXISTING_MODEL = 'zero.model'

    def test_without_parameter(self):

        out = StringIO()

        with self.assertRaises(CommandError):
            call_command(self.COMMAND, stdout=out)

    def test_with_invalid_app_model(self):

        out = StringIO()

        with self.assertRaises(LookupError):
            call_command(self.COMMAND, self.NON_EXISTING_MODEL, stdout=out)

    def test_with_no_records(self):

        out = StringIO()
        call_command(self.COMMAND, self.APP_MODEL, stdout=out)

        results = json.loads(out.getvalue())

        self.assertEqual(results, [])

    def test_with_one_records(self):
        OneModelFactory()

        out = StringIO()
        call_command(self.COMMAND, self.APP_MODEL, stdout=out)

        results = json.loads(out.getvalue())

        self.assertEqual(len(results), 1)

        one = results[0]

        self.assertEqual(one.get('model'), self.APP_MODEL)

    def test_with_100_records(self):
        BATCH_SIZE = 100
        OneModelFactory.create_batch(size=BATCH_SIZE)

        out = StringIO()
        call_command(self.COMMAND, self.APP_MODEL, stdout=out)

        results = json.loads(out.getvalue())

        self.assertEqual(len(results), BATCH_SIZE)

    def test_100_records_with_filter(self):
        BATCH_SIZE = 100
        OneModelFactory.create_batch(size=BATCH_SIZE)

        FILTER_STRING = 'pk__gt=0,integer_value=1'
        FIELDS_STRING = 'pk,name,decimal_value'

        out = StringIO()
        call_command(
            self.COMMAND,
            self.APP_MODEL,
            fields=FIELDS_STRING,
            filter=FILTER_STRING,
            stdout=out
        )

        results = json.loads(out.getvalue())

        self.assertEqual(len(results), BATCH_SIZE)

    def test_get_all_fields_method(self):
        OneModelFactory()

        out = StringIO()
        call_command(
            self.COMMAND,
            self.APP_MODEL,
            fields='*',
            stdout=out
        )

        results = json.loads(out.getvalue())

        self.assertEqual(len(results), 1)
