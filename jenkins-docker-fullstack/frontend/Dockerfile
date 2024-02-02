FROM node

WORKDIR /app
COPY *.json .

WORKDIR /app/src
COPY src .

RUN npm run build

ENTRYPOINT [npm run start]

