import json
from django.apps import apps
from django.core.files import File
from django.core.management.base import BaseCommand
from django.core.serializers.json import DjangoJSONEncoder


class Command(BaseCommand):

    def add_arguments(self, parser):

        parser.add_argument('app_model', type=str)
        parser.add_argument('--order', type=str, default='pk')
        parser.add_argument('--fields', type=str)
        parser.add_argument('--filter', type=str)
        parser.add_argument('--full_url', type=str)
        parser.add_argument('--limit', type=int)

    def handle(self, *args, **options):

        app_model = options['app_model']
        fields = options['fields']
        order = options['order']
        filters = self.get_filter_dict(options['filter'])
        full_urls = options['full_url']
        limit = options['limit']

        Model = apps.get_model(app_model)

        if fields == '*':
            fields = self.get_all_fields(Model)
        else:
            fields = fields.split(',') if fields is not None else []

        if 'pk' not in fields:
            fields.append('pk')

        full_urls = full_urls.split(',') if full_urls is not None else []

        records = Model.objects.all()
        if filters:
            records = records.filter(**filters)

        order_by = self.get_order_list(order)

        records = records.order_by(*order_by)
        if limit:
            records = records[:limit]

        dump_structure = self.get_dump_structure(
            app_model, records, fields, full_urls
        )
        result = json.dumps(dump_structure, cls=DjangoJSONEncoder)
        return result

    def get_dump_structure(self, app_model, records, fields, full_urls):
        results = []
        for item in records:
            values = {}
            for field in fields:
                if field != "pk":
                    model_field = getattr(item, field)
                    if isinstance(model_field, File):
                        values[field] = model_field.name
                    else:
                        values[field] = model_field

                if field in full_urls:
                    values[f"{field}__full_url"] = getattr(item, field).url

            item_structure = {
                "model": app_model,
                "pk": getattr(item, "pk"),
                "fields": values
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

    def get_order_list(self, order):
        return order.split(",")

    def get_all_fields(self, Model):
        return [field.name for field in Model._meta.fields]
