#!/usr/bin/env bash
echo "Pocet argumentov: $#"
echo '$1'"==$1"

echo "Vsetky agumenty: $@"

for ARG in "$@"; do
	echo "$ARG"
done

