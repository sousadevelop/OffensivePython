# Security Policy

## Ethical Scope

This repository contains educational cybersecurity labs. Use them only:

- In local environments.
- In isolated lab networks.
- Against systems you own.
- Against targets for which you have explicit written authorization.

Do not use these scripts to scan, inspect, enumerate, scrape, contact, or modify third-party systems or data without permission.

## Public Repository Safety

Do not commit:

- Real target IP addresses, hostnames, URLs, or phone numbers.
- Credentials, tokens, API keys, cookies, session data, or secrets.
- Payloads copied from real environments.
- Private files, hidden messages, generated wordlists, or scan output.
- Personal data or information collected from third parties.

Use safe placeholders such as `localhost`, `127.0.0.1`, `192.0.2.1`, `https://example.com/`, and `LAB_PLACEHOLDER_MESSAGE`.

## Reporting

Report suspected exposure privately to the repository maintainer. Do not open public issues containing sensitive values. Include the affected file, the type of exposure, and a safe remediation suggestion.

## Review Checklist

- [ ] Labs are framed for authorized environments only.
- [ ] Examples use reserved or local placeholders.
- [ ] No real credentials or secrets are present.
- [ ] No private scan output or personal data is committed.
- [ ] Documentation does not add operational guidance for abuse.
