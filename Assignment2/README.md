# Modular Sandwich Maker - Assignment 2

This version keeps the Assignment 1 behavior while splitting the program into
the four modules required by the assignment.

- `data.py` contains recipes and resources.
- `sandwich_maker.py` contains `SandwichMaker`, `check_resources()`, and
  `make_sandwich()`.
- `cashier.py` contains `Cashier`, `process_coins()`, and
  `transaction_result()`.
- `main.py` imports all three modules, creates both class instances, and starts
  the program.

Run the program from this directory:

```bash
python3 main.py
```

The PDF says `sandwich_makerr.py` once in the project-structure section. This
appears to be a typo because its import instructions and the provided skeleton
both use `sandwich_maker.py`.
