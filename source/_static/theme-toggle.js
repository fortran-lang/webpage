(function () {
  "use strict";

  function normalizeMode(value) {
    return value === "dark" ? "dark" : "light";
  }

  function getStoredMode() {
    return normalizeMode(localStorage.getItem("mode"));
  }

  function applyTheme(mode) {
    var normalized = normalizeMode(mode);

    document.documentElement.dataset.mode = normalized;
    document.documentElement.dataset.theme = normalized;

    localStorage.setItem("mode", normalized);
    localStorage.setItem("theme", normalized);

    document.querySelectorAll(".dropdown-menu").forEach(function (menu) {
      if (normalized === "dark") {
        menu.classList.add("dropdown-menu-dark");
      } else {
        menu.classList.remove("dropdown-menu-dark");
      }
    });
  }

  function updateSwitcherIcons(activeTheme) {
    document.querySelectorAll(".theme-switch-button").forEach(function (button) {
      button
        .querySelectorAll('.theme-switch[data-mode="auto"]')
        .forEach(function (icon) {
          icon.remove();
        });

      button.querySelectorAll(".theme-switch").forEach(function (icon) {
        icon.classList.toggle("d-none", icon.dataset.mode !== activeTheme);
      });
    });
  }

  function toggleTheme(event) {
    event.preventDefault();
    event.stopImmediatePropagation();

    var current = normalizeMode(document.documentElement.dataset.theme);
    var next = current === "dark" ? "light" : "dark";

    applyTheme(next);
    updateSwitcherIcons(next);
  }

  function initThemeToggleOverride() {
    var storedMode = getStoredMode();

    applyTheme(storedMode);
    updateSwitcherIcons(storedMode);

    document.querySelectorAll(".theme-switch-button").forEach(function (button) {
      button.addEventListener("click", toggleTheme, true);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initThemeToggleOverride);
  } else {
    initThemeToggleOverride();
  }
})();
