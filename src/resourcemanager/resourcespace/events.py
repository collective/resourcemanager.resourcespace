import os
from datetime import datetime

from resourcemanager.resourcespace.search import ResourceSpaceSearch


def upload_image(obj, event):
    """When a Plone image is modified, sync changes to RS
       Use the image's url to upload
    """
    # if image has a resource id, update that resource (if it still exists)
    # otherwise, add the resource
    rs_search = ResourceSpaceSearch(obj, obj.REQUEST)
    # param7 will be for metadata
    query = '&function=create_resource&param1=1&param2=0'
    resource_id = rs_search.query_resourcespace(query)

    rs_search.query_resourcespace(
        '&function=upload_file_by_url&param1={0}&param5={1}'.format(
            resource_id, 'http://0c1d467e.ngrok.io' + '/'.join(obj.getPhysicalPath())
        ))
    # put into test collection for now
    rs_search.query_resourcespace(
        '&function=add_resource_to_collection&param1={}&param2=1'.format(
            resource_id
        ))


def upload_image_file(obj, event):
    """When a Plone image is modified, sync changes to RS
       This one tries to upload the image as a file
    """
    # if image has a resource id, update that resource (if it still exists)
    # otherwise, add the resource
    rs_search = ResourceSpaceSearch(obj, obj.REQUEST)
    # param7 will be for metadata
    query = '&function=create_resource&param1=1&param2=0'
    resource_id = rs_search.query_resourcespace(query)

    # create a temporary file on the filesystem for uploading
    exp_path = 'rsimage-{0}.jpg'.format(datetime.now().microsecond)  # need to get actual extension
    if os.path.exists(exp_path):
        os.system('rm -rf {}'.format(exp_path))
    f = open(exp_path, 'wb')
    f.write(obj.image.data)
    f.close()

    rs_search.query_resourcespace(
        '&function=upload_file&param1={0}&param3=true&param5={1}'.format(
            resource_id, os.path.realpath(exp_path)
        ))
    os.system('rm -rf {}'.format(exp_path))
    # put into test collection for now #3151
    rs_search.query_resourcespace(
        '&function=add_resource_to_collection&param1={}&param2=1'.format(
            resource_id
        ))
