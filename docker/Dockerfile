FROM python:3.12.4-alpine3.20
#
# add bash to alpine Linux:
#
RUN apk update && apk upgrade
RUN apk add --no-cache bash
#
# turn off history file creation:
#
RUN echo "export HISTFILE=/dev/null" >> /etc/profile
#
# add a user (with no pwd) so we don't run as root:
#
RUN adduser -S user -G users -D
#
# install sqlite3 at the command-line to execute SQL:
#
RUN apk add --no-cache sqlite
#
# install any additional python packages we need:
#
# RUN pip3 install sqlite3
# RUN pip3 install pymysql
