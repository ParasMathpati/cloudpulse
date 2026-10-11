# CloudPulse — Automated DevOps CI/CD Platform

**A Dockerized web application deployed through an automated CI/CD pipeline using GitHub Actions and Render.**

[![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)](https://github.com/ParasMathpati/cloudpulse/actions)
[![Docker](https://img.shields.io/badge/Container-Docker-2496ED?logo=docker&logoColor=white)](https://www.docker.com/)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Deployment](https://img.shields.io/badge/Deployment-Render-46E3B7)](https://render.com/)

## 🚀 Live Demo

- **Live Application:** https://cloudpulse-i2xv.onrender.com
- **GitHub Repository:** https://github.com/ParasMathpati/cloudpulse
- **CI/CD Pipeline:** https://github.com/ParasMathpati/cloudpulse/actions
- **API Documentation:** https://cloudpulse-i2xv.onrender.com/docs

## 📌 Project Overview

CloudPulse is a containerized web application built to demonstrate practical DevOps engineering concepts, including application testing, Docker image builds, automated CI/CD workflows, and cloud deployment without relying on AWS.

The application is developed locally on Linux, version-controlled with Git, and hosted on GitHub. GitHub Actions automatically runs application tests and validates the Docker build. Once these checks succeed on the main branch, the workflow triggers a deployment on Render using a securely stored deployment hook.

The project demonstrates how automation can reduce manual deployment steps and improve the consistency and repeatability of application releases.

## 🏗️ Architecture

Developer → Linux Development Environment → GitHub Repository → GitHub Actions → Automated Tests → Docker Build Validation → Render Deploy Hook → Live Application

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.12 | Application runtime |
| FastAPI | Web framework and REST endpoints |
| Uvicorn | ASGI application server |
| Docker | Application containerization |
| Git & GitHub | Version control and source code management |
| GitHub Actions | CI/CD automation |
| Pytest | Automated application testing |
| Render | Public application hosting |
| Prometheus Client | Application metrics instrumentation |
| Linux | Development and local execution environment |

## ✨ Key Features

- **Containerization:** Packages the application and its runtime dependencies into a Docker image.
- **Automated Testing:** Executes Pytest test cases through GitHub Actions.
- **CI Pipeline:** Installs dependencies, runs tests, and validates the Docker image build.
- **Automated Deployment:** Triggers Render deployment after successful CI checks on pushes to the main branch.
- **Health Monitoring Endpoint:** Provides a `/health` endpoint to verify application availability.
- **Readiness Endpoint:** Exposes `/ready` to indicate application readiness.
- **Metrics Endpoint:** Exposes Prometheus-compatible application metrics at `/metrics`.
- **API Documentation:** Provides interactive API documentation through FastAPI at `/docs`.
- **Secure Configuration:** Stores the Render deployment hook in GitHub Actions repository secrets.

## 🔄 CI/CD Workflow

1. Develop and modify the application locally.
2. Commit changes and push them to the GitHub repository.
3. GitHub Actions starts the CI/CD workflow.
4. The workflow installs Python dependencies.
5. Pytest executes automated tests.
6. Docker builds the application image to validate the container configuration.
7. On a successful push to `main`, GitHub Actions triggers the Render deployment hook.
8. Render builds and deploys the application from the connected repository.
9. The deployed application can be verified using its public URL and health endpoint.

Pull requests run the test and Docker build stages without triggering production deployment.

## 📂 Project Structure

```text
cloudpulse/
├── app/
│   └── main.py
├── tests/
│   └── test_main.py
├── .github/
│   └── workflows/
│       └── ci-cd.yml
├── Dockerfile
├── .dockerignore
├── requirements.txt
├── requirements-dev.txt
└── README.md
```

## ⚙️ Run Locally

### Prerequisites

- Linux
- Python 3.12 or compatible version
- Git
- Docker Engine

### 1. Clone the repository

```bash
git clone https://github.com/ParasMathpati/cloudpulse.git
cd cloudpulse
```

### 2. Create a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements-dev.txt
```

### 4. Run automated tests

```bash
python -m pytest -v
```

### 5. Start the application

```bash
python -m uvicorn app.main:app --reload
```

Open `http://localhost:8000` in your browser.

## 🐳 Run with Docker

### Build the image

```bash
docker build -t cloudpulse:local .
```

### Run the container

```bash
docker run --rm -p 8001:8000 cloudpulse:local
```

Open `http://localhost:8001`.

If Docker requires elevated privileges on your Linux system, prefix the commands with `sudo`.

## 🔎 Application Endpoints

| Endpoint | Description |
|---|---|
| `/` | CloudPulse dashboard |
| `/health` | Application health check |
| `/ready` | Readiness status |
| `/metrics` | Prometheus-compatible metrics |
| `/docs` | Interactive API documentation |

## 🔐 Security Practices

- Uses a non-root user inside the Docker container.
- Excludes local virtual environments and `.env` files from the Docker build context.
- Uses GitHub Actions secrets for deployment credentials.
- Restricts GitHub Actions repository permissions to read-only content access for the current workflow.
- Keeps deployment credentials out of application source code.

## 🎯 Engineering Outcomes

This project demonstrates practical experience with:

- Containerizing Python applications.
- Writing and executing automated tests.
- Building CI/CD workflows with GitHub Actions.
- Validating Docker builds in a CI environment.
- Automating deployments to a public hosting platform.
- Implementing application health checks and metrics instrumentation.
- Managing source code and deployment configuration using Git and GitHub.

## 🔮 Future Enhancements

- Integrate Trivy for container vulnerability scanning.
- Add Prometheus and Grafana dashboards for metrics visualization.
- Introduce Docker Compose for multi-service local development.
- Deploy the application to a local Kubernetes cluster using Minikube or kind.
- Add Kubernetes readiness and liveness probes.
- Implement versioned releases and a documented rollback strategy.
- Add deployment notifications and improved pipeline reporting.

## 👨‍💻 Author

**Paras Mathpati**

Cloud & DevOps Engineering | Docker | GitHub Actions | Python | Linux | CI/CD

- GitHub: https://github.com/ParasMathpati

---

*CloudPulse is a hands-on DevOps portfolio project demonstrating automated testing, containerization, and continuous delivery using free-tier hosting services.*
