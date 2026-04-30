---
sd_hide_title: true
---

# Packages

:::{div} sd-text-center sd-fs-2 sd-font-weight-bold sd-text-primary
Fortran Packages
:::

:::{div} sd-text-center sd-fs-3
A rich ecosystem of high-performance code
:::

:::{div} sd-fs-3 sd-font-weight-bold sd-text-primary
Find a Package
:::

<form class="package-search-form" action="../search/index.html" method="get"> <input type="search" name="q" id="search-input" class="package-search-input" placeholder="Search for a package" aria-label="Search" autocomplete="off"></form>

:::::{grid} 2
:gutter: 3

::::{grid-item-card}
:shadow: none

:::{div} sd-fs-3
Package index
:::

:::{div} sd-fs-6
The fortran-lang package index is community-maintained and lists open source Fortran-related projects. This includes large-scale scientific applications, function libraries, Fortran interfaces, and developer tools.<br>
See [here](../community/packages/) for how to get your project listed. <br>
Use the box above to search the package index by keyword, package name, or author username.
:::

::::

::::{grid-item-card}
:shadow: none

:::{div} sd-fs-3
Featured topics
:::

:::{jinja} tags
{% for tag in tags %}{bdg-ref-secondary}`{{ tag }} <sphx_tag_{{ tag }}>`{% endfor %}
:::

::::

:::::

:::{div} sd-fs-3 sd-font-weight-bold sd-text-primary
Package Data Table
:::

:::{div} sd-fs-6
Explore and rank packages using repository metadata. You can sort by any column and filter by host, category, tags, stars, issues, and last commit recency.
:::

```{raw} html
<div class="package-table-filters" id="package-table-filters">
	<div class="filter-group">
		<label>Host</label>
		<div class="cc-combo" id="provider-cc"></div>
	</div>
	<div class="filter-group">
		<label>Category</label>
		<div class="cc-combo" id="category-cc"></div>
	</div>
	<div class="filter-group">
		<label>Tags</label>
		<div class="cc-combo" id="tag-cc"></div>
	</div>
	<div class="filter-group">
		<label>Owner</label>
		<input id="author-filter" type="text" placeholder="namespace" />
	</div>
	<div class="filter-group">
		<label>Since</label>
		<input id="recent-date-filter" type="date" />
	</div>
	<div class="filter-group">
		<label>Min ★</label>
		<input id="min-stars-filter" type="number" min="0" step="1" placeholder="0" />
	</div>
	<div class="filter-group filter-group--btn">
		<button id="clear-package-filters" type="button">Reset</button>
	</div>
</div>

<div class="package-table-wrap">
	<table id="package-data-table" class="display compact package-data-table" style="width:100%">
		<thead>
			<tr>
				<th>Name</th>
				<th>Host</th>
				<th>Owner</th>
				<th>Categories</th>
				<th>Tags</th>
				<th>Stars</th>
				<th>Forks</th>
				<th>Issues</th>
				<th>Pulls</th>
				<th>Last commit</th>
				<th>License</th>
			</tr>
		</thead>
		<tbody></tbody>
	</table>
</div>

<link rel="stylesheet" href="https://cdn.datatables.net/1.13.8/css/jquery.dataTables.min.css" />
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.datatables.net/1.13.8/js/jquery.dataTables.min.js"></script>
```

