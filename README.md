# Wizarr Docker Launcher

Automated Docker launcher script that spins up Wizarr in a local container and opens the setup wizard in your default browser upon startup.

Wizarr is a self-hosted tool that automates and simplifies inviting new users to your Plex media server. It generates unique, shareable invite links so friends and family can join your server without manual setup hassles.

## Prerequisites

Ensure the following tools are installed before setup:
* Docker Desktop (must be running on Windows/Mac/Linux)
* Git
* Python 3.8+

---

## Project Structure

```text
wizarr-launcher/
├── docker-compose.yml
├── requirements.txt
├── start.py
└── README.md
```

---

## Setup Instructions

1. Clone the Repository:
```bash
git clone https://github.com/sneseric/wizarr-launcher 

2. Navigate to Project Directory:
```bash
cd wizarr-launcher
```

3. Install Dependencies:
```bash
pip install -r requirements.txt
```

4. Run the Launcher:
```bash
python start.py
```
 