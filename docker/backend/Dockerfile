FROM node:10

COPY express_backend/ ./express_backend/
RUN cd express_backend && npm install

EXPOSE 8000

CMD ["node", "./app.js"]