FROM node:15.5-alpine

# Create app directory
RUN mkdir -p /app/src
WORKDIR /app

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)

# If you are building your code for production
# RUN npm ci --only=production

# Bundle app source
#COPY ./nodejs/server.js ./src/

COPY ./nodejs/package*.json ./
RUN npm install

EXPOSE 3000

CMD [ "node", "src/server.js" ]