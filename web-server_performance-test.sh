#!/usr/bin/env bash
# Leverages ApacheBench to test server performance

sudo apt update
sudo apt install -y apache2-utils
ab -c 100 -n 2000 localhost/
