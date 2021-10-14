# Ansible Role: microk8s

Role to download and install [microk8s](https://microk8s.io/) the smallest, simplest, pure production K8s.

## Requirements

* Ansible >= 2.7
* Linux Distribution
    * Debian Family
        * Ubuntu
            * Xenial (16.04)
            * Bionic (18.04)
    * Arch Linux (untested)

## License

MIT

## Usage

### Role Variables

Some variables available in this role are listed here.  The full set is
defined in `[defaults/main.yml](defaults/main.yml)`.

* `microk8s_version`: Version to use, defaults to `1.19/stable`.
* `microk8s_plugins`: Enable/disable various plugins. A string will be passed as `arg` when enabling addon using `name:arg`
* `microk8s_enable_HA`: Enable/disable high-availability.
* `microk8s_group_HA`: Hostgroup whose members will form HA cluster.
* `microk8s_csr_template`: If defined, will cause a custom CSR to be used in
  generating certificates.

### Basic playbook

```yaml
- hosts: servers
  roles:
    - role: istvano.microk8s
      vars:
        microk8s_plugins:
          dns: "1.1.1.1"
          istio: true
          ingress: true
```

### Custom certificate request template

It might be useful to customize the certificate request template used by
MicroK8s in generating cluster certificates.  For example, additional SANs can
be added to the certificates such that the MicroK8s certificates validate when
addressed from outside the cluster, such as through a reverse proxy.

To generate a CSR template, the easiest is probably to use the role without
a template, and then copy the CSR in
`/var/snap/microk8s/current/certs/csr.conf.template` to your playbook's
templates directory, make the edits and set the `microk8s_csr_template`
variable accordingly, and re-run the playbook.

## Testing

### Using Molecule wrapper and system Python

* `./moleculew lint`
* `./moleculew create`
* `./moleculew list`
* `./moleculew check`
* `./moleculew test`

### Using Python virtual environment

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
* Run the test commands:
  * `molecule lint`
  * `molecule create`
  * `molecule list`
  * `molecule check`
  * `molecule test`
