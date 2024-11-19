.. _nested-config-files:

Nested configuration files
--------------------------

*New in mlpstamps 2.5.0*

If you wish to create a hierarchy of templates and use mlpstamps to choose among them,
you need just to specify the key ``templates`` in the main configuration file to reach
the other ones.

Let's imagine to have the following structure::

    main-directory/
        ├── project-1
        │   ├── mlpstamps.json
        │   ├── {{mlpstamps.project_slug}}
        |	│   ├── ...
        ├── package
        │   ├── mlpstamps.json
        │   ├── {{mlpstamps.project_slug}}
        |	│   ├── ...
        └── mlpstamps.json

It is possible to specify in the main ``mlpstamps.json`` how to reach the other
config files as follows:

.. code-block:: JSON

    {
        "templates": {
            "project-1": {
                "path": "./project-1",
                "title": "Project 1",
                "description": "A mlpstamps template for a project"
            },
            "package": {
                "path": "./package",
                "title": "Package",
                "description": "A mlpstamps template for a package"
            }
        }
    }

Then, when ``mlpstamps`` is launched in the main directory it will ask to choose
among the possible templates:

.. code-block::

    Select template:
    1 - Project 1 (A mlpstamps template for a project)
    2 - Package (A mlpstamps template for a package)
    Choose from 1, 2 [1]:

Once a template is chosen, for example ``1``, it will continue to ask the info required by
``mlpstamps.json`` in the ``project-1`` folder, such as ``project-slug``


Old Format
++++++++++

*New in mlpstamps 2.2.0*

In the main ``mlpstamps.json`` add a `template` key with the following format:

.. code-block:: JSON

    {
        "template": [
            "Project 1 (./project-1)",
            "Project 2 (./project-2)"
        ]
    }

Then, when ``mlpstamps`` is launched in the main directory it will ask to choose
among the possible templates:

.. code-block::

    Select template:
    1 - Project 1 (./project-1)
    2 - Project 2 (./project-2)
    Choose from 1, 2 [1]:

Once a template is chosen, for example ``1``, it will continue to ask the info required by
``mlpstamps.json`` in the ``project-1`` folder, such as ``project-slug``
