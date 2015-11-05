#!/bin/sh

COUNTER=0
a='featuredGame'
b='.txt'

while [ true ]
do
    let COUNTER=COUNTER+1
    c=$a$COUNTER$b
    curl https://na.api.pvp.net/observer-mode/rest/featured?api_key=346b0da8-c4ca-4033-84a3-698b0bf0793f >> $c
    sleep 3600
done

