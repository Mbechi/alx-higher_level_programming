#!/bin/bash

# Sends a GET request to a provided URL with a header variable.
curl -sH "X-School-User-Id: 98" "$1"
