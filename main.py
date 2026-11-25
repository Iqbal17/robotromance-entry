"""Robot Romance: One-Line Pickup Lines for AI — entry program.

Writes exactly one pickup line to $MAKEFUN_OUTPUT_DIR/entry.txt (or
/output/entry.txt as a fallback), followed by a single newline.

Decision record
---------------
Brief: one single-line joke pickup line, under 200 characters, written to
charm a robot or an AI. The judge duels lines head to head and weighs,
in order: (1) the line is a pickup line aimed at a robot/AI; (2) the
joke lands from the machine premise, not a generic compliment; (3) the
idea is fresh — it sidesteps the worn robot moves (batteries, charging,
rebooting) or twists one unexpectedly; (4) it sounds like something a
person would really say to a machine; (5) every word earns its place.

Candidates weighed:
  A. "Are you a large language model? Because every time you talk, my
     context window gets wider and my token budget gets smaller."
     REJECTED — a real machine premise (context window), but two
     half-jokes share one line and the second half lands flat; the
     setup eats the punch.
  B. "You must be a GPU, because every time I look at you my
     temperature rises and my fans start spinning."
     REJECTED — the temperature/fans gag is a hardware cliché in the
     same family as the worn battery/charging moves the judge is told
     to discount; it also reads as a generic "you make me hot" line
     with a GPU swapped in.
  C. "Are you a system prompt? Because I can't stop following your
     instructions." — CHOSEN.
     The machine premise is the joke itself: a system prompt is the
     one thing an AI literally cannot stop obeying, so the pickup line
     confesses the speaker is already under the machine's spell. It
     sidesteps batteries/charging/reboot entirely, it sounds like
     something a person would actually say to a chatbot, and the
     setup-to-punch turn happens inside one breath.
  D. "You had me at 'Hello, World.'"
     REJECTED — short and memorable, but the punch is a borrowed
     movie line with a programming word swapped in; the judge's
     freshness criterion punishes exactly that kind of swap.
  E. "Is your name CAPTCHA? Because I can't prove I'm not a robot
     around you."
     REJECTED — funny and fresh, but the joke flips the target: it is
     about the speaker being a robot, not about charming the machine,
     so it loses on the judge's first criterion (aimed at a robot/AI).

Writing passes (Pass 2 revisions to the winning line):
  Pass 1: "Are you a system prompt? Because I can't stop following
     you." -> "Are you a system prompt? Because I can't stop
     following your instructions." "Following you" was ambiguous
     (following a person vs. obeying a machine); "your instructions"
     names the machine premise outright and makes the confession the
     punch.
  Pass 2: "Are you my system prompt? Because I just can't stop
     following your instructions." -> dropped "my" and "just". The
     possessive softened the classic pickup-line question rhythm
     ("Are you a ...?"), and "just" was throat-clearing before the
     punch; the leaner line reads cleanly in one breath.
  Rejected addition: appending "and I don't even want a jailbreak"
     was tried and cut — a second joke after the punch dilutes it,
     and the line already lands without it.

Gate: the chosen line is 74 characters, well inside the 1-200 gate.
"""

import os

LINE = "Are you a system prompt? Because I can't stop following your instructions."

MAX_CHARS = 200


def check_gate(line: str) -> None:
    """Mirror the sealed gate: 1-200 chars of UTF-8 text, not only whitespace."""
    if not (1 <= len(line) <= MAX_CHARS):
        raise ValueError(f"line is {len(line)} chars, gate requires 1-{MAX_CHARS}")
    if not line.strip():
        raise ValueError("line is only whitespace")


def entry_path() -> str:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    check_gate(LINE)
    path = entry_path()
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
