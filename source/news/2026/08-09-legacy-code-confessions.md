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
    summary: form.elements.summary.value.trim(),
    smell: form.elements.smell.value.trim(),
    benefits: form.elements.benefits.value.trim(),
    example: form.elements.example.value.trim(),
    solution: form.elements.solution.value.trim()
  };
  const issueTitle = `[Community Proposed pattern] ${fields.summary}`;
  const issueBody = `## Short summary of the pattern

${fields.summary}

## Code smells

${fields.smell}

## Benefits of removing the code smell

${fields.benefits}

## Example showing the pattern

\`\`\`fortran
${fields.example}
\`\`\`

## Updated example

${fields.solution ? `\`\`\`fortran
${fields.solution}
\`\`\`` : "Not provided"}`;
  const url =
    "https://github.com/carpentries-incubator/legacy-fortran/issues/new"
    + "?labels=legacy-fortran"
    + "&title=" + encodeURIComponent(issueTitle)
    + "&body=" + encodeURIComponent(issueBody);

  window.open(url, "_blank");
}
</script>

# Legacy Code Confessions

Legacy Fortran is full of code that works, has survived for decades, and is
difficult to change. Despite their success, these legacy systems can be hard to
understand, test, maintain, or modernise. To help, we are collecting the
patterns that give legacy systems these qualities, together with tried and
tested the alternatives that can help.

This is not about blaming the people who wrote the code. Constraints change,
and many of these choices were reasonable at the time. The goal is to give the
next developer a map: what to recognise, why it is risky, and where to start
improving it.

If you have knowledge to share, please continue reading and contribute today!

## What makes a useful contribution?

Tell us about one specific pattern. This won't necessarily be a bug and the
code may still appear to work. These patterns can usually be identified through
their [code smells](https://en.wikipedia.org/wiki/Code_smell) that hint at
deeper design or maintainability problems; It might involve a language feature,
a build or testing practice, or an organisational habit around a codebase. The
most useful reports include:

* A short summary naming the pattern.
* The code smells that help a developer identify the issue;
* The benefits of moving away from this pattern;
* A small example showing the pattern; and
* An updated code example showing the solution.

For example, the short summary could be "Break large procedures into smaller
units". The code smells might be that Multiple dummy arguments are updated in a
single procedure (i.e. many intent(out) arguments) or simply that a line of
code is deeply indented. The benefits could include that procedures with only
one purpose are much easier to unit test as well as being easier to fix should
a bug be introduced. A small example can show the original procedure updating
multiple dummy arguments, followed by an updated set of multiple procedures for
each task.

## Share a pattern

Submit one pattern at a time. You should not name any individual or
organisation, and please remove proprietary or confidential details. Your
submission will open as a GitHub issue so the curriculum team can discuss,
edit, and review it before anything is published.

<div class="legacy-patterns-container">
  <form class="submit-box" onsubmit="submitTip(event)">
    <label for="tip-summary">Short summary of the problem <span>*</span></label>
    <input
      class="tip-input"
      id="tip-summary"
      name="summary"
      required
      placeholder="e.g. Global state hidden in COMMON blocks"
    />
    <label for="tip-smell">Code smell <span>*</span></label>
    <textarea
      class="tip-textarea"
      id="tip-smell"
      name="smell"
      required
      placeholder="What recognisable sign helps a developer identify this issue?"
    ></textarea>
    <label for="tip-benefits">Benefits of removing the code smell <span>*</span></label>
    <textarea
      class="tip-textarea"
      id="tip-benefits"
      name="benefits"
      required
      placeholder="How will the code become easier to understand, test, maintain, or change?"
    ></textarea>
    <label for="tip-example">Small example showing the pattern <span>*</span></label>
    <textarea
      class="tip-textarea tip-code"
      id="tip-example"
      name="example"
      required
      placeholder="Paste a small, self-contained Fortran example"
    ></textarea>
    <label for="tip-solution">Updated code showing the solution <span class="optional">optional</span></label>
    <textarea
      class="tip-textarea tip-code"
      id="tip-solution"
      name="solution"
      placeholder="Show the same example after removing the code smell"
    ></textarea>
    <p class="submit-helper">
      Required fields are marked *. Keep examples small and remove confidential
      code or details that identify individuals.
    </p>
    <button class="tip-submit-btn" type="submit">Open a GitHub issue</button>
  </form>
</div>

## Learn more

This project grew from the fourth
[Back to the Fortran Future](https://rsecon26.society-rse.org/satellite-events/back-to-the-fortran-future-4/)
workshop, held as a satellite event to the
[10th annual Research Software Engineering Conference](https://rsecon26.society-rse.org/) in Sheffield on 8
September 2026. The workshop brought together people working on one of
Fortran's persistent challenges: developers inheriting large, important
codebases without the context needed to maintain them confidently.

One outcome will be a practical guide for developers who need to understand and
modernise legacy Fortran. We also want the resulting entries to be structured
enough for tools and AI assistants to use responsibly: a recognisable pattern,
the benefits of its removal, and examples grounded in real experience.
[Share a code smell above](#share-a-pattern) to help build this resource.

This guide will live in the
[Software Carpentries Incubator](https://carpentries-incubator.github.io/legacy-fortran/),
and may grow into a dedicated Carpentries-style workshop linked to the larger
[Fortran Carpentries curriculum](https://carpentries-incubator.github.io/intro-to-modern-fortran/profiles.html#pathways).
