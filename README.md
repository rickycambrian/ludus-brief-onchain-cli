# Ludus brief onchain_trading-61: the `onchain` command dispatcher

This repository is a public extract for one Ludus University brief. It holds one file,
`src/onchain/cli.py`, copied without change on 2026-10-28 from the `onchain_trading` project
(a private repository). The file is 46 lines. It has no test.

## The brief

Write a pytest behaviour test for `onchain.cli`. Work in your own repository:

1. Copy `src/onchain/cli.py` into a minimal package `onchain` in your repository
   (add an empty `src/onchain/__init__.py`).
2. Write `tests/test_cli.py`. Use test doubles for the command modules, so that no real
   command runs. Do not change `cli.py`.
3. Test each numbered behaviour of the spec below.
4. Keep `CONTRIBUTIONS.md`: the tests are your own work.

Deliver a link to your repository at a commit SHA, `tests/test_cli.py`, and a run receipt
(the test command and its output).

Test of value: the owner applies your test to `onchain_trading` with no change to `cli.py`.
The test passes there, and it fails on every mutant in a hidden mutant set. The owner then
merges it. The reviewer tells you only how many mutants your test kills.

## Spec of `onchain.cli`

1. `main(argv=None)` reads `sys.argv[1:]` when `argv` is `None`.
2. A fixed table `COMMANDS` maps 26 command names to 25 module names under the `onchain`
   package. Two commands (`promote`, `status`) map to one module (`registry`). One command
   (`venue`) maps to a nested module (`venues.cli`).
3. When `argv` is empty, or its first item is not a command name, `main` writes one usage
   line to standard error that lists every command name, and returns 2. It imports no
   command module.
4. For a known command, `main` imports `onchain.<module>` and calls its `main` with the full
   `argv` (the command name stays first). It returns that value, or 0 when the value is
   falsy (for example `None`).
5. Run as a script (`python -m onchain.cli`), the module exits with the return value of `main`.

## Licence

MIT. See `LICENSE`.
