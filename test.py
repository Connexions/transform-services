# -*- coding: utf-8 -*-
# ###
# Copyright (c) 2013, Rice University
# This software is subject to the provisions of the GNU Affero General
# Public License version 3 (AGPLv3).
# See LICENCE.txt for details.
# ###
"""Script for stimulating the transformation service system components."""
import os
import argparse
import sqlite3
import requests


here = os.path.abspath(os.path.dirname(__file__))
DATABASE_FILE = os.path.join(here, '.{}.db'.format(__file__))


# Commands inject, watch, kill

def inject(args, db_connection):
    """Inject a job into the system"""
    payload = {
        'job-type': args.job_type,
        'content-url': args.url,
        }
    resp = requests.post(args.acmeio, data=payload)
    watch_url = resp.text
    # Grab the job id off the URL.
    job_id = watch_url.split('/')[-1]

    cursor = db_connection.cursor()
    cursor.execute("INSERT INTO jobs VALUES (?, ?)",
                   (job_id, watch_url))
    print(watch_url)
    cursor.close()


def _has_database(db_connection):
    """Check to see if the database has been initialized."""
    cursor = db_connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type=? AND name=?",
                   ('table', 'jobs'))
    result = cursor.fetchone()
    cursor.close()
    return result is not None


def _init_database(db_connection):
    """Initialize the database"""
    cursor = db_connection.cursor()
    cursor.execute("CREATE TABLE jobs (id SERIAL PRIMARY KEY NOT NULL, url TEXT NOT NULL)")
    db_connection.commit()
    cursor.close()

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

    db_connection = sqlite3.connect(DATABASE_FILE)
    if not _has_database(db_connection):
        _init_database(db_connection)

    args.func(args, db_connection)

    db_connection.commit()

    return 0

if __name__ == '__main__':
    main()
