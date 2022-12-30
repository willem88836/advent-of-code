#!/bin/bash
readarray -d '' entries < <(printf '%s\0' ./* | sort -zV)
for f in "${entries[@]}"; do
    L=`expr length "$f"`
    if [ $L -lt 8 ]; then
        m=("${f[@]:2}")
        echo ">>>" $m
        python3 -m $m
        echo
    fi
done
