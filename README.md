# 🚀 Python Web App - Docker + Kubernetes

This project is a **Simple Python Web Application** that runs an HTTP server and is deployed inside a **Docker container** or on **Kubernetes**.  
The app exposes port **80** (inside the container) and is mapped to **8080** on the host and returns a "Hello World" message.   

---

## ✨ Features

* Lightweight Python HTTP server (`http.server`)  
* Containerized with **Docker**  
* Deployable on **Kubernetes** using a **Deployment** and **Service**  
* Exposed inside the cluster using a **Service** 
* Access via **port 8080** on the host  
* Accessible from host via `kubectl port-forward`  
* Scalable (replicas managed by Kubernetes)  

---

## 🏗️ Project Structure

```
python-k8s-app/
├── app.py             # Main Python web app
├── Dockerfile         # Docker image instructions
├── deployment.yaml    # Kubernetes Deployment manifest
├── service.yaml       # Kubernetes Service manifest
└── README.md          # Documentation
```

---

## 📐 Project Architecture

```
+---------+        +-------------+        +------------+        +----------+
| Client  | <----> | Kubernetes  | <----> |   Pod(s)   | <----> | Python   |
| (curl / |        |  Service    |        | Deployment |        | HTTP App |
| browser)|        | ClusterIP   |        |  (3 pods)  |        |   :80    |
+---------+        +-------------+        +------------+        +----------+
        ^                                                      
        |                                                      
        Port-forward (from localhost:8080 → :80)                               
```

---

## 🔧 Setup Steps

### 1. 🐳 Run with Docker (Local Test)

#### Build the Image
```bash
docker build -t my-python-app .
```

#### Run the Container
```bash
docker run --rm -p 8080:80 ayahelhwary/my-python-app:4.0
```
or 
Manually:
```bash
docker run -it --rm -p 8080:8080 ayahelhwary/my-python-app:4.0 bash
python app.py
```

#### Test the App
```bash
curl http://localhost:8080
```

✅ Expected output:
```
Hello from my Dockerized Python Web App!
```

---

### 2. ☸️ Run on Kubernetes

#### Push Image to DockerHub
```bash
docker tag my-python-app <your-dockerhub-username>/my-python-app:3.0
docker push <your-dockerhub-username>/my-python-app:3.0
```

#### Apply Deployment
```bash
kubectl apply -f deployment.yaml
kubectl get deployments
kubectl get pods
```

#### Apply Service
```bash
kubectl apply -f service.yaml
kubectl get svc
```

#### Access the App (Port Forwarding)
```bash
kubectl port-forward service/python-app-service 8080:80
```

Now open in another terminal:
```bash
curl http://localhost:8080
```

✅ Output:
```
Hello from my Dockerized Python Web App!
```

---
**Note**
Host:8080  --->  Service:80  --->  Pod:8080  --->  Container:80

---
## ✅ Done!
Your Python web app is now:  
- Runnable locally with Docker  
- Deployable and accessible on Kubernetes  
