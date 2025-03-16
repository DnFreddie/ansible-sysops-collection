prometheus
=========
Installs and setups prometheus as a service
To test run `molecule test`

Role Variables
--------------
By default it uses the latest release
```yaml
prom_url: "https://api.github.com/repos/prometheus/prometheus/releases/latest"
prom_config: "/etc/prometheus.yml"
prom_dir: "/opt/prometheus"
prom_port: 9090
prom_data: "/opt/prometheus/data"
```
Dependencies
------------

None

Example Playbook
----------------
With the current configuration u have to run is as root 
```yml
- hosts: servers
  become: true
  roles:
     -  role: prometheus
```

License
-------

MIT

Author Information
------------------

DnFreddie

