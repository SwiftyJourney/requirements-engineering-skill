# Clarifying Questions

Use this when:
- A requirement is vague, "lousy", or "open to interpretation" and you need to pin it down BEFORE writing any artifact
- A ticket, brief, or user story is missing user types, error cases, or data shape
- You need a repeatable way to turn a one-liner into precise, testable specs

Skip this file if:
- The requirement is already precise and you just need the artifact templates. Use `bdd-narratives.md`, `use-cases.md`, or `model-specs-and-contracts.md`.

Jump to:
- [BDD Is a Conversation, Not Tooling](#bdd-is-a-conversation-not-tooling)
- [The Lousy Ticket Teardown](#the-lousy-ticket-teardown)
- [Question Bank by Dimension](#question-bank-by-dimension)
- [Answer to Artifact](#answer-to-artifact)
- [Worked Example](#worked-example)
- [Guardrails](#guardrails)
- [Verification](#verification)

---

## BDD Is a Conversation, Not Tooling

The value of BDD is not the Gherkin syntax, the test runner, or the tooling — it is the **conversation** that happens before any of that. The goal of that conversation is to **eliminate assumptions**: every "obvious" detail you leave unstated is an assumption someone will resolve differently.

Principles:

- **Crush the assumptions.** If a term, source, timing, or failure mode is unstated, it is an assumption. Surface it by asking.
- **No question is too silly.** "What is a feed?" and "What does *load* mean?" are exactly the questions that expose the gaps. Asking them is the job, not a sign of ignorance.
- **Bridge business and technical.** Clarifying questions are where the domain expert's language and the developer's precision meet. The answers become the ubiquitous language used in every artifact (see `domain-language.md`).
- **Timebox it.** Fifteen to twenty minutes of clarification is usually enough to sharpen the requirement. "If I had eight hours to chop down a tree, I'd spend six sharpening the axe" — the clarification *is* the sharpening. It reduces risk and rework far more cheaply than code does.
- **Requirements reduce risk and cost.** Every ambiguity resolved on paper is a bug, a rewrite, or an argument you don't have later.

> **Good architecture is a byproduct of good requirements.** You do not design the architecture directly — you clarify the requirements until the modules, boundaries, and contracts they imply become obvious. This skill produces that WHAT; the architecture skill turns it into the HOW.

---

## The Lousy Ticket Teardown

The canonical bad requirement:

```
Story: Feed
As a user
I want the app to load the feed
So I can see the feed

Acceptance criteria:
Given a user
When the user opens the feed
Then the feed is displayed
```

It looks complete — it has a story, a narrative, and Given/When/Then. It is still unbuildable, because every word hides an assumption. The teardown is to interrogate each one:

| Phrase in the ticket | The question it forces |
|---|---|
| "a user" | *Which* user? Are there different kinds (online vs. offline, admin vs. customer)? Do they experience this differently? |
| "the feed" | What **is** a feed? A list of what? Whose? Ordered how? |
| "load" | What does *load* mean — from where? Remote? Cache? Both? |
| "load the feed" | What happens when loading **fails**? No connectivity? Invalid data? Empty result? |
| "so I can see the feed" | What is the actual **value**? "See the feed" restates the action — it is not a benefit. |
| "the feed is displayed" | Displayed from where — fresh remote data, or a saved copy? Is stale data acceptable? How stale is too stale? |

Notice the ticket is not *wrong* — it is *under-specified*. It states an action ("load the feed") but never the value, the user types, the source, the failure modes, or the freshness rules. The teardown turns each hidden assumption into a question, and each answer into an artifact (below).

---

## Question Bank by Dimension

A reusable checklist. Not every dimension applies to every feature — ask the ones the feature's behavior warrants.

| Dimension | Questions to ask | Feeds |
|---|---|---|
| **User types** | Who uses this? Do different users (online/offline, roles) experience it differently? | One narrative per distinct user type (`bdd-narratives.md`) |
| **Value / why** | What does the user actually *gain*? (Reject answers that just restate the action.) | The "So that" of each narrative |
| **Source** | Where does the data come from — remote, cache, both? What is the fallback order? | Use cases (Load From Remote / From Cache), flowchart |
| **Connectivity / offline** | What happens with no connectivity? Is there an offline mode? | Offline narrative, no-connectivity error course |
| **Error modes** | How can this fail? Invalid data, timeout, unauthorized, server error? | One error course per failure (`use-cases.md`) |
| **Empty / edge states** | What if there is nothing to show? Is empty a success or an error? | Empty-cache course; collection-empty vs. not-found distinction |
| **Freshness / expiry** | Does data go stale? After how long *exactly*? What happens when it does? | Time-based acceptance criteria (the seven-day rule) |
| **Data shape / optionality** | What fields exist? Which are required vs. optional? What types? | Model spec table, payload contract |
| **Cancellation** | Can the user interrupt this (navigate away, scroll past)? What should happen then? | Cancel course (`use-cases.md`) |
| **Concurrency / ordering** | Can this run more than once at a time? Does order matter? Replace or merge? | Use case steps, acceptance criteria ("replace the cache") |

> Ask about **freshness and empty states explicitly** — they are the two dimensions most often left as silent assumptions, and each answer tends to *add* an acceptance-criteria scenario rather than just refine one.

---

## Answer to Artifact

Clarification is not busywork — each answer produces a concrete artifact. Aim every question at the artifact it will populate:

| A clarifying answer like... | ...becomes this artifact |
|---|---|
| "There are online and offline customers, and they behave differently" | Two BDD narratives (`bdd-narratives.md`) |
| "Offline shows the last saved feed" | The offline narrative + a Load From Cache use case |
| "Cached data is only good for seven days" | The three cache acceptance-criteria scenarios (valid / expired / empty) |
| "An empty feed is fine; a missing single image is an error" | Empty-success vs. not-found error courses (`use-cases.md`) |
| "Loading can fail on bad data or no network" | Invalid-data and no-connectivity error courses |
| "The user can scroll past before the image loads" | A Cancel course |
| "Each item has an id and image; description and location are optional" | Model spec table + payload contract with optionality by omission (`model-specs-and-contracts.md`) |
| "The endpoint isn't decided yet, but the JSON shape is" | A payload contract with the URL marked `TBD` — the shape agreed before the URL exists |

If a clarifying answer does not map to an artifact, either it was not really about this feature, or you have found a new artifact the feature warrants.

---

## Worked Example

Starting from the lousy feed ticket above, the clarification conversation surfaces:

1. **"Which user?"** -> There are **online** and **offline** customers, and they need different things. -> *Two narratives.*
2. **"What is the value?"** -> Online: always see the newest images. Offline: still see the latest saved images. -> *The two "So that" clauses.*
3. **"Load from where?"** -> Remote when connected; fall back to the local cache when not. -> *Load From Remote and Load From Cache use cases + a flowchart with the fallback branch.*
4. **"What if it fails?"** -> Invalid data -> error; no connectivity -> fall back to cache. -> *Error courses.*
5. **"Is stale cached data OK?"** -> Only if it is **less than seven days old**; older or empty -> show an error. -> *This one answer splits the offline path into three acceptance-criteria scenarios (valid / expired / empty).*
6. **"What does an item look like?"** -> `id` and `image` always present; `description` and `location` optional. -> *Model spec + payload contract.*

The unbuildable one-liner is now a full, testable Feed specification — and the module boundaries it implies (a remote loader, a local cache, a shared feed model) fall out of the answers. That is the whole method: clarify until the artifacts, and then the architecture, are obvious.

> This is why acceptance criteria are **living specifications**. The seven-day rule was not in the original ticket; asking about freshness *created* new scenarios. Expect the same on real features — each clarified rule tends to add criteria, not just tidy them. See `bdd-narratives.md` for how that block grew from one scenario to three.

---

## Guardrails

- Do not start writing artifacts before asking clarifying questions — never encode your own assumptions as if they were requirements
- Do not accept a "So that" that restates the action ("so I can see the feed") — push for the real value
- Do not leave freshness, empty states, or error modes as silent assumptions — ask about each explicitly
- Do not treat "silly" questions as beneath you — the obvious-sounding ones expose the biggest gaps
- Do not open-endedly gold-plate — timebox the clarification and move to artifacts once the requirement is sharp

## Verification

- [ ] Every vague term in the original requirement was questioned, not assumed
- [ ] User types were clarified (is it really one kind of user?)
- [ ] The value/benefit is a real gain, not a restatement of the action
- [ ] Data source, error modes, empty states, and freshness were each asked about
- [ ] Cancellation was considered for any interruptible operation
- [ ] Each answer maps to a concrete artifact (narrative, use case, model spec, contract, or diagram)
