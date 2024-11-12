# Dynamic DNS Updater

This script is designed to dynamically update a DNS record's IP address with your public IP address on a configured schedule. The script uses the [GoDaddyPy](https://github.com/ebinel/godaddypy) library to interact with the GoDaddy API for managing DNS records. It checks for changes in your public IP and updates the DNS record accordingly.

## Features
- Automatically updates a specified DNS record with the current public IP address.
- Configurable logging with file rotation.
- Runs at a specified interval using the `schedule` library.
- Creates the DNS record if it doesn't exist.
- Uses GoDaddy API for DNS management.

## Requirements

- Python 3.x
- `schedule` (for task scheduling)
- `pif` (to retrieve the public IP address)
- `godaddypy` (to interact with GoDaddy's DNS API)

## Logging

The logging configuration is set up with a rotating file handler:
- **Log file path**: `./log/dns_scheduler.log`
- **Log rotation**: The log file will rotate when it reaches 5MB, keeping up to two backup logs.

## Schedule Configuration

Currently, the DNS update check runs every 5 seconds. To change this frequency, modify the `schedule.every(5).seconds.do(job)` line in the code.

## Troubleshooting

- **DNS not updating**: Ensure your GoDaddy API credentials are correct and have permission to modify DNS settings.
- **Logs not appearing**: Check that the `./log` directory exists and has write permissions.

## Setup Instructions

1. Install the required libraries:
```bash
   pip install schedule pif godaddypy
```

2. Clone this repository to your local machine.

3. Replace the following placeholder values in the script:

  <DOMAIN>: The domain name you want to manage (e.g., example.com).
  <SUB DOMAIN>: The subdomain (e.g., www, api) you want to update. Leave empty if it’s the root domain.
  PUB_KEY and SEC_KEY: Your GoDaddy API key and secret key, respectively.
  IP ADDR: Optionally, specify a static IP. The script will retrieve the IP automatically if this is left empty.

4. Run the script:
```bash
python3 dns_scheduler.py
```
