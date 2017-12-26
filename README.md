# Test of Ansible vars 

Test of Ansible vars which are calculated based on `group_vars`, `host_vars` and role default vars.

# Pre-requisites and assumptions

1. Docker Engine is installed and running.
1. Docker client is installed and configured to communicate with Docker Engine.
1. Repository is cloned into `/home/user/ansible_vars_test` directory on Docker host.

# Running on staging Ansible inventory

```bash
$ docker run --rm -w /etc/ansible -v /home/user/ansible_vars_test:/etc/ansible williamyeh/ansible:alpine3 ansible-playbook printer.yml -i inventories/staging/hosts
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

# Running on production Ansible inventory

## Running on canary servers

```bash
$ docker run --rm -w /etc/ansible -v /home/user/ansible_vars_test:/etc/ansible williamyeh/ansible:alpine3 ansible-playbook printer.yml -i inventories/production/hosts --limit canary
```

produces:

```
PLAY [all] *********************************************************************

TASK [printer : print] *********************************************************
ok: [jumper] => {
    "msg": "var_def is taken from 'printer' role defaults"
}

TASK [printer : print] *********************************************************
ok: [jumper] => {
    "msg": "var_def is taken from 'printer' role defaults"
}

TASK [printer : print] *********************************************************
ok: [jumper] => {
    "msg": "var_def is taken from 'printer' playbook"
}

TASK [printer : print] *********************************************************
ok: [jumper] => {
    "msg": "var_host is taken from 'production' inventory, 'jumper' host"
}

TASK [printer : print] *********************************************************
ok: [jumper] => {
    "msg": "var_all is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [jumper] => {
    "msg": "var_1 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [jumper] => {
    "msg": "var_2 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [jumper] => {
    "msg": "var_3 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [jumper] => {
    "msg": "var_3_1 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [jumper] => {
    "msg": "var_3_2 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [jumper] => {
    "msg": "var_3_z is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [jumper] => {
    "msg": "var_4 is taken from 'production' inventory, 'all' group"
}

PLAY RECAP *********************************************************************
jumper                     : ok=12   changed=0    unreachable=0    failed=0
```

## Running on non canary servers

```bash
$ docker run --rm -w /etc/ansible -v /home/user/ansible_vars_test:/etc/ansible williamyeh/ansible:alpine3 ansible-playbook printer.yml -i inventories/production/hosts --limit non_canary
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

## Running on all servers

```bash
$ docker run --rm -w /etc/ansible -v /home/user/ansible_vars_test:/etc/ansible williamyeh/ansible:alpine3 ansible-playbook printer.yml -i inventories/production/hosts
```
produces:

```
PLAY [all] *********************************************************************

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_def is taken from 'printer' role defaults"
}
ok: [jumper] => {
    "msg": "var_def is taken from 'printer' role defaults"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_def is taken from 'printer' role defaults"
}
ok: [jumper] => {
    "msg": "var_def is taken from 'printer' role defaults"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_def is taken from 'printer' playbook"
}
ok: [jumper] => {
    "msg": "var_def is taken from 'printer' playbook"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_host is taken from 'production' inventory, 'localhost' host"
}
ok: [jumper] => {
    "msg": "var_host is taken from 'production' inventory, 'jumper' host"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_all is taken from 'production' inventory, 'all' group"
}
ok: [jumper] => {
    "msg": "var_all is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_1 is taken from 'production' inventory, 'group_1' group"
}
ok: [jumper] => {
    "msg": "var_1 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_2 is taken from 'production' inventory, 'group_2' group"
}
ok: [jumper] => {
    "msg": "var_2 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3 is taken from 'production' inventory, 'group_3' group"
}
ok: [jumper] => {
    "msg": "var_3 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3_1 is taken from 'production' inventory, 'group_3_1' group"
}
ok: [jumper] => {
    "msg": "var_3_1 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3_2 is taken from 'production' inventory, 'group_3_2' group"
}
ok: [jumper] => {
    "msg": "var_3_2 is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_3_z is taken from 'production' inventory, 'group_3_z' group"
}
ok: [jumper] => {
    "msg": "var_3_z is taken from 'production' inventory, 'all' group"
}

TASK [printer : print] *********************************************************
ok: [localhost] => {
    "msg": "var_4 is taken from playbook, 'group_4' group"
}
ok: [jumper] => {
    "msg": "var_4 is taken from 'production' inventory, 'all' group"
}

PLAY RECAP *********************************************************************
jumper                     : ok=12   changed=0    unreachable=0    failed=0
localhost                  : ok=12   changed=0    unreachable=0    failed=0
```