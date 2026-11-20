# DevOps Practical — devops-practical

A simple Flask web application built for a university DevOps practical assignment.

## Features

- `/` — Returns `{"message": "Hello, DevOps World!", "version": "1.0"}`
- `/health` — Returns `{"status": "healthy"}`

## Tech Stack

- **Python 3.12** + **Flask 3.0**
- **pytest** for automated testing
- **Docker** for containerisation
- **GitHub Actions** for CI/CD
- **Render** for cloud hosting

## Local Development

```bash
# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate   # Linux/macOS

# Install dependencies
pip install -r requirements.txt

# Run tests
pytest test_app.py -v

# Run the app
python app.py
```

## CI/CD

Every push to `main`:
1. Runs automated tests on GitHub Actions (ubuntu-latest)
2. Builds and pushes a Docker image to Docker Hub
3. Triggers automatic re-deployment on Render
