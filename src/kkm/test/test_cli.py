from cli_test_helpers import shell

def test_runas_module():
    result = shell('python3 -m kkm --help')
    assert result.exit_code == 0

def test_entrypoint():
    result = shell('kkm --help')
    assert result.exit_code == 0
