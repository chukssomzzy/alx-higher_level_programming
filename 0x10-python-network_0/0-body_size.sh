#!/bin/bash 
# takes a URL, sends a request to that URL and displays the size of the body of the responds 
curl -s --head $1 | grep Content-Length | awk '{ print $2; }'
