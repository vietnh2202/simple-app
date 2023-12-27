# simple-app

## Overview

`simple-app` is a containerized web application powered by Flask.

## Prerequisites

- Docker
- Flask

You can install Flask by running:

```shell
pip install Flask
```

## Docker Image CI

The Docker image for `simple-app` is automatically built and pushed to GitHub Container Registry using GitHub Actions.

For more details, see the `.github/workflows/docker-push.yaml` in the repository.

## How to Run Locally

To run `simple-app` locally, you can use the following docker commands:

```shell
docker build -t simple-app .
docker run -p 5000:5000 simple-app
```

Visit `http://localhost:5000` in your browser to view the app.

## Contributions

Contributions are welcome! Please make a pull request against the `main` branch.
