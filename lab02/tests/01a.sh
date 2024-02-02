#!/bin/bash

SCRIPTPATH=`readlink -f $0`
BASEDIR=`dirname $SCRIPTPATH`
source $BASEDIR/common.sh

PORT=`shuf -i 2000-9999 -n 1`
$REPODIR/knock.py -p $PORT &
KPID=$!

sleep 1

SOCKETS=`netstat -nlp | grep "$KPID"`
kill -9 $KPID
echo "$SOCKETS"

echo "$SOCKETS" | grep $PORT > /dev/null
if [ $? -ne 0 ]; then
    exit $TEST_FAIL
fi

exit $TEST_PASS