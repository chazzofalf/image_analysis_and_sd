#!/bin/bash
SCRIPT_DIR="$(dirname "$(readlink -f "$0")")" 
pushd "${SCRIPT_DIR}" 
ollama create biggemma3
popd