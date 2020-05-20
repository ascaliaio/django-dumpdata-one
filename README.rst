Django Dumpdata One
===================

Custom dumpdata command which allow to export data from given fields of a model
and filter that data using standard Django lookups for filtering.

Exported data structure is compatible with Django dumpdata structure which
allows you to use standard loaddata command for import.

Instalation
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


.. code-block:: bash

    ./manage.py dumpdata_one app_name.model_name --fields=field1,field2 > dump_file.json


.. code-block:: bash

    ./manage.py loaddata dump_file.json

