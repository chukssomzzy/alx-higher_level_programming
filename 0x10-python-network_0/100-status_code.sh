#!/bin/bash 
# print status code 
curl -s  -w "%{http_code}" $1 -o /dev/null
