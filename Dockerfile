FROM python3

WORKDIR /src

COPY ./backend /src/backend

RUN chmod +x /src/backend/run.sh
ENTRYPOINT ["sh", "/src/backend/run.sh"]

EXPOSE 5000