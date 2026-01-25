# kubernetes_demo (koth)

This project serves to demonstrate how to deploy a backend utilizing FastAPI and a static frontend to a k3s cluster running on a private remote server (SSH connection), using Podman for containerization and Docker Hub for image registry.

## Architecture

Browser -> Traefik Ingress -> Frontend Service <br/>
Browser -> Traefik Ingress -> Backend Service

Routes:
- `/` → frontend (Nginx + static HTML + JS)
- `/api` → FastAPI backend

## Build container

podman build -t docker.io/kickinthedoor/koth:latest .<br/>
podman push docker.io/kickinthedoor/koth:latest

## Deploy to k3s (remote)

sudo k3s kubectl apply -f koth_kube/

