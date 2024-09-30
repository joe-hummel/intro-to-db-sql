@echo off
REM
REM Windows BATCH script to build docker container
REM
@echo on
docker rmi sqlite3
docker build -t sqlite3 .
