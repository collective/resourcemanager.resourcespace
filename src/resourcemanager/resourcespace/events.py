import logging
import transaction
from plone import api

from resourcemanager.resourcespace.search import ResourceSpaceSearch

logger = logging.getLogger("ResourceSpace")


def upload_image(obj, event):
    """When a Plone image is modified, sync changes to RS
       Use the image's url to upload
    """
    registry = api.portal.get_tool('portal_registry')
    reg_prefix = 'resourcemanager.resourcespace.settings.IResourceSpaceKeys'
    upload_to_rs = registry['{0}.upload_to_rs'.format(reg_prefix)]
    if not upload_to_rs:
        return
    rs_collection = registry['{0}.rs_collection'.format(reg_prefix)]

    rs_search = ResourceSpaceSearch(obj, obj.REQUEST)
    resource_id = obj.external_img_id.replace('rs-', '')
    if resource_id:
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
