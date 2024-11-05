# Model Deployment

Dockerized FastAPI application for model inference. This image allows you to easily deploy a machine learning model with an API endpoint for predictions.

## Getting Started

Follow these instructions to pull and run the image from Docker Hub.

### Prerequisites

- **Docker**: Ensure Docker is installed on your system. [Download Docker](https://docs.docker.com/get-docker/)

### Pull the Image

To get the latest version of the image, use:

```bash
docker pull asterikss/model-deployment:latest
```

### Run the Container

To start the container, run the following command:

```bash
docker run -p 8032:8032 asterikss/model-deployment:latest
```

This command exposes the application on port `8032` on your local machine.

### Using the API

Once the container is running, you can access the FastAPI documentation at:

- **Swagger UI**: [http://localhost:8032/docs](http://localhost:8032/docs)
  
  The Swagger UI provides an interactive API documentation, allowing you to easily test and see details of each endpoint.

### Example Usage

The API exposes a `/predict` endpoint for making predictions. Here’s an example of how to use it:

1. **Request Format**: Ensure you have the correct input format. Refer to the `/docs` page for the expected data structure.

2. **Sending a Request**: Use `curl` or any HTTP client to send a POST request.

   Example with `curl`:

   ```bash
   curl -X POST http://localhost:8032/predict \
   -H "Content-Type: application/json" \
   -d '{
   "gender": "male",
   "ethnicity": "other",
   "fcollege": true,
   "mcollege": true,
   "home": true,
   "urban": true,
   "unemp": 8.0,
   "wage": 19.0,
   "distance": 8.0,
   "tuition": 20.0,
   "education": 12,
   "income": "low",
   "region": "other"
   }'
   ```

3. **Response**: You’ll receive a JSON response with the "score" prediction.

## Stopping the Container

To stop the container, press `CTRL + C` in the terminal where the container is running, or run the following command in another terminal:

```bash
docker ps  # Find the container ID
docker stop <container_id>
```

## Running Locally

To run the FastAPI application on your local machine without Docker, follow these steps:

### Prerequisites

- **Python 3.12**: Ensure Python 3.12 is installed. [Download Python](https://www.python.org/downloads/)
- **Virtual Environment (optional)**: It’s recommended to create a virtual environment to manage dependencies.

### Installation Steps

1. **Clone the Repository**

First, clone this repository or download the source code to your local machine:

```bash
git clone https://github.com/asterikss/model-deployment.git
cd model-deployment
```

2. **Install Dependencies**

   Install the required Python packages listed in `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**

   Set PYTHONPATH:

   ```bash
   export PYTHONPATH="src/:$PYTHONPATH"
   ```

   Start the FastAPI server locally:

   ```bash
   uvicorn src.main:app --host 0.0.0.0 --port 8032
   ```

   This command starts the server on `http://0.0.0.0:8032`.

4. **Access the API Documentation**

   Once the server is running, you can access the FastAPI documentation at:

   - **Swagger UI**: [http://localhost:8032/docs](http://localhost:8032/docs)

5. **Testing the API**

   Use the example `curl` command to test the `/predict` endpoint as described above.
