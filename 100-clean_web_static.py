#!/usr/bin/python3
""" Script that deletes out-of-date archives """
from fabric.api import local, run, env, cd, lcd
import os

env.hosts = ['18.235.249.72', '34.239.254.179']
# env.user = "ubuntu"
# env.key_filename = '~/.ssh/school'


def do_clean(number=0):
    """ cleaning specific directories from out dated archives """

    if int(number) == 0:
        number = 1
 
    result = sorted(os.listdir("versions"))
    [result.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(archive)) for archive in result]

    with cd("/data/web_static/releases/"):
        result_remote = run("ls -tr").split()
        file_list = [fil for fil in result_remote if "web_static_" in fil]
        [file_list.pop() for i in range(number)]
        [run("rm -rf ./{}".format(file_web)) for file_web in file_list]
