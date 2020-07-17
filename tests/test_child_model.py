from io import StringIO
import json

from django.core.management import call_command
from django.test import TestCase

from .factories import ChildModelFactory


class DumpChildModelTests(TestCase):
    def setUp(self):
        self.APP_MODEL = 'tests.childmodel'
        self.COMMAND = 'dumpdata_one'

    def test_with_100_records(self):
        BATCH_SIZE = 100
        ChildModelFactory.create_batch(size=BATCH_SIZE)

        FIELDS_STRING = "one,name"

        out = StringIO()
        call_command(
            self.COMMAND,
            self.APP_MODEL,
            fields=FIELDS_STRING,
            stdout=out
        )

        results = json.loads(out.getvalue())

        self.assertEqual(len(results), BATCH_SIZE)
