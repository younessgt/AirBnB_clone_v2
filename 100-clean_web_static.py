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

    result = local("ls -t version", capture=True)
    file_list = result.split("\n")
    file_list = [archive for archive in file_list if archive.strip()]
    for i in range(int(number), len(file_list)):
        local(f"rm versions/{file_list[i]}")

    with cd("/data/web_static/releases"):
        result_remote = run("ls -t")
        file_list = result_remote.stdout.split(" ")
        file_list = [file_web for file_web in file_list if file_web.strip()]
        for i in range(int(number), len(file_list)):
            run(f"rm -rf /data/web_static/releases/{file_list[i]}")
