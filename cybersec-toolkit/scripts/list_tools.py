#!/usr/bin/env python3
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRENT = ROOT / 'references' / 'tool-registry-current.json'
SEED = ROOT / 'references' / 'tool-registry-seed.json'

def main():
    ap = argparse.ArgumentParser(description='List CyberSec Toolkit tools from local registry.')
    ap.add_argument('--module', default='', help='Filter by module')
    ap.add_argument('--json', action='store_true', help='Output JSON')
    args = ap.parse_args()
    path = CURRENT if CURRENT.exists() else SEED
    data = json.loads(path.read_text())
    if args.module:
        data = [x for x in data if x.get('module') == args.module]
    if args.json:
        print(json.dumps(data, indent=2))
    else:
        for item in data:
            url = f" {item.get('url')}" if item.get('url') else ''
            print(f"{item.get('module'):12} {item.get('name')}{url}")
        print(f"count={len(data)} source={path.name}")

if __name__ == '__main__':
    main()
