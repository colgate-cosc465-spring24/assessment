#!/bin/bash

# Determine path to scripts
SCRIPTPATH=`readlink -f $0`
BASEDIR=`dirname $SCRIPTPATH`
source $BASEDIR/common.sh

SIMULATOR=$BASEDIR/simulator.py
TOPO=`echo $0 | sed 's/sh$/json/'`
EXPECTOUT=`echo $0 | sed 's/sh$/out/'`
ACTUALOUT=/tmp/simulator.out

echo "Your simulator's output:"
$SIMULATOR $TOPO | tee $ACTUALOUT
echo ""
echo "Difference between expected output and your simulator's output:"
diff -U 1000 $EXPECTOUT $ACTUALOUT
