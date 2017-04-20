#!/usr/bin/python

import argparse
parser = argparse.ArgumentParser(description='Promote artifact')
parser.add_argument("--unit", dest="unit", default="web", required=True)
parser.add_argument("--product", dest="product", required=True)
parser.add_argument("--subproduct", dest="subproduct", required=True)
parser.add_argument("--from", dest="from_env", default="dev", required=True)
parser.add_argument("--to", dest="to_env", default="test", required=True)
parser.add_argument("--version", dest="vers", required=True)
parser.add_argument("--type", dest="dep_type", default="deployment", required=False)
args = parser.parse_args()
event = {
    "actions": [
        {
            "action": "promote_release",
            "unit": args.unit,
            "product": args.product,
            "subproduct": args.subproduct,
            "from_env": args.from_env,
            "to_env": args.to_env,
            "version": args.vers,
            "dep_type": args.dep_type,
        }
    ]
}
print event
'''
Usage: 
$ python example.py
usage: example.py [-h] --unit UNIT --product PRODUCT --subproduct SUBPRODUCT
                  --from FROM_ENV --to TO_ENV --version VERS [--type DEP_TYPE]
example.py: error: argument --unit is required
msp-jole:~/sandbox/operation-automation-framework/functions/recent-chgmgmt-service [master % u= fcfadf7]
$ python example.py --unit sysops --product monitoring --subproduct logicmonitor --from dev --to test --version 0.0.1
{'actions': [{'subproduct': 'logicmonitor', 'product': 'monitoring', 'version': '0.0.1', 'dep_type': 'deployment', 'to_env': 'test', 'action': 'promote_release', 'from_env': 'dev', 'unit': 'sysops'}]}
'''
