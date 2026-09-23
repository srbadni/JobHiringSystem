# Authentication design preview

Employer registration now has a dedicated three-step flow; see [Employer registration](./employer-registration.md) for its current behavior and final `onSubmit` integration point. The notes below describe the original shared-page design.

The four RTL pages follow the supplied desktop, tablet and mobile references:

| Page | URL |
| --- | --- |
| Job seeker login | `/auth/job-seeker/login` |
| Job seeker registration | `/auth/job-seeker/register` |
| Employer login | `/auth/employer/login` |
| Employer registration | `/auth/employer/register` |

The existing header's login link opens the job seeker login page. Role links preserve login/registration mode; the link below each form switches mode for the current role.

## Scope

These are UI previews. Submitting with the button or Enter prevents browser submission and shows a preview message. There is no authentication request, server action, credential storage, session handling or redirect. Inputs use native required/email/minimum-length constraints; complete registration validation belongs to the later authentication implementation. Password visibility toggles work independently. Password recovery is displayed as an unavailable button because its flow does not exist yet.

## FSD composition

- `app/(auth)/auth/*`: four thin route adapters and Persian metadata.
- `src/_pages/auth`: page composition, header/footer and role theme.
- `src/widgets/auth-showcase`: responsive promotional panel and illustrative cards. Cards are presentation samples, not real job/application entities.
- `src/features/authentication`: role/mode configuration, navigation and preview forms.
- `src/shared/ui`: reuse `Button`, `Typography`, `ArrowLeftIcon`, `BuildingIcon` and `BookmarkIcon`; add generic `Input`, `PasswordInput`, `Brand` and missing icons through public APIs.

The root layout still provides the font and QueryProvider. The existing routes moved into `(site)` **without URL changes**; their header/footer and backend-dependent GlobalStatesProviderWrapper live in that group's layout. Authentication pages consequently render without a backend URL or job-category request. There are no new production dependencies.

Below 768px the showcase is hidden. Between 768px and 1199px the two panels remain visible and all form fields stack. At 1200px and above registration uses paired fields, while the job seeker's name/email remain full width.

## Validation

- New and edited authentication/shared/header/layout code passes ESLint, including the repository's FSD boundary rules.
- Browser checks: all four routes return HTTP 200 at 1920px, 1025px and mobile reference widths (450px/517px); no horizontal overflow; correct panel visibility. Additional overflow checks pass at 320px, 375px, 768px, 1199px and 1200px.
- Desktop, tablet and mobile screenshots inspected for the four pages.
- Browser interactions pass: independent password toggles, Enter submission for both roles and modes, preview feedback, role/mode navigation and disabled recovery action. No POST requests or page errors in the final browser run.
- Full-repository lint still reports the same **40 errors and 7 warnings** reproduced on base commit `fc85af4`.
- `npm run typecheck` and `npm run build` stop at the pre-existing `TS2322` in `src/_pages/job-details/ui/JobDetails.tsx:58`: its form action returns an object instead of `void`. The same TypeScript error was reproduced on the unmodified base. The production bundle compiles before reaching that gate; no typecheck/lint gates were disabled.

For manual review, run `npm ci` and `npm run dev`, then open any URL above. The authentication previews do not need `.env` configuration or a running backend. Existing site routes retain their backend configuration requirements.
