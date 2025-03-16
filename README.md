
## **📖 Documentation**
### **Different Ansible Roles for Different Occasions**
| Collection       | Usage                                                                                                      |
|-----------------|------------------------------------------------------------------------------------------------------------|
| [systemd_containers](roles/systemd_containers) | Install containersas the systemd services using quadlet |
| [prometheus](roles/prometheus) | Installs and sets up Prometheus for monitoring. |
| [node_exporter](roles/node_exporter) | Installs and sets up Node Exporter for Prometheus. |
| [loki](roles/loki) | Sets up Loki and Promtail via Podman. |
| [virtualization](roles/virtualization) | Installs Vagrant and libvirtd for virtualization. |
| [desktop_env](roles/desktop_env) | Manages home machines and environment (nix, tmux, nvim, vim, Xterm, i3). |
| [control_center](roles/control_center) | Installs and sets up an Nginx proxy, Guacamole, and Portainer. |

---

### **Custom Modules**
| Custom Module | Usage                                      |
|--------------|--------------------------------------------|
| [go_install](plugins/go_install/go_install.py) | Installs Go packages using `go install`. |

---

