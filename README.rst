Transformation Services
=======================

This is an attempt to automate the installation of the
transformation services system.

Dependencies
------------

``*`` indicates that it is not included in this build.

- Python 2.7 *
- RabbitMQ *
- Postgres *
- Python 2.4 * (if using roadrunners lagacy)

And others depending on what runners you use.

Getting Started
---------------

You'll need to setup RabbitMQ and Postgres on your own. Postgres will
need to be setup with a ``pybit`` database and the ``pybit:pybit``
user:pass. And you'll need to initialize the database. This can be
done using the ``init-db.sh`` script provided with this project::

    $ ./init-db.sh

To build the main components of the system, run the following commands::

    $ python bootstrap.py -c buildout.cfg
    $ bin/buildout

To run acmeio (the transformation services web services API)::

    $ bin/pserve etc/acmeio.ini

To run tumbleweed (the status message consumer process)::

    $ bin/tumbleweed etc/tumbleweed.ini

An instance of coyote has been configured with the legacy runners as
part of this build. You can run them using::

    $ bin/coyote etc/coyote-legacy.ini
