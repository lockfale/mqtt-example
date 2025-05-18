# Sample MQTT

## Build

### Pre-req (windows)

py3.12
poetry
```bash
pipx install poetry
poetry --version
```

https://scoop.sh/
https://pipx.pypa.io/stable/installation/

# Running

Create lock file:
```bash
peotry lock
```

Install:
```bash
poetry install --no-root
```

Spin up the broker:
```bash
docker compose -f docker-compose.infrastructure.yaml up -d
```

Run subscriber:
```bash
poetry run .\subscriber.py
```

Publish a message:
```bash
poetry run .\publisher.py
```

Check the output in the subscriber:
```text
[2025-05-18 17:58:38,591.591] [INFO] [subscriber.py:57]: Creating client: subscriber-local
[2025-05-18 17:58:38,591.591] [INFO] [subscriber.py:75]: Connecting to localhost:1883...
[2025-05-18 17:58:38,600.600] [INFO] [subscriber.py:15]: Connected with result code: Success
[2025-05-18 17:58:38,602.602] [INFO] [subscriber.py:43]: Subscribed with QoS: 1
[2025-05-18 17:58:41,802.802] [INFO] [subscriber.py:33]: some/cool/topic
[2025-05-18 17:58:41,802.802] [INFO] [subscriber.py:34]: b'{"hello": "world"}'
```

# Maintenance

```bash
poetry run isort .
poetry run black .
```
