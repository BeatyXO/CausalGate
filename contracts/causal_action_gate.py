# { "Depends": "py-genlayer:1jb45aa8ynh2a9c9xn3b7qqh8sm5q93hwfp7jqmwsfhh8jpz09h6" }
"""Typed CausalGate consumer with definition pinning and action replay protection."""

from genlayer import *

ZERO_ADDRESS = "0x" + ("0" * 40)

@gl.contract_interface
class ICausalGate:
    class View:
        def is_attributed(self, case_id: u256, candidate_id: u32, expected_definition_hash: str) -> bool: ...
        def is_exclusively_attributed(self, case_id: u256, candidate_id: u32, expected_definition_hash: str) -> bool: ...
    class Write:
        pass

class CausalActionConsumed(gl.Event):
    def __init__(self, action_hash: str, case_id: u256, candidate_id: u32, /, **blob): ...

def valid_hash(value: str) -> bool:
    s = str(value).lower().strip()
    return len(s) == 64 and all(c in "0123456789abcdef" for c in s)

class CausalActionGate(gl.Contract):
    causal_gate: Address
    consumed: TreeMap[str, bool]

    def __init__(self, causal_gate: Address):
        if str(causal_gate).lower() == ZERO_ADDRESS:
            raise gl.vm.UserError("CausalGate address cannot be zero")
        self.causal_gate = causal_gate

    @gl.public.write
    def consume(self, case_id: u256, candidate_id: u32, expected_definition_hash: str, action_hash: str, require_exclusive: bool) -> bool:
        definition_hash = str(expected_definition_hash).lower().strip()
        action = str(action_hash).lower().strip()
        if not valid_hash(definition_hash):
            raise gl.vm.UserError("expected_definition_hash must be 64 hex")
        if not valid_hash(action):
            raise gl.vm.UserError("action_hash must be 64 hex")
        if self.consumed.get(action, False):
            raise gl.vm.UserError("action already consumed")

        if require_exclusive:
            allowed = ICausalGate(self.causal_gate).view().is_exclusively_attributed(case_id, candidate_id, definition_hash)
        else:
            allowed = ICausalGate(self.causal_gate).view().is_attributed(case_id, candidate_id, definition_hash)
        if not allowed:
            raise gl.vm.UserError("causal attribution requirement not satisfied")

        self.consumed[action] = True
        CausalActionConsumed(action, case_id, candidate_id).emit(definition_hash=definition_hash, require_exclusive=require_exclusive)
        return True

    @gl.public.view
    def is_consumed(self, action_hash: str) -> bool:
        action = str(action_hash).lower().strip()
        if not valid_hash(action): return False
        return self.consumed.get(action, False)
