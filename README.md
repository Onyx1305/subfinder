# 🔍 Subdomain Finder - Enhanced (Multithreaded)

A fast and simple Python tool to discover subdomains using a wordlist.  
It supports multithreading, timeout control, colored output, and graceful exit on `Ctrl+C`.

---

## 🚀 Features

- ✅ Multithreaded subdomain scanning
- ✅ Timeout handling for each request
- ✅ Colored terminal output using `colorama`
- ✅ Graceful exit on user interruption (`Ctrl+C`)
- ✅ Saves discovered subdomains to output file if specified

---

## 🛠️ Requirements

- Python 3.6+
- Modules:
  - `requests`
  - `colorama`

Install dependencies:

```bash
pip install -r requirements.txt
```

Or manually:

```bash
pip install requests colorama
```

---

## 📂 Usage

```bash
python subfinder.py example.com -w wordlist.txt -t 30 --timeout 3 -o results.txt
```

### 🔧 Arguments

| Argument           | Description                              | Default          |
|--------------------|------------------------------------------|------------------|
| `domain`           | The target domain                        | *(required)*     |
| `-w`, `--wordlist` | Path to the subdomain wordlist file      | `subdomains.txt` |
| `-t`, `--threads`  | Number of threads to use                 | `20`             |
| `--timeout`        | Timeout for each request (in seconds)    | `2`              |
| `-o`, `--output`   | Output file to save discovered subdomains | `None`           |

---

## 📝 Example

```bash
python subfinder.py google.com -w subdomains.txt -t 50 --timeout 2 -o found.txt
```

---

## 📄 Output

Discovered subdomains with status code `200` are saved in the specified output file.

---

## 💡 Notes

- Make sure to provide a valid `subdomains.txt` wordlist.

---

## 📜 License

This project is open-source and free to use for educational and personal use.

---

## 🙋 Author

**Dipon (aka Onyx)**  
Feel free to contribute, suggest features, or report issues.
