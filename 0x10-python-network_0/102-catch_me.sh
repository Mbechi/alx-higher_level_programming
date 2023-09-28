#!/bin/bash

# Use curl to make a request to the specified URL with a custom header
curl -s -X PUT -L -d "user_id=98" 0.0.0.0:5000/catch_me -H "Origin: HolbertonSchool"
