from __future__ import annotations
import ast, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FINAL='--final' in sys.argv
errors=[]
required=['README.md','SUBMISSION.md','DEPLOYMENT.md','BUILD_STATUS.md','AGENT_HANDOFF.md','docs/ARCHITECTURE.md','docs/INVARIANTS.md','docs/SECURITY.md','contracts/causalgate.py','contracts/causal_action_gate.py','tests/test_causalgate.py','tests/test_source_invariants.py','tests/test_live_studionet.py','fixtures/provider_incident.txt','fixtures/deployment_report.txt','fixtures/traffic_report.txt','proof/VERIFICATION_CHECKLIST.md']
for rel in required:
    if not (ROOT/rel).exists(): errors.append('missing required file: '+rel)
for rel in ['contracts/causalgate.py','contracts/causal_action_gate.py']:
    p=ROOT/rel
    if not p.exists(): continue
    src=p.read_text(encoding='utf-8')
    try: ast.parse(src)
    except SyntaxError as e: errors.append(f'syntax error in {rel}: {e}')
    if 'py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6' not in src: errors.append('unexpected dependency pin in '+rel)
core=(ROOT/'contracts/causalgate.py').read_text(encoding='utf-8')
for marker in ['run_nondet_unsafe','gl.nondet.web.render','response_format="json"','derive_candidate_status','derive_case_result','MULTIPLE_SUFFICIENT_CAUSES','CAUSALGATE_DEFINITION_V1','CAUSALGATE_RESOLUTION_V1','model returned duplicate candidate','model returned duplicate criterion','min_sources_available']:
    if marker not in core: errors.append('missing core marker: '+marker)
gate=(ROOT/'contracts/causal_action_gate.py').read_text(encoding='utf-8')
for marker in ['@gl.contract_interface','.view().is_attributed','.view().is_exclusively_attributed','action already consumed']:
    if marker not in gate: errors.append('missing consumer marker: '+marker)
if (ROOT/'frontend').exists(): errors.append('frontend directory present')
for p in ROOT.rglob('*'):
    if not p.is_file(): continue
    rel=p.relative_to(ROOT)
    if p.name in {'.env','id_rsa','id_ed25519'}: errors.append('sensitive file present: '+str(rel))
    if any(x in {'.venv','venv','__pycache__','.pytest_cache','node_modules'} for x in rel.parts): errors.append('generated/cache directory present: '+str(rel))
    if p.suffix in {'.pyc','.pyo'}: errors.append('compiled artifact present: '+str(rel))
network='\n'.join(p.read_text(encoding='utf-8',errors='ignore') for p in ROOT.rglob('*') if p.is_file() and p.resolve()!=Path(__file__).resolve() and p.suffix in {'.md','.py','.yaml','.yml','.txt'})
if 'https://studio.genlayer.com/api' not in network: errors.append('stable Studionet RPC reference missing')
if '61999' not in network: errors.append('stable Studionet chain ID reference missing')
if FINAL:
    if 'FIXTURE_COMMIT_PLACEHOLDER' in network: errors.append('fixture commit placeholder remains')
    dep=(ROOT/'DEPLOYMENT.md').read_text(encoding='utf-8')
    if 'PENDING' in dep: errors.append('DEPLOYMENT.md still contains PENDING proof')
if errors:
    print('PREFLIGHT FAIL'); [print(' -',e) for e in errors]; raise SystemExit(1)
print('PREFLIGHT PASS')
print(' - required repository files present')
print(' - contract Python parses')
print(' - stable dependency pin present')
print(' - causal consensus / deterministic derivation / consumer markers present')
print(' - no frontend directory')
print(' - no obvious sensitive/generated artifacts')
print(' - stable Studionet / chain 61999 references present')
if not FINAL: print(' - handoff mode: deployment placeholders permitted')
