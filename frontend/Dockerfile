FROM node:20-alpine

RUN addgroup -S appgroup && adduser -S -G appgroup appuser

RUN mkdir -p /home/appuser

COPY . /home/appuser

RUN chown -R appuser:appgroup /home/appuser

WORKDIR /home/appuser

COPY . .

RUN npm ci && npm run build

EXPOSE 4321

CMD ["node", "./dist/server/entry.mjs", "--host", "0.0.0.0"]
