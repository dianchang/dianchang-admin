# coding: utf-8
from fabric.api import run, env, cd, prefix, shell_env
from config import load_config

config = load_config()
host_string = config.HOST_STRING


def deploy():
    """部署"""
    env.host_string = config.HOST_STRING
    with cd('/var/www/dianchang-admin'):
        with shell_env(MODE='PRODUCTION'):
            run('git reset --hard HEAD')
            run('git pull')
            run('git submodule foreach git checkout master')
            run('git submodule foreach git pull origin master')
            with prefix('source venv/bin/activate'):
                run('pip install -r requirements.txt')
                run('pip install -r application/models/dc/requirements.txt')
                run('python manage.py db upgrade')
                run('python manage.py build_assets')
            run('supervisorctl restart dianchang-admin')


def restart():
    """重启"""
    env.host_string = config.HOST_STRING
    run('supervisorctl restart dianchang-admin')
