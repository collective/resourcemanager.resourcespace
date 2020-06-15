# -*- coding: utf-8 -*-

from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider
from z3c.form.browser.radio import RadioFieldWidget
from plone.autoform import directives

@provider(IFormFieldProvider)
class IUploadToRSBehavior(model.Schema):
    directives.widget('upload_this_to_rs', RadioFieldWidget)
    upload_this_to_rs = schema.Bool(
        title="Do you want to upload this image to Resource Space?",
        required=True
    )
