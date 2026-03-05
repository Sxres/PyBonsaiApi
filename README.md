# bonsai-api

A minimal FastAPI server that generates ASCII bonsai trees using [pybonsai](https://github.com/nicholaswmin/pybonsai).

## Endpoints

- `GET /tree/instant` — returns a randomly generated bonsai tree as a JSON string

## Usage
```bash
uvicorn main:app --reload
```

Then hit `http://localhost:8000/tree/instant`.

## Deployment

Deployed on Google Cloud Run. Rebuild and redeploy:
```bash
docker build -t bonsai-api .
docker tag bonsai-api us-central1-docker.pkg.dev/bonsai-api-489223/bonsai-api/bonsai-api:latest
docker push us-central1-docker.pkg.dev/bonsai-api-489223/bonsai-api/bonsai-api:latest
gcloud run deploy bonsai-api --image us-central1-docker.pkg.dev/bonsai-api-489223/bonsai-api/bonsai-api:latest --region northamerica-northeast2 --allow-unauthenticated
```

## Stack

- FastAPI
- pybonsai
- Docker
- Google Cloud Run
