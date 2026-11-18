#!/usr/bin/python

# Copyright: (c) 2018, Terry Jones <terry.jones@example.org>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_own_module

short_description: Creates a text file with the given content on the remote host

version_added: "1.0.0"

description:
    - Creates a text file at the given path with the given content.
    - If the file already exists with the same content, nothing is changed.
    - If the content differs, the file is rewritten.

options:
    path:
        description: Full path of the file to create on the remote host.
        required: true
        type: str
    content:
        description: Text to write into the file.
        required: true
        type: str

author:
    - DaneenaL (@DaneenaL)
'''

EXAMPLES = r'''
- name: Create a file
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/hello.txt
    content: "hello world"

- name: Rewrite it with new content
  my_own_namespace.yandex_cloud_elk.my_own_module:
    path: /tmp/hello.txt
    content: "new text"
'''

RETURN = r'''
path:
    description: The path of the file the module worked with.
    type: str
    returned: always
    sample: /tmp/hello.txt
message:
    description: What the module did (created, updated or already up to date).
    type: str
    returned: always
    sample: created
'''

import io
import os

from ansible.module_utils.basic import AnsibleModule


def read_current(path):
    """Return current file content or None if the file does not exist."""
    if not os.path.isfile(path):
        return None
    with io.open(path, 'r', encoding='utf-8') as f:
        return f.read()


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True)
    )
    result = dict(changed=False, path='', message='')
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)

    path = module.params['path']
    content = module.params['content']
    result['path'] = path

    if os.path.isdir(path):
        module.fail_json(msg='path is a directory: %s' % path, **result)
    parent = os.path.dirname(path) or '.'
    if not os.path.isdir(parent):
        module.fail_json(msg='directory does not exist: %s' % parent, **result)

    current = read_current(path)
    if current is None:
        result['changed'] = True
        result['message'] = 'created'
    elif current != content:
        result['changed'] = True
        result['message'] = 'updated'
    else:
        result['message'] = 'already up to date'

    if result['changed'] and not module.check_mode:
        try:
            with io.open(path, 'w', encoding='utf-8') as f:
                f.write(content)
        except (IOError, OSError) as e:
            module.fail_json(msg='cannot write %s: %s' % (path, e), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
