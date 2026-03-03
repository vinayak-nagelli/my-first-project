
# app.py

import subprocess

result = subprocess.run(
    ["python", "-m", "pytest", "-v"],
    capture_output=True,
    text=True
)

print("Return Code:", result.returncode)
print("Output:\n", result.stdout)
print("Errors:\n", result.stderr)