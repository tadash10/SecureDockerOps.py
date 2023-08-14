import docker

def create_safe_container(image_name, container_name, port_mappings=None):
    """
    Create a safe Docker container with the specified image.

    :param image_name: Name of the Docker image to use.
    :param container_name: Name to assign to the container.
    :param port_mappings: Dictionary of port mappings (host_port: container_port).
    :return: Docker container object or None if creation failed.
    """
    try:
        # Initialize Docker client
        client = docker.from_env()

        # Pull the specified image from Docker Hub (ensure the image is trusted)
        client.images.pull(image_name)

        # Define container options
        container_options = {
            "image": image_name,
            "name": container_name,
            "detach": True,  # Run container in detached mode
            "restart_policy": {"Name": "always"},  # Restart container on failure
            "security_opt": ["no-new-privileges"],  # Disable privilege escalation
            "network_mode": "bridge",  # Use bridge network mode
            "ports": port_mappings or {},  # Port mappings if provided
        }

        # Create the container
        container = client.containers.create(**container_options)

        # Start the container
        container.start()

        return container
    except Exception as e:
        print("Error creating safe container:", e)
        return None

# Example usage
if __name__ == "__main__":
    image_name = "nginx:latest"
    container_name = "my_nginx_container"
    port_mappings = {8080: 80}  # Map host port 8080 to container port 80

    container = create_safe_container(image_name, container_name, port_mappings)
    if container:
        print(f"Container '{container_name}' created and started successfully!")
    else:
        print(f"Failed to create container '{container_name}'. Check the error message.")
