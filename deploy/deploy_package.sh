#!/bin/bash
VERSION=$1

echo "Deploying CV package version $VERSION..."

mkdir -p /opt/cvpack

if [ ! -d "/opt/cvpack/${VERSION}" ]; then
    mkdir -p /opt/cvpack/${VERSION}
    tar -xzf /opt/lnpr/cvpack_${VERSION}.tar.gz -C /opt/cvpack/${VERSION}/ --strip-components=1
    echo "Package installed at /opt/cvpack/${VERSION}"
else
    echo "Package already installed. Skipping."
fi
