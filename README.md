Hashicorp Nomad
=========
> This repository is only a mirror. Development and testing is done on a private gitlab server.

This role install and configure nomad on **debian-based** distributions.

Requirements
------------

None.

Role Variables
--------------
Available variables are listed below, along with default values. A sample file for the default values is available in `default/hashicorp_nomad.yml.sample` in case you need it for any `group_vars` or `host_vars` configuration.

```yaml
hashi_nomad_install: true # by default, set to true
```
This variable defines if the nomad package is to be installed or not before configuring. If you install nomad using another task, you can set this to `false`.

```yaml
hashi_nomad_cni_plugins_install: true # by default, set to true
```
This variable defines whether or not to install the CNI plugins on the host. Defaults to `true`.

```yaml
hashi_nomad_start_service: true
```
This variable defines if the nomad service should be started once it has been configured. This is usefull in case you're using this role to build golden images, in which case you might want to only enable the service, to have it start on the next boot (when the image is launched)

```yaml
hashi_nomad_cni_plugins_version: latest # by default, set to latest
```
This variable defines the version of the CNI plugins to install.

```yaml
hashi_nomad_cni_plugins_install_path: /opt/cni/bin
```
This variable defines where to install the CNI plugins. Note that it should be referenced in the nomad configuration.

```yaml
hashi_nomad_version: latest # by default, set to latest
```
This variable specifies the version of nomad to install when `hashi_nomad_install` is set to `true`. The version to specify is the version of the package on the hashicorp repository (`1.5.1-1` for example). This can be found by running `apt-cache madison consul` on a machine with the repository installed.

```yaml
hashi_nomad_deploy_method: host # by default, set to host
```
This variable defines the method of deployment of nomad. The `host` method installs the binary directly on the host, and runs nomad as a systemd service. The `docker` method install nomad as a docker container.
> Currently, only the `host` method is available, the `docker` method will be added later.

```yaml
hashi_nomad_env_variables: # by default, set to empty
  env_var: value
```
This value is a list of key/value that will populate the `nomad.env` file. You do not have to capitalize the KEYS, as it will be done automatically.

```yaml
hashi_nomad_configuration: {} # by default, set to a simple configuration
```
This variable sets all of the configuration parameters for nomad. For more information on all of them, please check the [documentation](https://developer.hashicorp.com/nomad/docs/configuration). This variable is parsed and converted to json format to create the config file, so each key and value should be set according to the documentation. This method of passing configuration allows for compatibility with every configuration parameters that nomad has to offer. The defaults are simply here to deploy a simple, single-node nomad server without much configuration, and should NOT be used in production. You will want to edit this to deploy production-ready clusters.

Dependencies
------------

This role has a task that installs its own dependencies located in `task/prerequisites.yml`, so that you don't need to manage them. This role requires both `ednxzu.manage_repositories` and `ednxzu.manage_apt_packages` to install nomad.

Example Playbook
----------------

```yaml
# calling the role inside a playbook with either the default or group_vars/host_vars
- hosts: servers
  roles:
    - ednxzu.hashicorp_nomad
```

License
-------

MIT / BSD

Author Information
------------------

This role was created by Bertrand Lanson in 2023.
