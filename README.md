# Test of Ansible vars 

[![License](https://img.shields.io/badge/license-Apache%202.0-brightgreen.svg)](LICENSE)

Test of Ansible vars which are calculated based on `group_vars`, `host_vars` and role default vars.

# Pre-requisites and assumptions

1. Docker Engine is installed and running.
1. Docker client is installed and configured to communicate with Docker Engine.
1. Current directory is directory on Docker host where this repository is cloned into `$(pwd)` directory on Docker host.

# Ansible vars inheritance and overriding

Below example demonstrates standard inheritance and overriding of Ansible vars provided by Ansible out of the box.

Running printer playbook on staging environment:

```bash
$ docker run --rm -w /ansible -v $(pwd):/ansible abrarov/ansible ansible-playbook printer.yml -i inventories/staging/hosts
```

produces:

```
PLAY [all] *********************************************************************

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_def is taken from 'printer' role defaults"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_def is taken from 'printer' role defaults"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_def is taken from 'printer' playbook"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_host is taken from 'staging' inventory, 'localhost' host"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_all is taken from 'staging' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_1 is taken from 'staging' inventory, 'group_1' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_2 is taken from 'staging' inventory, 'group_2' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3 is taken from 'staging' inventory, 'group_3' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3_1 is taken from 'staging' inventory, 'group_3_1' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3_2 is taken from 'staging' inventory, 'group_3_2' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3_z is taken from 'staging' inventory, 'group_3_z' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_4 is taken from playbook, 'group_4' group"
}

PLAY RECAP *********************************************************************
localhost                  : ok=12   changed=0    unreachable=0    failed=0
```

# Dealing with multiple instances of the same application on one host

Below example demonstrates how to make your Ansible inventory to store configuration (Ansible vars) per application instance and not per host, i.e. it shows how to apply the same role (with different parameters) to the same target host and to keep all your Ansible vars in Ansible inventory and not in playbook.

Running printer playbook on canary production hosts:

```bash
$ docker run --rm -w /ansible -v $(pwd):/ansible abrarov/ansible ansible-playbook printer.yml -i inventories/production/hosts --limit canary
```

produces:

```
PLAY [all] *********************************************************************

TASK [printer : print] *********************************************************
ok: [localhost_canary] => {
    "msg": "var_def is taken from 'printer' role defaults"
}

TASK [printer : print] *********************************************************
ok: [localhost_canary] => {
    "msg": "var_def is taken from 'printer' role defaults"
}

TASK [printer : print] *********************************************************
ok: [localhost_canary] => {
    "msg": "var_def is taken from 'printer' playbook"
}

TASK [printer : print] *********************************************************
ok: [localhost_canary] => {
    "msg": "var_host is taken from 'production' inventory, 'localhost_canary' host"
}

TASK [printer : print] *********************************************************
ok: [localhost_canary] => {
    "msg": "var_all is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost_canary] => {
    "msg": "var_1 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost_canary] => {
    "msg": "var_2 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost_canary] => {
    "msg": "var_3 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost_canary] => {
    "msg": "var_3_1 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost_canary] => {
    "msg": "var_3_2 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost_canary] => {
    "msg": "var_3_z is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost_canary] => {
    "msg": "var_4 is taken from 'production' inventory, 'all' group"
}

PLAY RECAP *********************************************************************
localhost_canary           : ok=12   changed=0    unreachable=0    failed=0
```

Running printer playbook on non canary production hosts:

```bash
$ docker run --rm -w /ansible -v $(pwd):/ansible abrarov/ansible ansible-playbook printer.yml -i inventories/production/hosts --limit non_canary
```

produces:

```
PLAY [all] *********************************************************************

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_def is taken from 'printer' role defaults"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_def is taken from 'printer' role defaults"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_def is taken from 'printer' playbook"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_host is taken from 'production' inventory, 'localhost' host"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_all is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_1 is taken from 'production' inventory, 'group_1' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_2 is taken from 'production' inventory, 'group_2' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3 is taken from 'production' inventory, 'group_3' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3_1 is taken from 'production' inventory, 'group_3_1' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3_2 is taken from 'production' inventory, 'group_3_2' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3_z is taken from 'production' inventory, 'group_3_z' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_4 is taken from playbook, 'group_4' group"
}

PLAY RECAP *********************************************************************
localhost                  : ok=12   changed=0    unreachable=0    failed=0
```

Running printer playbook on all production hosts:

```bash
$ docker run --rm -w /ansible -v $(pwd):/ansible abrarov/ansible ansible-playbook printer.yml -i inventories/production/hosts
```

produces:

```
PLAY [all] *********************************************************************

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_def is taken from 'printer' role defaults"
}
ok: [localhost_canary] => {
    "msg": "var_def is taken from 'printer' role defaults"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_def is taken from 'printer' role defaults"
}
ok: [localhost_canary] => {
    "msg": "var_def is taken from 'printer' role defaults"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_def is taken from 'printer' playbook"
}
ok: [localhost_canary] => {
    "msg": "var_def is taken from 'printer' playbook"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_host is taken from 'production' inventory, 'localhost' host"
}
ok: [localhost_canary] => {
    "msg": "var_host is taken from 'production' inventory, 'localhost_canary' host"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_all is taken from 'production' inventory, 'all' group"
}
ok: [localhost_canary] => {
    "msg": "var_all is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_1 is taken from 'production' inventory, 'group_1' group"
}
ok: [localhost_canary] => {
    "msg": "var_1 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_2 is taken from 'production' inventory, 'group_2' group"
}
ok: [localhost_canary] => {
    "msg": "var_2 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3 is taken from 'production' inventory, 'group_3' group"
}
ok: [localhost_canary] => {
    "msg": "var_3 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3_1 is taken from 'production' inventory, 'group_3_1' group"
}
ok: [localhost_canary] => {
    "msg": "var_3_1 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3_2 is taken from 'production' inventory, 'group_3_2' group"
}
ok: [localhost_canary] => {
    "msg": "var_3_2 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3_z is taken from 'production' inventory, 'group_3_z' group"
}
ok: [localhost_canary] => {
    "msg": "var_3_z is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_4 is taken from playbook, 'group_4' group"
}
ok: [localhost_canary] => {
    "msg": "var_4 is taken from 'production' inventory, 'all' group"
}

PLAY RECAP *********************************************************************
localhost                  : ok=12   changed=0    unreachable=0    failed=0
localhost_canary           : ok=12   changed=0    unreachable=0    failed=0
```

# Dealing with configuration files

Below examples demonstrates how to deal with environment (inventory, group, host) specific files which content can not be stored in Ansible var (like binary key store or large files).

Running file_printer playbook on staging environment:

```bash
$ docker run --rm -w /ansible -v $(pwd):/ansible abrarov/ansible ansible-playbook file_printer.yml -i inventories/staging/hosts
```

produces:

```
PLAY [all] *********************************************************************

TASK [file_printer : debug] ****************************************************
ok: [localhost] => {
    "msg": [
        "reading from: group_files/all/message.txt",
        "full path is: /ansible/inventories/staging/group_files/all/message.txt"
    ]
}

TASK [file_printer : read file] ************************************************
ok: [localhost]

TASK [file_printer : print file] ***********************************************
ok: [localhost] => {
    "msg": [
        "message file is taken from 'staging' inventory, 'all' group"
    ]
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0

```

Running file_printer playbook on production environment:

```bash
$ docker run --rm -w /ansible -v $(pwd):/ansible abrarov/ansible ansible-playbook file_printer.yml -i inventories/production/hosts
```

produces:

```
PLAY [all] *********************************************************************

TASK [file_printer : debug] ****************************************************
ok: [localhost] => {
    "msg": [
        "reading from: /etc/hosts",
        "full path is: /etc/hosts"
    ]
}

TASK [file_printer : read file] ************************************************
ok: [localhost]

TASK [file_printer : print file] ***********************************************
ok: [localhost] => {
    "msg": [
        "127.0.0.1\tlocalhost\n::1\tlocalhost ip6-localhost ip6-loopback\nfe00::0\tip6-localnet\nff00::0\tip6-mcastprefix\nff02::1\tip6-allnodes\nff02::2\tip6-allrouters\n172.17.0.2\t3c9c03458b02"
    ]
}

PLAY [all] *********************************************************************

TASK [file_printer : debug] ****************************************************
ok: [localhost_canary] => {
    "msg": [
        "reading from: host_files/localhost_canary/message.txt",
        "full path is: /ansible/inventories/production/host_files/localhost_canary/message.txt"
    ]
}

TASK [file_printer : read file] ************************************************
ok: [localhost_canary]

TASK [file_printer : print file] ***********************************************
ok: [localhost_canary] => {
    "msg": [
        "message file is taken from 'production' inventory, 'localhost_canary' host"
    ]
}

PLAY RECAP *********************************************************************
localhost                  : ok=3    changed=0    unreachable=0    failed=0
localhost_canary           : ok=3    changed=0    unreachable=0    failed=0
```