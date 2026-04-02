# Containerized System Status API 🐳

## 🎯 Overview
This project demonstrates a lightweight **RESTful API** built with **Python (Flask)** and containerized using **Docker**. It simulates a system health check endpoint, showcasing the ability to develop and deploy portable backend services.

## 🚀 Key Features
- **RESTful Endpoint:** Provides real-time system metrics via JSON.
- **Containerization:** Fully Dockerized to ensure "It works on my machine" translates to "It works in production."
- **Scalability:** Designed with a microservice mindset, ready for deployment on **AWS (EC2)** or **Azure**.

## 🛠 Tech Stack
- **Language:** Python 3.9
- **Framework:** Flask
- **Platform:** Docker

## 📦 How to Run
1. **Build the Docker Image:**
   `docker build -t status-api .`
2. **Run the Container:**
   `docker run -p 5000:5000 status-api`
3. **Access the API:**
   Navigate to `http://localhost:5000/status`

---
*Authored by Şeyma Çavdar | Backend Developer Candidate at Boğaziçi University*
