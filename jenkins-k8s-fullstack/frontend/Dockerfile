FROM node

WORKDIR /app
COPY *.json .
RUN npm install

WORKDIR /app/public
COPY public .

WORKDIR /app/src
COPY src .

WORKDIR /app
RUN npm run build

EXPOSE 3000

ENTRYPOINT ["npm", "start"]

