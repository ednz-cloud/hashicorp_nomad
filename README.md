hashicorp_nomad
=========
> This repository is only a mirror. Development and testing is done on a private gitea server.

This role install and configure nomad on **debian-based** distributions.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/hashicorp_nomad.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
hashicorp_nomad_install: true # by default, set to true
```
This variable defines if the nomad package is to be installed or not before configuring. If you install nomad using another task, you can set this to `false`.

```yaml
hashicorp_nomad_cni_plugins_install: true # by default, set to true
```
This variable defines whether or not to install the CNI plugins on the host. Defaults to `true`.

```yaml
hashicorp_nomad_start_service: true
```
This variable defines if the nomad service should be started once it has been configured. This is usefull in case you're using this role to build golden images, in which case you might want to only enable the service, to have it start on the next boot (when the image is launched)

```yaml
hashicorp_nomad_cni_plugins_version: latest # by default, set to latest
```
This variable defines the version of the CNI plugins to install.

```yaml
hashicorp_nomad_cni_plugins_install_path: /opt/cni/bin
```
This variable defines where to install the CNI plugins. Note that it should be referenced in the nomad configuration.

```yaml
hashicorp_nomad_version: latest # by default, set to latest
```
This variable specifies the version of nomad to install when `hashicorp_nomad_install` is set to `true`. The version to specify is the version of the package on the hashicorp repository (`1.5.1-1` for example). This can be found by running `apt-cache madison consul` on a machine with the repository installed.

```yaml
hashicorp_nomad_deploy_method: host # by default, set to host
```
This variable defines the method of deployment of nomad. The `host` method installs the binary directly on the host, and runs nomad as a systemd service. The `docker` method install nomad as a docker container.
> Currently, only the `host` method is available, the `docker` method will be added later.

```yaml
hashicorp_nomad_env_variables: # by default, set to empty
  env_var: value
```
This value is a list of key/value that will populate the `nomad.env` file. You do not have to capitalize the KEYS, as it will be done automatically.

```yaml
hashicorp_nomad_extra_files: false # by default, set to false
```
This variable defines whether or not there is extra configuration files to copy to the target. If there are, these extra files are expected to be jinja2 templates located all in the same directory, and will be copied to the specified directory on the target machine.


```yaml
hashicorp_nomad_extra_files_list: [] # by default, set to []
  # - src: /tmp/directory
  #   dest: /etc/nomad.d/directory
  # - src: /tmp/file.conf
  #   dest: /etc/nomad.d/file.conf
  # - src: /etc/nomad.d/file.j2
  #   dest: /etc/nomad.d/file
```
This variable lets you copy extra configuration files and directories over to the target host(s). It is a list of dicts. Each dict needs a `src` and a `dest` attribute. The source is expected to be located on the deployment machine. The source can be either a file or a directory. The destination must match the type of the source (file to file, dir to dir). If the source is a directory, every file inside of it will be recursively copied and templated over to the target directory.

For example, if you have the following source files to copy:

```bash
├── directory
│   ├── recursive
│   │   ├── test4.j2
│   │   └── test.j2024.conf
│   └── test3
├── file
├── file2.j2
```
You can set:

```yaml
hashicorp_nomad_extra_files_list: [] # by default, set to []
  - src: /tmp/directory
    dest: /etc/nomad.d/directory
  - src: /tmp/file
    dest: /etc/nomad.d/file.conf
  - src: /etc/nomad.d/file2.j2
    dest: /etc/nomad.d/file2.conf
```
all the files shown above will be copied over, and the directory structure inside `directory` will be preserved.

> **Note**
> In case you're using the `docker` deployment method, every destination path will be added automatically to the `hashicorp_nomad_extra_container_volumes` variable, so you don't need to set them manually.

```yaml
hashicorp_nomad_configuration: {} # by default, set to a simple configuration
```
This variable sets all of the configuration parameters for nomad. For more information on all of them, please check the [documentation](https://developer.hashicorp.com/nomad/docs/configuration). This variable is parsed and converted to json format to create the config file, so each key and value should be set according to the documentation. This method of passing configuration allows for compatibility with every configuration parameters that nomad has to offer. The defaults are simply here to deploy a simple, single-node nomad server without much configuration, and should NOT be used in production. You will want to edit this to deploy production-ready clusters.

Dependencies
------------

`ednz_cloud.manage_repositories` to configure the hashicorp apt repository.
`ednz_cloud.manage_apt_packages` to install nomad.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednz_cloud.hashicorp_nomad
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
