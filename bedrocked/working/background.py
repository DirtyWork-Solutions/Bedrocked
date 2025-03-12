import threading
import queue
import time

class BackgroundWorker:
    def __init__(self):
        self._queue = queue.Queue()
        self._stop_event = threading.Event()
        self._thread = threading.Thread(target=self._worker, daemon=True)
        self._thread.start()

    def _worker(self):
        while not self._stop_event.is_set():
            try:
                func, args, kwargs = self._queue.get(timeout=0.1)
                func(*args, **kwargs)
            except queue.Empty:
                continue

    def defer(self, func, *args, **kwargs):
        """Schedule a function to be executed in the background."""
        self._queue.put((func, args, kwargs))

    def stop(self):
        """Gracefully stop the background worker."""
        self._stop_event.set()
        self._thread.join()

# Example usage:
if __name__ == "__main__":
    def sample_job(message):
        print(f"Background job says: {message}")

    worker = BackgroundWorker()
    worker.defer(sample_job, "Hello, background!")
    # Allow some time for the job to be processed.
    time.sleep(1)
    worker.stop()
