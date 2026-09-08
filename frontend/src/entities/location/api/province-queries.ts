import { queryOptions } from "@tanstack/react-query";
import { provinceApi } from "./province-api";

export const provinceKeys = {
  all: ["location", "provinces"] as const,
};

export const provinceQueries = {
  all: () => queryOptions({
    queryKey: provinceKeys.all,
    queryFn: ({ signal }) => provinceApi.getAll(signal),
    staleTime: 5 * 60 * 1000,
  }),
};
