# bonsai-api

A minimal FastAPI server that generates ASCII bonsai trees using [pybonsai](https://github.com/Ben-Edwards44/PyBonsai).

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
docker tag yourimage/yourrepo
docker push yourrepo/yourimage
```

## Stack

- FastAPI
- Docker






