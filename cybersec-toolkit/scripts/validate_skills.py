#!/usr/bin/env python3
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
skills = sorted((ROOT / '.hermes' / 'skills').glob('*/SKILL.md'))
errors = []

for f in skills:
    text = f.read_text(encoding='utf-8')
    lines = text.splitlines()
    if not text.startswith('---\n'):
        errors.append(f'{f}: missing frontmatter')
        continue
    try:
        end = lines[1:].index('---') + 1
    except ValueError:
        errors.append(f'{f}: unclosed frontmatter')
        continue
    fm = '\n'.join(lines[1:end])
    m_name = re.search(r'^name:\s*(.+)$', fm, re.M)
    m_desc = re.search(r'^description:\s*(.+)$', fm, re.M)
    if not m_name or not m_desc:
        errors.append(f'{f}: missing name or description')
        continue
    name = m_name.group(1).strip()
    desc = m_desc.group(1).strip()
    if len(name) > 64 or not re.fullmatch(r'[a-z0-9-]+', name):
        errors.append(f'{f}: invalid name {name!r}')
    if len(desc) > 1024:
        errors.append(f'{f}: description too long')
    if len(lines) > 500:
        errors.append(f'{f}: too many lines {len(lines)}')

print(f'skills={len(skills)}')
if errors:
    print('\n'.join(errors))
    sys.exit(1)
print('VALIDATION_OK')
