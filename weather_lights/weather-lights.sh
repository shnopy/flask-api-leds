#!/bin/bash
. config

if [ `./sunset` ] && [ $HOUR -gt 15 ]
then
    if [ `./status` -eq 0 ]
    then
        echo `./onoff on`
    fi


    TEMP=`curl -s ${HOSTS[temp]}/sensor/$SENSOR |jq .value`
    if [ $TEMP -gt 15 ]
    then
        ./setCol ${WEATHER[vHot]}
    else
        if [ $TEMP -gt 10 ]
        then
            ./setCol ${WEATHER[normal]}
        else
            ./setCol ${WEATHER[vCold]}
        fi
    fi

else
    if [ `./status` -eq 1 ]
    then
        echo `./onoff`
    fi
fi




# LEDSTATUS=`./status`

# echo $TEMP
# echo $LEDSTATUS



