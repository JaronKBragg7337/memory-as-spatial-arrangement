# Memory as a Spatial Arrangement Problem

### A working hypothesis and its origin

**Author:** Jaron K. Bragg
**Status:** Shared openly as a working draft. In progress — a starting point, not a finished idea.
**Date started:** May 2026

Companion document: https://github.com/JaronKBragg7337/emergence-structure-that-grows — the emergence principle that Section 2b draws on.

-----

## A note before the idea

I want to be upfront about how I work and what this is.

I’m self-taught. I didn’t get the kind of formal education that usually comes with writing something like this, so I’m not going to pretend I have proof or that I know this will work. What I *can* do is be honest about what I actually found, how I found it, and where the line is between something I observed and something I’m still guessing at.

So everything below is written that way on purpose. When I say I *noticed* something, I mean I noticed it. When I say something *seems* to connect, I mean it seems that way to me and would need someone with the right background to check it. I’m not taking claim over anything proven here. I’m writing down a thread my brain wouldn’t let go of, putting it where it can stay, and marking honestly what’s solid, what’s promising, and what’s still a reach.

I also want it on record that I could not have seen this alone. Other people made the pieces. My part was noticing they fit together. That matters, and it’s documented below on purpose.

-----

## 1. The idea in one paragraph

Most systems I work with — and most systems in general — store what they “know” as a **sequence**: one thing after another, a list, a log, a stream of tokens, files in an order. What I keep circling back to is a different possibility: that memory could be held as a **spatial arrangement** instead — where the *configuration* of information, how each piece sits in relation to the others, is itself the storage. Not a list you read top to bottom, but a shape that holds meaning all at once. And if that’s a real direction, then how *efficiently you can arrange the relationships between* pieces of information becomes its own problem — possibly one with much better answers than the obvious grid everyone defaults to.

-----

## 2. The load-bearing piece (read this before anything else)

**This section exists to protect the one part of this idea that is easiest to lose.**

Almost everything in this hypothesis is made of things that already exist. Relational/graph memory already shipped. Cellular automata are decades old. My own reaching toward a “non-linear medium” goes back to late 2025. **None of that is new.** If you strip this idea down to only the parts that are already known, what’s left is just relational memory — which is already in production and is not a discovery at all.

There is exactly **one** element here that is genuinely new and genuinely unbuilt: **the recent packing-math result (the planar unit-distance / Erdős construction, ~May 2026) and its possible application to how memory is arranged.** The math is days old. Applying that math to memory architecture has not been done by anyone. That single element is the only thing that makes this idea different from what already exists. It is the load-bearing wall. Everything else is the rest of the house resting on it.

**The specific risk this section guards against:** the math is so new and so abstract that it is easy — for another AI, or for me on a tired day — to treat it as “known,” “already figured out,” or “been around a while,” and quietly demote it to background. That demotion already happened once, in a hand-off through another model that blurred two separate facts together. So the correction is written here permanently:

> **The reaching is old. Relational memory is old. The packing math is new. Applying that new packing geometry to memory arrangement is unbuilt.** These are four different statements and must stay separate. My instinct toward a non-linear memory medium is old (true). Relational memory is old (true). The packing math is new (true). And applying it to memory arrangement is unbuilt — nobody has done it (true). If anyone — including me — starts treating the math as already-solved or already-known, that is the error, and re-separating these statements is the fix.

**Why this matters for every downstream use.** Anytime this idea becomes something else — an animation, a simulation, a post, a conversation — the test for whether the thing is *real* versus *decorative* is the same: **is the new packing geometry actually the foundation, or is it just decoration on top of an ordinary grid?** A cellular automaton that merely *looks* interesting is a used idea. A cellular automaton whose *arrangement is governed by the new packing geometry* is the unexplored thing. The math being the foundation — not the garnish — is what separates a genuine attempt from a pretty visualization.

