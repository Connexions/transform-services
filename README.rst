Transformation Services
=======================

This is a *poor* attempt to automate the installation of the
transformation services system. It is a poor attempt because the setup
is inherently complicated due to the dependent components, wrapping of
environments and external or system dependencies needed to run various
pieces of the system. That said, this should be used as a baseline
rather than a complete install. 

Dependencies
------------

``*`` indicates that it is not included in this build.

- RabbitMQ *
- Postgres *
- PyBit
- rbit
- rbit-ext

And others depending on depending on what runners you use in ``rbit-ext``.

Getting started
---------------

You'll need to setup RabbitMQ and Postgres on your own. Postgres will
need to be setup with a ``pybit`` database and the ``pybit:pybit``
user:pass.

To initialize the main components of the system, run the following commands::

    $ ./bootstrap.sh

Unfortunatly, I don't recall enough bash and sed to generate the
configs. So you'll need to copy the ``*.in`` files and replace the
``@ENV@`` variables yourself.

From this point forward, ``$PYTHON`` will refer to the the python at
``bin/python`` in the created environment. And ``$ENV`` will refer to
the environment itself.

To run PyBit (it is very important to call the script from within it's
project location)::

    $ cd $ENV/pybit
    $ $PYTHON pybit_web.py --config $ENV/pybit.conf -v

To run cnx-pybit::

    $ cd $ENV
    $ $ENVbin/cnx-pybit --config $ENV/pybit.conf -v

Before you run rbit, you'll likely want to configure a runner or
two. See the rbit documentation regarding this configuration and you
can also use the ``src/rbit/development.ini`` as a guide.

To run rbit::

    $ $ENV/bin/rbit $VENV/rbit.ini
