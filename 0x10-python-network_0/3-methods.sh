#!/bin/bash
# allow  
curl -s --head $1 | grep Allow | sed -r "s/Allow:\s//"
