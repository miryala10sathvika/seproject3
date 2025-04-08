import os
import yaml

def load_config(env: str = "development"):
    config_file = f"config/{env}.yaml"
    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            return yaml.safe_load(f)
    return {}
