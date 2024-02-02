#!/bin/bash

SCRIPTPATH=`readlink -f $0`
BASEDIR=`dirname $SCRIPTPATH`
source $BASEDIR/common.sh

PORT=`shuf -i 2000-9999 -n 1`
TMPFILE=`mktemp`
strace -f -e trace=accept4,sendto -D $REPODIR/knock.py -p $PORT >$TMPFILE 2>&1 &
KPID=$!

sleep 1

NC=`echo "Goodbye" | nc -v -q 1 127.0.0.1 $PORT 2>&1`
kill -9 $KPID
echo "$NC"
cat $TMPFILE

ACCEPT=`cat $TMPFILE | grep "accept4" | head -n 1`
CLIENTSOCK=`echo "${ACCEPT: -1}"`
echo "Client socket: $CLIENTSOCK"

SEND=`cat $TMPFILE | grep "sendto($CLIENTSOCK" | head -n 1`

echo "$SEND" | grep "I don't understand"
if [ $? -ne 0 ]; then
    rm $TMPFILE
    exit $TEST_FAIL
fi

rm $TMPFILE
exit $TEST_PASS