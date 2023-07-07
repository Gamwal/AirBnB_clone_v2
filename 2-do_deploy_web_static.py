#!/usr/bin/python3
"""Compress a folder to an archive before sending"""
from fabric.api import run
from fabric.api import put
from fabric.api import env
import os.path

env.hosts = ["52.91.127.215", "100.25.152.92"]


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
    if not os.path.isfile(archive_path):
        return False

    archive = archive_path.split("/")[-1]
    folder_name = archive.split(".")[0]
    dest_path = f"/data/web_static/releases/{folder_name}"

    try:
        print("Executing task 'do_deploy'")
        put(archive_path, f'/tmp/{archive}')
        run(f'mkdir -p /data/web_static/releases/{folder_name}')
        run(f"tar -xzf /tmp/{archive} -C {dest_path}")
        run(f'rm -rf /tmp/{archive}')
        run(f'mv {dest_path}/web_static/* {dest_path}')
        run(f"rm -rf {dest_path}/web_static")
        run('rm -rf /data/web_static/current')
        run(f'ln -sf {dest_path}/ /data/web_static/current')
        print('New version deployed!')
        return True
    except Exception as e:
        return False
