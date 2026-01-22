import re
import sys

def deobfuscate(code):
    m = re.search(r'THT_6669=\[(.*?)\]', code, re.S)
    if not m:
        return None
    items = re.findall(r'"([^"]*)"', m.group(1))
    chars = [chr(len(x)) for x in items]
    return "".join(chars)

def main():
    if len(sys.argv) < 2:
        return
    with open(sys.argv[1], "r", encoding="utf-8", errors="ignore") as f:
        data = f.read()
    result = deobfuscate(data)
    if result is None:
        return
    out = sys.argv[1].replace(".py", ".unpacked.py")
    with open(out, "w", encoding="utf-8") as f:
        f.write(result)

if __name__ == "__main__":
    main()
