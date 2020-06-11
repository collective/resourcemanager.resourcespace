import logging
import transaction
from plone import api

from resourcemanager.resourcespace.search import (
    ResourceSpaceSearch,
    ResourceSpaceCopy
)

logger = logging.getLogger("ResourceSpace")


def fill_image_metadata(obj, resource_id):
    rs_copy = ResourceSpaceCopy(obj, obj.REQUEST)
    img_data = rs_copy.get_image_metadata(resource_id.replace('rs-', ''))
    if not obj.title:
        obj.title = img_data['title']
    if not obj.description:
        obj.description = img_data['description']
    rs_data = img_data['resource_metadata']
    data_str = '\n'.join(['{0}: {1}'.format(x, rs_data[x]) for x in rs_data])
    obj.resource_metadata = data_str
    obj.reindexObject()


def upload_image(obj, event):
    """When an image is uploaded into Plone,
       upload it to RS
    """
    resource_id = obj.external_img_id
    if resource_id:
        # if is an image from ResourceSpace, get the metadata
        if 'rs-' in resource_id:
            fill_image_metadata(obj, resource_id)
        return
    registry = api.portal.get_tool('portal_registry')
    reg_prefix = 'resourcemanager.resourcespace.settings.IResourceSpaceKeys'
    upload_to_rs = registry['{0}.upload_to_rs'.format(reg_prefix)]
    
    #check each upload instance before uploading to RS
    upload_this_to_rs = getattr(obj, 'upload_this_to_rs', None)

    if not upload_to_rs:
        return

    if upload_this_to_rs is not None:
        if not upload_this_to_rs:
            return

    rs_collection = registry['{0}.rs_collection'.format(reg_prefix)]

    rs_search = ResourceSpaceSearch(obj, obj.REQUEST)
    if resource_id:
        resource_id = resource_id.replace('rs-', '')
        logger.info("Resource ID #{} will be updated".format(resource_id))
    else:
        # param7 will be for metadata
        query = '&function=create_resource&param1=1&param2=0'
        resource_id = rs_search.query_resourcespace(query)
        logger.info("Resource ID #{} created".format(resource_id))
    portal_url = api.portal.get().absolute_url()
    item_path = '/'.join(obj.getPhysicalPath()[2:])
    logger.info("Image at URL {} will be uploaded".format(
        portal_url + '/' + item_path))
    transaction.commit()

    response = rs_search.query_resourcespace(
        '&function=upload_file_by_url&param1={0}&param5={1}'.format(
            resource_id, portal_url + '/' + item_path
        ))
    if response and int(response) != resource_id:
        logger.info("Response: {}".format(response))
    if rs_collection:
        rs_search.query_resourcespace(
            '&function=add_resource_to_collection&param1={0}&param2={1}'.format(
                resource_id, rs_collection
            ))
    obj.external_img_id = 'rs-{}'.format(resource_id)
    obj.reindexObject()
