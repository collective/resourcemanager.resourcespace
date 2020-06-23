# -*- coding: utf-8 -*-
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IUpload_ImageToRSBehavior(model.Schema):
    # The behaviors is for ++add++Image
    upload_this_to_rs = schema.Bool(
        title="Uncheck to disable upload this image to Resource Space",
        required=True,
        default = True
    )
