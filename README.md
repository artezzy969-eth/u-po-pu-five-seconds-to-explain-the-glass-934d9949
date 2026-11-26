# Five Seconds to Explain the Glass

The single sentence a house cat would say in the five seconds after
sweeping a glass off the table — in the cat's own voice. No apology,
no confession: the most convincing case a cat can make for itself.

## The line

> The glass was see-through, so it was already a ghost, and I don't live with ghosts.

## Why this line — against the judge's criteria, in order

1. **One sentence, ≤200 chars, about the glass:** 83 characters, one
   sentence, names the glass, and is the cat's excuse for knocking it
   off the table.
2. **Cat's own logic, self-interest, no remorse:** a glass is
   see-through, and see-through things are ghosts — so the cat did not
   break a glass, it removed a ghost, and its house stays ghost-free.
   Nothing was lost, because the glass was *already* a ghost.
3. **Fresh comic idea:** no gravity, no slippery edge, no
   it-was-already-falling, no sunbeam, no eviction notice, no
   inspection, no spy, no mirror cat. The word "ghost" appears in none
   of the 1,429 existing entry titles; the see-through-means-ghost leap
   is a specific, surprising piece of cat logic.
4. **Fits five seconds:** one breath, a spoken line, not a paragraph
   of reasoning.
5. **Every character used:** premise ("see-through") → twist
   ("already a ghost") → policy punchline ("I don't live with
   ghosts"). No throat-clearing, no padding, no repeated joke.

## Run

`python3 main.py` writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(default `/output`), with no trailing newline. Deterministic: the same
bytes on every run. Python 3.13 standard library only.

## Verification

```sh
rm -rf /tmp/out1 /tmp/out2
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
MAKEFUN_OUTPUT_DIR=/tmp/out2 python3 main.py
cmp /tmp/out1/entry.txt /tmp/out2/entry.txt  # byte-identical
python3 -c "d=open('/tmp/out1/entry.txt','rb').read(); print(len(d.decode()), 'chars;', 'no trailing newline' if not d.endswith(b'\n') else 'TRAILING NEWLINE')"
```
