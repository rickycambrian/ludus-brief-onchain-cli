"""`onchain <cmd> ...` -> `onchain.<module>.main(argv)`. Each module owns its own argparse."""

import importlib
import sys

COMMANDS = {
    "ingest": "ingest",
    "extract": "extract",
    "data": "data",
    "backtest": "backtest",
    "validate": "validate",
    "promote": "registry",
    "status": "registry",
    "run": "runner",
    "reconcile": "reconcile",
    "evo": "evo_bridge",
    "wallet": "wallet",
    "collect": "collect",
    "translate": "translate",
    "pipeline": "pipeline",
    "venue": "venues.cli",
    "lending": "lending",
    "lending-run": "lending_runner",
    "risk": "risk",
    "probe": "probe",
    "lp": "lp",
    "fidelity": "fidelity",
    "funding": "funding",
    "power": "power",
    "forward": "forward",
    "hypothesis": "hypotheses",
    "watch": "watch",
}


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if not argv or argv[0] not in COMMANDS:
        print("usage: onchain {" + ",".join(COMMANDS) + "} ...", file=sys.stderr)
        return 2
    module = importlib.import_module(f"onchain.{COMMANDS[argv[0]]}")
    return module.main(argv) or 0


if __name__ == "__main__":
    raise SystemExit(main())
