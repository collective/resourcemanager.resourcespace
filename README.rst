=============================
resourcemanager.resourcespace
=============================

This add-on is meant to work with collective.resourcemanager.

See the collective.resourcemanager documentation for more details: https://github.com/collective/collective.resourcemanager


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
* 'Upload all images to ResourceSpace'. With this option selected, any images uploaded into Plone
  will also be uploaded to ResourceSpace.
* 'Collection ID for Uploads': If you are uploading images to ResourceSpace, you can specify
  a collection for all the images to be added to (not required).

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
