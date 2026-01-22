# SymbolObf Python Unpacker

Simple Python deobfuscator for scripts obfuscated with **SymbolObf-Python** by TheHellTower.

---

## Features

* Restores original Python source
* Removes SymbolObf character-based encoding
* Saves output as `.unpacked.py`

---

## Requirements

* Python 3.x

---

## Usage

```
python SymbolObf-Deobfuscator.py obfuscated.py
```

Output:

```
obfuscated.unpacked.py
```

---

## Limitations

* Works only with SymbolObf-Python format
* No runtime decryption, static only

---
