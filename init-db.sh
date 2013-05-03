#!/bin/bash

DB_NAME='pybit'
HERE=$(pwd -P)
PYBIT="$HERE/src/pybit"

psql $DB_NAME -c "\i $HERE/src/pybit/db/schema.sql"
psql $DB_NAME -c "\i $HERE/src/acmeio/sql_additions.sql"
psql $DB_NAME -c "\i $HERE/database/populate.sql"
