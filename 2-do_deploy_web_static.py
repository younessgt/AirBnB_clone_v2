#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers
using the function do_deploy """

from fabric.api import run, put, env
import os


env.hosts = ['18.235.249.72', '34.239.254.179']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """ deploying the website into the specific servers """

    if not os.path.exists(archive_path):
        return False
    """ extracting just the file name including the extension """
    base_name = os.path.basename(archive_path)

    """ extracting the file name without extension """
    file_no_ext = os.path.splitext(base_name)[0]

    """ uploding the archive to /tmp/ """
    put(archive_path, '/tmp/')

    run(f'mkdir -p /data/web_static/releases/{file_no_ext}')

    run(f'tar -xzf /tmp/{base_name} -C \
            /data/web_static/releases/{file_no_ext}')

    run(f'rm /tmp/{base_name}')

    file_html_css = f'/data/web_static/releases/{file_no_ext}'

    run(f'mv /data/web_static/releases/{file_no_ext}/web_static/* \
            {file_html_css}')

    run(f'rm -rf /data/web_static/releases/{file_no_ext}/web_static')

    run('rm -rf /data/web_static/current')

    run(f'ln -s {file_html_css} /data/web_static/current')

    print("New version deployed!")

    return True
