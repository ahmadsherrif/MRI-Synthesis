"""Print a YAML configuration after applying CLI overrides."""
from __future__ import annotations

import pprint
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from src.utils.config import build_config_argparser, load_config


def main() -> None:
    parser = build_config_argparser()
    args = parser.parse_args()
    config = load_config(args.config, args.override)
    pprint.pprint(config)


if __name__ == "__main__":
    main()
