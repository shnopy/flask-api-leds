#!/usr/local/bin/env bats 

setup() {
  load 'test_helper/common-setup'
  _common_setup

  run onoff
}


teardown() {
  run onoff
}



@test "onoff_and_status 1: turn off while off" {
  run onoff
  assert_output 'LEDs off'
  run status
  assert_output '0'
  [ "$status" -eq 0 ]
}

@test "onoff_and_status 2: turn on while off" {
  run onoff on
  assert_output 'LEDs on'
  run status
  assert_output '1'
  [ "$status" -eq 1 ]
}

@test "onoff_and_status 3: turn on while on" {
  onoff on
  run onoff on
  assert_output 'LEDs on'
  run status
  assert_output '1'
  [ "$status" -eq 1 ]
}

@test "onoff_and_status 4: turn off while on" {
  run onoff 
  assert_output 'LEDs off'
  run status
  assert_output '0'
  [ "$status" -eq 0 ]
}
