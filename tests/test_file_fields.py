from io import StringIO
import json

from django.core.management import call_command
from django.test import TestCase

from .factories import ModelWithFileFactory


class DumpDataWithFilesTests(TestCase):
    def setUp(self):
        self.APP_MODEL = 'tests.onemodel'
        self.COMMAND = 'dumpdata_one'

    def test_one_file(self):
        record = ModelWithFileFactory()

        out = StringIO()
        call_command(
            self.COMMAND,
            self.APP_MODEL,
            fields="document",
            stdout=out
        )

        results = json.loads(out.getvalue())

        self.assertEqual(len(results), 1)

        result_record = results[0]

        self.assertEqual(
            record.document.name,
            result_record.get("fields").get("document")
        )

    def test_one_file_with_full_url(self):
        record = ModelWithFileFactory()

        out = StringIO()
        call_command(
            self.COMMAND,
            self.APP_MODEL,
            fields="document",
            full_url="document",
            stdout=out
        )

        results = json.loads(out.getvalue())

        self.assertEqual(len(results), 1)

        result_record = results[0]

        self.assertEqual(
            record.document.name,
            result_record.get("fields").get("document")
        )

        self.assertEqual(
            result_record.get("fields").get("document__full_url"),
            record.document.url
        )
