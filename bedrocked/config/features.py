import threading

class FeatureFlagManager:
    def __init__(self):
        self._flags = {}
        self._lock = threading.RLock()

    def set_flag(self, name, value):
        """Enable or disable a feature flag."""
        with self._lock:
            self._flags[name] = value

    def is_enabled(self, name):
        """Check if a feature flag is enabled. Defaults to False."""
        with self._lock:
            return self._flags.get(name, False)

    def remove_flag(self, name):
        """Remove a feature flag from the manager."""
        with self._lock:
            self._flags.pop(name, None)

    def list_flags(self):
        """Return a dictionary of all feature flags."""
        with self._lock:
            return dict(self._flags)

# Example usage:
if __name__ == "__main__":
    feature_manager = FeatureFlagManager()
    feature_manager.set_flag("new_dashboard", True)
    print("New dashboard enabled?", feature_manager.is_enabled("new_dashboard"))
