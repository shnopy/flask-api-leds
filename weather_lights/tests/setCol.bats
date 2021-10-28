#!/usr/local/bin/env bats 

setup() {
  load 'test_helper/common-setup'
  _common_setup
}


teardown() {
  run onoff
}



@test "setCol: setting when lights off" {
  run onoff
  run bash -c 'setCol 10,0,0 | jq -r .response'
  [ "$output" = "LEDs are not currently on or an invalid RGB value was provided!" ]
}

@test "setCol: setting when lights on" {
  run onoff on
  run bash -c 'setCol 10,11,12 | jq -r .response'
  red=`echo $output |jq .red`
  green=`echo $output |jq .green`
  blue=`echo $output |jq .blue`
  [ "$red" -eq 10 ]
  [ "$green" -eq 11 ]
  [ "$blue" -eq 12 ]
}

@test "setCol: no params" {
  run onoff
  run bash -c 'setCol  | jq -r .response'
  [ "$output" = "LEDs are not currently on or an invalid RGB value was provided!" ]
}

@test "setCol: invalid params" {
  run onoff
  run bash -c 'setCol invalid | jq -r .response'
  [ "$output" = "LEDs are not currently on or an invalid RGB value was provided!" ]
}