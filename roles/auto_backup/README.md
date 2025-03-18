# Auto Backup Role

##  Description
This Ansible role automates **system backups** using systemd timers and rsync.
It ensures backups are performed  automatically.

Playthrough
###  **Task Overview: `auto_backup**

1. Ensure systemd directory exists
2. Deploy systemd timer & service files
3. Enable and start systemd timer
4. Ensure backup directory exists
5. Synchronize backup directories using rsync
6. Install GitPython for backup versioning
7. Create private repo and Commit backup changes to Git

##  Requirements
This role requires the following dependencies on the target system:
- `pip3` (for Python package management)
- `gitpython` (for managing Git repositories in backups)

Ensure they are installed before running the role.

---

##  Role Variables

You can customize the role using the following variables:

| Variable | Description | Default |
|----------|-------------|---------|
| `systemd_dir` | Path to store systemd service files | `"{{ lookup('env', 'HOME') }}/.config/systemd/user"` |
| `backup_dir` | Location where backups will be stored | `"{{ ansible_env.HOME }}/Documents/Backup"` |
| `service_templates` | List of systemd service & timer templates | `["ansible_backup.service", "ansible_backup.timer"]` |
| `to_backup` | Directories to include in the backup | `["Documents", ".dotfiles", "github.com"]` |
| `rsync_flags` | Exclude patterns for rsync | `["--exclude=.git", "--exclude=node_modules", "--exclude=venv", "--exclude=*.log"]` |

---
##  Dependencies

This role relies on:
- `pip3` for installing dependencies
- `gitpython` for managing Git commits within backups

To install dependencies manually:
```sh
pip3 install gitpython
```

---

##  Example Playbook
```yaml
- name: Run Auto Backup Role
  hosts: homelab
  gather_facts: false
  roles:
    - auto_backup
```
---

##  License
MIT


