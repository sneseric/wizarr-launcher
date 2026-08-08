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

## Reverse Proxy & Remote Access Setup

This setup routes external traffic through a Caddy reverse proxy over HTTPS (Port 443) using DuckDNS subdomains. Caddy automatically provisions SSL certificates via Let's Encrypt / ZeroSSL, while DuckDNS keeps our subdomains mapped to our home IP address.

---

### 1. Prerequisites: DuckDNS & Caddy Installation

#### Step A: Set Up DuckDNS Subdomains
1. Go to https://www.duckdns.org and log in.
2. Under the subdomains section, create your subdomains (e.g., for Plex, Wizarr, and Status).
3. Note down your DuckDNS Token.

#### Step B: Install Caddy on Windows
1. Download the Windows binary from https://caddyserver.com/download.
2. Create a folder at C:\caddy on your host machine.
3. Move the downloaded executable into C:\caddy and rename it to caddy.exe.
4. Add C:\caddy to your Windows System PATH environment variables.
5. Create your configuration file named Caddyfile inside C:\caddy.

---

### 2. Port Forwarding
Forward standard web ports on your router to your host machine's local IP:
* TCP Port 80 (HTTP - SSL validation)
* TCP Port 443 (HTTPS - secure traffic)

---

### 3. Caddy Reverse Proxy Setup (Caddyfile)
Create or update C:\caddy\Caddyfile:

```
# Main Plex Reverse Proxy
[INSERT_PLEX_SUBDOMAIN].duckdns.org {
    reverse_proxy 127.0.0.1:32400
}

# Wizarr Invites
[INSERT_INVITE_SUBDOMAIN].duckdns.org {
    reverse_proxy 127.0.0.1:5690
}

# Legacy / Status URL
[INSERT_STATUS_SUBDOMAIN].duckdns.org {
    reverse_proxy 127.0.0.1:32400
}
```

Open PowerShell or Command Prompt and reload Caddy:
```
caddy reload --config C:\caddy\Caddyfile
```

---

### 4. Dynamic DNS Maintenance (DuckDNS PowerShell Script)
Create a PowerShell script named duckdns-update.ps1 to update DuckDNS when your IP changes:

```
$Token = "[INSERT_DUCKDNS_TOKEN]"
$URL = "https://www.duckdns.org/update?domains=[INSERT_SUBDOMAIN_1],[INSERT_SUBDOMAIN_2],[INSERT_SUBDOMAIN_3]&token=$Token"
Invoke-RestMethod -Uri $URL
```

---

### 5. Plex UI Configuration
1. Open Plex Web -> Settings -> Network:
2. Change `Secure Connections` to `Required`
2. Set Custom server access URLs to:
   ```
   https://[INSERT_PLEX_SUBDOMAIN].duckdns.org
   ```
3. Save Changes.

---

### 6. Wizarr Setup
1. Open Wizarr: `https://[INSERT_INVITE_SUBDOMAIN].duckdns.org`
2. Go to Settings -> Servers and edit your Plex server:
   * URL (Internal): `http://host.docker.internal:32400`
   * External URL: `https://[INSERT_PLEX_SUBDOMAIN].duckdns.org`
   * API Key: Enter your Plex Authentication Token (X-Plex-Token).

---

### 7. Sharing Invite Links
Generated invite links automatically use your HTTPS domain:
* Wizarr Dashboard Access: https://[INSERT_INVITE_SUBDOMAIN].duckdns.org
* Invite Format: https://[INSERT_INVITE_SUBDOMAIN].duckdns.org/j/[INSERT_INVITE_CODE]