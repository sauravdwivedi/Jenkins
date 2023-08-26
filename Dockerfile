FROM python

WORKDIR /src

COPY ./backend /src/backend

RUN chmod +x /src/backend/run.sh
RUN sh /src/backend/run.sh

ENTRYPOINT ["screen python3", "app.py", "> log.txt 2>&1 &"]

EXPOSE 5000