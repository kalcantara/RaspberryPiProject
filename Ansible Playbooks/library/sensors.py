#!/usr/bin/python

DOCUMENTATION = '''

---
module: Sensors
short_description: Check Hardware

'''

EXAMPLES = '''

---
- name: Check Hardware Usage
  Sensors:
    run: True

'''

try:
    import sensors
    import sys

def initSensor(module):
    sensors.init()
    if(module == 'true'):
        try:
            for chip in sensors.iter_detected_chips():
                print '%s at %s' % (chip, chip.adapter_name)
                for feature in chip:
                    print ' %s: %.2f' % (feature.label, feature.get_value())
        finally:
            sensors.cleanup()
    else:
        sys.exit("Parameter Wasn't True")

def main():
    module = AnsibleModule(
        argument_spec=dict(
            run=dict(required=True)
        )
    )
    initSensor(module.params.get('run'))

from ansible.module_utils.basic import *

if __name__ == '__main__':
    main()
