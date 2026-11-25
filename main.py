# Two Robots in an Elevator — make.fun competition
# (u-motasimfuad-two-robots-in-an-elevator-8c6aeb8f)
#
# The line: one robot avoids eye contact with the other by running a
# diagnostic, then blurts out a forced compliment about its optical
# sensors — machine logic (diagnostic, optical sensors) doing the work
# of human awkwardness (avoiding eye contact, the "by the way" filler).
#
# v1 draft: "I ran a full diagnostic just now so I wouldn't have to make
# eye contact. Your optical sensors look great, by the way."
# Revision notes (v2): tightened the opener ("just ran" instead of
# "ran ... just now"), dropped the filler "so I wouldn't have to" into
# the shorter "to avoid", so the confession lands in one breath and the
# compliment hits sooner.

import os

LINE = "I just ran a full diagnostic to avoid eye contact. Your optical sensors look great, by the way."

# Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters, not
# only white space, a single line.
assert 1 <= len(LINE) <= 200, "line length out of range"
assert LINE == LINE.strip(), "no leading/trailing whitespace"
assert "\n" not in LINE, "must be a single line"

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)

print(f"wrote {LINE!r} ({len(LINE)} chars) to {os.path.join(output_dir, 'entry.txt')}")
