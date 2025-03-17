prometheus
=========
Installs and setups prometheus as a service
To test run `molecule test`

Role Variables
--------------
By default it uses the latest release
```yaml

url: "https://api.github.com/repos/prometheus/prometheus/releases/latest"
config:
  file: "/etc/prometheus.yml"
  templ: prometheus.yml.j2
  service_templ: prometheus.service.j2

dir:
  install: "/opt/prometheus"
  data: "/opt/prometheus/data"
prom_port: 9090
# Only updates the binary to the latest realse and  restarts the serivce
update: false

```
Dependencies
------------

None

Example Playbook
----------------
With the default  configuration u have to run is as root 
```yaml
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

