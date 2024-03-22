#!/bin/bash

SCRIPTPATH=`readlink -f $0`
ASSESSDIR=`dirname $SCRIPTPATH`

REPODIR=$HOME/`ls $HOME | grep lab07-`
echo $REPODIR

# Link source code
echo Initializing...
ln -s $REPODIR/simulator.py $ASSESSDIR/tests/simulator.py
rm -f $ASSESSDIR/report.txt

# Run tests
echo Testing...
$ASSESSDIR/../common/test.sh $ASSESSDIR $REPODIR 
RETVAL=$?
if [ $RETVAL -ne 0 ]; then
    echo "Failed to run tests"
fi

# Clean-up
echo Cleaning...
cd $ASSESSDIR
rm $ASSESSDIR/tests/simulator.py

exit $RETVAL