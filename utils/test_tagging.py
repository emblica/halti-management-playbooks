#!/usr/bin/env python
"""
Test if the UpCloud account has permissions for tagging.
"""
import os
import sys
import upcloud_api

manager = upcloud_api.CloudManager(os.environ.get('UPCLOUD_API_USER'), os.environ.get('UPCLOUD_API_PASSWD'))

try:
	t = manager.create_tag('test-tag-123')
	t.destroy()
	print('OK')
	sys.exit(0)
except Exception as e:
	print('FAIL', e)
	sys.exit(-1)