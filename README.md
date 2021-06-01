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

Some variables available in this role are listed here.  The full set is
defined in `[defaults/main.yml](defaults/main.yml)`.

* `microk8s_version`: Version to use, defaults to `1.19/stable`.
* `microk8s_plugin_*_enable: true`: Enable/disable various plugins.
* `microk8s_enable_HA: false`: Enable/disable high-availability.
* `microk8s_group_HA: microk8s_HA`: Hostgroup whose members will form HA
  cluster.

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

Test
-------

## Using Molecule wrapper and system Python

* ./moleculew lint
* ./moleculew create
* ./moleculew list
* ./moleculew check
* ./moleculew test

## Using Python virtual environment

* Set up virtual environment
    ```
    $ python3 -m venv venv
    ```
* Activate the environment
    ```
    $ . venv/bin/activate
    ```
* Install Molecule with lint and Docker options
    ```
    $ pip install 'molecule[lint,docker]'
    ```
* Install up-to-date Ansible package if necessary
    ```
    $ pip install ansible
    ```
* Add the following to your `.yamllint`:
    ```
    ignore: |
      venv/
    ```
    It might be necessary to run `molecule lint` first in order to create the
    `.yamllint` file.
* Run the test commands:
  * `molecule lint`
  * `molecule create`
  * `molecule list`
  * `molecule check`
  * `molecule test`
