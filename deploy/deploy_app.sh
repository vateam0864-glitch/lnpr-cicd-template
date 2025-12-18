#!/bin/bash
set -e

echo "=============================="
echo " LNPR APP DEPLOY STARTED"
echo "=============================="

APP_DIR="/opt/lnpr/docker"
IMAGE="ghcr.io/vateam0864-glitch/lnpr-cid-template"
DEFAULT_TAG="latest"

# Optional: allow version override from manifest
if [ -f /opt/lnpr/manifest.yaml ]; then
  VERSION=$(grep -E '^app_version:' /opt/lnpr/manifest.yaml | awk '{print $2}')
else
  VERSION="$DEFAULT_TAG"
fi

echo "Using image version: $VERSION"

cd $APP_DIR

echo "Pulling latest image..."
docker pull ${IMAGE}:${VERSION}

echo "Stopping existing containers..."
docker compose down || true

echo "Starting LNPR services..."
LNPR_VERSION=$VERSION docker compose up -d

echo "=============================="
echo " LNPR APP DEPLOY COMPLETED"
echo "=============================="
