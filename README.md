# Apache NiFi Tutorial with Docker Compose

This project provides a Docker Compose configuration to quickly spin up an instance of Apache NiFi using Docker. The setup is designed to run Apache NiFi on `localhost` using the default ports.

---

## 🚀 Prerequisites

Before you begin, ensure that you have the following installed:

- **Docker**: A platform for developing, shipping, and running applications in containers.  
  🔗 [Installation Guide](https://docs.docker.com/get-docker/)

- **Docker Compose**: A tool for defining and running multi-container Docker applications.  
  🔗 [Installation Guide](https://docs.docker.com/compose/install/)

---

## 🛠️ Getting Started

### 1. Clone the Repository

If you are working with a Git repository for your project, clone it to your local machine. Skip this step if you are setting up the project independently.

```bash
git clone https://github.com/Shiavnski-Technologies-LLP/apache-nifi.git
cd your-repository-folder
```


---

### 2. Start the NiFi Service

Use Docker Compose to start Apache NiFi. Run the following command in your project directory:

```bash
docker-compose up -d
```

- The `-d` flag runs the containers in detached mode (in the background).  
- Once the containers are running, you can access the NiFi web UI at:  
  **http://localhost:8080**

---

### 3. Verify the Setup

To ensure the service is running, use the following command:

```bash
docker ps
```

This will display all running containers. You should see the `nifi` container listed.

---

### 4. Stop the NiFi Service

To stop the NiFi service, run:

```bash
docker-compose down
```

This will stop and remove all containers defined in the `docker-compose.yml` file.

---

## 🪒 Additional Commands

Here are some useful Docker commands for managing your NiFi container:

- **View Logs**:  
  ```bash
  docker logs -f nifi
  ```
  Use this command to view real-time logs of the NiFi container.

- **Restart Container**:  
  ```bash
  docker restart nifi
  ```

- **Remove Unused Resources**:  
  ```bash
  docker system prune -f
  ```

---

## 📚 Documentation & Resources

- **Apache NiFi Documentation**:  
  [https://nifi.apache.org/docs.html](https://nifi.apache.org/docs.html)

- **Docker Hub (Apache NiFi)**:  
  [https://hub.docker.com/r/apache/nifi](https://hub.docker.com/r/apache/nifi)

---

### 🌟 Enjoy your journey with Apache NiFi and Docker Compose! 🌟
