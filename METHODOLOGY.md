# Methodology: How the First Tests Were Run and Verified

**Author:** Jaron K. Bragg
**Date:** May 2026
**Status:** Working record, in progress.

This document records how the first simulations testing the hypothesis (see main README) were built, run, and verified. It is written so that anyone can reproduce the results independently and understand exactly what was and wasn’t established.

-----

## What was being tested

The main hypothesis asks whether memory held as a **spatial arrangement** could outperform memory held as a **linear sequence**. The open questions in the README (Section 7) name the first thing worth checking: *is there any task where an arrangement-based memory measurably beats linear storage — in recall, robustness, or efficiency?*

That is the narrow question these first tests address. Not the full hypothesis. Not whether the recent packing-math result transfers (that remains untested). Only: **does arrangement beat a linear baseline at all, and if so, where?**

-----

## The setup

Two memory models were compared on identical tasks with identical retrieval budgets, so neither had an unfair advantage:

- **Linear memory (baseline):** memories held as a flat sequence; retrieval scans a bounded window of nearby positions. This is the honest default — how lists, logs, and ordinary stored sequences work.
- **Arrangement memory (challenger):** memories connected to their most-related items; retrieval walks the structure from a starting point toward the target.

Both were measured on:

- **Recall** — can the system find the right memory from a noisy query?
- **Robustness** — does recall survive when part of the memory is damaged or unavailable?

Two versions were run. A first, simple version (random vectors), and a second, more realistic version adding three things closer to a real system: clustered data so relationships actually mean something, hub-targeted damage (knocking out the most-connected nodes first, the worst case for arrangement memory) alongside random damage, and beam search instead of single-step greedy retrieval for both systems.

All runs used a fixed random seed, making the results deterministic — the same code produces the same numbers every time. This property is important for verification (see below).

-----

## Results

Both versions found the same direction: arrangement beat linear at recall, with the advantage strongest under moderate damage and largest on structured data. The advantage narrowed toward parity only under heavy damage (40%+ of memory destroyed). Full numbers are in `RESULTS.md`.

The single most informative result was the **hub-targeted damage** case in the realistic version: even when arrangement memory’s most-connected nodes were destroyed first — the attack designed to hurt it most — it still roughly doubled the linear baseline’s recall. That was the test most likely to expose the advantage as fragile, and it held.

-----

## How the results were verified

The results were treated as unconfirmed until independently reproduced. The verification process was:

1. **Fixed-seed determinism as a check.** Because the seed is fixed, each test has exactly one correct output. Any model genuinely executing the code must produce identical numbers; differing numbers across runs of the same code indicate the code was not actually executed.
1. **A discrepancy surfaced and was resolved.** During development, one set of reported results could not be reconciled with the deterministic output — the same code, same seed, returned different numbers across reported runs, which is impossible under a fixed seed. This indicated those particular numbers had not come from real execution. They were discarded.
1. **Cross-checking across independent runners.** The code was then run by two independent code-executing systems that could not see each other’s work. Their outputs were compared to the decimal. They matched exactly on both versions of the test. Only after that match were the results trusted.

The takeaway worth recording: a confident-looking result is not the same as a real one. The discipline that made these results trustworthy was independent reproduction, not the apparent authority of any single source.

-----

## What this does and does not establish

**Established (in simulation, reproduced independently):**

- Arrangement-based memory outperforms a linear baseline at recall on structured data.
- The advantage is largest under moderate and hub-targeted damage — i.e. arrangement memory is more robust to partial loss.

**Not established — still open:**

- Whether this holds in a real system rather than a controlled simulation.
- **Whether the recent packing-math result (the load-bearing piece in the main README, Section 2) specifically improves anything.** These tests used ordinary relationship-based arrangement, *not* the unit-distance geometry. The load-bearing claim remains unproven and untested. This is the next question, and it is the harder one.

The honest summary: these tests give the idea a measurable pulse and point at robustness as the property that matters. They do not prove the architecture, and they do not yet touch the one element that makes the hypothesis genuinely new.

-----

## Reproduce it yourself

The exact code is in this folder:

- `sim_linear_vs_arrangement.py` — the first, simple comparison
- `sim_lesstoy.py` — the realistic version (clustered data, hub-targeted damage, beam search)

Requirements: `numpy`, `networkx`, `scikit-learn`. Run either file directly. The seed is fixed, so your output should match `RESULTS.md` to the decimal. If it doesn’t, that discrepancy is itself worth investigating — under a fixed seed, the numbers cannot drift.