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

Component Overview
------------------

This is one implementation of the transformation services system. The
system is made up of several parts that function together to
asynchronously produce the transformed content. The following is a
list of packages that make up the system.

- acmeio -
  A web application that is an implementation of the transformation
  services API specification. This service is used to create an
  monitor transform requests (or jobs or build requests). This
  application is the producer of messages in the message queue
  (RabbitMQ) and maintains the state of these messages (in
  PostgreSQL).
- coyote -
  A process for consuming messages and managing the message's state.
  It is the communication medium between the message queue (RabbitMQ)
  and the transformation logic.
- roadrunners -
  A Python library of various transformation functions (or
  runners). The runners in this package receive their processing data
  via a coyote process.
- tumbleweed -
  A background process for consuming status messages from the message
  queue (RabbitMQ) to persist them in the acmeio database (PostgreSQL).

License
-------

This software is subject to the provisions of the GNU Affero General
Public License Version 3.0 (AGPL). See license.txt for details.
Copyright (c) 2013 Rice University
