import os
import json

class EnvManager:
    def __init__(self):
        self._overrides = {}

    def get(self, key, default=None):
        """
        Retrieve the value for a given key.
        Checks dynamic overrides first, then falls back to os.environ.
        """
        return self._overrides.get(key, os.environ.get(key, default))

    def set_override(self, key, value):
        """Dynamically override an environment variable."""
        self._overrides[key] = value

    def clear_override(self, key):
        """Remove an override so the value falls back to os.environ."""
        self._overrides.pop(key, None)

    def load_from_file(self, file_path):
        """
        Load environment variable overrides from a JSON file.
        The file should contain a simple key/value mapping.
        """
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
                self._overrides.update(data)
        except Exception as e:
            raise RuntimeError(f"Failed to load environment from {file_path}: {e}")

# Example usage:
if __name__ == "__main__":
    env_manager = EnvManager()
    env_manager.set_override("DEBUG", "true")
    print("DEBUG:", env_manager.get("DEBUG"))
