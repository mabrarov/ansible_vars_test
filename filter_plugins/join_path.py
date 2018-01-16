# -*- coding: utf-8 -*-

import os.path

"""
This filter joins path and returns absolute path. If child is already absolute path then child is returned.
"""

def join_path(parent, child):
    return os.path.abspath(os.path.join(parent, child))

class FilterModule(object):
    def filters(self):
        return {
            'join_path': join_path
        }
