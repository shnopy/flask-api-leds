#!/bin/bash
. config

SUNSET=`./sunset 20`
if [ $SUNSET -eq -1 ]
then
    echo sunset error - skipping
fi

if [ $SUNSET -eq 1 ] && [ $HOUR -gt 15 ]
then
    echo `date`: hour is $HOUR sunset is $SUNSET -  going in...
    
    if [ `./status` -eq 0 ]
    then
        echo `./onoff on`
    fi
    
    
    TEMP=`curl -s ${HOSTS[temp]}/sensor/$SENSOR |jq .value`
    
    case $TEMP in
        2[0-9]) COL=vHot;;
        1[5-9]) COL=hot;;
        1[0-4]) COL=normal;;
        [5-9]) COL=cold;;
        *) COL=vCold;;
    esac;
    
    echo `date`: temperature is $TEMP setting to $COL
    ./setCol ${WEATHER[$COL]}
    
    
else
    if [ `./status` -eq 1 ]
    then
        echo `./onoff`
    fi
fi