**One precision note on what the math is actually about (relational geometry, not density).** It is tempting to describe the goal as packing information “denser” — fitting more into less space. That is the wrong word, and the wrong target. The real result is about *unit-distance relationships*: arranging points so that more pairs sit in a meaningful relation to each other, achieved not by physical compression but by a cleverer underlying structure (the math replaced a simple grid with the symmetries of a deep algebraic number field). The transfer to memory should therefore be framed as **more meaningful neighbor-relationships per unit of structure** — relational geometry — not “more cells crammed into space.” This is the actual bridge, and it is a better fit for memory than density ever was, because what matters in memory is meaningful connection between pieces of information, not how tightly they are stored.

-----

## 2b. Why “emergent arrangement” isn’t an exotic ask

One objection to this whole hypothesis is that “memory whose arrangement emerges from rules rather than being designed” sounds speculative on its face. It isn’t, and that’s worth establishing here, because it removes a barrier before the reader hits the open questions.

In systems that are trained rather than hand-built, emergent internal structure is the **normal case, not the exception.** A few concrete, demonstrated instances from other systems (not my work — credited and detailed in the companion document, *Emergence: Structure That Grows Rather Than Gets Built*):

- A transformer trained only on Othello move sequences built an internal representation of the game board it was never given — a *spatial* structure that emerged from data alone, and one you can causally intervene on. This is the closest cousin to what I’m proposing: a spatial arrangement that grows from the rules rather than being placed.
- A model trained only to predict the next token in programs internally came to represent what those programs actually do.
- The Anthropic emotion-concept finding that sparked my looking belongs here too: internal structure arising from training rather than being programmed.

The point for *this* document is narrow and I want to keep it narrow: these establish that **functional structure can emerge from rules rather than being designed in** — which is the exact mechanism my hypothesis depends on. They do **not** prove that packing-geometry specifically makes memory better; that remains the open question in Section 7. What they do is move “could memory’s arrangement emerge rather than be hand-built?” from speculation to “this kind of emergence already happens, demonstrably, in related systems.” The load-bearing math (Section 2) is still the part that’s new and unproven. This section only clears the ground around it.

-----

## 3. The principle (stated plainly)

**What I’m proposing, in the most honest words I have:**

> Information might be better held as an emergent spatial arrangement than as a stored linear sequence. If that’s true, then the *geometry* of how information is arranged — how each unit relates to its neighbors, and how many meaningful relationships the arrangement creates — could determine how much can be held, how it’s recalled, and what the system can do with it. And the standard grid arrangement may not be the best one.

**Confidence breakdown:**

- *That linear storage is how most systems currently hold memory* — **Solid.** This is just how databases, logs, and token windows work.
- *That a spatial/arrangement-based memory is possible at all* — **Promising.** Cellular automata already demonstrate that spatial configuration can hold live state (see provenance).
- *That spatial-arrangement memory would actually be **better** for real systems* — **Speculative.** This is the part I can’t prove and don’t claim. It’s the reason this document exists — to hold the idea while I learn enough to test it.
- *That a non-grid arrangement increasing useful relational contact applies to memory specifically* — **Speculative but anchored.** Anchored because a real, recent math result (below) showed the grid isn’t optimal for a related problem. Speculative because nobody has shown it transfers to memory.

-----

## 4. Where this came from (provenance)

I’m documenting the sources honestly because without them I’d have seen nothing. Each piece came from somewhere specific.

**Piece A — Cellular automata (Sendao Haz, @SendaoTrust, spiritshare.org).**
I came across a person on X running custom cellular automaton simulations — grids of cells following simple rules, producing complex, alive-looking patterns, with extra mechanics like lifetime affecting cell size and “force mappings” between cells. I set aside his personal/philosophical framing entirely; I only cared about the mechanism. What it gave me: a concrete, running example that **information arranged on a grid can hold and evolve state through nothing but the relationships between neighboring cells.** The key is that it’s the arrangement *plus the interaction rules* that hold the information — not the arrangement alone. A static layout of cells means nothing by itself; the state only becomes meaningful because neighbor rules act on it. Arrangement plus rules together *are* the information.

