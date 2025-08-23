''' Build a small library that:

Loads defaults from default_config.json.
Overrides with user_config.json (if exists).
Validates required keys. '''

# config_loader.py
import json
from pathlib import Path

class ConfigError(Exception): pass

class ConfigLoader:
    def __init__(self, default_path, user_path=None):
        self.default_path = Path(default_path)
        self.user_path    = Path(user_path) if user_path else None
        self.config       = {}

    def load(self):
        # 1. Load defaults
        self.config = json.loads(self.default_path.read_text())
        # 2. Override
        if self.user_path and self.user_path.exists():
            user_cfg = json.loads(self.user_path.read_text())
            self.config.update(user_cfg)
        # 3. Validate
        required = ['host','port','api_key']
        missing = [k for k in required if k not in self.config]
        if missing:
            raise ConfigError(f"Missing keys: {missing}")
        return self.config

if __name__ == '__main__':
    loader = ConfigLoader('default_config.json','user_config.json')
    cfg = loader.load()
    print("Loaded config:", cfg)
