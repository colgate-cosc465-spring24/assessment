#!/bin/bash

SCRIPTPATH=`readlink -f $0`
BASEDIR=`dirname $SCRIPTPATH`
source $BASEDIR/common.sh

PORT=`shuf -i 2000-9999 -n 1`
TMPFILE=`mktemp`
strace -f -e trace=socket,accept4 -D $REPODIR/knock.py -p $PORT >$TMPFILE 2>&1 &
KPID=$!

sleep 1

NC=`echo "" | nc -v 127.0.0.1 $PORT 2>&1`
kill -9 $KPID
echo "$NC"
cat $TMPFILE

SOCKET=`cat $TMPFILE | grep "socket" | head -n 1`
SERVERSOCK=`echo ${SOCKET: -1}`
echo "Server socket: $SERVERSOCK"

cat $TMPFILE | grep "accept4($SERVERSOCK,"
if [ $? -ne 0 ]; then
    rm $TMPFILE
    exit $TEST_FAIL
fi

rm $TMPFILE
exit $TEST_PASS