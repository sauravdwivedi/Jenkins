FROM python

WORKDIR /src

COPY ./backend ./backend

ENV PYTHONPATH=/src:/src/backend:/src/backend/controllers

WORKDIR /src/backend

ENV FLASK_APP=app

RUN chmod +x run.sh
RUN sh run.sh

ENTRYPOINT ["python3", "app.py"]

EXPOSE 5000