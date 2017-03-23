.PHONY: inventory

make inventory:
	./upcloud-ansible/inventory/upcloud.py | jq .
