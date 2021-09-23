def test_help(cli_client, cli):
    result = cli_client.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "run" in result.stdout
    assert "shell" in result.stdout
