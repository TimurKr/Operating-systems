#!/usr/bin/env bash

curl -s https://www.bing.com/search?q="$( tr ' ' '+' <<< "$@" )" |
tr -d '\n' | sed 's#<li>#\n<li>#g' | sed 's#</li>#</li>\n#g' |
grep --color=auto '^<li class=\"b_algo\">' | 
sed 's#.*<a href=\"\([^"]*\)\(.*\)#\1#g' | sort | uniq