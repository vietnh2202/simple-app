FROM python:alpine3.19 as builder

WORKDIR /app

COPY . .

FROM python:alpine3.19

RUN adduser -D appuser
USER appuser

WORKDIR /app

COPY --chown=adduser:adduser --from=builder /root/.local /home/appuser/.local
COPY --chown=adduser:adduser --from=builder /app /app

RUN pip install --user --upgrade pip==23.3

ENV PATH=/home/appuser/.local/bin:$PATH

RUN pip install --user -r requirements.txt

EXPOSE 5000

CMD [ "flask", "run", "--host", "0.0.0.0" ]