FROM python

WORKDIR /src/backend
COPY . .

ENV FLASK_APP=app
ENV PYTHONPATH=/src

RUN pip3 install -r requirements.txt
RUN chmod +x run.sh
RUN sh run.sh

EXPOSE 5000

ENTRYPOINT ["python3", "app.py"]