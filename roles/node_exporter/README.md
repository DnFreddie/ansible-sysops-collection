node_exporter
=========

Installs and setups node_exporter



Role Variables
--------------

The url to the offical node_exporter release (*the defualt version is 1.8.2*)
```yml
node_exporter_url: "https://github.com/prometheus/node_exporter/releases/download/v1.8.2/node_exporter-1.8.2.linux-amd64.tar.gz"

```
Dependencies
------------

None

Example Playbook
----------------

Including an example of how to use your role (for instance, with variables passed in as parameters) is always nice for users too:

```yml
- hosts: servers
  roles:
     - { role: node_exporterde, node_exporter_url: "url" }
```

License
-------

MIT

Author Information
------------------

DnFreddie