::::{jinja} fortran_index_enriched
<script>
(() => {
	const enriched = {{ (fortran_index_enriched | default({}, true)) | tojson }};
	const tableElement = document.getElementById("package-data-table");
	const authorFilter = document.getElementById("author-filter");
	const recentDateFilter = document.getElementById("recent-date-filter");
	const minStarsFilter = document.getElementById("min-stars-filter");
	const clearFiltersButton = document.getElementById("clear-package-filters");

	// ── Check-combobox factory ──────────────────────────────────────────────────
	function makeCheckCombo(container, items, onChange) {
		const trigger = document.createElement("div");
		trigger.className = "cc-trigger";
		trigger.setAttribute("tabindex", "0");
		const chipsEl = document.createElement("span");
		chipsEl.className = "cc-chips";
		const placeholder = document.createElement("span");
		placeholder.className = "cc-placeholder";
		placeholder.textContent = "All";
		const arrow = document.createElement("span");
		arrow.className = "cc-arrow";
		arrow.textContent = "▾";
		trigger.appendChild(chipsEl);
		trigger.appendChild(placeholder);
		trigger.appendChild(arrow);

		const panel = document.createElement("div");
		panel.className = "cc-panel";
		panel.hidden = true;

		const selected = new Set();

		function renderChips() {
			chipsEl.innerHTML = "";
			if (selected.size === 0) {
				placeholder.style.display = "";
			} else {
				placeholder.style.display = "none";
				selected.forEach((val) => {
					const chip = document.createElement("span");
					chip.className = "cc-chip";
					chip.textContent = val + " \u00d7";
					chip.addEventListener("click", (e) => {
						e.stopPropagation();
						selected.delete(val);
						panel.querySelectorAll("input[type=checkbox]").forEach((cb) => {
							if (cb.value === val) cb.checked = false;
						});
						renderChips();
						onChange();
					});
					chipsEl.appendChild(chip);
				});
			}
		}

		items.forEach(({ value, label }) => {
			const itemEl = document.createElement("label");
			itemEl.className = "cc-item";
			const cb = document.createElement("input");
			cb.type = "checkbox";
			cb.value = value;
			cb.addEventListener("change", () => {
				if (cb.checked) selected.add(value);
				else selected.delete(value);
				renderChips();
				onChange();
			});
			itemEl.appendChild(cb);
			itemEl.appendChild(document.createTextNode("\u00a0" + label));
			panel.appendChild(itemEl);
		});

		function positionPanel() {
			const r = trigger.getBoundingClientRect();
			panel.style.top = (r.bottom + 2) + "px";
			panel.style.left = r.left + "px";
			panel.style.minWidth = r.width + "px";
		}

		function openPanel() {
			positionPanel();
			panel.hidden = false;
		}

		function closePanel() {
			panel.hidden = true;
		}

		trigger.addEventListener("click", () => { panel.hidden ? openPanel() : closePanel(); });
		trigger.addEventListener("keydown", (e) => {
			if (e.key === "Enter" || e.key === " ") { e.preventDefault(); panel.hidden ? openPanel() : closePanel(); }
		});
		document.addEventListener("click", (e) => {
			if (!container.contains(e.target) && !panel.contains(e.target)) closePanel();
		});
		window.addEventListener("scroll", () => { if (!panel.hidden) positionPanel(); }, { passive: true });
		window.addEventListener("resize", () => { if (!panel.hidden) positionPanel(); }, { passive: true });

		document.body.appendChild(panel);
		container.appendChild(trigger);
		renderChips();

		container._getSelected = () => selected;
		container._renderChips = renderChips;
		container.clearSelection = () => {
			selected.clear();
			panel.querySelectorAll("input[type=checkbox]").forEach((cb) => { cb.checked = false; });
			renderChips();
		};
	}

	// ── Data helpers ────────────────────────────────────────────────────────────
	function asString(value) {
		if (typeof value === "string") return value;
		if (value == null) return "";
		return String(value);
	}

	function splitSlug(value) {
		return asString(value).split("/").map((p) => p.trim()).filter(Boolean);
	}

	function parseTags(value) {
		if (Array.isArray(value)) return value.map((t) => asString(t).trim()).filter(Boolean);
		return asString(value).split(/\s+/).filter(Boolean);
	}

	function packageKey(pkg) {
		if (pkg.repository && pkg.repository.provider && pkg.repository.repo_slug) {
			return `${asString(pkg.repository.provider)}:${asString(pkg.repository.repo_slug)}`;
		}
		if (pkg.github) return `github:${asString(pkg.github)}`;
		if (pkg.gitlab) return `gitlab:${asString(pkg.gitlab)}`;
		if (pkg.url) return `url:${asString(pkg.url)}`;
		return `name:${asString(pkg.name)}`;
	}

	function ownerFromPackage(pkg) {
		if (pkg.github) return splitSlug(pkg.github)[0] || "";
		if (pkg.gitlab) return splitSlug(pkg.gitlab)[0] || "";
		if (pkg.repository && pkg.repository.repo_slug) return splitSlug(pkg.repository.repo_slug)[0] || "";
		return "";
	}

	function normalizeProvider(pkg) {
		if (pkg.repository && pkg.repository.provider) return pkg.repository.provider;
		if (pkg.github) return "github";
		if (pkg.gitlab) return "gitlab";
		return "url";
	}

	function mergePackage(existing, incoming, category) {
		existing.categories.add(category);
		parseTags(incoming.tags).forEach((tag) => existing.tags.add(tag));
		if (!existing.description && incoming.description) existing.description = incoming.description;
		if (!existing.repositoryUrl && incoming.repositoryUrl) existing.repositoryUrl = incoming.repositoryUrl;
		if (!existing.license && incoming.license) existing.license = incoming.license;
		["stars", "forks", "issues", "pulls"].forEach((field) => {
			if (existing[field] == null && incoming[field] != null) existing[field] = incoming[field];
		});
		if (!existing.lastCommit && incoming.lastCommit) existing.lastCommit = incoming.lastCommit;
	}

	// ── Build package map ───────────────────────────────────────────────────────
	const packageMap = new Map();
	const knownCategories = Object.keys(enriched).filter((c) => c !== "meta");
	knownCategories.forEach((category) => {
		(enriched[category] || []).forEach((pkg) => {
			const repository = pkg.repository || {};
			const normalized = {
				key: packageKey(pkg),
				name: asString(pkg.name),
				provider: normalizeProvider(pkg),
				owner: ownerFromPackage(pkg),
				repositoryUrl: asString(repository.repository_url || pkg.url),
				categories: new Set([category]),
				tags: new Set(parseTags(pkg.tags)),
				stars: repository.stars_count ?? null,
				forks: repository.forks_count ?? null,
				issues: repository.open_issues_count ?? null,
				pulls: repository.open_pulls_count ?? null,
				lastCommit: asString(repository.last_commit_date || ""),
				license: asString(pkg.license || repository.license),
				description: asString(pkg.description),
			};
			if (!packageMap.has(normalized.key)) {
				packageMap.set(normalized.key, normalized);
			} else {
				mergePackage(packageMap.get(normalized.key), normalized, category);
			}
		});
	});

	// ── Top-50 tags by frequency ────────────────────────────────────────────────
	const tagFreq = new Map();
	packageMap.forEach((pkg) => {
		pkg.tags.forEach((tag) => tagFreq.set(tag, (tagFreq.get(tag) || 0) + 1));
	});
	const topTags = Array.from(tagFreq.entries())
		.sort((a, b) => b[1] - a[1])
		.slice(0, 50)
		.map(([tag]) => tag)
		.sort();

	// ── Build rows ──────────────────────────────────────────────────────────────
	// cols: name(0) provider(1) owner(2) categories(3) tags-csv(4)
	//       stars(5) forks(6) issues(7) pulls(8) lastCommit(9) license(10)
	const rows = Array.from(packageMap.values()).map((pkg) => {
		const categories = Array.from(pkg.categories).sort().join(", ");
		const tags = Array.from(pkg.tags).sort().join(", ");
		const displayName = pkg.repositoryUrl
			? `<a href="${pkg.repositoryUrl}" target="_blank" rel="noopener noreferrer">${pkg.name}</a>`
			: pkg.name;
		return [
			displayName,
			pkg.provider,
			pkg.owner,
			categories,
			tags,
			pkg.stars ?? "",
			pkg.forks ?? "",
			pkg.issues ?? "",
			pkg.pulls ?? "",
			pkg.lastCommit || "",
			pkg.license || "",
		];
	});

	// ── Populate check-comboboxes ───────────────────────────────────────────────
	const providerCC = document.getElementById("provider-cc");
	const categoryCC = document.getElementById("category-cc");
	const tagCC = document.getElementById("tag-cc");

	makeCheckCombo(
		providerCC,
		[{ value: "github", label: "GitHub" }, { value: "gitlab", label: "GitLab" }, { value: "url", label: "Other" }],
		function () { redrawTable(); },
	);
	makeCheckCombo(
		categoryCC,
		knownCategories.sort().map((c) => ({ value: c, label: c })),
		function () { redrawTable(); },
	);
	makeCheckCombo(
		tagCC,
		topTags.map((t) => ({ value: t, label: t })),
		function () { redrawTable(); },
	);

	// ── Tag badge helpers ───────────────────────────────────────────────────────
	function renderTagBadgesHtml(tagsCsv) {
		if (!tagsCsv) return "";
		const sel = tagCC && tagCC._getSelected ? tagCC._getSelected() : new Set();
		return asString(tagsCsv).split(",").map((t) => {
			const tag = t.trim();
			if (!tag) return "";
			const cls = sel.has(tag) ? " active" : "";
			return `<span class="pkg-tag${cls}" data-tag="${tag}">${tag}</span>`;
		}).join(" ");
	}

	function applyTagClick(cell) {
		cell.querySelectorAll(".pkg-tag").forEach((el) => {
			el.addEventListener("click", () => {
				const tag = el.dataset.tag;
				const sel = tagCC._getSelected();
				if (sel.has(tag)) sel.delete(tag);
				else sel.add(tag);
				tagCC.querySelectorAll("input[type=checkbox]").forEach((cb) => {
					if (cb.value === tag) cb.checked = sel.has(tag);
				});
				if (tagCC._renderChips) tagCC._renderChips();
				redrawTable();
			});
		});
	}

	// ── Filter predicate ────────────────────────────────────────────────────────
	function rowMatchesFilters(rowData) {
		const selProviders = providerCC._getSelected ? providerCC._getSelected() : new Set();
		const selCats = categoryCC._getSelected ? categoryCC._getSelected() : new Set();
		const selTags = tagCC._getSelected ? tagCC._getSelected() : new Set();
		const authorNeedle = asString(authorFilter.value).toLowerCase().trim();
		const dateThreshold = recentDateFilter.value ? new Date(recentDateFilter.value) : null;
		const minStars = minStarsFilter.value ? Number(minStarsFilter.value) : null;

		if (selProviders.size > 0 && !selProviders.has(rowData[1])) return false;

		if (selCats.size > 0) {
			const rowCats = asString(rowData[3]).split(",").map((c) => c.trim()).filter(Boolean);
			if (!rowCats.some((c) => selCats.has(c))) return false;
		}

		if (selTags.size > 0) {
			const rowTags = asString(rowData[4]).split(",").map((t) => t.trim()).filter(Boolean);
			if (!rowTags.some((t) => selTags.has(t))) return false;
		}

		if (authorNeedle && !asString(rowData[2]).toLowerCase().includes(authorNeedle)) return false;

		const rowStars = rowData[5] === "" ? null : Number(rowData[5]);
		const rowLastCommit = rowData[9] ? new Date(rowData[9]) : null;
		if (dateThreshold && (!rowLastCommit || rowLastCommit < dateThreshold)) return false;
		if (minStars != null && (rowStars == null || rowStars < minStars)) return false;

		return true;
	}

	// ── Plain-table renderer (no DataTables) ───────────────────────────────────
	function renderPlainTable(filteredRows) {
		const tbody = tableElement.querySelector("tbody");
		tbody.innerHTML = "";
		filteredRows.forEach((rowData) => {
			const tr = document.createElement("tr");
			rowData.forEach((cell, index) => {
				const td = document.createElement("td");
				if (index === 0) {
					td.innerHTML = cell;
				} else if (index === 4) {
					td.innerHTML = renderTagBadgesHtml(asString(cell));
					applyTagClick(td);
				} else if ([5, 6, 7, 8].includes(index)) {
					td.textContent = String(cell ?? "");
					td.style.textAlign = "right";
				} else {
					td.textContent = String(cell ?? "");
				}
				tr.appendChild(td);
			});
			tbody.appendChild(tr);
		});
	}

	// ── DataTables init ─────────────────────────────────────────────────────────
	const hasDataTables = !!(window.jQuery && window.jQuery.fn && window.jQuery.fn.DataTable);
	let table = null;
	const fallbackStatus = document.createElement("p");
	fallbackStatus.className = "package-table-status";
	tableElement.insertAdjacentElement("afterend", fallbackStatus);

	if (hasDataTables) {
		table = $(tableElement).DataTable({
			data: rows,
			pageLength: 50,
			order: [[9, "desc"]],
			autoWidth: false,
			columnDefs: [
				{ targets: [0], createdCell: function (td, cellData) { td.innerHTML = cellData; } },
				{
					targets: [4],
					createdCell: function (td, cellData) {
						td.innerHTML = renderTagBadgesHtml(asString(cellData));
						applyTagClick(td);
					},
				},
				{ targets: [5, 6, 7, 8], type: "num", className: "dt-body-right" },
				{ targets: [9], type: "date" },
			],
			drawCallback: function () {
				if (tagCC && tagCC._getSelected) {
					const sel = tagCC._getSelected();
					tableElement.querySelectorAll(".pkg-tag").forEach((el) => {
						el.classList.toggle("active", sel.has(el.dataset.tag));
					});
				}
			},
			language: {
				search: "Search:",
				lengthMenu: "Show _MENU_",
				info: "_START_\u2013_END_ of _TOTAL_",
				infoFiltered: "(filtered from _MAX_)",
				zeroRecords: "No matching packages",
			},
		});

		$.fn.dataTable.ext.search.push((settings, rowData) => {
			if (settings.nTable !== tableElement) return true;
			return rowMatchesFilters(rowData);
		});
	}

	// ── Redraw / event wiring ───────────────────────────────────────────────────
	function redrawTable() {
		if (table) {
			table.draw();
			fallbackStatus.textContent = "";
			return;
		}
		const filteredRows = rows.filter(rowMatchesFilters);
		renderPlainTable(filteredRows);
		fallbackStatus.textContent = `Showing ${filteredRows.length} of ${rows.length} packages`;
	}

	[authorFilter, recentDateFilter, minStarsFilter].forEach((el) => {
		el.addEventListener("input", redrawTable);
		el.addEventListener("change", redrawTable);
	});

	clearFiltersButton.addEventListener("click", () => {
		if (providerCC.clearSelection) providerCC.clearSelection();
		if (categoryCC.clearSelection) categoryCC.clearSelection();
		if (tagCC.clearSelection) tagCC.clearSelection();
		authorFilter.value = "";
		recentDateFilter.value = "";
		minStarsFilter.value = "";
		if (table) { table.search("").draw(); return; }
		redrawTable();
	});

	if (!table) redrawTable();
})();
</script>
:::::

:::{div} sd-fs-3 sd-font-weight-bold sd-text-primary
Browse Packages by Category
:::

:::{jinja} categories
{% for slug, item in categories.items() %}
## [{{item.title}}](../categories/{{slug}})

{{item.description}}
{% endfor %}

See [package index guidelines](../community/packages) for how to get your project listed.

::::::{jinja} categories
:::{toctree}
:hidden:

{% for slug,item in categories.items() %}
categories/{{slug}}
{% endfor %}
:::
::::::
