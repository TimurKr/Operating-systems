#!/usr/bin/env bash

while read URL
do
    echo $URL
    curl -A Lynx -s $URL |
    tr -d '\n' | sed 's#<#\n<#g' |
    egrep -o "[-a-zA-Z1-9\.]+@([-a-zA-Z1-9]+\.)+[-a-zA-Z1-9]{2,4}"
done
