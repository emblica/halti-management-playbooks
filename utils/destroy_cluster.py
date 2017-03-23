#!/usr/bin/env python
"""
Destroy the Halti cluster based on 'haltimaster' and 'haltinode' tags.
This script is for development purposes and only works against UpCloud's API.
"""
import os
import sys
import upcloud_api
import multiprocessing

manager = upcloud_api.CloudManager(os.environ.get('UPCLOUD_API_USER'), os.environ.get('UPCLOUD_API_PASSWD'))

def destroy(server):
	"""Destroy a server and it's storates."""
	print('destroying: {} ({})'.format(server.hostname, server.title))
	server.stop_and_destroy()


def destroy_cluster():
	"""halt and catch fire, in parallel."""
	print('servers: {}'.format(servers_str or '<nothing>'))
	pool = multiprocessing.Pool()
	pool.map(destroy, servers)


servers = manager.get_servers(tags_has_one=['haltimaster', 'haltinode'])
servers_str = ', '.join([s.hostname for s in servers])


# for automation purposes, just do it
if len(sys.argv) > 1 and sys.argv[1] == '--no-input-danger':	
	destroy_cluster()
	sys.exit(0)


# for humans
yes = raw_input('WARNING! About to destroy the following servers: {}. Type "yes" to continue: '.format(servers_str))
if yes != 'yes':
	print('confirmation failed, exit...')
	sys.exit(0)
else:
	print('confirmation successful...')
	destroy_cluster()
	sys.exit(0)

