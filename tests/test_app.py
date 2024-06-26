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

    # Capture the output
    captured = capfd.readouterr()

    # Verify that the unknown command was handled as expected
    assert "Unknown command: unknown_command" in captured.err
    assert "Application shutdown" in captured.err

def test_app_start_exit_command(capfd, monkeypatch):
    """Test how the REPL handles 'exit' command."""
    # Simulate user entering 'exit' command
    inputs = iter(['exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()

    with pytest.raises(SystemExit):
        app.start()

    # Capture the output
    captured = capfd.readouterr()

    # Verify that the application exits gracefully
    assert "Application shutdown" in captured.err

if __name__ == "__main__":
    pytest.main()
