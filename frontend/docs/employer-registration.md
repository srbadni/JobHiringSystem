# Employer registration

Only `/auth/employer/register` uses `EmployerRegistrationForm`. The two login routes and job-seeker registration still use the existing `AuthForm`.

## Flow

1. Existing account fields and submit label. Native required/email/minimum-password-length validation and matching passwords must pass before continuing.
2. Phone verification preview. Any non-whitespace code plus the continue button advances; no SMS or verification request is made. Editing account details clears the previous code.
3. Persian/English company names, optional logo file (required when its switch is enabled), confidential contact phone, optional website, one or more distinct activity selections, and employee count.

Fields stay mounted while inactive fieldsets are hidden and disabled. Back navigation preserves account/company values, activity selections, and the selected file. Disabled steps do not block native validation. The Persian company name is initially copied from step one and preserves an explicit edit in step three.

## API integration point

Edit `onSubmit(data: EmployerRegistrationData)` in `src/features/authentication/ui/employer-registration-form.tsx`. It runs only on the final submission and currently displays a preview confirmation without making a request or claiming an account was created.

```ts
{
    account: { fullName, companyName, email, phone, password, confirmPassword },
    company: { nameFa, nameEn, logo, phone, website, activityCodes, employeeCount }
}
```

`logo` is `File | null`, so use multipart `FormData` or a separate upload when adding the API. The verification code is intentionally absent. Values live only in component memory; reloading resets the flow. Passwords and company details are not logged or persisted by this form.

`companyActivityOptions` in `model/employer-registration.ts` contains **temporary UI options**, not backend IDs. Replace those options and map activity selections to the API contract when integrating registration. Employee-count values already match the backend `EmployeeCount` enum. This form's payload is a UI contract, not a claim that the current backend accepts all these fields or multiple activities.

## Manual checks

- Try blank/invalid step-one fields and mismatching passwords; then submit valid values with Enter.
- Try an empty/whitespace code, then any nonempty code; the latter advances without a request.
- Fill company information, choose a logo and multiple distinct activities, go back twice, edit the phone and advance again. Confirm values/file are retained and the code was reset.
- Remove an activity and disable the logo switch; the final payload should omit the disabled file (`logo: null`).
- Submit the final step; only preview feedback appears. Check 320px/mobile, tablet and desktop widths and the other three auth routes.

## Validation results

- Targeted ESLint, including FSD boundaries, and `git diff --check` pass.
- Chromium interaction checks pass for the three-step flow, invalid/blank inputs, password matching, Enter submission, back/edit persistence, phone/code reset, file retention and disabling, activity add/remove/deduplication, final feedback, and the other three authentication routes. No page errors or POST requests occurred.
- No horizontal overflow at 320px, 375px, or 768px; desktop and mobile screenshots were visually inspected.
- `npm run build` compiles successfully, then stops at the existing `TS2322` in `src/_pages/job-details/ui/JobDetails.tsx:58`. `npm run typecheck` reports the same error. It was reproduced in an unchanged checkout of base commit `bf5359f`; no validation gate was disabled.
