import pytest
from CLI_Subprocess.cli_client import CLIClient


@pytest.mark.cli
class TestCLI:

    def test_01_verify_docker_installed(self, logger):
        logger.info("Test Started: Verify docker installation")

        client = CLIClient(logger=logger)
        result = client.run_command(["docker", "--version"])

        assert result.returncode == 0, "Test Failed: Docker is not installed"
        assert "docker" in result.stdout.lower(), "Test Failed: Invalid docker version output"

        logger.info("Test Passed: Verified docker installation")

    def test_02_verify_docker_daemon_running(self, logger):
        logger.info("Test Started: Verify docker daemon is running")

        client = CLIClient(logger=logger)
        result = client.run_command(["docker", "info"])

        assert result.returncode == 0, "Test Failed: Docker daemon is not running"

        logger.info("Test Passed: Verified docker daemon is running")


    def test_03_verify_docker_images_available(self, logger):
        logger.info("Test Started: Verify docker images are available")

        client = CLIClient(logger=logger)
        result = client.run_command(["docker", "images"])

        assert result.returncode == 0, "Test Failed: Failed to fetch docker images"
        assert len(result.stdout.strip().split("\n")) > 1, "Test Failed: No docker images found"

        logger.info("Test Passed: Verified docker images are available")

    def test_04_verify_docker_containers_running(self, logger):
        logger.info("Test Started: Verify docker containers are running")

        client = CLIClient(logger=logger)
        result = client.run_command(["docker", "ps"])

        assert result.returncode == 0, "Test Failed: Docker command failed"
        assert "CONTAINER ID" in result.stdout, "Test Failed: Empty container is not running"
        assert "IMAGE" in result.stdout, "Test Failed: Empty container is not running"

        logger.info("Test Passed: Verified Docker containers are running")

    def test_05_verify_docker_network_listing(self, logger):
        logger.info("Test Started: Verify docker networks listing")

        client = CLIClient(logger=logger)
        result = client.run_command(["docker", "network", "ls"])

        assert result.returncode == 0, "Test Failed: Failed to fetch docker networks"
        assert "NETWORK ID" in result.stdout, "Test Failed: Invalid network list output"
        assert "bridge" in result.stdout.lower(), "Test Failed: Default bridge network missing"

        logger.info("Test Passed: Verified docker networks listed")
