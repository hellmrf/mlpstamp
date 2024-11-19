.. _tutorial2:

==================================
Create a mlpstamps From Scratch
==================================

In this tutorial, we are creating `mlpstamps-website-simple`, a mlpstamps for generating simple, bare-bones websites.

Step 1: Name Your mlpstamps
------------------------------

Create the directory for your mlpstamps and cd into it:

.. code-block:: bash

    $ mkdir mlpstamps-website-simple
    $ cd mlpstamps-website-simple/

Step 2: Create mlpstamps.json
----------------------------------

`mlpstamps.json` is a JSON file that contains fields which can be referenced in the mlpstamps template. For each, default value is defined and user will be prompted for input during mlpstamps execution. Only mandatory field is `project_slug` and it should comply with package naming conventions defined in `PEP8 Naming Conventions <https://www.python.org/dev/peps/pep-0008/#package-and-module-names>`_ .

.. code-block:: json

    {
      "project_name": "mlpstamps Website Simple",
      "project_slug": "{{ mlpstamps.project_name.lower().replace(' ', '_') }}",
      "author": "Anonymous"
    }


Step 3: Create project_slug Directory
---------------------------------------

Create a directory called `{{ mlpstamps.project_slug }}`.

This value will be replaced with the repo name of projects that you generate from this mlpstamps.

Step 4: Create index.html
--------------------------

Inside of `{{ mlpstamps.project_slug }}`, create `index.html` with following content:

.. code-block:: html

    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>{{ mlpstamps.project_name }}</title>
        </head>

        <body>
            <h1>{{ mlpstamps.project_name }}</h1>
            <p>by {{ mlpstamps.author }}</p>
        </body>
    </html>

Step 5: Pack mlpstamps into ZIP
----------------------------------
There are many ways to run mlpstamps templates, and they are described in details in `Usage chapter <https://mlpstamps.readthedocs.io/en/latest/usage.html#grab-a-mlpstamps-template>`_. In this tutorial we are going to ZIP mlpstamps and then run it for testing.

By running following command `mlpstamps.zip` will get generated which can be used to run mlpstamps. Script will generate `mlpstamps.zip` ZIP file and echo full path to the file.

.. code-block:: bash

   $ (SOURCE_DIR=$(basename $PWD) ZIP=mlpstamps.zip && # Set variables
   pushd .. && # Set parent directory as working directory
   zip -r $ZIP $SOURCE_DIR --exclude $SOURCE_DIR/$ZIP --quiet && # ZIP mlpstamps
   mv $ZIP $SOURCE_DIR/$ZIP && # Move ZIP to original directory
   popd && # Restore original work directory
   echo  "mlpstamps full path: $PWD/$ZIP")

Step 6: Run mlpstamps
------------------------
Set your work directory to whatever directory you would like to run mlpstamps at. Use mlpstamps full path and run the following command:

.. code-block:: bash

   $ mlpstamps <replace with mlpstamps full path>

You can expect similar output:

.. code-block:: bash

   $ mlpstamps /Users/admin/mlpstamps-website-simple/mlpstamps.zip
   project_name [mlpstamps Website Simple]: Test web
   project_slug [test_web]:
   author [Anonymous]: mlpstamps Developer

Resulting directory should be inside your work directory with a name that matches `project_slug` you defined. Inside that directory there should be `index.html` with generated source:

.. code-block:: html

    <!doctype html>
    <html>
        <head>
            <meta charset="utf-8">
            <title>Test web</title>
        </head>

        <body>
            <h1>Test web</h1>
            <p>by mlpstamps Developer</p>
        </body>
    </html>
