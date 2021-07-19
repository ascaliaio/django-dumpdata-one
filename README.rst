.. image:: https://travis-ci.org/ascaliaio/django-dumpdata-one.svg
    :target: https://travis-ci.org/github/ascaliaio/django-dumpdata-one/

.. image:: https://codecov.io/gh/ascaliaio/django-dumpdata-one/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/ascaliaio/django-dumpdata-one

Django Dumpdata One
===================

Custom ``dumpdata`` command which allows to exporting from given fields of a model
and filter that data using standard Django lookups for filtering.

The exported data structure is compatible with Django ``dumpdata`` structure which
allows you to use standard ``loaddata`` command for import.

Installation
------------

To get the latest stable release from PyPi

.. code-block:: bash

    pip install django-dumpdata-one


Add ``dumpdata_one`` to your ``INSTALLED_APPS``

.. code-block:: python

    INSTALLED_APPS = (
        ...,
        "django_dumpdata_one",
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

Set order by:

.. code-block:: bash

    ./manage.py dumpdata_one app_name.model_name --fields=field1,field2 --order=field2,field2

Export all fields:

.. code-block:: bash

    ./manage.py dumpdate_one app_name.model_name --fields=*


Limit number of exported records:

.. code-block:: bash

    ./manage.py dumpdata_one app_name.model_name --fields=* --limit=10


Export full file URL:

.. code-block:: bash

    ./manage.py dumpdata_one app_name.model_name --fields=image --full_url=image


Export from another database than 'default':

.. code-block:: bash

    ./manage.py dumpdata_one app_name.model_name --database=other_database