#!/bin/bash 
# post request 
curl -s -X POST --data-raw email="test@gmail.com" --data-raw subject="I will always be here for PLD" $1
