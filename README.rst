Transformation Services
=======================

This is an attempt to automate the installation of the
transformation services system.

Dependencies
------------

- Python 2.7
- RabbitMQ
- Postgres
- Python 2.4 (if using roadrunners legacy)

And others depending on what runners you use.

Getting Started
---------------

You'll need to setup RabbitMQ and Postgres on your own. Postgres will
need to be setup with a ``pybit`` database and the ``pybit:pybit``
user:pass. And you'll need to initialize the database.

.. note:: You will likely want to install ``psycopg2`` at the system level
   or in a virtual environment before running the following command.

To initialize the system use the provided ``init.sh`` script. This script
initializes git submodules, builds the system (via buildout), and initializes
the database.

::

    $ ./init.sh

.. note:: ``init.sh`` uses the system python by default. If you are building
   against a virtual environment, you can set the ``PYTHON`` environment
   variable to the executable in the virtual environment. For example, if
   our virtual environment were one layer down::

       $ PYTHON=../bin/python ./init.sh

To run acmeio (the transformation services web services API)::

    $ bin/pserve etc/acmeio.ini

To run tumbleweed (the status message consumer process)::

    $ bin/tumbleweed etc/tumbleweed.ini

An instance of coyote has been configured with the legacy runners as
part of this build. You can run them using::

    $ bin/coyote etc/coyote-legacy.ini

If you make changes to the buildout configuration in ``buildout.cfg``, you
will need to rebuild the project. You can do this by running the
following commands::

    $ bin/buildout
