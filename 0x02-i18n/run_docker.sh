#!/bin/bash

#!/bin/bash

IMAGE_NAME="flask-babel-app"
CONTAINER_NAME="my_flask_babel_app"

# Check if image exists
if ! docker images --quiet --filter=reference="$IMAGE_NAME" | grep -q "$IMAGE_NAME"; then
    # Build image if it doesn't exist
    docker build -t "$IMAGE_NAME" . || exit 1
fi

# Check if container exists
if ! docker ps --quiet --filter=name="$CONTAINER_NAME" | grep -q "$CONTAINER_NAME"; then
    # Run container if it doesn't exist
    docker run -d -p 5000:5000 -v "$(pwd):/app" --name "$CONTAINER_NAME" "$IMAGE_NAME" || exit 1
else
    # Start existing container
    docker start "$CONTAINER_NAME" || exit 1
fi

echo "Happy coding :)"
