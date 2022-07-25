from typer.testing import CliRunner

from app.main import app


runner = CliRunner()


def test_hello():
    result = runner.invoke(app, ["hello", "tmptmp"])
    assert result.exit_code == 0
    assert "hello tmptmp" in result.stdout


def test_bye():
    result = runner.invoke(app, ["bye", "tmptmp"])
    assert result.exit_code == 0
    assert "bye tmptmp" in result.stdout
