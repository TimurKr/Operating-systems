#!/usr/bin/env bash
for X in $(seq 10)
do
	for Y in $(seq 10)
	do
		printf "%2s * %2s = %2s\n" $X $Y $(echo "$X*$Y" | bc)
	done
done
