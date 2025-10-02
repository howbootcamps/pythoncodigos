"""Utilities for updating JSON files."""
from __future__ import annotations

import json
import os
from collections.abc import Mapping
from typing import Any


def update_json_file(path: str, new_data: Mapping[str, Any]) -> bool:
    """Update JSON keys in ``path`` with values from ``new_data``.

    The function reads the current JSON content from ``path``. If the file does not
    exist, it is created with ``new_data`` as its content. When the file exists, only
    keys already present in the JSON document are updated. Other keys in
    ``new_data`` are ignored so the structure of the original document is
    preserved.

    Args:
        path: Path to the JSON file that should be updated.
        new_data: Mapping containing key/value pairs to update.

    Returns:
        ``True`` if the update succeeds, otherwise ``False``.
    """

    if not isinstance(new_data, Mapping):
        return False

    try:
        existing_data: dict[str, Any] = {}
        file_exists = os.path.exists(path)

        if file_exists:
            with open(path, "r", encoding="utf-8") as file:
                content = file.read().strip()

            if content:
                loaded = json.loads(content)
                if not isinstance(loaded, dict):
                    return False
                existing_data = loaded
        else:
            directory = os.path.dirname(path)
            if directory:
                os.makedirs(directory, exist_ok=True)

        if file_exists:
            for key, value in new_data.items():
                if key in existing_data:
                    existing_data[key] = value
        else:
            existing_data = dict(new_data)

        with open(path, "w", encoding="utf-8") as file:
            json.dump(existing_data, file, ensure_ascii=False, indent=4)
            file.write("\n")

        return True
    except (OSError, json.JSONDecodeError):
        return False
