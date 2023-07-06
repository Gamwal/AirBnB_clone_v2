#!/usr/bin/python3
"""Compress a folder to an archive before sending"""

from fabric.api import local
from fabric import Connection
from datetime import datetime
import os


env.hosts = ['52.91.127.215', '100.25.152.92']


def do_pack():
    """
    This is a function that packs the contents of
    folder web_static

    args:
        None

    Return:
        None if function failed
        else, returns
    """

    if not os.path.exists("versions"):
        os.makedirs("versions")

    dir = "web_static"
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    arc_name = "web_static_{}.tgz".format(timestamp)
    arc_path = "versions/{}".format(arc_name)

    print(f"Packing web_static to {arc_path}")

    try:
        local(f"tar -cvzf {arc_path} {dir}")
        size = os.stat(arc_path)
        print(f"{dir} packed: {arc_path} -> {size.st_size}Bytes")
        return f"{arc_path}"
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    This is a function that transfers the archive to the server,
    upacks it and puts it in the right destination

    args:
        archive_path: the archive to be uploaded to the server

    Return:
        True if successful
        False if not successful
    """

    if not os.path.exists(archive_path):
        return False
    dest_path = f"/data/web_static/releases/{archive_path[0:-4]}"
    for host in env.hosts:
        try:
            with Connection(host) as c:
                print("Executing task 'do_deploy'")
                c.put(archive_path, remote='/tmp/')
                c.run('mkdir -p /data/web_static/releases/')
                c.run(f"tar -xzf /tmp/{archive_path} -C {dest_path}")
                c.run(f'rm -rf {archive_path}')
                c.run('rm -rf /data/web_static/current')
                c.run(f'ln -sf {dest_path}/ /data/web_static/current')
                print('New version deployed!')
                return True
        except Exception as e:
            return False
