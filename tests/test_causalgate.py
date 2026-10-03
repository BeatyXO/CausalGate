"""Direct Mode/adversarial tests for CausalGate."""
import json
import pytest
pytest.importorskip("gltest", reason="genlayer-test is required for Direct Mode")

CONTRACT='contracts/causalgate.py'
PROMPT=r'CAUSALGATE / CAUSAL STANDARD APPLICATION'
URL1='https://evidence.example/provider'
URL2='https://evidence.example/deploy'
URL3='https://evidence.example/traffic'
PROVIDER='Nimbus regional networking outage caused Alpha Marketplace unavailability.'
DEPLOY='The prior Alpha software deployment caused the outage.'
DDOS='A denial-of-service attack caused the outage.'
PAGE1='Nimbus outage 09:58-11:29. Alpha failed 10:02-11:34 and recovered after Nimbus networking recovered.'
PAGE2='Deployment completed previous evening. Same version recovered without rollback after Nimbus recovery.'
PAGE3='Normal traffic. No DDoS alert or mitigation. Failures were upstream dependency connectivity.'

def criteria():
    return json.dumps([
        {'key':'temporal_link','mode':'REQUIRED','expected':'SUPPORTED','question':'Did the candidate cause precede and overlap the outcome in a causally relevant way?'},
        {'key':'mechanism_link','mode':'REQUIRED','expected':'SUPPORTED','question':'Does the evidence support a concrete mechanism connecting this candidate to the outcome?'},
        {'key':'scope_link','mode':'REQUIRED','expected':'SUPPORTED','question':'Does the affected scope of this candidate align with the observed outcome?'},
        {'key':'independent_alternative','mode':'REQUIRED','expected':'CONTRADICTED','question':'Is there an independently sufficient alternative cause that explains this outcome instead of this candidate?'},
        {'key':'contemporaneous_reporting','mode':'SUPPORTING','expected':'SUPPORTED','question':'Is the candidate supported by contemporaneous incident evidence?'}
    ])

def result(provider=('SUPPORTED','SUPPORTED','SUPPORTED','CONTRADICTED','SUPPORTED'), deploy=('SUPPORTED','CONTRADICTED','CONTRADICTED','SUPPORTED','CONTRADICTED'), ddos=('CONTRADICTED','CONTRADICTED','CONTRADICTED','SUPPORTED','CONTRADICTED')):
    keys=['temporal_link','mechanism_link','scope_link','independent_alternative','contemporaneous_reporting']
    out=[]
    for cid, vals in [(1,provider),(2,deploy),(3,ddos)]:
        out.append({'candidate_id':cid,'criteria':[{'key':k,'status':s,'note':f'{k} evidence'} for k,s in zip(keys,vals)]})
    return {'candidates':out}

def deploy(direct_vm,direct_deploy):
    direct_vm.check_pickling=True
    return direct_deploy(CONTRACT)

def configure(direct_vm,direct_deploy):
    c=deploy(direct_vm,direct_deploy)
    case=c.create_case('Alpha outage','Alpha Marketplace was unavailable from 10:02 to 11:34 UTC.',criteria(),1,2)
    c.add_evidence_source(case,'provider incident',URL1)
    c.add_evidence_source(case,'deployment report',URL2)
    c.add_evidence_source(case,'traffic report',URL3)
    c.add_candidate(case,'provider_outage',PROVIDER)
    c.add_candidate(case,'deployment',DEPLOY)
    c.add_candidate(case,'ddos',DDOS)
    definition=c.seal_case(case)
    return c,case,definition

def mock_sources(vm):
    vm.mock_web(r'evidence\.example/provider',{'status':200,'body':PAGE1})
    vm.mock_web(r'evidence\.example/deploy',{'status':200,'body':PAGE2})
    vm.mock_web(r'evidence\.example/traffic',{'status':200,'body':PAGE3})

def test_draft_configuration_and_seal(direct_vm,direct_deploy):
    c,case,definition=configure(direct_vm,direct_deploy)
    assert len(definition)==64
    item=c.get_case(case)
    assert item['status_name']=='SEALED'
    assert len(item['sources'])==3 and len(item['candidates'])==3
    with direct_vm.expect_revert('case configuration is sealed'):
        c.add_candidate(case,'late','late candidate')

def test_only_creator_can_configure(direct_vm,direct_deploy,direct_alice):
    c=deploy(direct_vm,direct_deploy)
    case=c.create_case('x','outcome',criteria(),1,1)
    with direct_vm.prank(direct_alice):
        with direct_vm.expect_revert('only case creator may configure draft'):
            c.add_candidate(case,'x','cause')

def test_duplicate_keys_urls_and_private_urls_rejected(direct_vm,direct_deploy):
    c=deploy(direct_vm,direct_deploy)
    case=c.create_case('x','outcome',criteria(),1,1)
    c.add_evidence_source(case,'a',URL1)
    with direct_vm.expect_revert('duplicate evidence source URL'):
        c.add_evidence_source(case,'b',URL1)
    with direct_vm.expect_revert('source URL must use https'):
        c.add_evidence_source(case,'bad','http://example.com')
    with direct_vm.expect_revert('source URL host is not public'):
        c.add_evidence_source(case,'bad','https://127.0.0.1/test')
    c.add_candidate(case,'cause_a','cause a')
    with direct_vm.expect_revert('duplicate candidate key'):
        c.add_candidate(case,'CAUSE_A','cause b')

