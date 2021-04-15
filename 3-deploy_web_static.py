#!/usr/bin/python3
"""based on task 2 file, distributes an archive to web servers
using the prototype function deploy()
"""
from fabric.api import env
from fabric.operations import local, put, run
from os import path
from datetime import datetime
env.user = 'ubuntu'
env.hosts = ['35.190.138.21', '3.94.64.65']


def do_pack():
    """Fabric script that generates a .tgz archive using
    function do_pack() and store the path of the created archive
    """
    dt = datetime.now()
    dt_format = dt.strftime("%Y%m%d%H%M%S")
    archive = "web_static_" + dt_format + ".tgz"
    local("mkdir -p versions")

    try:
        local('tar -cvzf versions/{} web_static'.format(archive))
        return 'versions/{}'.format(archive)
    except:
        return None


def do_deploy(archive_path):
    """Upload the archive to the /tmp/ directory of the web server
       Uncompress the archive to the folder on the web server
       Delete the archive from the web server
       Delete the symbolic link /data/web_static/current
       from the web server
       Create a new the symbolic link /data/web_static/current
       linked to the new version of code:
       /data/web_static/releases/<archive filename w/o extension>
    """
    if not path.exists(archive_path):
        return(False)
    try:
        put(archive_path, "/tmp/")
        arch = archive_path.split('/')[1]
        res = "/data/web_static/releases/{}".format(arch.split('.')[0])
        run("mkdir -p {}/".format(res))
        run("tar -xzf /tmp/{} -C {}/".format(arch, res))
        run("rm -rf /tmp/{}".format(arch))
        run("mv {}/web_static/* {}".format(res, res))
        run("rm -rf /data/web_static/current")
        run("ln -s {}/ /data/web_static/current".format(res))
        print("New version deployed!")
        return True
    except:
        return False


def deploy():
    """Return the return value of do_deploy"""
    my_file = do_pack()
    if my_file is None:
        return False
    return do_deploy(my_file)
