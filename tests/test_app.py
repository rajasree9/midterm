"""
Module containing unit tests for the App class.
"""

import pytest
from app import App

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    # Introduce a slight delay before capturing the output
    import time
    time.sleep(0.1)

    # Capture the output after a slight delay
    captured = capfd.readouterr()

    # Verify that the unknown command was handled as expected
    assert "No such command: unknown_command" in captured.out
