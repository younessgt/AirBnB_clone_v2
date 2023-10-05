#!/usr/bin/python3
""" Script that deletes out-of-date archives """
from fabric.api import local, run, env, cd

env.hosts = ['18.235.249.72', '34.239.254.179']
# env.user = "ubuntu"
# env.key_filename = '~/.ssh/school'


def do_clean(number=0):
    """ cleaning specific directories from out dated archives """

    if int(number) == 0:
        number = 1

    local("ls -t versions | tail -n +{} | xargs -I {{}} rm versions/{{}}"
          .format(int(number) + 1))

    with cd("/data/web_static/releases"):
        run("ls -t | tail -n +{} | xargs -I {{}} "
            "rm -rf /data/web_static/releases/{{}}".format(int(number) + 1))
