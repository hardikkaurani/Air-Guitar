# Air Guitar

Air Guitar is a gesture-controlled instrument system that turns wrist motion and strum force into real-time synthesized audio. It combines Arduino sensor input, a modular Python audio engine, configurable effects, optional MIDI output, session recording, and a lightweight web dashboard for control and monitoring.

## Why This Repo Exists

This repository is structured like a real software project rather than a one-file prototype. The goal is to show production-minded engineering around a creative hardware/software build:

- modular application architecture
- isolated domain components for audio, sensing, and control
- clear configuration and documentation boundaries
- test coverage for core audio behavior
- room for future packaging, deployment, and feature growth

## Highlights

- Real-time gesture-to-note triggering from Arduino sensor data
- Polyphonic audio engine with Karplus-Strong synthesis
- Multiple instrument models and configurable effects
- MIDI output support for DAW integration
- WAV recording for captured sessions
- Optional Flask-based monitoring and control UI

## Repository Layout

```text
.
|-- config/
|   `-- config.yaml
|-- docs/
|   |-- architecture.md
|   |-- api.md
|   |-- docs-index.md
|   |-- features.md
|   |-- production.md
|   |-- quickstart.md
|   `-- testing.md
|-- hardware/
|   `-- arduino_code.ino
|-- src/
|   `-- air_guitar/
|       |-- app.py
|       |-- core/
|       |-- utils/
|       `-- web/
|-- tests/
|   `-- test_audio_engine.py
|-- .gitignore
|-- main.py
|-- pyproject.toml
`-- requirements.txt
```

## Getting Started

```bash
pip install -r requirements.txt
python main.py
```

Update `config/config.yaml` with the correct serial port before starting the system.

## Documentation

- [Quickstart](docs/quickstart.md)
- [Architecture](docs/architecture.md)
- [API](docs/api.md)
- [Testing](docs/testing.md)
- [Production Notes](docs/production.md)

## Tech Stack

Python, NumPy, PySerial, SoundDevice, SoundFile, Flask, PyYAML, and Arduino-based motion sensing.
