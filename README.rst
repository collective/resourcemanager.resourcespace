=============================
resourcemanager.resourcespace
=============================

This add-on is meant to work with collective.resourcemanager.

See the collective.resourcemanager documentation for more details


Installation
------------

Install the collective.resourcemanager and resourcemanager.resourcespace packages by adding them to your buildout::

    [instance]
    ...
    eggs =
        ...
        collective.resourcemanager
        resourcemanager.resourcespace


Run ``bin/buildout``, and start the instance.

Within Plone:
* Install the add-ons in the Add-ons Control Panel
* Go to the ResourceSpace Keys Control Panel
* Enter your API keys and information.
  The field descriptions tell you how to find the necessary information in ResourceSpace

Use
---

Searching ResourceSpace within Plone will show you the available collections by default.
You can browse the collections, or enter a search term to find images.


Contribute
----------

- Issue Tracker: https://github.com/collective/resourcemanager.resourcespace/issues
- Source Code: https://github.com/collective/resourcemanager.resourcespace


License
-------

The project is licensed under the GPLv2.
