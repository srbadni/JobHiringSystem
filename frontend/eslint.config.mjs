import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
  ]),
  {
    files: ["src/shared/**/*.{ts,tsx}"],
    rules: { "no-restricted-imports": ["error", { patterns: ["@/entities/**", "@/features/**", "@/widgets/**", "@/views/**"] }] },
  },
  {
    files: ["src/entities/**/*.{ts,tsx}"],
    rules: { "no-restricted-imports": ["error", { patterns: ["@/features/**", "@/widgets/**", "@/views/**"] }] },
  },
  {
    files: ["src/features/**/*.{ts,tsx}"],
    rules: { "no-restricted-imports": ["error", { patterns: ["@/widgets/**", "@/views/**"] }] },
  },
  {
    files: ["src/widgets/**/*.{ts,tsx}"],
    rules: { "no-restricted-imports": ["error", { patterns: ["@/views/**"] }] },
  },
]);

export default eslintConfig;
