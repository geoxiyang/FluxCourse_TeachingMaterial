#!/usr/bin/env python3
"""Start a local HTTP server for the TLS point cloud viewer."""

from __future__ import annotations

import os
import socket
import webbrowser
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path


def available_port(start: int = 8791) -> int:
    for port in range(start, start + 20):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            try:
                sock.bind(("127.0.0.1", port))
            except OSError:
                continue
            return port
    raise RuntimeError("Could not find an available local port")


def main() -> None:
    folder = Path(__file__).resolve().parent
    os.chdir(folder)
    port = available_port()
    url = f"http://localhost:{port}/tls_point_cloud_viewer.html"
    print(f"Serving TLS viewer from: {folder}")
    print(f"Open: {url}")
    webbrowser.open(url)
    ThreadingHTTPServer(("127.0.0.1", port), SimpleHTTPRequestHandler).serve_forever()


if __name__ == "__main__":
    main()
