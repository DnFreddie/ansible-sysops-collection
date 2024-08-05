Role Name
=========

Setup my home enviaroment with i3,.bashrc ,tmux , xterm and couple other pacages 

Requirements
------------

[My dotfiles repo](https://github.com/DnFreddie/nixdotfiles.git)


Role Variables
--------------
Just to find the location of my repo and copy everything
```yaml
user_home: "/home/{{ inventory_hostname }}"
git_repo: "{{ user_home }}/Desktop/nixconfig"
dotfiles: "{{ git_repo }}/dotfiles"
config_dest: "{{ user_home }}/.config/"

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
