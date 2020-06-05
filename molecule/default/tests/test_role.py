import os

import testinfra.utils.ansible_runner

import re

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_dir(host):
    dir = host.file('/snap/bin')
    assert dir.exists
    assert dir.is_directory
    assert dir.user == 'root'


def test_file(host):
    installed_file = host.file('/snap/bin/microk8s')
    assert installed_file.exists
    assert installed_file.is_file
    assert installed_file.user == 'root'
    assert installed_file.group == 'root'


def test_version(host):
    version = host.check_output('snap info microk8s | grep installed:')
    pattern = 'v[0-9\\.]+'
    assert re.search(pattern, version)
