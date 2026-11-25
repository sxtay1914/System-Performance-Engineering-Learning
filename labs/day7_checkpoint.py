#!/usr/bin/env python3
"""Loopback-only HTTP fixture for the Day 7 performance checkpoint."""

import fcntl
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import os
from pathlib import Path
import signal
import subprocess
import sys
import tempfile
import threading
import time


HOST, PORT = "127.0.0.1", 8077


def scenario_worker(path):
    deadline = time.monotonic() + 45
    with path.open("rb+") as file:
        while (remaining := deadline - time.monotonic()) > 0:
            fcntl.flock(file, fcntl.LOCK_EX)
            try:
                time.sleep(min(1.6, remaining))
            finally:
                fcntl.flock(file, fcntl.LOCK_UN)
            time.sleep(0.15)


def serve():
    def stop(_signum, _frame):
        raise SystemExit(0)

    signal.signal(signal.SIGTERM, stop)

    with tempfile.TemporaryDirectory(prefix="day7-checkpoint-") as directory:
        report = Path(directory) / "report.txt"
        report.write_bytes(b"report ok\n")
        scenario = None
        guard = threading.Lock()

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                if self.path != "/report":
                    self.send_error(404)
                    return
                with report.open("rb") as file:
                    fcntl.flock(file, fcntl.LOCK_SH)
                    body = file.read()
                self.send_response(200)
                self.send_header("Content-Type", "text/plain")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def do_POST(self):
                nonlocal scenario
                if self.path != "/scenario":
                    self.send_error(404)
                    return
                with guard:
                    if scenario is not None and scenario.poll() is None:
                        self.send_error(409, "Scenario already running")
                        return
                    scenario = subprocess.Popen(
                        [sys.executable, str(Path(__file__).resolve()), "--worker", str(report)]
                    )
                self.send_response(204)
                self.end_headers()

        try:
            with ThreadingHTTPServer((HOST, PORT), Handler) as server:
                print(f"Day 7 endpoint: http://{HOST}:{PORT}/report (PID {os.getpid()})", flush=True)
                server.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            with guard:
                if scenario is not None and scenario.poll() is None:
                    scenario.terminate()
                    scenario.wait(timeout=3)


if __name__ == "__main__":
    if len(sys.argv) == 3 and sys.argv[1] == "--worker":
        scenario_worker(Path(sys.argv[2]))
    else:
        serve()
