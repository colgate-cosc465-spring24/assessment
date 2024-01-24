#!/bin/bash

SCRIPTPATH=`readlink -f $0`
ASSESSDIR=`dirname $SCRIPTPATH`

REPODIR=$HOME/`ls $HOME | grep lab01-`
echo $REPODIR

# Link source code
echo Initializing...
ln -s $REPODIR/reference.py $ASSESSDIR/tests/reference.py
ln -s $REPODIR/terminology.py $ASSESSDIR/tests/terminology.py
ln -s $REPODIR/networking.json $ASSESSDIR/tests/networking.json
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
rm $ASSESSDIR/tests/reference.py $ASSESSDIR/tests/terminology.py $ASSESSDIR/tests/networking.json


exit $RETVAL
