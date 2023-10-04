#!/usr/bin/python3
""" Python script that generate a .tgz archive from the contents
of the web_static folder """


from fabric.api import local
import os
from datetime import datetime


def do_pack():
    """ function that generate a tgz archive
    from a folder """

    date_time = datetime.now()
    custom_date_time = date_time.strftime("%Y%m%d%H%M%S")
    archive_name = f'web_static_{custom_date_time}.tgz'
    folder_to_compress = "web_static"

    """ create the archive """
    local(f'tar czvf {archive_name} {folder_to_compress}')

    """ checking if the archive file is generated """
    if os.path.exists(archive_name):
        local('mkdir -p versions')
        local(f'mv {archive_name} versions')
        return f"versions/{archive_name}"
    else:
        return None
