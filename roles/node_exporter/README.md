node_exporter
=========
Installs and setups node_exporter as a service
To test run `molecule test`

Role Variables
--------------
By default it uses the latest release
```yaml
url: "https://api.github.com/repos/prometheus/node_exporter/releases/latest
"
config: 
  file: "/etc/sysconfig/node_exporter"
  templ: "node_exporter.j2"
  service_templ: "node_exporter.service.j2"
dir: 
  install: "/opt/node_exporter"
  data: "/var/lib/node_exporter/textfile_collector"
node_port: 9100
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
     -  role: node_exporter
```

License
-------

MIT

Author Information
------------------

DnFreddie


