import axios from "axios";

// NEXT_PUBLIC variables are public and are embedded at build time by Next.js.
const baseURL = process.env.NEXT_PUBLIC_BASE_URL?.trim();

export const httpClient = axios.create({
  baseURL,
  timeout: 15_000,
  headers: { Accept: "application/json" },
});

// Fail on request, not during module evaluation or static page generation.
httpClient.interceptors.request.use((config) => {
  if (!config.baseURL) {
    throw new Error("NEXT_PUBLIC_BASE_URL is not configured.");
  }
  return config;
});
