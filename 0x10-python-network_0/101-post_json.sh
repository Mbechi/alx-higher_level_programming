#!/bin/bash
# Sends POST request to a providd URL with a relevant JSON file.
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
