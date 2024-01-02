FROM python:alpine3.19 as builder

WORKDIR /app

COPY . .

RUN pip install --upgrade pip==23.3

RUN pip install --user -r requirements.txt

FROM python:alpine3.19

RUN adduser -D appuser
USER appuser

WORKDIR /app

COPY --chown=adduser:adduser --from=builder /root/.local /home/appuser/.local
COPY --chown=adduser:adduser --from=builder /app /app

ENV PATH=/home/appuser/.local/bin:$PATH

EXPOSE 5000

CMD [ "flask", "run", "--host", "0.0.0.0" ]