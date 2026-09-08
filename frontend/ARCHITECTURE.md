# Frontend architecture

This frontend uses **Feature-Sliced Design (FSD)** together with the Next.js App Router.

## Layers

Dependencies flow only from higher layers to lower layers:

1. `app/` — Next.js routing, global styles, metadata, and providers. Route files remain thin and render a page slice.
2. `src/views/` — the FSD **Pages layer**: complete screens that compose widgets and features. It is named `views` because Next.js reserves `pages` for its Pages Router; this avoids enabling a second router while preserving the FSD layer and its responsibilities.
3. `src/widgets/` — large reusable page sections, such as the application header.
4. `src/features/` — user interactions that deliver business value, such as submitting a job search.
5. `src/entities/` — business concepts, their API operations, types, and small domain UI controls.
6. `src/shared/` — business-agnostic UI, API infrastructure, configuration, and utilities.

ESLint enforces the downward dependency rule. Each slice exposes a public API through `index.ts`; consumers should import from that entry point rather than reaching into another slice's internals.

## Slice conventions

Use only the segments a slice needs:

- `ui/` for React components;
- `model/` for types and state;
- `api/` for requests and transport mapping;
- `lib/` for helpers local to the slice;
- `config/` for slice configuration.

Create a feature for an actual user action, not every visual component. Generic controls belong in `shared/ui`; domain nouns belong in `entities`; composition without a new interaction belongs in `widgets` or `views`.

## Adding a route

1. Build the screen in `src/views/<page>/ui` and export it from the slice's `index.ts`.
2. Add a thin route adapter at `app/<route>/page.tsx`.
3. Put route paths in `src/shared/config/routes.ts` instead of scattering string literals.

The API client reads `NEXT_PUBLIC_API_URL` and defaults locally to `http://localhost:8000/api/v1`.
