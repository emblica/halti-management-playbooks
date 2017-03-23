# halti-management-playbooks

Provision and install a small Halti cluster on UpCloud.

### Dependencies

* python2 (because ansible)
* install dependencies

```
pip install ansible

# if using upcloud for inventory / provisioning servers
pip install upcloud_api
```

* check that `upcloud-ansible` submodule is loaded


### Running

* provision servers and install Halti cluster

```
export UPCLOUD_API_USER=user
export UPCLOUD_API_PASSWD=pass
ansible-playbook -i ./upcloud-ansible/inventory/upcloud.py -M ./upcloud-ansible/modules/ site.yml
```

* install Halti against existing servers

```
ansible-playbook -i hosts site.yml --tags install
```

### Notes

* `ansible_eth1` is assumed to be the private IP of the machine
	* edit halti-nodes.yml if this is not the case
* Halti master will run at port 4040 by default
* `utils/test_tagging.py` is used by `halti-servers` to ensure the user has tagging permissions
* `utils/destroy_cluster.py` can be used to clean up (main usecase is integration testing)
