from src.app import hello

def test_hello():
    assert hello("X") == "Hello, X!"
