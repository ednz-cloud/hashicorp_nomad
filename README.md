# hashicorp_nomad

![Ansible Badge](https://img.shields.io/badge/Ansible-E00?logo=ansible&logoColor=fff&style=for-the-badge)
![HashiCorp Badge](https://img.shields.io/badge/HashiCorp-000?logo=hashicorp&logoColor=fff&style=for-the-badge)
![Nomad Badge](https://img.shields.io/badge/Nomad-00CA8E?logo=nomad&logoColor=fff&style=for-the-badge)

> This repository is only a mirror. Development and testing is done on a private gitea server.
<!-- DOCSIBLE START -->

# 📃 Role overview

## hashicorp_nomad



Description: Install and configure hashicorp nomad for debian-based distros.


| Field                | Value           |
|--------------------- |-----------------|
| Readme update        | 17/07/2024 |

### Defaults

**These are static variables with lower priority**

#### File: main.yml



| Var          | Type         | Value       |Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [hashicorp_nomad_version](defaults/main.yml#L4)   | str   | `latest`  |  n/a  |  n/a |
| [hashicorp_nomad_start_service](defaults/main.yml#L5)   | bool   | `True`  |  n/a  |  n/a |
| [hashicorp_nomad_config_dir](defaults/main.yml#L6)   | str   | `/etc/nomad.d`  |  n/a  |  n/a |
| [hashicorp_nomad_data_dir](defaults/main.yml#L7)   | str   | `/opt/nomad`  |  n/a  |  n/a |
| [hashicorp_nomad_certs_dir](defaults/main.yml#L8)   | str   | `{{ hashicorp_nomad_config_dir }}/tls`  |  n/a  |  n/a |
| [hashicorp_nomad_logs_dir](defaults/main.yml#L9)   | str   | `/var/log/nomad`  |  n/a  |  n/a |
| [hashicorp_nomad_cni_plugins_install](defaults/main.yml#L11)   | bool   | `True`  |  n/a  |  n/a |
| [hashicorp_nomad_cni_plugins_version](defaults/main.yml#L12)   | str   | `latest`  |  n/a  |  n/a |
| [hashicorp_nomad_cni_plugins_install_path](defaults/main.yml#L13)   | str   | `/opt/cni/bin`  |  n/a  |  n/a |
| [hashicorp_nomad_extra_files](defaults/main.yml#L15)   | bool   | `False`  |  n/a  |  n/a |
| [hashicorp_nomad_extra_files_list](defaults/main.yml#L16)   | list   | `[]`  |  n/a  |  n/a |
| [hashicorp_nomad_env_variables](defaults/main.yml#L18)   | dict   | `{}`  |  n/a  |  n/a |
| [hashicorp_nomad_extra_configuration](defaults/main.yml#L29)   | dict   | `{}`  |  n/a  |  n/a |
| [hashicorp_nomad_region](defaults/main.yml#L35)   | str   | `global`  |  n/a  |  n/a |
| [hashicorp_nomad_datacenter](defaults/main.yml#L36)   | str   | `dc1`  |  n/a  |  n/a |
| [hashicorp_nomad_bind_addr](defaults/main.yml#L42)   | str   | `0.0.0.0`  |  n/a  |  n/a |
| [hashicorp_nomad_advertise_addr](defaults/main.yml#L43)   | str   | `{{ ansible_default_ipv4.address }}`  |  n/a  |  n/a |
| [hashicorp_nomad_address_configuration](defaults/main.yml#L44)   | dict   | `{'bind_addr': '{{ hashicorp_nomad_bind_addr }}', 'addresses': {'http': '{{ hashicorp_nomad_advertise_addr }}', 'rpc': '{{ hashicorp_nomad_advertise_addr }}', 'serf': '{{ hashicorp_nomad_advertise_addr }}'}, 'advertise': {'http': '{{ hashicorp_nomad_advertise_addr }}', 'rpc': '{{ hashicorp_nomad_advertise_addr }}', 'serf': '{{ hashicorp_nomad_advertise_addr }}'}, 'ports': {'http': 4646, 'rpc': 4647, 'serf': 4648}}`  |  n/a  |  n/a |
| [hashicorp_nomad_autopilot_configuration](defaults/main.yml#L63)   | dict   | `{}`  |  n/a  |  n/a |
| [hashicorp_nomad_leave_on_interrupt](defaults/main.yml#L69)   | bool   | `False`  |  n/a  |  n/a |
| [hashicorp_nomad_leave_on_terminate](defaults/main.yml#L70)   | bool   | `False`  |  n/a  |  n/a |
| [hashicorp_nomad_enable_server](defaults/main.yml#L76)   | bool   | `True`  |  n/a  |  n/a |
| [hashicorp_nomad_server_bootstrap_expect](defaults/main.yml#L77)   | int   | `1`  |  n/a  |  n/a |
| [hashicorp_nomad_server_configuration](defaults/main.yml#L78)   | dict   | `{'enabled': '{{ hashicorp_nomad_enable_server }}', 'data_dir': '{{ hashicorp_nomad_data_dir }}/server', 'encrypt': "{{ 'mysupersecretgossipencryptionkey'\|b64encode }}", 'server_join': {'retry_join': ['{{ ansible_default_ipv4.address }}']}}`  |  n/a  |  n/a |
| [hashicorp_nomad_enable_client](defaults/main.yml#L90)   | bool   | `False`  |  n/a  |  n/a |
| [hashicorp_nomad_client_configuration](defaults/main.yml#L91)   | dict   | `{'enabled': '{{ hashicorp_nomad_enable_client }}', 'state_dir': '{{ hashicorp_nomad_data_dir }}/client', 'cni_path': '{{ hashicorp_nomad_cni_plugins_install_path }}', 'bridge_network_name': 'nomad', 'bridge_network_subnet': '172.26.64.0/20'}`  |  n/a  |  n/a |
| [hashicorp_nomad_ui_configuration](defaults/main.yml#L102)   | dict   | `{'enabled': '{{ hashicorp_nomad_enable_server }}'}`  |  n/a  |  n/a |
| [hashicorp_nomad_driver_enable_docker](defaults/main.yml#L109)   | bool   | `True`  |  n/a  |  n/a |
| [hashicorp_nomad_driver_enable_podman](defaults/main.yml#L110)   | bool   | `False`  |  n/a  |  n/a |
| [hashicorp_nomad_driver_enable_raw_exec](defaults/main.yml#L111)   | bool   | `False`  |  n/a  |  n/a |
| [hashicorp_nomad_driver_enable_java](defaults/main.yml#L112)   | bool   | `False`  |  n/a  |  n/a |
| [hashicorp_nomad_driver_enable_qemu](defaults/main.yml#L113)   | bool   | `False`  |  n/a  |  n/a |
| [hashicorp_nomad_driver_configuration](defaults/main.yml#L115)   | dict   | `{'raw_exec': {'enabled': False}}`  |  n/a  |  n/a |
| [hashicorp_nomad_driver_extra_configuration](defaults/main.yml#L119)   | dict   | `{}`  |  n/a  |  n/a |
| [hashicorp_nomad_enable_log_to_file](defaults/main.yml#L125)   | bool   | `False`  |  n/a  |  n/a |
| [hashicorp_nomad_logging_configuration](defaults/main.yml#L126)   | dict   | `{'log_file': '{{ hashicorp_nomad_logs_dir }}/nomad.log', 'log_level': 'info', 'log_rotate_duration': '24h', 'log_rotate_max_files': 30}`  |  n/a  |  n/a |
| [hashicorp_nomad_acl_configuration](defaults/main.yml#L136)   | dict   | `{'enabled': False, 'token_ttl': '30s', 'policy_ttl': '60s', 'role_ttl': '60s'}`  |  n/a  |  n/a |
| [hashicorp_nomad_enable_tls](defaults/main.yml#L146)   | bool   | `False`  |  n/a  |  n/a |
| [hashicorp_nomad_tls_configuration](defaults/main.yml#L147)   | dict   | `{'http': True, 'rpc': True, 'ca_file': '/etc/ssl/certs/ca-certificates.crt', 'cert_file': '{{ hashicorp_nomad_certs_dir }}/cert.pem', 'key_file': '{{ hashicorp_nomad_certs_dir }}/key.pem', 'verify_server_hostname': True}`  |  n/a  |  n/a |
| [hashicorp_nomad_certificates_extra_files_dir](defaults/main.yml#L155)   | list   | `[]`  |  n/a  |  n/a |
| [hashicorp_nomad_enable_consul_integration](defaults/main.yml#L178)   | bool   | `False`  |  n/a  |  n/a |
| [hashicorp_nomad_consul_integration_configuration](defaults/main.yml#L179)   | dict   | `{'address': '127.0.0.1:8500', 'auto_advertise': True, 'ssl': False, 'token': '', 'tags': []}`  |  n/a  |  n/a |
| [hashicorp_nomad_consul_integration_tls_configuration](defaults/main.yml#L186)   | dict   | `{'ca_file': '/etc/ssl/certs/ca-certificates.crt'}`  |  n/a  |  n/a |
| [hashicorp_nomad_consul_integration_server_configuration](defaults/main.yml#L189)   | dict   | `{'server_auto_join': True}`  |  n/a  |  n/a |
| [hashicorp_nomad_consul_integration_client_configuration](defaults/main.yml#L192)   | dict   | `{'client_auto_join': True, 'grpc_address': '127.0.0.1:8502'}`  |  n/a  |  n/a |
| [hashicorp_nomad_consul_integration_client_tls_configuration](defaults/main.yml#L196)   | dict   | `{'grpc_ca_file': '/etc/ssl/certs/ca-certificates.crt'}`  |  n/a  |  n/a |
| [nomad_enable_vault_integration](defaults/main.yml#L203)   | bool   | `False`  |  n/a  |  n/a |
| [nomad_vault_integration_configuration](defaults/main.yml#L204)   | dict   | `{}`  |  n/a  |  n/a |


### Vars

**These are variables with higher priority**
#### File: main.yml


| Var          | Type         | Value       | Required    | Title       |
|--------------|--------------|-------------|-------------|-------------|
| [hashicorp_nomad_user](vars/main.yml#L3)    | str   | `nomad`  | n/a | n/a |
| [hashicorp_nomad_group](vars/main.yml#L4)    | str   | `nomad`  | n/a | n/a |
| [hashicorp_nomad_binary_path](vars/main.yml#L5)    | str   | `/usr/local/bin/nomad`  | n/a | n/a |
| [hashicorp_nomad_deb_architecture_map](vars/main.yml#L6)    | dict   | `{'x86_64': 'amd64', 'aarch64': 'arm64', 'armv7l': 'arm', 'armv6l': 'arm'}`  | n/a | n/a |
| [hashicorp_nomad_architecture](vars/main.yml#L11)    | str   | `{{ hashicorp_nomad_deb_architecture_map[ansible_architecture] \| default(ansible_architecture) }}`  | n/a | n/a |
| [hashicorp_nomad_service_name](vars/main.yml#L12)    | str   | `nomad`  | n/a | n/a |
| [hashicorp_nomad_github_api](vars/main.yml#L13)    | str   | `https://api.github.com/repos`  | n/a | n/a |
| [hashicorp_nomad_cni_github_project](vars/main.yml#L14)    | str   | `containernetworking/plugins`  | n/a | n/a |
| [hashicorp_nomad_github_project](vars/main.yml#L15)    | str   | `hashicorp/nomad`  | n/a | n/a |
| [hashicorp_nomad_github_url](vars/main.yml#L16)    | str   | `https://github.com`  | n/a | n/a |
| [hashicorp_nomad_repository_url](vars/main.yml#L17)    | str   | `https://releases.hashicorp.com/nomad`  | n/a | n/a |
| [hashicorp_nomad_configuration](vars/main.yml#L19)    | dict   | `{'datacenter': '{{ hashicorp_nomad_datacenter }}', 'region': '{{ hashicorp_nomad_region }}', 'data_dir': '{{ hashicorp_nomad_data_dir }}', 'leave_on_interrupt': '{{ hashicorp_nomad_leave_on_interrupt }}', 'leave_on_terminate': '{{ hashicorp_nomad_leave_on_terminate }}', 'acl': '{{ hashicorp_nomad_acl_configuration }}', 'server': '{{ hashicorp_nomad_server_configuration }}', 'client': '{{ hashicorp_nomad_client_configuration }}', 'ui': '{{ hashicorp_nomad_ui_configuration }}'}`  | n/a | n/a |
| [hashicorp_nomad_configuration_string](vars/main.yml#L30)    | str   | `server:
  bootstrap_expect: {{ hashicorp_nomad_server_bootstrap_expect }}
`  | n/a | n/a |


### Tasks


#### File: recursive_copy_extra_dirs.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Ensure destination directory exists | ansible.builtin.file | False |
| Nomad \| Create extra directory sources | ansible.builtin.file | True |
| Nomad \| Template extra directory sources | ansible.builtin.template | True |

#### File: merge_variables.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Merge stringified configuration | vars | False |
| Nomad \| Merge addresses configuration | vars | False |
| Nomad \| Merge consul integration configuration | block | True |
| Nomad \| Merge consul tls configuration | block | True |
| Nomad \| Merge consul default client configuration | vars | False |
| Nomad \| Merge consul configuration for nomad servers | block | True |
| Nomad \| Merge consul default server configuration | vars | False |
| Nomad \| Merge consul configuration for nomad clients | block | True |
| Nomad \| Merge consul default client configuration | vars | False |
| Nomad \| Merge consul tls client configuration | vars | True |
| Nomad \| Merge consul block into main configuration | vars | False |
| Nomad \| Merge TLS configuration | block | True |
| Nomad \| Merge TLS configuration | vars | False |
| Nomad \| Add certificates directory to extra_files_dir | ansible.builtin.set_fact | False |
| Nomad \| Merge plugin configuration | vars | True |
| Nomad \| Merge extra configuration settings | vars | False |

#### File: main.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Set reload-check & restart-check variable | ansible.builtin.set_fact | False |
| Nomad \| Import merge_variables.yml | ansible.builtin.include_tasks | False |
| Nomad \| Import prerequisites.yml | ansible.builtin.include_tasks | False |
| Nomad \| Import install.yml | ansible.builtin.include_tasks | False |
| Nomad \| Import cni_install.yml | ansible.builtin.include_tasks | True |
| Nomad \| Import configure.yml | ansible.builtin.include_tasks | False |
| Nomad \| Populate service facts | ansible.builtin.service_facts | False |
| Nomad \| Set restart-check variable | ansible.builtin.set_fact | True |
| Nomad \| Enable service: {{ hashicorp_nomad_service_name }} | ansible.builtin.service | False |
| Nomad \| Reload systemd daemon | ansible.builtin.systemd | True |
| Nomad \| Start service: {{ hashicorp_nomad_service_name }} | ansible.builtin.service | True |

#### File: install.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Get latest release of nomad | block | True |
| Nomad \| Get latest nomad release from github api | ansible.builtin.uri | False |
| Nomad \| Set wanted nomad version to latest tag | ansible.builtin.set_fact | False |
| Nomad \| Set wanted nomad version to {{ hashicorp_nomad_version }} | ansible.builtin.set_fact | True |
| Nomad \| Get current nomad version | block | False |
| Nomad \| Stat nomad version file | ansible.builtin.stat | False |
| Nomad \| Get current nomad version | ansible.builtin.slurp | True |
| Nomad \| Download and install nomad binary | block | True |
| Nomad \| Set nomad package name to download | ansible.builtin.set_fact | False |
| Nomad \| Download checksum file for nomad archive | ansible.builtin.get_url | False |
| Nomad \| Extract correct checksum from checksum file | ansible.builtin.command | False |
| Nomad \| Parse the expected checksum | ansible.builtin.set_fact | False |
| Nomad \| Download nomad binary archive | ansible.builtin.get_url | False |
| Nomad \| Create temporary directory for archive decompression | ansible.builtin.file | False |
| Nomad \| Unpack nomad archive | ansible.builtin.unarchive | False |
| Nomad \| Copy nomad binary to {{ hashicorp_nomad_binary_path }} | ansible.builtin.copy | False |
| Nomad \| Update nomad version file | ansible.builtin.copy | False |
| Nomad \| Set restart-check variable | ansible.builtin.set_fact | False |
| Nomad \| Cleanup temporary directory | ansible.builtin.file | False |
| Nomad \| Copy systemd service file for nomad | ansible.builtin.template | False |
| Nomad \| Set reload-check & restart-check variable | ansible.builtin.set_fact | True |

#### File: cni_install.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Get release for cni_plugins:{{ hashicorp_nomad_cni_plugins_version }} | vars | False |
| Nomad \| Check if cni plugin is already installed | ansible.builtin.stat | False |
| Nomad \| Check current cni plugin version | ansible.builtin.command | True |
| Nomad \| Set facts for wanted cni plugins release | ansible.builtin.set_fact | True |
| Nomad \| Set facts for current cni plugins release | ansible.builtin.set_fact | True |
| Nomad \| Create cni directory | ansible.builtin.file | False |
| Nomad \| Install cni plugins | block | True |
| Nomad \| Install cni plugins version:{{ hashicorp_nomad_cni_plugins_version }} | ansible.builtin.get_url | False |
| Nomad \| Unpack cni plugins | ansible.builtin.unarchive | False |
| Nomad \| Remove temporary archive | ansible.builtin.file | False |
| Nomad \| Update version file | ansible.builtin.copy | False |

#### File: prerequisites.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Create group {{ hashicorp_nomad_group }} | ansible.builtin.group | False |
| Nomad \| Create user {{ hashicorp_nomad_user }} | ansible.builtin.user | False |
| Nomad \| Create directory {{ hashicorp_nomad_config_dir }} | ansible.builtin.file | False |
| Nomad \| Create directory {{ hashicorp_nomad_data_dir }} | ansible.builtin.file | False |
| Nomad \| Create directory {{ hashicorp_nomad_certs_dir }} | ansible.builtin.file | False |
| Nomad \| Create directory {{ hashicorp_nomad_logs_dir }} | ansible.builtin.file | True |

#### File: configure.yml

| Name | Module | Has Conditions |
| ---- | ------ | --------- |
| Nomad \| Create nomad.env | ansible.builtin.template | False |
| Nomad \| Copy nomad.json template | ansible.builtin.template | False |
| Nomad \| Set restart-check variable | ansible.builtin.set_fact | True |
| Nomad \| Copy extra configuration files | block | True |
| Nomad \| Get extra file types | ansible.builtin.stat | False |
| Nomad \| Set list for file sources | vars | True |
| Nomad \| Set list for directory sources | vars | True |
| Nomad \| Template extra file sources | ansible.builtin.template | True |
| Nomad \| Template extra directory sources | ansible.builtin.include_tasks | True |







## Author Information
Bertrand Lanson

#### License

license (BSD, MIT)

#### Minimum Ansible Version

2.10

#### Platforms

- **Ubuntu**: ['focal', 'jammy', 'noble']
- **Debian**: ['bullseye', 'bookworm']

<!-- DOCSIBLE END -->
