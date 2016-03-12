#!/bin/bash
x=1;
while [ $x -le 100000 ] ; do
    echo "Running - $x"
    time curl 'http://df.hern.as/matches/current/'
    x=$[x + 1]
done