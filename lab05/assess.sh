#!/bin/bash

SCRIPTPATH=`readlink -f $0`
ASSESSDIR=`dirname $SCRIPTPATH`

REPODIR=$HOME/`ls $HOME | grep lab05-`
echo $REPODIR

# Link source code
echo Initializing...
ln -s $REPODIR/ipsubnet.py $ASSESSDIR/tests/ipsubnet.py
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
rm $ASSESSDIR/tests/ipsubnet.py

exit $RETVAL