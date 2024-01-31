#!/usr/bin/python3
"""
Module 1-pack_web_static:
Fabric script that distributes an archive to your web servers
"""

from os import path
from datetime import datetime as dt
from fabric.api import env, local, put, run

env.user = 'ubuntu'
env.hosts = ['100.24.74.255', '52.86.146.141']
env.key_filename = ['~/.ssh/alx.key', '~/.ssh/alx']


def do_pack():
    """generates a .tgz archive"""
    file = "versions/web_static_{:%Y%m%d%H%M%S}.tgz".format(dt.now())
    if path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file


def do_deploy(archive_path):
    """Distributes an archive to your web servers

    Args:
        archive_path (str): archive path to distribute
    """
    if path.isfile(archive_path) is False:
        return False
    target_path = "/data/web_static/releases/"
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if run("rm -rf {}{}/".
           format(target_path, name)).failed is True:
        return False
    if run("sudo mkdir -p {}{}/".
           format(target_path, name)).failed is True:
        return False
    if run("sudo tar -xzf /tmp/{} -C {}{}/".
           format(file, target_path, name)).failed is True:
        return False
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    if run("sudo mv {0:}{1:}/web_static/* "
           "{0:}{1:}/".format(target_path, name)).failed is True:
        return False
    if run("sudo rm -rf {}{}/web_static".
           format(target_path, name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("sudo ln -s {}{}/ /data/web_static/current".
           format(target_path, name)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
