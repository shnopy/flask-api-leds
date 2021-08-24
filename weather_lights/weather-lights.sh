#!/bin/bash
. config



if [ `./sunset` -eq 1 ] && [ $HOUR -gt 15 ]
then
    echo `date`: hour is $HOUR sunset is `./sunset` -  going in...

    if [ `./status` -eq 0 ]
    then
        echo `./onoff on`
    fi


    TEMP=`curl -s ${HOSTS[temp]}/sensor/$SENSOR |jq .value`
    echo `date`: temperature is $TEMP
    if [ $TEMP -gt 20 ]
    then
        ./setCol ${WEATHER[vHot]}
    else
        if [ $TEMP -gt 10 ]
        then
            if [ $TEMP -gt 15 ]
            then
                ./setCol ${WEATHER[hot]}
            else
                ./setCol ${WEATHER[normal]}
            fi
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