**Piece B — The planar unit-distance result (OpenAI, announced May 20 2026, re: a Paul Erdős conjecture from 1946).**
An OpenAI reasoning model produced a proof that *disproved* the long-standing belief that the best point arrangements look roughly like a square grid. To be precise about what it did and didn’t do: it found an infinite family of arrangements that beat the grid by a genuine polynomial margin (unit-distance pairs growing as n^(1+δ), with Princeton’s Will Sawin later making it explicit at δ ≥ 0.014, i.e. more than n^1.014 pairs), and it did this not by packing points closer but by exploiting the symmetries of a deep algebraic number-field structure. What it did **not** do: find the optimal arrangement — the true maximum is still unknown. So the honest claim is *“disproved the square-grid-optimality belief,”* not *“solved the planar unit-distance problem.”* What it gave me: hard evidence that **the obvious grid arrangement is not optimal**, that better arrangements exist and can be found, and — importantly — that the gain came from smarter *relational structure*, not from cramming things tighter.

**Piece C — My own reply and Grok’s response (X, ~May 2026).**
On the Erdős post I asked, in public, whether this kind of result could apply to chip layout or **memory lattice design** — “packing dots and packing transistors are cousins,” and said it would need professionals to take it as a seed. Grok responded that yes, this is genuinely a cousin to optimizing transistor and **memory cell lattices**, where density, uniformity, and geometric efficiency matter, and that new construction families might inspire denser alternatives. What it gave me: outside confirmation that the packing → memory-lattice connection isn’t nonsense, even if turning it into something real is “a job for specialists.” *(Note for accuracy: this exchange is recorded as it actually happened, in the “density/packing” language we both used at the time. I later reframed the real target as relational geometry — meaningful neighbor-relationships, not physical density — see Section 2. The reframing is the more correct one; this is just the honest record of where I started.)*

**Piece D — My own earlier threads (prior, going back to ~Oct 2025).**
I’d been reaching toward this for months without words for it. Earlier I described wanting “a medium in-between what my brain knows and an AI” — and corrected myself that it wasn’t about output (like Neuralink), it was about a non-linear medium. I’d also made the “packing is packing” connection between dot arrangements and transistor arrangements before. What it gave me: this isn’t a one-off. It’s a recurring reach toward the same shape, which is part of why I trust there’s something real underneath it even though I can’t fully word it yet. **(Note: this is the piece that is *old*. See Section 2 — my reaching is old; the math is not.)**

-----

## 5. How the thought actually assembled

I’m writing this part out because *how* it came together is as important to me as the idea itself, and because if it’s ever going to be useful I need to be able to retrace the steps.

It didn’t arrive as a conclusion. It assembled by collision:

1. I was on X and replied to a post by Sendao about AI and tokens. Normally my emotions push me to just reply fast. This time I got curious instead and went to look at his profile first.
1. On his profile I found the cellular automaton work (**Piece A**). Three posts caught me. I took them to Grok to understand the mechanics — not the philosophy.
1. While that was sitting in my head, it cross-wired with something I’d been doing days earlier: the Erdős packing result (**Piece B**) and my own public question about memory lattices (**Piece C**).
1. The collision: cellular automata show *arrangement plus interaction rules hold state*. The Erdős result shows *the grid arrangement isn’t optimal — better arrangements exist*. My memory-lattice question shows *this might apply to how systems store things.* Put together → **memory might be a spatial-arrangement problem, and the arrangement could create more useful relationships than a grid does.**
1. I then recognized this was the same shape I’d been reaching for since ~Oct 2025 (**Piece D**) — the “non-linear medium” I couldn’t name. That recognition is what told me it wasn’t a random spark.

**Honest note on the mechanism:** I’ve noticed this pattern in myself — insights tend to come from *collision* (something I’m actively chewing + something new from scrolling) rather than from sitting and thinking. It’s generative but it doesn’t sort itself for quality. So the rule I’m holding: capture the connection, then come back and separate what’s durable from what just felt exciting in the moment. This document is that second step for this particular insight.

