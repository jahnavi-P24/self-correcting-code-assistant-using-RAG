import json
import requests
import time

API_URL = 'http://localhost:8000/api/code'
SAMPLE_FILE = 'mbpp_sample.json'
RESULTS_FILE = 'mbpp_results.json'

with open(SAMPLE_FILE, 'r') as f:
    samples = json.load(f)

results = []
for i, entry in enumerate(samples):
    code = entry['code']
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
        'task_id': entry.get('task_id'),
        'description': entry.get('text'),
        'code': code,
        'result': data,
        'time': elapsed,
    })
    print(f"[{i+1}/{len(samples)}] Task {entry.get('task_id')}: {data.get('error') or 'OK'} ({elapsed:.2f}s)")

with open(RESULTS_FILE, 'w') as f:
    json.dump(results, f, indent=2)

print(f"\nResults saved to {RESULTS_FILE}") 