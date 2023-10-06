# 1Password Secret Replacement HTTP Proxy

## Overview

This Python script provides a simple way to automatically replace secret references in HTTP requests with actual secrets retrieved from 1Password. The script uses the `mitmproxy` library to intercept and modify HTTP requests. It scans for secret references formatted as `op://...` in the request headers and replaces them with the actual secrets fetched using the 1Password CLI.

## Prerequisites

- Python 3.x
- `mitmproxy` library
- 1Password CLI installed and authenticated with a human user or a service account

## Installation

1. Clone the repository:
    ```bash
    git clone git@github.com:carey404/op-proxy.git
    ```

2. Navigate into the directory:
    ```bash
    cd op-proxy
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run `mitmproxy` with the script:
    ```bash
    mitmproxy -s proxy.py
    ```

2. Configure your HTTP client (e.g., Postman, curl) to use the proxy running at `http://localhost:8080` (default `mitmproxy` address).

3. In your HTTP requests, you can now include secrets in the format `op://...` in the headers, and they will be automatically replaced by the script.

## Contributing

Feel free to submit pull requests or issues to improve the script or extend its functionalities.

## License

This project is licensed under the MIT License.

---

For more information, please refer to the inline comments in the script.