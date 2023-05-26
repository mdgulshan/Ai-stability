#FROM python:3.12-rc-alpine3.17
#FROM python:3.17.3
#FROM 3.12.0b1-slim-bullseye
#FROM node:12
FROM python:14.16-alpine3.13
WORKDIR ./Ai_Software_Stability\Ai_Software_Stability\Ai_Software_Stability_Frontend_code_Dynamic \Ai_Software_Stability_Frontend_code_Dynamic\macy-app
# Copying all the files in our project
COPY . .
COPY . /app
# Installing dependencies
COPY ./package.json ./
#RUN npm install
CMD ["package.json","run","--host=0.0.0.0"]