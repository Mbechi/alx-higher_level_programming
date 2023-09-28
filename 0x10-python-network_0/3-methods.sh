#!/bin/bash

# Displays all HTTP methods that the server will accept of the given URL.
curl -sI "$1" | grep "Allow" | cut -d " " -f 2-
