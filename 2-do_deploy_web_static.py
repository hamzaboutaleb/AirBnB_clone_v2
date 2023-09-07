#!/usr/bin/python3
"""
distributes an archive to your web servers
"""

from fabric.api import env, run, put, sudo
from os import path

env.hosts = ['100.26.238.129', '18.210.15.20']


def do_deploy(archive_path):

    if not path.exists(archive_path):
        return False
    try:
        # get folder name from filePath
        folder_name = path.splitext(os.path.basename(archive_path))[0]
        folder_path = "/data/web_static/releases/{}".format(folder_name)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(folder_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("rm -rf /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}".format(folder_path, folder_path))
        run("rm -rf {}/web_static".format(folder_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder_path))
        return True
    except Exception:
        return False
