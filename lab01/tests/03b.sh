#!/bin/bash

SCRIPTPATH=`readlink -f $0`
BASEDIR=`dirname $SCRIPTPATH`
source $BASEDIR/common.sh

TMPFILE=`mktemp`
cd $REPODIR
python3 reference.py -k network > $TMPFILE 2>&1

diff $TMPFILE $BASEDIR/03b.txt
if [ $? -ne 0 ]; then
    echo "Unexpected output"
    rm $TMPFILE
    exit $TEST_FAIL
fi

rm $TMPFILE
exit $TEST_PASS