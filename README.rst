Django Dumpdata One
===================

Custom ``dumpdata`` command which allow to exporting from given fields of a model
and filter that data using standard Django lookups for filtering.

The exported data structure is compatible with Django ``dumpdata`` structure which
allows you to use standard ``loaddata`` command for import.

Installation
-----------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-dumpdata-one


Add ``dumpdata_one`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        "dumpdata_one",
    )

Usage
-----

Export data:

.. code-block:: bash

    ./manage.py dumpdata_one app_name.model_name --fields=field1,field2 > dump_file.json


Import data:

.. code-block:: bash

    ./manage.py loaddata dump_file.json


How to use filters? If you not familiar take a look at Django Field
lookups - https://docs.djangoproject.com/en/3.0/topics/db/queries/#field-lookups

.. code-block:: bash

    ./manage.py dumpdata_one app_name.model_name --fields=field1 --filter=name__icontains=django

    ./manage.py dumpdata_one app_name.model_name --fields=field1 --filter=name__icontains=django,pk__gt=300
