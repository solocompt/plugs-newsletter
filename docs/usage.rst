=====
Usage
=====

To use Plugs Newsletter in a project, add it to your `INSTALLED_APPS`:

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
