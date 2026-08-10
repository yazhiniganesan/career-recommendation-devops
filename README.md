# Automated CI/CD Pipeline for Career Recommendation System

## Overview
The Career Recommendation System is a web-based application that helps users identify suitable career paths based on their skills, interests, and preferences. This project demonstrates the implementation of DevOps practices by automating the build, deployment, and delivery process using Jenkins, Docker, GitHub, and AWS EC2.

## Features
- User-friendly web interface
- Career recommendations based on user inputs
- Automated Continuous Integration and Continuous Deployment (CI/CD)
- Containerized application using Docker
- Cloud deployment on AWS EC2
- Version control using GitHub

## Tech Stack

### Frontend
- HTML
- CSS

### Backend
- Python
- Flask

### DevOps Tools
- GitHub
- Jenkins
- Docker
- Docker Hub
- AWS EC2

## Architecture

GitHub Repository
↓
Jenkins Pipeline
↓
Docker Build
↓
Docker Hub
↓
AWS EC2 Deployment

## Project Workflow

1. Source code is maintained in GitHub.
2. Jenkins automatically detects code changes.
3. Jenkins triggers the CI/CD pipeline.
4. Docker image is built automatically.
5. Docker image is pushed to Docker Hub.
6. Application is deployed on AWS EC2.
7. Updated application becomes available to users.

## Installation

### Clone the Repository

```bash
git clone https://github.com/yazhiniganesan/career-recommendation-devops.git
cd career-recommendation-devops
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

## Docker Setup

Build Docker Image

```bash
docker build -t career-recommendation-system .
```

Run Docker Container

```bash
docker run -p 5000:5000 career-recommendation-system
```

## Jenkins Pipeline

The Jenkins pipeline automates:

- Code checkout from GitHub
- Build process
- Docker image creation
- Docker Hub image push
- Deployment to AWS EC2

## AWS Deployment

The application is hosted on an AWS EC2 instance using Docker containers to ensure scalability and easy deployment.

## Key Learning Outcomes

- Continuous Integration and Continuous Deployment (CI/CD)
- Jenkins Pipeline Configuration
- Docker Containerization
- Cloud Deployment using AWS EC2
- GitHub Version Control
- DevOps Best Practices
- Application Deployment Automation

## Project Highlights

- Individual Project
- End-to-End CI/CD Implementation
- Cloud-Based Deployment
- Automated Build and Release Process
- Hands-on Experience with DevOps Tools

## Future Enhancements

- User Authentication
- Database Integration
- Machine Learning Based Recommendations
- Kubernetes Deployment
- Monitoring using Prometheus and Grafana

