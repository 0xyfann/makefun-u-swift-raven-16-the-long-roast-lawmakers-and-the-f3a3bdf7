# Build notes

- Kit read first: RULES.txt + competition.yaml. Despite the "Long Roast"
  title, the task is ONE satirical sentence, max 320 characters, about
  lawmakers who regulate AI/crypto/the internet but cannot convert a file
  to PDF. Gate: /output/entry.txt must be UTF-8, 1–320 chars, not only
  whitespace.
- Judge criteria followed: authority set-up then undercut by the file,
  aim kept on lawmakers/power/competence, punch on the last few words,
  specific detail (FINAL_final_v7_REAL.docx) over a generic cliche.
- main.py v1: first draft of the sentence ("wonders why the future won't
  return his calls") plus a naive single-sentence check counting ".".
- Local test v1 FAILED: the check counted the dot inside ".docx" and
  raised AssertionError — the sentence itself was fine, the validator
  was wrong.
- main.py v2 (revision): fixed the check to count only sentence
  terminators (`.`, `!`, `?` followed by whitespace or end of text) via
  regex, and sharpened the punch to "wonders why the future keeps
  sending him to voicemail."
- Local test v2: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
  — exit 0. out/entry.txt = 214 chars stripped (215 with trailing
  newline), one sentence, UTF-8, gate 1–320 passes.
- Stdlib only (os, re). No network, no secrets, no files read at runtime.
