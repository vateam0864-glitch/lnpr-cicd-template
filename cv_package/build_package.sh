#!/bin/bash
VERSION=v2
PACKAGE_DIR="package_${VERSION}"

tar -czf cvpack_${VERSION}.tar.gz $PACKAGE_DIR
echo "Built CV package version: $VERSION"
