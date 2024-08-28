# Subdomain Enumeration Tool

## Description
This Python script is a subdomain enumeration tool that helps identify valid subdomains for a given domain by using a wordlist. It sends HTTP requests to potential subdomains and reports those that return a 200 OK status, indicating the subdomain is active.

## Features
- Enumerates subdomains for a given domain.
- Uses a custom wordlist or a default `subdomains.txt` file.
- Displays valid subdomains that respond with a status code of 200.

## Requirements
- Python 3.x
- Required Python modules: `requests`, `argparse`

## Installation
1. Clone the repository to your local machine:

