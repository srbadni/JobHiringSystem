import { checkFsdImport } from "./fsd-policy.mjs";

export default {
  rules: {
    boundaries: {
      meta: {
        type: "problem",
        schema: [],
        messages: { boundary: "{{reason}}" },
      },
      create(context) {
        function inspect(source) {
          if (!source || typeof source.value !== "string") return;
          const reason = checkFsdImport(context.filename, source.value, context.cwd);
          if (reason) context.report({ node: source, messageId: "boundary", data: { reason } });
        }
        return {
          ImportDeclaration: (node) => inspect(node.source),
          ExportNamedDeclaration: (node) => inspect(node.source),
          ExportAllDeclaration: (node) => inspect(node.source),
          ImportExpression: (node) => inspect(node.source),
          TSImportType: (node) => inspect(node.argument?.literal ?? node.argument ?? node.parameter?.literal),
          CallExpression(node) {
            if (node.callee.type === "Identifier" && node.callee.name === "require") inspect(node.arguments[0]);
          },
        };
      },
    },
  },
};
