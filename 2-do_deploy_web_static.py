#!/usr/bin/python3
"""
distributes an archive to your web servers
"""

from fabric.api import env, run, put, sudo
import os

# env.hosts = ['100.26.238.129', '18.210.15.20']
# env.user = "ubuntu"
# env.key_filename = "~/.ssh/school"


def do_pack():
    """Compress content web_static"""

    local("mkdir -p versions")
    now = datetime.now()
    filename = now.strftime("web_static_%Y%m%d%H%M%S.tgz")
    path = "versions/{}".format(filename)
    result = local("tar -czvf {} web_static".format(path))

    if result.failed:
        return None
    return path


def do_deploy(archive_path):
    """ do deploy """

    if not os.path.exists(archive_path):
        print("no file exist")
        return False
    try:
        # get folder name from filePath
        file_name = os.path.splitext(os.path.basename(archive_path))[0]
        folder_path = "/data/web_static/releases/{}".format(file_name)
        print(file_name, folder_path)

        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(folder_path))
        run("sudo tar -xzf /tmp/{}.tgz -C {}".format(file_name, folder_path))
        run("sudo rm -rf /tmp/{}.tgz".format(file_name))
        run("sudo cp -a /data/web_static/releases/{}/web_static/. {}"
            .format(file_name, folder_path))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(file_name))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(folder_path))
        return True
    except Exception as e:
        print("sometihng went wrong", e)
        return False
