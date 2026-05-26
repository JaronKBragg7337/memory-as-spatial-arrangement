"""
LESS-TOY version of: does ARRANGEMENT memory beat LINEAR memory?
Built from the repo's Section 7, with all three realism upgrades:

1) REAL STRUCTURE in the data: memories are no longer pure random noise. They're
   drawn in CLUSTERS (like real memory -- related things sit near each other),
   so relationships actually mean something.
2) REALISTIC FAILURE: instead of only random knockout, we also test HUB-TARGETED
   damage -- killing the most-connected nodes first, which is how real networks
   actually fail (and the worst case for arrangement memory).
3) SMARTER RETRIEVAL: beam search (keep the best few paths) instead of a single
   greedy step, for BOTH systems, so neither is handicapped by a dumb walk.

Same fixed seed so it's deterministic and cross-checkable.
"""

import random
import numpy as np
import networkx as nx
from sklearn.metrics.pairwise import cosine_similarity

N = 300
DIM = 48
N_CLUSTERS = 12
SEED = 7
random.seed(SEED); np.random.seed(SEED)

# ---- 1) REAL STRUCTURE: clustered memories ----
centers = np.random.randn(N_CLUSTERS, DIM)
centers = centers / np.linalg.norm(centers, axis=1, keepdims=True)
labels = np.random.randint(0, N_CLUSTERS, size=N)
mem = centers[labels] + 0.6 * np.random.randn(N, DIM)   # cluster + spread
mem = mem / np.linalg.norm(mem, axis=1, keepdims=True)
sims = cosine_similarity(mem)

def make_query(target, noise):
    q = mem[target] + noise * np.random.randn(DIM)
    return q / np.linalg.norm(q)

# ---- 3) SMARTER RETRIEVAL: beam search, shared by both systems ----
def beam_recall(neighbors_fn, target, noise, budget, beam=3):
    q = make_query(target, noise)
    # start from a few random places (beam)
    frontier = random.sample(range(N), min(beam, N))
    if target in frontier:
        return True
    for _ in range(budget):
        cand = set()
        for node in frontier:
            cand.add(node)
            for nb in neighbors_fn(node):
                cand.add(nb)
        if not cand:
            break
        scored = sorted(cand, key=lambda c: float(q @ mem[c]), reverse=True)
        frontier = scored[:beam]
        if target in frontier:
            return True
    return False

# ---- LINEAR memory: neighbors = a window of adjacent list slots ----
def make_linear_neighbors(alive, window):
    def fn(node):
        out = []
        for d in range(1, window+1):
            for cand in (node-d, node+d):
                if 0 <= cand < N and cand in alive:
                    out.append(cand)
        return out
    return fn

# ---- ARRANGEMENT memory: neighbors = most-related items ----
def build_arrangement(k):
    G = nx.Graph(); G.add_nodes_from(range(N))
    for i in range(N):
        order = np.argsort(sims[i])[::-1]
        added = 0
        for j in order:
            if j == i: continue
            G.add_edge(i, int(j)); added += 1
            if added >= k: break
    return G

def make_arrangement_neighbors(G, alive):
    def fn(node):
        if node not in alive: return []
        return [n for n in G.neighbors(node) if n in alive]
    return fn

# ---- 2) REALISTIC FAILURE: random vs hub-targeted knockout ----
def random_dead(frac):
    return set(random.sample(range(N), int(frac*N)))

def hub_dead(G, frac):
    deg = sorted(G.degree, key=lambda x: -x[1])   # highest degree first
    return set(n for n, d in deg[:int(frac*N)])

# ---- run ----
TRIALS = 1000
NOISE = 0.40
BUDGET = 12
WINDOW = 5
K = 5

G = build_arrangement(K)

def eval_system(kind, dead):
    alive = set(range(N)) - dead
    if kind == "linear":
        nf = make_linear_neighbors(alive, WINDOW)
    else:
        nf = make_arrangement_neighbors(G, alive)
    hits = 0
    for _ in range(TRIALS):
        t = random.randrange(N)
        if t in dead:
            continue
        if beam_recall(nf, t, NOISE, BUDGET):
            hits += 1
    return hits / TRIALS

def run_block(title, dead_lin, dead_arr):
    random.seed(SEED); np.random.seed(SEED)
    lin = eval_system("linear", dead_lin)
    random.seed(SEED); np.random.seed(SEED)
    arr = eval_system("arrangement", dead_arr)
    print(f"{title}")
    print(f"  linear      : {lin:.3f}")
    print(f"  arrangement : {arr:.3f}\n")

print("=== LESS-TOY: arrangement vs linear (clustered data, beam search) ===\n")

run_block("RECALL (clean, no damage):", set(), set())

run_block("ROBUSTNESS (20% RANDOM knockout):",
          random_dead(0.20), random_dead(0.20))

run_block("ROBUSTNESS (20% HUB-TARGETED knockout -- worst case):",
          hub_dead(G, 0.20), hub_dead(G, 0.20))

run_block("ROBUSTNESS (40% RANDOM knockout):",
          random_dead(0.40), random_dead(0.40))