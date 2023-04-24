"""Role testing files using testinfra."""
import json

def test_hosts_file(host):
    """Validate /etc/hosts file."""
    etc_hosts = host.file("/etc/hosts")
    assert etc_hosts.exists
    assert etc_hosts.user == "root"
    assert etc_hosts.group == "root"

def test_nomad_user_group(host):
    """Validate nomad user and group."""
    nomad_group = host.group("nomad")
    nomad_user = host.user("nomad")
    assert nomad_group.exists
    assert nomad_user.exists
    assert nomad_user.group == "nomad"
    assert nomad_user.shell == "/bin/false"

def test_nomad_config(host):
    """Validate /etc/nomad.d/ files."""
    etc_nomad_d_nomad_env = host.file("/etc/nomad.d/nomad.env")
    etc_nomad_d_nomad_json = host.file("/etc/nomad.d/nomad.json")
    for file in etc_nomad_d_nomad_env, etc_nomad_d_nomad_json:
        assert file.exists
        assert file.user == "nomad"
        assert file.group == "nomad"
        assert file.mode == 0o600
        if file == etc_nomad_d_nomad_json:
            assert file.content_string != ""

def test_nomad_storage(host):
    """Validate /opt/nomad directory."""
    opt_nomad = host.file("/opt/nomad")
    assert opt_nomad.exists
    assert opt_nomad.is_directory
    assert opt_nomad.user == "nomad"
    assert opt_nomad.group =="nomad"
    assert opt_nomad.mode == 0o755

def test_nomad_service_file(host):
    """Validate nomad service file."""
    lib_systemd_system_nomad_service = host.file("/etc/systemd/system/nomad.service")
    assert lib_systemd_system_nomad_service.exists
    assert lib_systemd_system_nomad_service.user == "root"
    assert lib_systemd_system_nomad_service.group == "root"
    assert lib_systemd_system_nomad_service.mode == 0o644
    assert lib_systemd_system_nomad_service.content_string != ""

def test_nomad_service(host):
    """Validate nomad service."""
    nomad_service = host.service("nomad.service")
    assert nomad_service.is_enabled
    assert nomad_service.is_running
    assert nomad_service.systemd_properties["Restart"] == "on-failure"
    assert nomad_service.systemd_properties["User"] == "nomad"
    assert nomad_service.systemd_properties["Group"] == "nomad"
    assert nomad_service.systemd_properties["EnvironmentFiles"] == "/etc/nomad.d/nomad.env (ignore_errors=yes)"
    assert nomad_service.systemd_properties["FragmentPath"] == "/etc/systemd/system/nomad.service"

def test_nomad_interaction(host):
    """Validate interaction with nomad."""
    nomad_acl_bootstrap = json.loads(host.check_output("nomad acl bootstrap -json"))
    nomad_token = nomad_acl_bootstrap['SecretID']
    nomad_var_put = host.check_output("NOMAD_TOKEN=" + nomad_token + " nomad var put secret/foobar foo=bar")
    nomad_var_get = host.check_output("NOMAD_TOKEN=" + nomad_token + " nomad var get secret/foobar")
    nomad_var_delete = host.check_output("NOMAD_TOKEN=" + nomad_token + " nomad var purge secret/foobar")
    assert host.check_output("NOMAD_TOKEN=" + nomad_token + " nomad server members")
    assert '"Items": {\n    "foo": "bar"\n  }' in nomad_var_put
    assert '"Items": {\n    "foo": "bar"\n  }' in nomad_var_get
    assert nomad_var_delete == 'Successfully purged variable \"secret/foobar\"!'