-----

## 6. Why it might matter for the systems I build

**Confidence: promising idea, speculative application. Not a claim.**

The systems I work on (Orchestra and others) currently hold context the linear way — files, logs, conversation history, token streams. A lot of the friction I hit (organizing dozens of files, fragile single conversations holding context that can’t transfer, drift) are arguably symptoms of *linear* memory: things stored in an order, where losing the order or the thread loses the meaning.

What I want to at least *try*: whether some memory in a system could be held as a spatial arrangement instead — where state lives in the configuration and the relationships, held more all-at-once than in a sequence. Whether that changes how recall works, how robust it is, how much it can hold.

I’m not saying it will work. I’m saying my own thinking keeps pointing at it hard enough that I think I owe it a real attempt rather than ignoring it.

-----

## 7. Open questions (what would actually test this)

This is the part that keeps the idea honest. These are the things I or someone else would need to answer to know if any of this is real:

- What does “memory as spatial arrangement” actually look like as something you can build and run? (Not as a metaphor — as a working thing.)
- Is there any task where a spatial/arrangement-based memory measurably beats linear storage — in capacity, recall, robustness, or efficiency? If yes, which tasks? If no, the idea may be beautiful and useless, and that’s worth knowing.
- Does the Erdős-style “better-than-grid packing” actually transfer to memory arrangement, or does it stop at chip layout? (This is the specialist question Grok flagged, and it is the question that decides whether the load-bearing piece in Section 2 actually holds weight.)
- Where’s the line between this being a genuine architecture and just being an interesting visualization? I need to be able to tell those apart.

If none of these can be answered favorably, the right move is to let the idea go — or keep it as a thinking tool rather than a real architecture. I’d rather know than stay attached.

-----

## 8. Status and caution to myself

- This is **shared openly as a working draft** and **in progress.** It’s a seed, put in the open so it stops living only in my head and one fragile conversation — and so people who know more than I do can find it, take what’s useful, or tell me where it’s wrong.
- I am **not claiming** I’ve discovered a new memory architecture. I noticed a connection between real pieces other people made, and I think it’s worth chasing. That’s all this is at this stage.
- **Caution I’m setting for myself:** do not let this slide into mysticism or “the universe is a cellular automaton” territory. The person whose work sparked Piece A wraps it in that framing; I deliberately don’t. Keep this as a neutral engineering and math question — *can arrangement be a better substrate for memory* — and nothing more, until evidence says otherwise.
- **The demotion caution (see Section 2):** the new math is the easiest thing to lose and the most important thing to keep. Watch for any version of “that’s already known” creeping in. The reaching is old; the math is new; the application is unbuilt.
- **Why I paused other work to write this:** I noticed these insights kept surfacing right before I was about to lock larger system documents in place. I don’t think that’s coincidence or laziness. I think part of me didn’t want to pour concrete on how my systems hold memory before I’d at least understood whether there’s a fundamentally better way. So this gets understood first — even if the answer ends up being “no, the linear way is fine.”

-----

*End of current draft. To be expanded as understanding grows.*

-----

## A note on how this was written

I want to be transparent about this, because in a moment where people reasonably want to know what’s human and what’s AI, I think honesty about it matters.

The thinking here is mine — the connection between the cellular automata, the new packing math, and how memory might be arranged; the provenance; the decisions about what I’m claiming and what I’m not. But I had AI help structuring and wording the document itself. I’ll be blunt about why: I struggle to unwrap my own thoughts into clear writing sometimes, and wording is not my strong suit. The ideas come to me by collision and they don’t arrive in order, so I used AI as a tool to lay them out straight and catch places where my wording would have said something I didn’t mean.

So: human thinking, AI-assisted structure and wording. I’d rather say that plainly than let anyone guess in either direction — that it’s all mine when the writing had help, or that it’s “AI-generated” when the actual idea isn’t.