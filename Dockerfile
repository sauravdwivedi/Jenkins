FROM python

WORKDIR /src

COPY ./backend ./backend

WORKDIR /src/backend

ENV FLASK_APP=app
ENV PYTHONPATH=/src:/src/backend:/src/backend/controllers

RUN pip3 install -r requirements.txt
RUN chmod +x run.sh
RUN sh run.sh

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]