FROM python:3.10-alpine as builder

WORKDIR /app

COPY . .

RUN pip install --user -r requirements.txt

FROM python:3.10-alpine

RUN adduser -D appuser
USER appuser

WORKDIR /app

COPY --from=builder /root/.local /home/appuser/.local
COPY --from=builder /app /app

ENV PATH=/home/appuser/.local/bin:$PATH

EXPOSE 5000

CMD [ "flask", "run", "--host", "0.0.0.0" ]