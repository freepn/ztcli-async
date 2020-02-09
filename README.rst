=============
 ztcli-async
=============

ztcli-async is a thin async Python client wrapper for the zerotier-cli
node API (mainly based on `zerotier-client`_ and the `ZeroTier API doc`_).


.. image:: https://img.shields.io/github/license/freepn/ztcli-async
   :alt: GitHub
   :target: https://github.com/freepn/ztcli-async/blob/master/LICENSE

.. image:: https://img.shields.io/github/v/tag/freepn/ztcli-async?color=green&include_prereleases&label=latest%20release
   :target: https://github.com/freepn/ztcli-async/releases
   :alt: GitHub tag (latest SemVer, including pre-release)

.. image:: https://travis-ci.org/freepn/ztcli-async.svg?branch=master
   :target: https://travis-ci.org/freepn/ztcli-async

.. image:: https://img.shields.io/github/issues/freepn/ztcli-async
    :target: https://github.com/freepn/ztcli-async/issues?q=is:issue+is:open
    :alt: Open Issues

.. image:: https://img.shields.io/github/issues-pr/freepn/ztcli-async
    :target: https://github.com/freepn/ztcli-async/issues?q=is:open+is:pr
    :alt: Pull Requests

.. image:: https://img.shields.io/codeclimate/maintainability/freepn/ztcli-async
    :target: https://codeclimate.com/github/freepn/ztcli-async
    :alt: Code Climate maintainability


.. _zerotier-client: https://github.com/fabaff/zerotier-client
.. _ZeroTier API doc: https://zerotier.com/manual/


Getting Started
===============

This is a Python thin client interface to the zerotier JSON API, only some
of which is exposed by the ``zerotier-cli`` command-line interface.  New
packages are available for `Debian and Ubuntu`_, and the latest can be
installed on Gentoo using the ebuilds in `this portage overlay`_.


.. _Debian and Ubuntu: https://launchpad.net/~nerdboy/+archive/ubuntu/embedded
.. _this portage overlay: https://github.com/freepn/python-overlay/dev-libs/ztcli-async/


Prerequisites
-------------

A supported linux distribution, mainly something that uses either `.ebuilds`
(eg, Gentoo or funtoo) or `.deb` packages, starting with at least Ubuntu
xenial or Debian stretch (see the above PPA package repo on Launchpad).

For the latter, make sure you have the ``add-apt-repository`` command
installed and then add the PPA:

::

  $ sudo apt-get install software-properties-common ubuntu-keyring ubuntu-archive-keyring
  $ sudo add-apt-repository -y -s ppa:nerdboy/embedded


.. note:: Since the only package series currently published is for xenial
          the second command above will need to be manually corrected
          afterwards if installing on Debian.


To install on Debian you *can* use the above method, but you will need
to edit the file under ``sources.d`` and set the distro to ``xenial``
and then run the update command:

::

  $ sudo apt-get update

If you get a key error you will also need to manually import the PPA
signing key like so:

::

  $ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys <PPA_KEY>

where <PPA_KEY> is the key shown in the launchpad PPA page under "Adding
this PPA to your system", eg, ``41113ed57774ed19`` for `Embedded device ppa`_.


.. _Embedded device ppa: https://launchpad.net/~nerdboy/+archive/ubuntu/embedded


Dev Install
-----------

As long as you have git and at least Python 3.5, then the "easy" dev
install is to clone this repository and install the latest zerotier package
(there are packages in the PPA and Gentoo overlay).  Check the version of
zerotier in the main portage tree; you will need at least version ``1.4.6:0``.

Do the usual install dance, either::

  # emerge zerotier

or::

  $ sudo apt-get install zerotier-one


After cloning this repository, you can try running the example scripts
from the source tree; if you have already installed this package, the
examples should run from any directory, otherwise you'll need to copy
the file you want to run to the top-level source tree first.

Without installing ztcli-async, first install the two package dependencies
listed below, then install zerotier and make sure the service has started.
You can check the zerotier client state with::

  $ sudo zerotier-cli info

which should respond with::

  200 info <your ID> 1.4.6 ONLINE

If the above is working, you can try one of the examples:

::

  $ git clone https://github.com/freepn/ztcli-async
  $ cd ztcli-async
  $ cp examples/pprint_data.py .
  $ sudo python3 pprint_data.py


.. note:: By default you will not have correct permissions to access the
          local zerotier node directly, due to the permissions on zerotier
          identity files.  You can either prefix the commands with ``sudo``,
          or add a usr ACL (for your local user) to the ``authtoken.secret``
          file.


Standards and Coding Style
--------------------------

Currently pep8 and flake8 are the only tests besides some CI code analysis
checks for complexity and security issues (we try to keep the "cognitive
complexity" low when possible).


User Install / Deployment
=========================

Use the latest ztcli-async package for your Linux distro and hardware
architecture; all arch-specific packages should support at least the
following:

* armhf/arm
* aarch64/arm64
* x86_64/amd64
* i686/x86


Software Stack and Tool Dependencies
====================================

* `python`_ - at least version 3.5
* `async_timeout`_ - timeout context manager for asyncio
* `aiohttp`_ - http client/server for asyncio
* `ZeroTier`_ - network virtualization engine

.. _Python: https://docs.python.org/3.5/index.html
.. _async_timeout: https://github.com/aio-libs/async-timeout
.. _aiohttp: https://pypi.org/project/aiohttp/
.. _ZeroTier: https://www.zerotier.com/



Versioning
==========

We use `SemVer`_ for versioning. For the versions available, see the
`releases on this repository`_.

.. _SemVer: http://semver.org/
.. _releases on this repository: https://github.com/freepn/ztcli-async/releases


Contributing
============

Please read `CONTRIBUTING.rst`_ for details on our code of conduct, and the
process for submitting pull requests to us.

.. _CONTRIBUTING.rst: https://github.com/freepn/ztcli-async/CONTRIBUTING.rst


Authors
=======

* **Stephen Arnold** - *Current implementation, cleanup, and packaging* - `freepn`_
* **Fabian Affolter** - *Original implementation* - `fabaff`_

.. _freepn: https://github.com/freepn/
.. _fabaff: https://github.com/fabaff/


License
=======

This project is licensed under the MIT license - see the `LICENSE file`_ for
details.

.. _LICENSE file: https://github.com/freepn/ztcli-async/blob/master/LICENSE


Acknowledgments
===============

* Thanks to Fabian for the clean original client implementation and inspiration
* Thanks to the ZeroTier project for providing the network virtualization engine
