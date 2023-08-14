import os
import json

# Load configuration from environment variables or a config file (JSON or YAML)
def load_config(config_file=None):
    config = {}
    if config_file and os.path.exists(config_file):
        with open(config_file, 'r') as file:
            config = json.load(file)
    else:
        # Load from environment variables
        config['image_name'] = os.getenv('IMAGE_NAME', 'nginx:latest')
        config['container_name'] = os.getenv('CONTAINER_NAME', 'my_nginx_container')
        # Add other configuration options as needed
    return config
