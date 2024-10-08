Role Name
=========

Setup my home enviaroment with i3,.bashrc ,tmux , xterm and couple other packages 

Requirements
------------

[My dotfiles repo](https://github.com/DnFreddie/.dotfiles.git)


Role Variables
--------------
Just to find the location of my repo and copy everything
```yaml
# Defautls
repo_url: "https://github.com/DnFreddie/.dotfiles.git"

# varaibles
home_dir: "{{ lookup('env', 'HOME') }}"
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
