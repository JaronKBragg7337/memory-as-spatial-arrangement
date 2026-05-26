"""
Test built from the repo's own Section 7 open questions:
  "Is there any task where a spatial/arrangement-based memory measurably beats
   linear storage -- in capacity, recall, robustness, or efficiency?"

Baseline  = LINEAR memory (the honest default: a flat list, retrieve by scanning).
Challenger = ARRANGEMENT memory (items connected by relationship; retrieve by
             walking the structure from a starting point).

We measure the two things the doc names: RECALL and ROBUSTNESS (what happens
when part of the memory is damaged/unavailable).

No fancy graph zoo. Just: does structure beat the list. That's the question
that decides whether to build arrangement into a real system.
"""

import random
import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity

N = 200          # number of memories
DIM = 32         # vector size
SEED = 7
random.seed(SEED); np.random.seed(SEED)

# memories as unit vectors
mem = np.random.randn(N, DIM)
mem = mem / np.linalg.norm(mem, axis=1, keepdims=True)
sims = cosine_similarity(mem)

def make_query(target, noise):
    q = mem[target] + noise * np.random.randn(DIM)
    return q / np.linalg.norm(q)

# ---------- LINEAR memory ----------
# The honest baseline. Memory is a flat list. To recall, you can only look at a
# WINDOW of items near where you currently are in the list (bounded attention --
# you can't scan all 200 at once for free; that's the cost linear storage pays).
def linear_recall(target, noise, window, budget):
    q = make_query(target, noise)
    pos = random.randrange(N)              # start somewhere in the list
    for _ in range(budget):
        lo = max(0, pos - window); hi = min(N, pos + window + 1)
        idxs = list(range(lo, hi))
        scores = [float(q @ mem[i]) for i in idxs]
        best = idxs[int(np.argmax(scores))]
        if best == pos:                    # stuck: nudge to expand search
            pos = (pos + window) % N
        else:
            pos = best
        if pos == target:
            return True
    return False

# ---------- ARRANGEMENT memory ----------
# Items connected to their most-related items. To recall, walk from a start node
# to whichever neighbor best matches the query. Same retrieval budget as linear.
def build_arrangement(k, dropout=0.0):
    G = nx.Graph(); G.add_nodes_from(range(N))
    alive = set(range(N))
    if dropout > 0:
        dead = set(random.sample(range(N), int(dropout * N)))
        alive -= dead
    for i in range(N):
        order = np.argsort(sims[i])[::-1]
        added = 0
        for j in order:
            if j == i: continue
            G.add_edge(i, int(j)); added += 1
            if added >= k: break
    return G, alive

def arrangement_recall(G, alive, target, noise, budget):
    if target not in alive:
        return False                       # target itself was knocked out
    q = make_query(target, noise)
    start = random.choice(list(alive))
    cur = start
    for _ in range(budget):
        nbrs = [n for n in G.neighbors(cur) if n in alive]
        if not nbrs: break
        cand = [cur] + nbrs
        scores = [float(q @ mem[c]) for c in cand]
        cur = cand[int(np.argmax(scores))]
        if cur == target:
            return True
    return False

# ---------- run the comparison ----------
TRIALS = 1000
NOISE = 0.35
BUDGET = 15          # same retrieval effort for both
WINDOW = 5           # linear can look at +/-5 items (avg_degree ~ arrangement k)
K = 5                # arrangement: 5 links per node (comparable local fan-out)

def eval_linear(noise, dropout=0.0):
    # dropout for linear = some list slots are dead/corrupted
    dead = set(random.sample(range(N), int(dropout*N))) if dropout>0 else set()
    hits = 0
    for _ in range(TRIALS):
        t = random.randrange(N)
        if t in dead:
            continue_flag = False  # target gone -> automatic miss, count as attempt
            continue
        if linear_recall(t, noise, WINDOW, BUDGET):
            hits += 1
    return hits / TRIALS

def eval_arrangement(noise, dropout=0.0):
    G, alive = build_arrangement(K, dropout)
    hits = 0
    for _ in range(TRIALS):
        t = random.randrange(N)
        if arrangement_recall(G, alive, t, noise, BUDGET):
            hits += 1
    return hits / TRIALS

print("=== Q: does ARRANGEMENT memory beat LINEAR memory? (same budget) ===\n")

print("RECALL (clean, no damage):")
lin = eval_linear(NOISE, 0.0)
arr = eval_arrangement(NOISE, 0.0)
print(f"  linear      : {lin:.3f}")
print(f"  arrangement : {arr:.3f}\n")

print("ROBUSTNESS (20% of memory knocked out):")
random.seed(SEED); np.random.seed(SEED)
lin20 = eval_linear(NOISE, 0.20)
random.seed(SEED); np.random.seed(SEED)
arr20 = eval_arrangement(NOISE, 0.20)
print(f"  linear      : {lin20:.3f}")
print(f"  arrangement : {arr20:.3f}\n")

print("ROBUSTNESS (40% of memory knocked out):")
random.seed(SEED); np.random.seed(SEED)
lin40 = eval_linear(NOISE, 0.40)
random.seed(SEED); np.random.seed(SEED)
arr40 = eval_arrangement(NOISE, 0.40)
print(f"  linear      : {lin40:.3f}")
print(f"  arrangement : {arr40:.3f}")