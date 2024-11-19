.. _user-config:

User Config
===========

*New in mlpstamps 0.7*

If you use mlpstamps a lot, you'll find it useful to have a user config file.
By default mlpstamps tries to retrieve settings from a `.mlpstampsrc` file in your home directory.

*New in mlpstamps 1.3*

You can also specify a config file on the command line via ``--config-file``.

.. code-block:: bash

    mlpstamps --config-file /home/audreyr/my-custom-config.yaml mlpstamps-pypackage

Or you can set the ``mlpstamps_CONFIG`` environment variable:

.. code-block:: bash

    export mlpstamps_CONFIG=/home/audreyr/my-custom-config.yaml

If you wish to stick to the built-in config and not load any user config file at all, use the CLI option ``--default-config`` instead.
Preventing mlpstamps from loading user settings is crucial for writing integration tests in an isolated environment.

Example user config:

.. code-block:: yaml

    default_context:
        full_name: "Audrey Roy"
        email: "audreyr@example.com"
        github_username: "audreyr"
    mlpstampss_dir: "/home/audreyr/my-custom-mlpstampss-dir/"
    replay_dir: "/home/audreyr/my-custom-replay-dir/"
    abbreviations:
        pp: https://github.com/audreyfeldroy/mlpstamps-pypackage.git
        gh: https://github.com/{0}.git
        bb: https://bitbucket.org/{0}

Possible settings are:

``default_context``:
    A list of key/value pairs that you want injected as context whenever you generate a project with mlpstamps.
    These values are treated like the defaults in ``mlpstamps.json``, upon generation of any project.
``mlpstampss_dir``
    Directory where your mlpstampss are cloned to when you use mlpstamps with a repo argument.
``replay_dir``
    Directory where mlpstamps dumps context data to, which you can fetch later on when using the
    :ref:`replay feature <replay-feature>`.
``abbreviations``
    A list of abbreviations for mlpstampss.
    Abbreviations can be simple aliases for a repo name, or can be used as a prefix, in the form ``abbr:suffix``.
    Any suffix will be inserted into the expansion in place of the text ``{0}``, using standard Python string formatting.
    With the above aliases, you could use the ``mlpstamps-pypackage`` template simply by saying ``mlpstamps pp``, or ``mlpstamps gh:audreyr/mlpstamps-pypackage``.
    The ``gh`` (GitHub), ``bb`` (Bitbucket), and ``gl`` (Gitlab) abbreviations shown above are actually **built in**, and can be used without defining them yourself.

Read also: :ref:`injecting-extra-content`
