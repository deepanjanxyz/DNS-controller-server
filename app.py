from flask import Flask, jsonify
import requests
import re

app = Flask(__name__)

# হ্যাকার লিস্টের সোর্স (তুই চাইলে আরও বাড়াতে পারিস)
SOURCES = [
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn/hosts",
    "https://adaway.org/hosts.txt"
]

def get_hacker_list():
    unique_domains = set()
    
    for url in SOURCES:
        try:
            print(f"Downloading from {url}...")
            response = requests.get(url)
            if response.status_code == 200:
                # 0.0.0.0 domain.com প্যাটার্ন খোঁজা
                matches = re.findall(r'0\.0\.0\.0\s+([\w\.-]+)', response.text)
                unique_domains.update(matches)
        except Exception as e:
            print(f"Error downloading {url}: {e}")
            
    return list(unique_domains)

@app.route('/')
def home():
    return "ABS VPN Server is Running! 🚀"

@app.route('/api/blocklist')
def blocklist():
    # সার্ভার লেটেস্ট লিস্ট নামিয়ে ক্লিন করে অ্যাপকে দেবে
    domains = get_hacker_list()
    return jsonify({
        "total_rules": len(domains),
        "domains": domains
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
  
