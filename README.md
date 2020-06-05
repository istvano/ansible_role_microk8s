Ansible Role: microk8s
==================

Role to download and install [microk8s](https://microk8s.io/) the smallest, simplest, pure production K8s.


Requirements
------------

* Ansible >= 2.7

* Linux Distribution

    * Debian Family


        * Ubuntu

            * Xenial (16.04)
            * Bionic (18.04)


Role Variables
--------------

The following variables will change the behavior of this role (default values
are shown below):

```yaml
# microk8s version number
microk8s_version: '1.18/stable'


Example Playbook
----------------

```yaml
- hosts: servers
  roles:
    - role: istvano.microk8s
```

License
-------

MIT
