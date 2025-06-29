import json
import requests
import time

API_URL = 'http://localhost:8000/api/code'
SAMPLE_FILE = 'bigcode_sample.json'
RESULTS_FILE = 'bigcode_results.json'

with open(SAMPLE_FILE, 'r') as f:
    samples = [json.loads(line) for line in f if line.strip()]

results = []
for i, entry in enumerate(samples):
    code = entry.get('content', '')
    payload = {
        'code': code,
        'language': 'python',
        'action': 'execute',
    }
    t0 = time.time()
    try:
        resp = requests.post(API_URL, json=payload, timeout=30)
        elapsed = time.time() - t0
        data = resp.json() if resp.ok else {'error': resp.text}
    except Exception as e:
        elapsed = time.time() - t0
        data = {'error': str(e)}
    results.append({
        'id': entry.get('id'),
        'sha1': entry.get('sha1'),
        'code': code,
        'result': data,
        'elapsed': elapsed,
    })
    if (i+1) % 25 == 0:
        print(f"Processed {i+1}/{len(samples)}...")

with open(RESULTS_FILE, 'w') as f:
    json.dump(results, f, indent=2)

print(f"Done. Results saved to {RESULTS_FILE}") 