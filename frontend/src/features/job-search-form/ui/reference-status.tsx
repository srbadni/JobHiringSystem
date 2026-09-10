interface ReferenceStatusProps {
  id: string;
  label: string;
  pending: boolean;
  failed: boolean;
  empty: boolean;
  fetching: boolean;
  onRetry: () => void;
}

export function ReferenceStatus({ id, label, pending, failed, empty, fetching, onRetry }: ReferenceStatusProps) {
  return (
    <div id={id} role="status" className="text-sm text-muted">
      {pending && `در حال دریافت ${label}…`}
      {empty && `${label} برای انتخاب موجود نیست.`}
      {failed && (
        <p>
          دریافت {label} ناموفق بود.{" "}
          <button type="button" disabled={fetching} className="text-primary underline disabled:opacity-50" onClick={onRetry}>
            تلاش مجدد
          </button>
        </p>
      )}
    </div>
  );
}
