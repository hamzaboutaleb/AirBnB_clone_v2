#!/usr/bin/python3
"""
    Write a Fabric script that generates a .tgz archive from the contents of 
    the web_static folder of your AirBnB Clone repo, using the function do_pack
"""

from fabric.api import local
from datetime import datetime


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

