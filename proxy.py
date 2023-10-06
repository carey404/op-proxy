import re
from mitmproxy import http
import subprocess

def get_secret_from_1password(secret_reference: str):
    """
    Retrieve a secret from 1Password using the op CLI.
    """
    print(f"Getting secret for: {secret_reference}")
    cmd = f'op read "{secret_reference}"'
    result = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout.strip()

def replace_secrets(text: str):
    """
    Replace any secret references in a text with the corresponding 1Password secrets.
    """
    pattern = re.compile(r'\bop://[^\s]+(?:\s+[^\s]+)*\b')
    for match in pattern.findall(text):
        secret = get_secret_from_1password(match)
        if secret:  # Only replace if a secret is actually found
            text = text.replace(match, secret)
    return text

def request(flow: http.HTTPFlow) -> None:
    """
    This function is called for every incoming HTTP request.
    It modifies the request based on our requirements.
    """
    # Replace secrets in request headers
    for key, value in flow.request.headers.items():
        flow.request.headers[key] = replace_secrets(value)
