Loki
=========

A role to set up Loki and Promtail via Podman (*but could be easly switched to docker*).


Requirements
------------

This role only requires **Podman** but can be easily converted to Docker. Just literally swap `containers.podman.podman_container` with Docker.

Role Variables
--------------
```yml
config_files:
  - promtail.yml
  - local-config.yaml
```
Those names shouldnt be changed but u can easily tailor the contents (*they are located in files dir*)

Dependencies
------------
**None**

Example Playbook
----------------

```yml
- hosts: servers
  roles:
        - loki
```

License
-------
**MIT**

Author Information
------------------
DnFreddie
