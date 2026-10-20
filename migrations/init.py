import os
import re


def verify(ctx):
    issues = []
    sp = os.path.join(ctx.root, "wiki", "structure.md")
    if os.path.exists(sp):
        text = open(sp, encoding="utf-8").read()
        if not re.search(r"^\s*diary/?:", text, re.M):
            issues.append(("warning",
                           "wiki/structure.md exists but does not declare diary/ "
                           "(append `diary/: <one-line semantics>` to the structure block)"))
    return issues
