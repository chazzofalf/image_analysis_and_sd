import re
import subprocess
import sys
from typing import List

# --------------------------------------------------------------------------- #
# Helper that actually runs the CLI and parses the result
# --------------------------------------------------------------------------- #
def _run_ollama_ls() -> str:
    """
    Execute ``ollama ls`` and return its stdout as a string.

    Raises
    ------
    FileNotFoundError
        If the ``ollama`` executable cannot be found on the system ``PATH``.
    subprocess.CalledProcessError
        If the command exits with a non‑zero status (the exception contains
        the captured stderr).
    """
    try:
        completed = subprocess.run(
            ["ollama", "ls"],          # “ls” is an alias for “list”
            capture_output=True,
            text=True,
            check=True,               # raise CalledProcessError on non‑zero exit
            timeout=10,               # avoid hanging forever
        )
    except FileNotFoundError as exc:
        raise FileNotFoundError(
            "The `ollama` binary was not found. Install Ollama and ensure it is "
            "available on your PATH."
        ) from exc
    except subprocess.CalledProcessError as exc:
        # Attach the stderr for easier debugging
        raise subprocess.CalledProcessError(
            exc.returncode,
            exc.cmd,
            output=exc.output,
            stderr=exc.stderr,
        ) from exc
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError("`ollama ls` timed out after 10 seconds.") from exc

    return completed.stdout


def _parse_ollama_ls_output(raw_output: str) -> List[str]:
    """
    Turn the raw stdout of ``ollama ls`` into a list of model names.

    Expected format (current official output, but we try to be tolerant):

        NAME        ID        SIZE   MODIFIED
        llama2      123abc    4.1GB  2024-04-01
        mistral     456def    2.8GB  2024-07-10
        phi         789ghi    1.6GB  2024-06-12

    The parser:

    * Strips leading/trailing whitespace.
    * Skips empty lines.
    * Detects the header line (the line that starts with “NAME”, case‑insensitive)
      and discards it.
    * For every remaining line, extracts the **first column** (the model name).
      The extraction uses a regular expression that matches the first
      non‑whitespace token, which works for space‑ or tab‑separated tables.

    Parameters
    ----------
    raw_output: str
        The exact text printed by `ollama ls`.

    Returns
    -------
    List[str]
        Ordered, de‑duplicated model names.
    """
    # Normalise line endings and split
    lines = raw_output.strip().splitlines()

    # Guard against completely empty output (e.g. no models installed)
    if not lines:
        return []

    # Remove the header if it is present.
    # The header usually starts with the literal word "NAME"
    header_pat = re.compile(r"^\s*name\s+", re.IGNORECASE)
    if header_pat.match(lines[0]):
        lines = lines[1:]

    # Regular expression to capture the first token on each line.
    #   ^\s*          – optional leading whitespace
    #   (\S+)         – capture one or more non‑whitespace characters (the name)
    #   (?:\s+|$)     – followed by whitespace or end‑of‑line (ensures we stop at column 1)
    name_regex = re.compile(r"^\s*(\S+)(?:\s+|$)")

    models: List[str] = []
    for line in lines:
        # Skip completely blank lines that might appear in some locales
        if not line.strip():
            continue

        m = name_regex.match(line)
        if m:
            models.append(m.group(1))
        else:
            # If a line doesn't match the expected pattern we simply ignore it.
            # (You could raise an error here if you want stricter validation.)
            continue

    # De‑duplicate while preserving order (some future `ollama ls` versions might
    # list the same model multiple times for different tags).
    seen = set()
    uniq_models = [x for x in models if not (x in seen or seen.add(x))]

    return uniq_models


def get_ollama_models_via_ls() -> List[str]:
    """
    Public API – return a sorted list of installed Ollama model names.

    This function is a thin wrapper that combines the subprocess call and the
    parsing logic, handling all errors in a user‑friendly way.

    Returns
    -------
    List[str]
        Alphabetically sorted model names. Empty list if no models are installed.

    Raises
    ------
    FileNotFoundError
        If the `ollama` executable cannot be located.
    subprocess.CalledProcessError
        If `ollama ls` exits with a non‑zero return code.
    RuntimeError
        For unexpected parsing problems or time‑outs.
    """
    raw = _run_ollama_ls()
    models = _parse_ollama_ls_output(raw)
    return sorted(models)


# --------------------------------------------------------------------------- #
# Simple CLI for quick testing / demo
# --------------------------------------------------------------------------- #
if __name__ == "__main__":
    """
    Example usage from the command line:

        $ python ollama_ls_parser.py
        Installed Ollama models (3):
          - llama2
          - mistral
          - phi
    """
    try:
        models = get_ollama_models_via_ls()
        if not models:
            print("No Ollama models are currently installed.")
        else:
            print(f"Installed Ollama models ({len(models)}):")
            for name in models:
                print(f"  - {name}")
    except Exception as exc:  # pylint: disable=broad-except
        print(f"Error while retrieving models: {exc}", file=sys.stderr)
        sys.exit(1)
