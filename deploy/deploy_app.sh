#!/bin/bash

MANIFEST="/opt/lnpr/manifest.yaml"

PKG=$(grep 'package_required:' "$MANIFEST" | awk '{print $2}')

if [ ! -d "/opt/cvpack/$PKG" ]; then
    echo "Installing missing package $PKG..."
    tar -xzf /opt/lnpr/cvpack_${PKG}.tar.gz -C /opt/cvpack/$PKG --strip-components=1
fi

docker stop lnpr-app || true
docker rm lnpr-app || true

docker run -d --name lnpr-app -p 5000:5000 ghcr.io/vateam0864-glitch/lnpr-app:latest
