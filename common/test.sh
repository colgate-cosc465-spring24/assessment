#!/bin/bash

ASSESSDIR=$1
REPODIR=$2

RUBRIC=$ASSESSDIR/tests.csv
TESTS_DIR=$ASSESSDIR/tests
TEST_PASS=0
TEST_FAIL=1
TEST_HALF=2
TEST_MANUAL=255
LOG="$ASSESSDIR/report.txt"

RED=$(tput setaf 1)
GREEN=$(tput setaf 2)
BLUE=$(tput setaf 3)
NORMAL=$(tput sgr0)
RED=""
GREEN=""
BLUE=""
NORMAL=""

function print_log_line() {
    LINE="==========================================================================="
    printf "=== %s %s\n" "$1" "${LINE:${#1}}" >> $LOG
}

SUBTOTAL=0
TOTAL=0
SUBPOSSIBLE=0
POSSIBLE=0

while read LINE; do
    LINE=`echo $LINE | tr -d '\r\n'`
    NAME=`echo $LINE | cut -d',' -f1`
    TEST=`echo $LINE | cut -d',' -f2`
    if [ -z $TEST ]; then 
        NAME=`echo $NAME | awk '{print toupper($0)}'`
        print_log_line "$NAME"
        echo >> $LOG
        continue
    elif [ $TEST == "C" ]; then
        NAME=`echo $NAME | awk '{print toupper($0)}'`
        print_log_line "$NAME"
        echo >> $LOG
        continue
    fi

    print_log_line "$NAME"

    if [ $TEST == "P" ]; then
        RESULT=$TEST_PASS
    elif [ $TEST == "M" ]; then
        RESULT=$TEST_MANUAL
    else
        TEST_SCRIPT=$TESTS_DIR/$TEST.sh
        if [ ! -f $TEST_SCRIPT ]; then
            TEST_SCRIPT=$TESTS_DIR/$TEST.py
            if [ ! -f $TEST_SCRIPT ]; then
                echo "Missing test: $TEST"
                exit 1
            fi
        fi

        $TEST_SCRIPT >> $LOG 2>&1
        RESULT=$?
    fi

    if [ $RESULT -eq $TEST_PASS ]; then
        print_log_line "PASS"
    elif [ $RESULT -eq $TEST_HALF ]; then
        print_log_line "PART"
    elif [ $RESULT -eq $TEST_MANUAL ]; then
        print_log_line "MANUAL"
    else
        print_log_line "MISS"
    fi
    echo >> $LOG
done < <(tail -n+2 $RUBRIC)

exit 0