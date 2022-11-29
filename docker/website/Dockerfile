FROM node:14 AS UI

COPY vue_frontend/ ./vue_frontend/

RUN cd vue_frontend && npm install && npm run build

EXPOSE 8080

FROM node:14 AS server

COPY express_backend/ ./express_backend/
COPY --from=ui ./vue_frontend/dist/ ./express_backend/dist/
RUN cd express_backend && npm install

EXPOSE 3000

CMD ["node", "./app.js"]