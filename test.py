# -*- coding: utf-8 -*-
# ###
# Copyright (c) 2013, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
"""Script for stimulating the transformation service system components."""
import argparse
import requests


# Commands inject, watch, kill

def inject(args):
    """Inject a job into the system"""
    payload = {
        'job-type': args.job_type,
        'content-url': args.url,
        }
    resp = requests.post(args.acmeio, data=payload)
    watch_url = resp.text
    print(watch_url)

def main(argv=None):
    """Main commandline interface"""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--acmeio', default="http://localhost:6543",
                        help="URL where the 'acmeio' instance can be found")
    subparsers = parser.add_subparsers()
    inject_parser = subparsers.add_parser('inject')
    inject_parser.add_argument('job_type')
    inject_parser.add_argument('url')
    inject_parser.set_defaults(func=inject)
    args = parser.parse_args(argv)

    args.func(args)

    return 0

if __name__ == '__main__':
    main()
