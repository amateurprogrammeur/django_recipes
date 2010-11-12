from fabric.api import *
from fabric.context_managers import cd
import os

svn_url = 'http://django-recipes.googlecode.com/svn/branches/pip'
CURR_DIR = os.path.abspath(os.path.split(__file__)[0])

def dev():
    env.config = 'dev'
    env.hosts = ['david@localhost:55555']
    env.root_dir = CURR_DIR
    env.show = ['debug']
    env.mysqlpackage = 'libmysqlclient-dev'

def local():
    env.config = 'local'
    env.hosts = ['david@localhost:55555']
    env.root_dir = 'test-pip'
    env.show = ['debug']
    env.svn = 'svn export ' + (svn_url) + ' src'
    env.mysqlpackage = 'libmysqlclient-dev'

def prod():
    env.config = 'prod'
    env.hosts = ['david@slice:55555']
    env.root_dir = '/home/david/public_html/recipes.davidgrant.ca/public'
    env.user = "david"
    env.key_filename = ["/home/david/.ssh/id_dsa"]
    env.show = ['debug']
    env.svn = 'svn export ' + (svn_url) + ' src'
    env.mysqlpackage = 'libmysqlclient15-dev'

def __prereqcheck():
    require('hosts', provided_by=[local,slice])
    require('root_dir', provided_by=[local,slice])

def clean():
    run('rm -rf %(root_dir)s' % env)

def setup():
    __prereqcheck()
    sudo('apt-get update')
    sudo('apt-get install python-setuptools python2.6-dev subversion %(mysqlpackage)s' % env)
    sudo('easy_install -U virtualenv')
    sudo('easy_install -U pip')

def virtualenv():
    __prereqcheck()
    run('mkdir -p %(root_dir)s' % env)
    with cd('%(root_dir)s' % env):
        run('rm -rf env')
        run('mkdir --parents ~/.pipcache')
        run('virtualenv --distribute --no-site-packages env')

def deploy():
    __prereqcheck()
    PIP_PATH = os.path.join('%(root_dir)s' % env, 'env', 'bin', 'pip')
    with cd('%(root_dir)s' % env):
        if env.config == 'dev':
            run('%(pip_path)s -E env install --upgrade -r requirements.txt --download-cache=~/.pipcache' % {'pip_path': PIP_PATH})
        else:
            run('rm -rf src')
            run('%(svn)s' % env)
            run('%(pip_path)s -E env install --upgrade -r src/requirements.txt --download-cache=~/.pipcache' % {'pip_path': PIP_PATH})

