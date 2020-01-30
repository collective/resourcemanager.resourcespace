from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from zope import schema
from zope.interface import Interface


class IResourceSpaceKeys(Interface):

    rs_url = schema.TextLine(
        title=u"ResourceSpace API URL",
        description=u"The URL to your ResourseSpace with /api on the end",
    )
    rs_user = schema.TextLine(
        title=u"ResourceSpace User",
        description=u"User to access the API. See the Manage Users screen \
            in ResourceSpace",
    )
    rs_private_key = schema.TextLine(
        title=u"ResourceSpace Private Key",
        description=u"Key to access the API. In ResourceSpace's Manage \
            Users screen, you can find a user's API key when you edit them.",
    )

    upload_to_rs = schema.Bool(
        title=u"Upload all images to ResourceSpace",
        description=u"If selected, any images added into Plone will be \
            uploaded to ResourceSpace"
    )
    rs_collection = schema.Int(
        title=u"Collection ID for Uploads",
        description=u"Specify a collection ID for uploaded images to be \
            added to"
    )


class ResourceSpaceKeysEditForm(RegistryEditForm):
    """
    Define form logic
    """
    schema = IResourceSpaceKeys
    label = u"ResourceSpace Keys"


class ResourceSpaceKeysView(ControlPanelFormWrapper):
    form = ResourceSpaceKeysEditForm
