#!/usr/bin/python3
"""Compress a folder to an archive before sending"""
from fabric.api import local
from datetime import datetime
import os


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
