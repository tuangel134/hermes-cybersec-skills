#!/usr/bin/env python3
"""Sync CyberSec Toolkit tools_config.json into this skill package.

Usage:
  python3 scripts/sync_cybersec_toolkit.py --repo ~/cybersec-toolkit
  python3 scripts/sync_cybersec_toolkit.py --clone-to /tmp/cybersec-toolkit
"""
import argparse, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'references' / 'tool-registry-current.json'
URL = 'https://github.com/26zl/cybersec-toolkit.git'

def run(cmd):
    return subprocess.run(cmd, check=True, text=True)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--repo', help='Existing local cybersec-toolkit repo')
    ap.add_argument('--clone-to', help='Clone upstream repo here if --repo is not provided')
    args = ap.parse_args()

    if args.repo:
        repo = Path(args.repo).expanduser().resolve()
    else:
        repo = Path(args.clone_to or '/tmp/cybersec-toolkit').expanduser().resolve()
        if not repo.exists():
            run(['git', 'clone', '--depth=1', URL, str(repo)])
        else:
            run(['git', '-C', str(repo), 'pull', '--ff-only'])

    cfg = repo / 'tools_config.json'
    if not cfg.exists():
        raise SystemExit(f'tools_config.json not found in {repo}')
    data = json.loads(cfg.read_text())
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False) + '
')
    modules = sorted({x.get('module','') for x in data})
    print(f'wrote {OUT} tools={len(data)} modules={len(modules)}')
    for module in modules:
        print(f'{module}: {sum(1 for x in data if x.get("module")==module)}')

if __name__ == '__main__':
    main()
