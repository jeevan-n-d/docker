## Stage 1
FROM python:3.14-slim AS builder
LABEL maintainer="jeeva"
LABEL project="simple-calculator"
WORKDIR /app
COPY . .
RUN pip install --upgrade pip
RUN ls -ltr

## Stage 2
FROM python:3.14-alpine
WORKDIR /app
COPY --from=builder /app/cal.py .
ENV APP_NAME=Calculator
CMD ["python3","cal.py"]
