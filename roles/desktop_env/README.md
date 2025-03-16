Role Name
=========

Setup my home enviaroment with i3,.bashrc ,tmux , xterm and couple other packages 

This playbook playbook install the **latest most stable verion of nvim**  the 
rest is beeing takend form the **your pacage manager**

[My dotfiles repo](https://github.com/DnFreddie/.dotfiles.git)

Requirements
------------
Defualt ansible modules


Example playbook
------------

```yaml
- name: install DefnotFreddie  dotfiles
  hosts: servers
  become: true
  roles:
    - desktop_env
```


Role Variables
--------------
```yaml
# Defautls
repo_url: "https://github.com/DnFreddie/.dotfiles.git"

# varaibles
home_dir: "/home/{{ ansible_hostname }}"
dot_config: "{{ home_dir }}/.config/"

repo_name:   "{{ repo_url.split('/')[-1].replace('.git', '') }}"
git_repo: "{{ home_dir }}/{{repo_name}}"

```

Dependencies
------------

None


License
-------

MIT

Author Information
------------------
DnFreddie
