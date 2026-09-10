---
category: blogpost
date: 2026-09-08
author: Andrew Brown, Connor Aird, <Everyone from our group>
...

<script>
function submitTip(event) {
  event.preventDefault();

  const form = event.target;
  const fields = {
    pattern: form.elements.pattern.value.trim(),
    problem: form.elements.problem.value.trim(),
    alternative: form.elements.alternative.value.trim(),
    context: form.elements.context.value.trim()
  };
  const issueTitle = `[Legacy Fortran pattern] ${fields.pattern}`;
  const issueBody = `## Pattern to avoid
${fields.pattern}

## Why it causes trouble
${fields.problem}

## Better alternative or mitigation
${fields.alternative}

## Context
${fields.context || "Not provided"}`;
  const url =
    "<repo-url>/issues/new"
    + "?labels=legacy-fortran"
    + "&title=" + encodeURIComponent(issueTitle)
    + "&body=" + encodeURIComponent(issueBody);

  window.open(url, "_blank");
}
</script>

# Legacy Code Confessions

Legacy Fortran is full of code that works, has survived for decades, and is
difficult to change. We are collecting the patterns that make legacy
systems harder to understand, test, maintain, or modernise, together with the
practical alternatives that helped.

This is not about blaming the people who wrote the code. Constraints change,
and many of these choices were reasonable at the time. The goal is to give the
next developer a map: what to recognise, why it is risky, and where to start
improving it.

If you are some knowledge to share please continue reading and contribute today!

## What makes a useful contribution?

Tell us about one specific pattern. It might be a language feature, an
interface convention, a build or testing practice, or an organisational habit
around a codebase. The most useful reports include:

* The pattern, described plainly enough that someone can recognise it;
* The failure mode: what makes it hard to work with or easy to get wrong;
* A better alternative, a mitigation, or a safe first step; and
* Context such as a Fortran standard, compiler, tool or domain.

For example, "passing array dimensions as unrelated integer arguments" is more
useful than "bad interfaces". Explain that mismatched dimensions can compile
and corrupt results, then suggest assumed-shape dummy arguments with explicit
interfaces, or a smaller mitigation when a full refactor is not yet possible.

## Share a pattern

Submit one pattern at a time. You do not need to name a person or organisation,
and please remove proprietary or confidential details. Your submission will
open as a GitHub issue so the curriculum team can discuss, edit, and review it
before anything is published.

<div class="legacy-patterns-container">
  <form class="submit-box" onsubmit="submitTip()">
    <label for="tip-pattern">Pattern to avoid <span>*</span></label>
    <input
      class="tip-input"
      id="tip-pattern"
      name="pattern"
      required
      placeholder="e.g. Global state hidden in COMMON blocks"
    />
    <label for="tip-problem">Why does it cause trouble? <span>*</span></label>
    <textarea
      class="tip-textarea"
      id="tip-problem"
      name="problem"
      required
      placeholder="What makes the code hard to understand, test, or change?"
    ></textarea>
    <label for="tip-alternative">Better alternative or mitigation <span>*</span></label>
    <textarea
      class="tip-textarea"
      id="tip-alternative"
      name="alternative"
      required
      placeholder="What would you recommend, and what is a realistic first step?"
    ></textarea>
    <label for="tip-context">Context <span class="optional">optional</span></label>
    <textarea
      class="tip-textarea"
      id="tip-context"
      name="context"
      placeholder="Fortran standard, compiler, domain, toolchain, or code age"
    ></textarea>
    <p class="submit-helper">
      Required fields are marked *. Do not include confidential code or details
      that identify individuals.
    </p>
    <button class="tip-submit-btn" type="submit">Open a GitHub issue</button>
  </form>
</div>

## Learn more

This project grew from the fourth [Back to the Fortran Future](https://fortran-lang.org/news/2026/05-05-Back-to-the-Fortran-Future-3/)
workshop, held as a satellite event to the [10th annual Research Software
Engineering Conference](https://rsecon26.society-rse.org/) in Sheffield on 8
September 2026. The workshop brought together people working on one of
Fortran's persistent challenges: developers inheriting large, important
codebases without the context needed to maintain them confidently.

One outcome will be a practical guide for developers who need to understand and
modernise legacy Fortran. We also want the resulting entries to be structured
enough for tools and AI assistants to use responsibly: a recognisable pattern,
its consequences, and advice grounded in real experience. [Share a pattern
above](#share-a-pattern) to help build that resource.

This guide will live in the [Software Carpentries
Incubator](https://carpentries-incubator.github.io/legacy-fortran/), and may
grow into a dedicated Carpentries-style workshop linked to the larger [Fortran
Carpentries curriculum](https://carpentries-incubator.github.io/intro-to-modern-fortran/profiles.html#pathways).
