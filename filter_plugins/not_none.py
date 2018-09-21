# -*- coding: utf-8 -*-

from ansible import errors

"""
This filter vlidates that provided value is not None.
"""

def not_none(a):
    if a is None:
        raise errors.AnsibleFilterError('Mandatory variable is None.')
    return a

class FilterModule(object):
    def filters(self):
        return {
            'not_none': not_none
        }
