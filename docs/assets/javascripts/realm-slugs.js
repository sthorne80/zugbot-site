(function () {
  "use strict";

  function dataUrl() {
    var script = document.querySelector('script[src*="assets/javascripts/realm-slugs.js"]');
    return script ? new URL("../realm-slugs.json", script.src).href : "../assets/realm-slugs.json";
  }

  function text(value) {
    return document.createTextNode(String(value));
  }

  function cell(value, className) {
    var element = document.createElement("td");
    if (className) element.className = className;
    element.appendChild(text(value));
    return element;
  }

  function initialize(root) {
    var input = root.querySelector("#realm-search");
    var status = root.querySelector("[data-realm-status]");
    var updated = root.querySelector("[data-realm-updated]");
    var results = root.querySelector("[data-realm-results]");
    var realms = [];
    var renderLimit = 100;

    function render() {
      var query = input.value.trim().toLocaleLowerCase();
      var matches = realms.filter(function (realm) {
        return !query || [realm.name, realm.slug, realm.region].some(function (value) {
          return String(value).toLocaleLowerCase().includes(query);
        });
      });
      var visible = matches.slice(0, renderLimit);
      results.replaceChildren();

      if (!visible.length) {
        status.textContent = "No realms match that search.";
        return;
      }

      var table = document.createElement("table");
      table.className = "realm-table";
      var head = document.createElement("thead");
      var headRow = document.createElement("tr");
      ["Realm", "Slug", "Region"].forEach(function (label) {
        var heading = document.createElement("th");
        heading.scope = "col";
        heading.appendChild(text(label));
        headRow.appendChild(heading);
      });
      head.appendChild(headRow);
      table.appendChild(head);

      var body = document.createElement("tbody");
      visible.forEach(function (realm) {
        var row = document.createElement("tr");
        row.appendChild(cell(realm.name));
        row.appendChild(cell(realm.slug, "realm-slug-value"));
        row.appendChild(cell(String(realm.region).toUpperCase(), "realm-region-value"));
        body.appendChild(row);
      });
      table.appendChild(body);
      results.appendChild(table);

      status.textContent = matches.length > renderLimit
        ? "Showing the first " + renderLimit + " of " + matches.length + " matching realms. Refine your search to narrow the list."
        : "Showing " + matches.length + (matches.length === 1 ? " realm." : " realms.");
    }

    fetch(dataUrl(), { credentials: "same-origin" })
      .then(function (response) {
        if (!response.ok) throw new Error("Realm data unavailable");
        return response.json();
      })
      .then(function (payload) {
        if (!payload || !Array.isArray(payload.realms)) throw new Error("Invalid realm data");
        realms = payload.realms;
        if (updated && typeof payload.generated_at === "string") {
          var generatedAt = new Date(payload.generated_at);
          if (!Number.isNaN(generatedAt.getTime())) {
            updated.textContent = "Last updated: " + generatedAt.toISOString().replace("T", " ").replace(/\.\d{3}Z$/, " UTC");
            updated.hidden = false;
          }
        }
        input.disabled = false;
        input.addEventListener("input", render);
        render();
      })
      .catch(function () {
        status.textContent = "Realm reference data has not been generated yet. /character and /link autocomplete are still available in Discord.";
        results.replaceChildren();
      });
  }

  function start() {
    document.querySelectorAll("[data-realm-reference]").forEach(initialize);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start);
  } else {
    start();
  }
}());
