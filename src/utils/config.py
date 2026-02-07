"""Configuration utilities for YAML configs and CLI overrides."""
from __future__ import annotations

import argparse
from pathlib import Path
from typing import Any, Dict, Iterable

import yaml


def _set_nested(config: Dict[str, Any], key_path: Iterable[str], value: Any) -> None:
    """Set a nested key in a dict given a path of keys."""
    current = config
    *parents, last = list(key_path)
    for key in parents:
        if key not in current or not isinstance(current[key], dict):
            current[key] = {}
        current = current[key]
    current[last] = value


def _parse_override(raw: str) -> tuple[list[str], Any]:
    """Parse CLI override in the form key1.key2=value."""
    if "=" not in raw:
        raise ValueError(f"Override '{raw}' must be in key=value format.")
    key, raw_value = raw.split("=", 1)
    key_path = key.split(".")
    try:
        value = yaml.safe_load(raw_value)
    except yaml.YAMLError as exc:
        raise ValueError(f"Failed to parse override value '{raw_value}'.") from exc
    return key_path, value


def load_config(path: str | Path, overrides: Iterable[str] | None = None) -> Dict[str, Any]:
    """Load YAML config and apply dotted-key overrides."""
    config_path = Path(path)
    if not config_path.exists():
        raise FileNotFoundError(f"Config file not found: {config_path}")
    with config_path.open("r", encoding="utf-8") as handle:
        config = yaml.safe_load(handle) or {}

    if overrides:
        for raw in overrides:
            key_path, value = _parse_override(raw)
            _set_nested(config, key_path, value)
    return config


def build_config_argparser() -> argparse.ArgumentParser:
    """Create an argument parser for configuration usage."""
    parser = argparse.ArgumentParser(description="Config loader")
    parser.add_argument("--config", required=True, help="Path to YAML config file")
    parser.add_argument(
        "--override",
        action="append",
        default=[],
        help="Override config with key=value (use multiple times).",
    )
    return parser
