=============================
Plugs Newsletter
=============================

.. image:: https://badge.fury.io/py/plugs-newsletter.png
    :target: https://badge.fury.io/py/plugs-newsletter

.. image:: https://travis-ci.org/ricardolobo/plugs-newsletter.png?branch=master
    :target: https://travis-ci.org/ricardolobo/plugs-newsletter

n

Documentation
-------------

The full documentation is at https://plugs-newsletter.readthedocs.io.

Quickstart
----------

Install Plugs Newsletter::

    pip install plugs-newsletter

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'plugs_newsletter.apps.PlugsNewsletterConfig',
        ...
    )

Add Plugs Newsletter's URL patterns:

.. code-block:: python

    from plugs_newsletter import urls as plugs_newsletter_urls


    urlpatterns = [
        ...
        url(r'^', include(plugs_newsletter_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
