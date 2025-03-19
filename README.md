# **📖 Documentation**

## dnfreddie.sysops.collection

| Collection                                     | Usage                                                                                                              |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| [systemd_containers](roles/systemd_containers) | Install containers the systemd services using quadlet                                                              |
| [prometheus](roles/prometheus)                 | Installs and sets up Prometheus for monitoring.                                                                    |
| [node_exporter](roles/node_exporter)           | Installs and sets up Node Exporter for Prometheus.                                                                 |
| [auto_backup](roles/auto_backup/)            | Creates a user service to backup directories on target host and store them in a private repo on the remote machines |
| [loki](roles/loki)                             | Sets up Loki and Promtail via Podman.                                                                              |
| [virtualization](roles/virtualization)         | Installs Vagrant and libvirtd for vitalization.                                                                    |
| [desktop_env](roles/desktop_env)               | Manages home machines and environment (nix, tmux, nvim, vim, Xterm, i3).                                           |
| [control_center](roles/control_center)         | Installs and sets up an Nginx proxy, Guacamole, and Portainer.                                                     |

---

### **Custom Modules**

| Custom Module                               | Usage                                                          |
| ------------------------------------------- | -------------------------------------------------------------- |
| [git_tools](plugins/modules/git_tools)     | Creates repos if not existent and commits to it _(using gitpython)_ |
| [go_install](plugins/modules/go_install/) | Installs Go packages using `go install`.                       |

---
