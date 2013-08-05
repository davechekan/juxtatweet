#!/bin/bash

cd ~/src/juxtapy/juxtapy/config

vim __init__.py            \
    base_config.py         \
    testing.py             \
    default_development.py \
    development.py         \
    integration.py         \
    staging.py             \
    production.py          \
