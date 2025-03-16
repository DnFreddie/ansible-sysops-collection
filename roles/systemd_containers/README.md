systemd_containers
=========
Run exisitg podman images as systemd user serivces 
with quadlet

Requirements
------------
podman >= 4.4


Role Variables
--------------
```yaml
# Should the user  linger
linger: false
# Base directory for container configuration
container_dir: Containers  # ~/Containers
# This is an array of the containers u want to create 
containers:
  - name: linkding
    env_file: "env.j2"  # Jinja2 template for environment variables
    image: docker.io/sissbruecker/linkding:latest
    ports:
      - host: "9090"
        container: "9090"
    volumes:
      - host: "data"
        container: "/app/data"

# For local usage the image has to be already build
  - name: mkdocs
    image: localhost/notes_mkdocs
    ports:
      - host: "8000"
        container: "8000"
    volumes:
      - host: "/home/aura/github.com/DnFreddie/Notes/mkdocs.yml"
        container: "/app/mkdocs.yml"
        create: false
      - host: "/home/aura/github.com/DnFreddie/Notes/content/"
        container: "/app/docs"
        create: false
    exec: serve --dev-addr=0.0.0.0:8000
```



License
-------
MIT

Author Information
------------------
github.com/Dnfreddie 
