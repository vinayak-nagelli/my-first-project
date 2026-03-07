
# app.py

import subprocess

result = subprocess.run(
    ["python", "-m", "pytest", "-v"],
    capture_output=True,
    text=True
)
print("step1")

print("Return Code:", result.returncode)
print("step2")

print("Output:\n", result.stdout)
print("step3")

print("Errors:\n", result.stderr)