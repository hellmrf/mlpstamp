.. _calling-from-python:

Calling mlpstamps Functions From Python
------------------------------------------

You can use mlpstamps from Python:

.. code-block:: python

    from mlpstamps.main import mlpstamps

    # Create project from the mlpstamps-pypackage/ template
    mlpstamps('mlpstamps-pypackage/')

    # Create project from the mlpstamps-pypackage.git repo template
    mlpstamps('https://github.com/audreyfeldroy/mlpstamps-pypackage.git')

This is useful if, for example, you're writing a web framework and need to provide developers with a tool similar to `django-admin.py startproject` or `npm init`.

See the :ref:`API Reference <apiref>` for more details.
