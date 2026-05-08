import subprocess


class CLIClient:

    def __init__(self, logger=None, timeout=30):
        self.logger = logger
        self.timeout = timeout

    def run_command(self, command):
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            timeout=self.timeout
        )

        stdout = result.stdout.strip()
        stderr = result.stderr.strip()

        if self.logger:
            self.logger.info(f"COMMAND: {' '.join(command)}")
            self.logger.info(f"RETURN CODE: {result.returncode}")

            if stdout:
                self.logger.info(f"STDOUT:\n{stdout}")

            if stderr:
                self.logger.error(f"STDERR:\n{stderr}")

        return result