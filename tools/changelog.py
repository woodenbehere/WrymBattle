#!/usr/bin/env python3
"""Rebuild the CHANGELOG list inside index.html from git history.
Usage: python3 tools/changelog.py [vX.Y.Z "what changed"]   (the optional pair adds the release being made now)"""
import re, subprocess, sys, json, datetime, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from rename import scrub
root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
log = subprocess.run(['git', 'log', '--reverse', '--format=%aI\t%s'], cwd=root, capture_output=True, text=True).stdout.splitlines()
seen, out = set(), []
def add(v, when, msg):
    if v in seen: return
    seen.add(v); msg = scrub(msg.strip().rstrip('.')); out.append({'v': v, 't': when, 'd': msg[:1].upper() + msg[1:]})
for line in log:
    when, s = line.split('\t', 1)
    if re.match(r'(Redeploy|Retrigger|README)', s): continue
    m = re.match(r'v(\d+\.\d+\.\d+):\s*(.+)', s) or None
    if m: add(m.group(1), when, m.group(2)); continue
    m = re.match(r'(.+?)\s*\(v(\d+\.\d+\.\d+)\)\s*$', s)
    if m: add(m.group(2), when, m.group(1)); continue
    if s.startswith('Add Ember Wyrm'): add('1.0.0', when, 'First release: the Ember Wyrm battle, installable as an app')
if len(sys.argv) == 3:
    add(sys.argv[1].lstrip('v'), datetime.datetime.now().astimezone().isoformat(timespec='seconds'), sys.argv[2])
out.reverse()
p = os.path.join(root, 'index.html'); html = open(p).read()
new = '/*CHANGELOG*/' + json.dumps(out, ensure_ascii=False, separators=(',', ':')) + '/*/CHANGELOG*/'
html, n = re.subn(r'/\*CHANGELOG\*/.*?/\*/CHANGELOG\*/', lambda m: new, html, flags=re.S)
assert n == 1, 'marker missing'
open(p, 'w').write(html); print(len(out), 'entries; newest', out[0]['v'])
