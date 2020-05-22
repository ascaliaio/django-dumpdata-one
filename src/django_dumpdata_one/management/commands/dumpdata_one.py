import json
from django.apps import apps
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder


class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument('app_model', type=str)
        parser.add_argument('--order', type=str, default='pk')
        parser.add_argument('--fields', type=str)
        parser.add_argument('--filter', type=str)

    def handle(self, *args, **options):

        app_model = options['app_model']
        fields = options['fields']
        order = options['order']
        filters = self.get_filter_dict(options['filter'])

        Model = apps.get_model(app_model)

        fields = fields.split(',') if fields is not None else []

        if 'pk' not in fields:
            fields.append('pk')

        records = Model.objects.all()
        if filters:
            records = records.filter(**filters)

        records = records.order_by(order).values(*fields)

        dump_structure = self.get_dump_structure(app_model, records)
        result = json.dumps(dump_structure, cls=DjangoJSONEncoder)
        return result

    def get_dump_structure(self, app_model, records):
        results = []
        for item in records:
            fields = {}
            for key, value in item.items():
                if key != "pk":
                    fields[key] = value

            item_structure = {
                "model": app_model,
                "pk": item.get("pk"),
                "fields": fields
            }
            results.append(item_structure)

        return results

    def get_filter_dict(self, filter_string):
        filters = {}
        if filter_string:
            pairs = filter_string.split(',')
            for pair in pairs:
                key, value = pair.split('=')
                filters[key] = value

        return filters
