Linkding
=========

Install the podman container with [linkding](https://github.com/sissbruecker/linkding) instance that uses `postgres`

Requirements
------------

Podman

Role Variables
--------------
This are the defualts

```yml
# Name and password of the admin user
user_name: placeholder
user_password: password
# Name and password for db user
db_user : linkdin
db_password : passwd
# Container networking
host: localhost
container_port: 9090
```
Other varaibles

```yaml
container_name: linkding
env_vars:
  - { key: "LD_SUPERUSER_NAME", value: "{{ user_name }}" }
  - { key: "LD_SUPERUSER_PASSWORD", value: "{{ user_password }}" }
  - { key: "LD_DB_USER", value: "{{ db_user }}" }
  - { key: "LD_DB_PASSWORD", value: "{{ db_password }}" }
  - { key: "LD_DB_HOST", value: "{{ host }}" }
  - { key: "LD_HOST_PORT", value: "{{ container_port }}" }

```




Dependencies
------------
Podman

Example Playbook
----------------
```yaml

- name: Deploy Linkeding Application
  hosts: all
  become: false
  roles:
    - { role: linkding,
        user_name: "placeholder",
        user_password : "password",
        db_user: linkdin,
        db_password: "password" ,
        host: localhost,}

```

License
-------

BSD

Author Information
------------------
github.com/Dnfreddie 
