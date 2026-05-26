# Results

Raw output from the two simulations. The seed is fixed (`SEED=7`), so these are deterministic — running the code yourself should reproduce these numbers exactly. Both sets below were reproduced identically by two independent code-executing systems.

All numbers are recall accuracy (fraction of queries that reached the correct memory).

-----

## Test 1 — `sim_linear_vs_arrangement.py`

Simple version: 200 random-vector memories, single-step greedy retrieval, same retrieval budget for both systems.

|Condition        |Linear|Arrangement|
|-----------------|------|-----------|
|Clean (no damage)|0.105 |0.137      |
|20% knocked out  |0.064 |0.127      |
|40% knocked out  |0.053 |0.051      |

Reading: arrangement beats linear at recall, and the gap widens under moderate damage (nearly 2x at 20% loss) before converging at heavy damage.

-----

## Test 2 — `sim_lesstoy.py`

Realistic version: 300 memories drawn in 12 clusters (so relationships carry meaning), beam search for both systems, and damage tested both randomly and hub-targeted (most-connected nodes destroyed first).

|Condition                             |Linear|Arrangement|
|--------------------------------------|------|-----------|
|Clean (no damage)                     |0.100 |0.272      |
|20% random knockout                   |0.107 |0.207      |
|20% hub-targeted knockout (worst case)|0.082 |0.163      |
|40% random knockout                   |0.075 |0.087      |

Reading: on structured data the advantage grows (arrangement nearly 3x linear on clean recall). Under moderate damage arrangement holds roughly a 2x edge — including the hub-targeted worst case, the attack designed to be hardest on arrangement memory. As before, the advantage narrows toward parity only under heavy (40%) damage.

-----

## What these numbers do and don’t show

They show, reproducibly, that **arrangement beats a linear baseline at recall and is more robust to partial memory loss.** They do **not** show that the recent packing-math result specifically helps — these tests used ordinary relationship-based arrangement, not the unit-distance geometry that is the load-bearing piece of the hypothesis. See `METHODOLOGY.md` for the full scope and limits.