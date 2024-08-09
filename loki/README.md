Loki
=========

A role to set up Loki and Promtail via Podman (*but could be easly switched to docker*).


Requirements
------------


This role only requires Podman, but it can be easily converted to Docker. To do this, simply replace `containers.podman.podman_container` with the equivalent Docker module.

Additionally, I changed the context of the files to `container_file_t`, which allows SELinux to permit these files to be used as volumes.


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
