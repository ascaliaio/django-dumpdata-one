from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OneModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('text', models.TextField(default='')),
                ('is_active', models.BooleanField(default=True)),
                ('time_is', models.DateTimeField(auto_now_add=True)),
                ('decimal_value', models.DecimalField(decimal_places=2, max_digits=5)),
                ('integer_value', models.IntegerField(default=1)),
                ('document', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='ChildModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('one', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tests.OneModel')),
            ],
        ),
    ]
