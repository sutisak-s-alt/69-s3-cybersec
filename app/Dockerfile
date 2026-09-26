FROM node:20-alpine

WORKDIR /app

COPY package*.json ./
COPY yarn.lock ./

RUN yarn install

COPY . .

ENV NODE_ENV=development

EXPOSE 1337

CMD ["yarn", "develop"]
