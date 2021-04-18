#!/usr/bin/python3
"""generates a .tgz archive from the contents
of the web_static folder"""

from datetime import datetime
from fabric.api import local
import os.path


def do_pack():
    """generate tgz archive using fabric"""
    date = datatime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(date)
    if os.path.isdir("versions") is False:
        local("mkdir versions")
    if os.path.exists(file_path):
        return file_path
    return None
