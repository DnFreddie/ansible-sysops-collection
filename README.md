
## Diffrent ansible roles for different ansible occasions
| Collection| Usage                                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------|
|  [prometheus](/prometheus/README.md) | Installs and sets up grafana prometheus|
| [node_exporter](/roles/node_exporter/README.md) | Installs and sets up node_exporter for proemtheus|
| [loki](/roles/loki/README.md)  | Setsup loki and promail via podman|
| [desktop_env](/roles/desktop_env/README.md)  | Role that manages my home machines and environment. It provides all the tools that I use: nix, tmux, nvim, vim, Xterm, and i3. |
| [control_center](/control_center/README.md)  | Installs and setups nginx proxy,guacamole,portainer |
| [linkding](roels/linkding/README.md)  | Installs and setusps [linkding](https://github.com/sissbruecker/linkding)  trhough podman service|
| [virutalization](roles/virtualization/README.md)  | Installs vagrant and libvirtd|

-----------------------------------------

| Custom Module| Usage                                                                                                      |
|---------------|------------------------------------------------------------------------------------------------------------|
| [go_install](/lib/go_install.py) | Installs using `go isntall` |
