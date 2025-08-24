from common_sense import obvious, wisdom, shrug, sarcastic, future_truth, agree, disagree

def test_obvious():
    assert obvious('water is wet').startswith('Obviously')

def test_wisdom():
    assert isinstance(wisdom(), str)
    assert len(wisdom()) > 0

def test_shrug():
    assert '¯\\_(ツ)_/¯' in shrug()
    assert '¯\\_(ツ)_/¯' in shrug('Oops')

def test_sarcastic():
    assert isinstance(sarcastic('test'), str)

def test_future_truth():
    assert isinstance(future_truth(), str)

def test_agree():
    assert 'Absolutely' in agree('Python is great') or 'agree' in agree('Python is great')

def test_disagree():
    assert 'differ' in disagree('No way') or 'disagree' in disagree('No way')
