## v1.0.0 (2024-07-17)

### Feat

- ename tasks, add docsible readme
- rework variables to integrate better with ednz_cloud.hashistack collection while still being usable on its own

## v0.4.1 (2024-07-12)

### Fix

- check if nomad service is not in a failed state to trigger restart if needed

## v0.4.0 (2024-06-19)

### Feat

- add noble to list of supported distro

### Fix

- remove unecessary and deprecated code, cleanup documentation

## v0.3.0 (2024-06-18)

### Feat

- **tests**: add binary check to ensure nomad is installed correctly
- add more precise restart checks and force restart at the end of the role instead of relying on handlers

### Fix

- add task to enable service when install and configuration is complete

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
