#!/usr/bin/python3
"""
generates a .tgz archive from the contents of the web_static
"""
from fabric.operations import local
from datetime import datetime


def do_pack():
    """Fabric script that generates a .tgz archive using
    function do_pack()
    """
    dt = datetime.now()
    dt_format = dt.strftime("%Y%m%d%H%M%S")
    arch = "web_static_" + dt_format + ".tgz"
    local("mkdir -p versions")

    try:
        local('tar -cvzf versions/{} web_static'.format(arch))
        path = 'versions/{}'.format(arch)
        path = local('tar -cvzf versions/{} web_static'.format(arch))
        return path
    except:
        return None
