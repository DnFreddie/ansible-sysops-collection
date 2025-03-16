prometheus
=========

Installs and setups prometheus

Role Variables
--------------

The url to the offical prometheus release (*2.25.0*)
```yml
prometheus_url: "https://github.com/prometheus/prometheus/releases/download/v2.25.0/prometheus-2.25.0.linux-amd64.tar.gz"

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
     - { role: prometheus, prometheus_url: "url" }
```

License
-------

MIT

Author Information
------------------

DnFreddie

