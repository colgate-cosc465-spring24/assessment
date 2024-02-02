#!/bin/bash

SCRIPTPATH=`readlink -f $0`
BASEDIR=`dirname $SCRIPTPATH`
source $BASEDIR/common.sh

PORT=`shuf -i 2000-9999 -n 1`
$REPODIR/knock.py -p $PORT &
KPID=$!

sleep 1

NC1OUT=`mktemp`
echo -e "Knock, knock\nBoo\nDon't cry" | nc -v -q 1 -i 1 127.0.0.1 $PORT >$NC1OUT 2>&1 &

sleep 1

NC2OUT=`mktemp`
echo -e "Knock, knock\nSpell\nw-h-o" | nc -v -q 1 -i 1 127.0.0.1 $PORT >$NC2OUT 2>&1

kill -9 $KPID
cat $NC1OUT
cat $NC2OUT

cat $NC1OUT | grep "Boo who?"
if [ $? -ne 0 ]; then
    rm $NC1OUT
    rm $NC2OUT
    exit $TEST_FAIL
fi

cat $NC2OUT | grep "Spell who?"
if [ $? -ne 0 ]; then
    rm $NC1OUT
    rm $NC2OUT
    exit $TEST_FAIL
fi

rm $NC1OUT
rm $NC2OUT
exit $TEST_PASS