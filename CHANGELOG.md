## v0.2.0 (2024-06-16)

### Feat

- change installation method from package manager to direct archive download from hcp release servers
- rename some cni related variables, prepare variables for new installation method
- add enhanced extra files options, allowing to recursively copy template files into different directories
- remove auto-update option

### Fix

- cni plugin install idempotence on creating directories

## v0.1.0 (2024-05-15)

### Feat

- rename variables to conform with var-naming convention of ansible-lint, fix #3
- **core**: change namespace
- remove become from role
- add vagrant tests, add become:true, fix #1
