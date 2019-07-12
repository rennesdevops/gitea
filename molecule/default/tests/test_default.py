import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'


def test_gitea_file(host):
    f = host.file('/usr/local/bin/gitea')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o555


def test_git_group(host):
    assert host.group('git').exists


def test_git_user(host):
    assert host.run('id git').rc == 0


def test_gitea_exec(host):
    gitea = host.service("gitea")
    assert gitea.is_running
    assert gitea.is_enabled


def test_git_is_installed(host):
    gitpackage = host.package('git')
    assert gitpackage.is_installed


def test_gitea_config_dir(host):
    f = host.file('/etc/gitea')

    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755


def test_gitea_work_dir(host):
    f = host.file('/var/lib/gitea')

    assert f.exists
    assert f.is_directory
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o755


def test_gitea_custom_dir(host):
    f = host.file('/var/lib/gitea/custom')

    assert f.exists
    assert f.is_directory
    assert f.user == 'git'
    assert f.group == 'git'
    assert f.mode == 0o755


def test_gitea_config(host):
    f = host.file('/etc/gitea/app.ini')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert f.mode == 0o444


def test_port_listen(host):
    assert host.socket("tcp://0.0.0.0:3000").is_listening
