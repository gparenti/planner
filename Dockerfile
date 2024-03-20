FROM python:slim

RUN mkdir /home/ubuntu/planner
WORKDIR /home/ubuntu/planner

COPY . .

RUN chmod a+x boot.sh

RUN pip install -r requirements.txt
RUN pip install gunicorn pymysql cryptography

ENV FLASK_APP microblog.py

EXPOSE 5000

RUN if [ ! -f /home/ubuntu/planner/boot.sh ]; then echo "boot.sh not found"; exit 1; fi --> pfad isch komplett falsch gsi und ned nach best practice gsi

ENTRYPOINT [ "/home/ubuntu/planner/boot.sh" ]