.. _directories:

Organizing mlpstampss in directories
---------------------------------------

*New in mlpstamps 1.7*

mlpstamps introduces the ability to organize several templates in one repository or zip file, separating them by directories.
This allows using symlinks for general files.
Here's an example repository demonstrating this feature::

    https://github.com/user/repo-name.git
        ├── directory1-name/
        |   ├── {{mlpstamps.project_slug}}/
        |   └── mlpstamps.json
        └── directory2-name/
            ├── {{mlpstamps.project_slug}}/
            └── mlpstamps.json

To activate one of templates within a subdirectory, use the ``--directory`` option:

.. code-block:: bash

    mlpstamps https://github.com/user/repo-name.git --directory="directory1-name"
