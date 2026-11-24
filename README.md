# NIDS (Network Intrusion Detection System)

A Network Intrusion Detection System featuring a distributed client-agent and centralized server architecture, containerized with Docker for easy deployment and monitoring.

## Project Structure

```text
NIDS/
├── client-agent/           # Client-side network traffic capture and monitoring agent
├── server/                 # Central server for threat analysis, logging, and dashboard
├── docker-compose.yml      # Multi-container Docker orchestration
├── structure.txt           # Project architecture and directory layout
└── README.md               # Project documentation
```

## Features

- **Client-Agent Monitoring:** Captures and forwards network traffic/events from monitored hosts (`client-agent/`).
- **Centralized Detection Server:** Processes incoming data, detects suspicious network activity, and manages alerts (`server/`).
- **Containerized Deployment:** Quick setup and orchestration using `docker-compose.yml`.

## Prerequisites

- [Docker](https://docker.com) and [Docker Compose](https://docker.com)
- Git

## Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mr-Rohan-tech/NIDS.git
   cd NIDS
   ```

2. **Start the services using Docker Compose:**
   ```bash
   docker-compose up --build -d
   ```

3. **Verify running containers:**
   ```bash
   docker-compose ps
   ```

## Usage

- **Server & Dashboard:** Access the server interface or API once the containers are running (update this line with your configured port, e.g., `http://localhost:8000`).
- **Client Agent:** Configure the client agent inside `client-agent/` to point to your server's IP address and start monitoring network traffic.
- **Stop the system:**
  ```bash
  docker-compose down
  ```

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the [issues page](https://github.com) or submit a pull request.

## License

This project is open-source. Specify your preferred license (e.g., MIT License) here.
