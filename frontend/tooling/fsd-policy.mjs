import path from "node:path";

const layers = ["_app", "_pages", "widgets", "features", "entities", "shared"];
const sliced = new Set(["_pages", "widgets", "features", "entities"]);

function describe(filename, root) {
  const relative = path.relative(root, filename).split(path.sep).join("/");
  if (relative.startsWith("app/")) return { layer: "router", parts: relative.split("/") };
  if (!relative.startsWith("src/")) return null;
  const parts = relative.slice(4).split("/");
  return { layer: parts[0], slice: parts[1], parts };
}

function publicEntry(target) {
  const parts = [...target.parts];
  parts[parts.length - 1] = parts.at(-1).replace(/\.(?:[cm]?[jt]sx?)$/, "");
  if (parts.at(-1) === "index" || parts.at(-1) === "index.server") parts.pop();
  if (sliced.has(target.layer)) return parts.length === 2;
  if (target.layer === "shared") {
    return parts[1] === "ui" ? parts.length === 3 : parts.length === 2;
  }
  return true;
}

export function checkFsdImport(filename, specifier, root) {
  const from = describe(filename, root);
  if (!from) return null;
  let destination;
  if (specifier.startsWith("@/")) destination = path.resolve(root, "src", specifier.slice(2));
  else if (specifier.startsWith(".")) destination = path.resolve(path.dirname(filename), specifier);
  else return null; // Third-party packages are outside FSD's layer rules.

  const to = describe(destination, root);
  if (!to || (to.layer !== "router" && !layers.includes(to.layer))) {
    return "Local application code must live in a recognized FSD layer.";
  }
  if (to.layer === "router" && from.layer !== "router") {
    return "FSD code must not import the Next.js routing directory.";
  }
  if (from.layer === "router") {
    return to.layer !== "router" && !publicEntry(to) ? "Import the slice's public API." : null;
  }
  if (layers.indexOf(to.layer) < layers.indexOf(from.layer)) {
    return "FSD layers may only import lower layers.";
  }
  if (from.layer === to.layer) {
    if (sliced.has(from.layer) && from.slice !== to.slice) {
      return "Slices in the same layer must not import each other.";
    }
    // App and Shared are organized into segments, not isolated slices.
    return null;
  }
  return publicEntry(to) ? null : "Import the slice's public API.";
}
