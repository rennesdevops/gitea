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
