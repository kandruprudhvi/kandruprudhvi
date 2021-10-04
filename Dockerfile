### in case to run a container always and query pull requests periodically from cronjob running python script
FROM python:3.7
RUN apt-get update && apt-get -y install cron vim
RUN pip install requests
WORKDIR /app
COPY crontab /etc/cron.d/crontab
COPY  notification.py /app/notification.py
RUN chmod 0644 /etc/cron.d/crontab
RUN /usr/bin/crontab /etc/cron.d/crontab
# run crond as main process of container
CMD ["cron", "-f"]
