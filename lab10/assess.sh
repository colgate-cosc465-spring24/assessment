#!/bin/bash

SCRIPTPATH=`readlink -f $0`
ASSESSDIR=`dirname $SCRIPTPATH`

REPODIR=$HOME/`ls $HOME | grep lab10-`
echo $REPODIR

# Link source code
echo Initializing...
ln -s $REPODIR/sliding_window.py $ASSESSDIR/tests/sliding_window.py
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
rm $ASSESSDIR/tests/sliding_window.py

exit $RETVAL