def test_exclusive_provider_attribution(direct_vm,direct_deploy):
    c,case,definition=configure(direct_vm,direct_deploy)
    mock_sources(direct_vm); direct_vm.mock_llm(PROMPT,result())
    rh=c.resolve_case(case)
    assert direct_vm.run_validator() is True
    assert len(rh)==64
    r=c.get_resolution(case)
    assert r['result_name']=='ATTRIBUTED' and r['winning_candidate_id']==1
    assert c.is_attributed(case,1,definition) is True
    assert c.is_exclusively_attributed(case,1,definition) is True
    assert c.is_attributed(case,2,definition) is False

def test_multiple_sufficient_causes_not_forced_to_one_winner(direct_vm,direct_deploy):
    c,case,definition=configure(direct_vm,direct_deploy)
    mock_sources(direct_vm)
    both=('SUPPORTED','SUPPORTED','SUPPORTED','CONTRADICTED','SUPPORTED')
    direct_vm.mock_llm(PROMPT,result(provider=both,deploy=both))
    c.resolve_case(case)
    r=c.get_resolution(case)
    assert r['result_name']=='MULTIPLE_SUFFICIENT_CAUSES' and r['winning_candidate_id']==0
    assert c.is_attributed(case,1,definition) is True
    assert c.is_attributed(case,2,definition) is True
    assert c.is_exclusively_attributed(case,1,definition) is False

def test_required_ambiguity_produces_indeterminate(direct_vm,direct_deploy):
    c,case,_=configure(direct_vm,direct_deploy); mock_sources(direct_vm)
    uncertain=('SUPPORTED','AMBIGUOUS','SUPPORTED','CONTRADICTED','SUPPORTED')
    direct_vm.mock_llm(PROMPT,result(provider=uncertain)); c.resolve_case(case)
    assert c.get_resolution(case)['result_name']=='INDETERMINATE'

def test_all_rejected_produces_not_attributed(direct_vm,direct_deploy):
    c,case,_=configure(direct_vm,direct_deploy); mock_sources(direct_vm)
    bad=('CONTRADICTED','CONTRADICTED','CONTRADICTED','SUPPORTED','CONTRADICTED')
    direct_vm.mock_llm(PROMPT,result(provider=bad,deploy=bad,ddos=bad)); c.resolve_case(case)
    assert c.get_resolution(case)['result_name']=='NOT_ATTRIBUTED'

def test_model_unknown_duplicate_or_omitted_rows_fail_closed(direct_vm,direct_deploy):
    variants=[]
    unknown=result(); unknown['candidates'][0]['criteria'][0]['key']='unknown'; variants.append((unknown,'unknown criterion'))
    dup=result(); dup['candidates'][1]['candidate_id']=1; variants.append((dup,'duplicate candidate'))
    missing=result(); missing['candidates']=missing['candidates'][:-1]; variants.append((missing,'exactly one row per candidate'))
    badstatus=result(); badstatus['candidates'][0]['criteria'][0]['status']='LIKELY'; variants.append((badstatus,'unknown criterion status'))
    for raw,msg in variants:
        c,case,_=configure(direct_vm,direct_deploy); mock_sources(direct_vm); direct_vm.mock_llm(PROMPT,raw)
        with direct_vm.expect_revert(msg): c.resolve_case(case)
        direct_vm.clear_mocks()

def test_validator_rejects_forged_material_matrix(direct_vm,direct_deploy):
    c,case,_=configure(direct_vm,direct_deploy); mock_sources(direct_vm); direct_vm.mock_llm(PROMPT,result()); c.resolve_case(case)
    forged={'source_states':[{'source_id':1,'status':1},{'source_id':2,'status':1},{'source_id':3,'status':1}],'candidates':[]}
    keys=['temporal_link','mechanism_link','scope_link','independent_alternative','contemporaneous_reporting']; modes=[1,1,1,1,2]; expected=[1,1,1,2,1]
    for cid in [1,2,3]:
        forged['candidates'].append({'candidate_id':cid,'criteria':[{'key':k,'mode':m,'expected':e,'status':1,'note':'forged'} for k,m,e in zip(keys,modes,expected)]})
    assert direct_vm.run_validator(leader_result=forged) is False

def test_second_resolution_is_rejected(direct_vm,direct_deploy):
    c,case,_=configure(direct_vm,direct_deploy); mock_sources(direct_vm); direct_vm.mock_llm(PROMPT,result()); c.resolve_case(case)
    with direct_vm.expect_revert('case must be sealed and unresolved'): c.resolve_case(case)

def test_wrong_definition_hash_is_not_consumable(direct_vm,direct_deploy):
    c,case,definition=configure(direct_vm,direct_deploy); mock_sources(direct_vm); direct_vm.mock_llm(PROMPT,result()); c.resolve_case(case)
    assert c.is_attributed(case,1,'0'*64) is False
    assert c.is_attributed(case,1,definition) is True
