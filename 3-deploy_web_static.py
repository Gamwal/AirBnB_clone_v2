#!/usr/bin/python3
"""Compress a folder to an archive before sending"""
from fabric.api import run
from fabric.api import put
from fabric.api import env
import os.path
do_pack = __import__("1-pack_web_static")
do_deploy = __import__("2-do_deploy_web_static")

env.hosts = ["52.91.127.215", "100.25.152.92"]
arc_path = do_pack.do_pack()


def deploy():
    """
    This is a function that transfers the archive to the server,
    upacks it and puts it in the right destination

    args:
        archive_path: the archive to be uploaded to the server

    Return:
        True if successful
        False if not successful
    """
    if arc_path is None:
        return False

    result = do_deploy.do_deploy(arc_path)
    return result
