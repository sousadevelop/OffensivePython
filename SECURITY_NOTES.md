# Publication Safety Review Notes

This file records risks identified during the public publication review without repeating sensitive values.

## Sanitized During Review

- Replaced a fixed hidden message and operating-system-specific output path in the steganography lab with a fictional placeholder and local example filename.
- Replaced public hosts in the ping list with local or documentation-reserved values.
- Replaced private network examples with documentation-reserved IP addresses.
- Replaced a fixed crawling example URL with `https://example.com/`.
- Replaced a phone-number-shaped prompt example with a clearly fictional placeholder.
- Replaced an external wordlist reference and local sample content with a short fictional laboratory list.
- Removed scanner screenshots that displayed an internal network address and a local filesystem path.
- Removed editor scratch files that were not part of the labs.

## Remaining Risks Requiring User Judgment

- Port scanner labs accept user-provided targets. They must be used only in authorized labs.
- Ping and socket labs can generate network traffic. Keep tests local or explicitly authorized.
- Web crawling and scraping labs accept user-provided URLs. Do not use them against third-party websites without permission.
- The external IP checker calls a third-party endpoint and prints network metadata. Review privacy implications before running it.
- The phone metadata lab must be used only with fictional numbers or numbers whose owner authorized the test.
- The wordlist generator can produce sensitive-looking output. Do not commit generated lists or use them against real accounts.
- The steganography lab generates a local output image. Do not commit files containing private messages.

## Publication Decision

The repository is suitable for educational publication only when accompanied by the ethical scope in `README.md` and `SECURITY.md`. The scripts remain study labs, not approved tools for real-world offensive activity.
