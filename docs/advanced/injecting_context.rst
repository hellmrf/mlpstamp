.. _injecting-extra-content:

Injecting Extra Context
-----------------------

You can specify an ``extra_context`` dictionary that will override values from ``mlpstamps.json`` or ``.mlpstampsrc``:

.. code-block:: python

    mlpstamps(
        'mlpstamps-pypackage/',
        extra_context={'project_name': 'TheGreatest'},
    )

This works as command-line parameters as well:

.. code-block:: bash

    mlpstamps --no-input mlpstamps-pypackage/ project_name=TheGreatest

You will also need to add these keys to the ``mlpstamps.json`` or ``.mlpstampsrc``.


Example: Injecting a Timestamp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have ``mlpstamps.json`` that has the following keys:

.. code-block:: JSON

    {
        "timestamp": "{{ mlpstamps.timestamp }}"
    }


This Python script will dynamically inject a timestamp value as the project is
generated:

.. code-block:: python

    from mlpstamps.main import mlpstamps

    from datetime import datetime

    mlpstamps(
        'mlpstamps-django',
        extra_context={'timestamp': datetime.utcnow().isoformat()}
    )

How this works:

1. The script uses ``datetime`` to get the current UTC time in ISO format.
2. To generate the project, ``mlpstamps()`` is called, passing the timestamp
   in as context via the ``extra_context``` dict.
