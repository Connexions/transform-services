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
- PyBit
- rbit
- rbit-ext

And others depending on depending on what runners you use in ``rbit-ext``.

Getting started
---------------

To initialize the main components of the system, run the following commands::

    $ ./bootstrap.sh
