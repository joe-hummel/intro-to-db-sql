#!/bin/bash
#
# Linux/Mac BASH script to build docker container
#
docker rmi sqlite3
docker build -t sqlite3 .
