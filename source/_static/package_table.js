document.addEventListener("DOMContentLoaded", () => {
    new Tabulator("#package_table_test", {
        columns: [
            {title: "Package", field: "name"},
            {title: "Release", field: "release"},
            {title: "Stars", field: "stars", sorter: "number"},
            {title: "Forks", field: "forks", sorter: "number"},
            {title: "Last Commit", field: "lastCommit", sorter: "date"},
            {title: "Issues", field: "issues", sorter: "number"},
            {title: "Pull Requests", field: "prs", sorter: "number"},
        ]
    });
});
