#!/usr/bin/env bash

source env/bin/activate

INDENT="--indent 2"
FIXTURES_PATH=FPD/fixtures

mkdir -p ${FIXTURES_PATH}

function dump () {
    echo "Dumping \"$1\" to \"${FIXTURES_PATH}/$2.json\"..."
    python manage.py dumpdata $1 ${INDENT} > ${FIXTURES_PATH}/$2.json
}

if [ "$1" != "" ] && [ "$2" != "" ]; then
    dump $1 $2
else
    dump api.info infos
fi