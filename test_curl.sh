#!/bin/bash
x=1;
while [ $x -le 100000 ] ; do
    time curl 'http://127.0.0.1:8000/matches/current/'
    x=$[x + 1]
done