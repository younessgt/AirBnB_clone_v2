#!/usr/bin/python3
""" Python script for a full deployment to the web servers"""

from fabric.api import run, put, env, local, runs_once
import os
from datetime import datetime

env.hosts = ['18.235.249.72', '34.239.254.179']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


@runs_once
def do_pack():
    """ function that generate a tgz archive
    from a folder """

    date_time = datetime.now()
    custom_date_time = date_time.strftime("%Y%m%d%H%M%S")
    archive_name = f'web_static_{custom_date_time}.tgz'
    folder_to_compress = "web_static"

    """ create the archive """
    local(f'tar -czvf {archive_name} {folder_to_compress}')

    """ checking if the archive file is generated """
    if os.path.exists(archive_name):
        local('mkdir -p versions')
        local(f'mv {archive_name} versions')
        return f"versions/{archive_name}"
    else:
        return None


def do_deploy(archive_path):
    """ deploying the website into the specific servers """

    if not os.path.exists(archive_path):
        return False
    try:
        """ extracting just the file name including the extension """
        base_name = os.path.basename(archive_path)

        """ extracting the file name without extension """
        file_no_ext = os.path.splitext(base_name)[0]

        """ uploding the archive to /tmp/ """
        put(archive_path, '/tmp/')

        run(f'mkdir -p /data/web_static/releases/{file_no_ext}/')

        run(f'tar -xzf /tmp/{base_name} -C \
/data/web_static/releases/{file_no_ext}/')

        run(f'rm /tmp/{base_name}')

        file_html_css = f'/data/web_static/releases/{file_no_ext}'

        run(f'mv /data/web_static/releases/{file_no_ext}/web_static/* \
{file_html_css}/')

        run(f'rm -rf /data/web_static/releases/{file_no_ext}/web_static')

        run('rm -rf /data/web_static/current')

        run(f'ln -s {file_html_css} /data/web_static/current')

        print("New version deployed!")

        return True

    except Exception as e:
        with open('/dev/null', 'w') as null_file:
            print(e, file=null_file)
        return False


def deploy():
    """ full deployment into the two servers """

    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
