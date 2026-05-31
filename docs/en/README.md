# Cybersecurity Python Labs

## Overview

This repository contains small educational Python labs for cybersecurity fundamentals. Use the content only in local environments, isolated lab networks, systems you own, or explicitly authorized scenarios.

The scripts are learning exercises, not approved tools for real-world offensive operations.

## Ethical Scope

- Obtain authorization before testing any environment.
- Prefer `localhost`, `127.0.0.1`, and isolated lab networks.
- Use documentation-reserved values such as `192.0.2.1`.
- Do not use real credentials, phone numbers, URLs, files, or personal data.
- Do not publish third-party scan output or collected information.

## Lab Areas

The repository includes local labs for hashing, password generation, text permutations, sockets, port scanning, ping, IP calculations, web parsing, steganography, external IP metadata, and phone metadata.

Network, web, and metadata labs require explicit authorization.

## Installation

```bash
python -m venv .venv
pip install -r requirements.txt
```

## Safe Placeholders

- `localhost`
- `127.0.0.1`
- `192.0.2.1`
- `https://example.com/`
- `LAB_PLACEHOLDER_MESSAGE`

## Limitations

- Some scripts are early or incomplete studies.
- Network labs generate traffic and must remain inside authorized environments.
- External services may collect request metadata.
- This repository does not provide instructions for use against real targets.

See [SECURITY.md](../../SECURITY.md) and [SECURITY_NOTES.md](../../SECURITY_NOTES.md).
