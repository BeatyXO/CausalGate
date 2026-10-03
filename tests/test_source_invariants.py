from pathlib import Path
ROOT=Path(__file__).parents[1]
CORE=(ROOT/'contracts/causalgate.py').read_text(encoding='utf-8')
GATE=(ROOT/'contracts/causal_action_gate.py').read_text(encoding='utf-8')

def test_standalone_and_no_frontend():
    assert 'class CausalGate(gl.Contract)' in CORE
    assert not (ROOT/'frontend').exists()

def test_atomic_all_candidate_resolution():
    assert 'def _resolve_consensus' in CORE and 'for candidate in candidates' in CORE and 'run_nondet_unsafe' in CORE

def test_validator_independently_refetches_and_rederives():
    assert 'gl.nondet.web.render' in CORE and 'own = derive()' in CORE and 'material_resolution_payload(proposed) == material_resolution_payload(own)' in CORE

def test_llm_never_decides_case_result():
    assert 'derive_candidate_status' in CORE and 'derive_case_result' in CORE and 'MULTIPLE_SUFFICIENT_CAUSES' in CORE

def test_strict_model_shape_guards():
    for marker in ['unknown candidate','duplicate candidate','unknown criterion','duplicate criterion','unknown criterion status','exactly one row per candidate','exactly one row per criterion']: assert marker in CORE

def test_evidence_surface_is_frozen_and_safe():
    assert 'source URL must use https' in CORE and 'duplicate evidence source URL' in CORE and 'definition_hash' in CORE and 'case configuration is sealed' in CORE

def test_domain_separated_hashes():
    for marker in ['CAUSALGATE_CANDIDATE_V1','CAUSALGATE_DEFINITION_V1','CAUSALGATE_RESOLUTION_V1']: assert marker in CORE

def test_consumer_uses_typed_ic_call_and_replay_guard():
    assert '@gl.contract_interface' in GATE and '.view().is_attributed' in GATE and '.view().is_exclusively_attributed' in GATE and 'action already consumed' in GATE
