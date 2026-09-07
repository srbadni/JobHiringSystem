# پروژهٔ JobHiringSystem

بک‌اند و فرانت‌اند در یک مخزن و در دو پوشهٔ مستقل نگهداری می‌شوند.

| مسیر | کاربرد |
| --- | --- |
| `backend/src/` | لایه‌های فعلی بک‌اند و ورودی برنامه |
| `backend/alembic/` و `backend/alembic.ini` | migrationها و تنظیمات Alembic |
| `backend/pyproject.toml` و `backend/uv.lock` | تنظیمات پایتون و وابستگی‌های قفل‌شده |
| `backend/tests/` | تست‌های بک‌اند |
| `backend/.env` | تنظیمات محلی بک‌اند |
| `backend/var/media/` | محل پیش‌فرض فایل‌های آپلودی |
| `frontend/` | محل اپ آیندهٔ Next.js یا React؛ فعلاً فقط راهنما دارد |
| `docs/` | مستندات مشترک، از جمله قرارداد API |

## راه‌اندازی بک‌اند

پیش‌نیازها: Python 3.14 یا جدیدتر، uv و PostgreSQL.

از ریشهٔ مخزن اجرا کنید:

```bash
cd backend
uv sync --frozen
```

فایل `.env` همراه بک‌اند منتقل شده است. برای نصب تازه، اگر این فایل وجود ندارد، از `.env.example` کپی بگیرید و `DATABASE_URL` را تنظیم کنید.

محیط مجازی باید در `backend/.venv` ساخته شود. اگر قبلاً محیط مجازی داشتید، با دستور بالا محیط جدید بسازید و مفسر IDE را به آن تغییر دهید.

از داخل `backend` برنامه را اجرا کنید:

```bash
uv run uvicorn main:app --app-dir src
```

معادل آن از ریشهٔ مخزن:

```bash
uv run --directory backend uvicorn main:app --app-dir src
```

برای اعمال migrationها روی دیتابیس تنظیم‌شده، از داخل `backend`:

```bash
uv run alembic upgrade head
```

یا از ریشهٔ مخزن:

```bash
uv run --directory backend alembic upgrade head
```

## مبنای مسیرهای تنظیمات

- فایل `.env` بر اساس محل `backend` خوانده می‌شود؛ تغییر پوشهٔ اجرای دستور، فایل تنظیمات دیگری را انتخاب نمی‌کند.
- مقدار نسبی `MEDIA_STORAGE_PATH` نسبت به `backend` محاسبه می‌شود. مثلاً `var/media` به `backend/var/media` اشاره می‌کند. مسیر مطلق نیز قابل استفاده است.
- در `alembic.ini`، مسیرهای `script_location` و `prepend_sys_path` نسبت به محل خود فایل تنظیمات هستند.
- مسیرهای `src` و `.venv` در `backend/pyproject.toml` نسبت به همان پوشه‌اند؛ به پیشوند دوبارهٔ `backend` نیاز ندارند.
- دستور `uv --directory backend` پوشهٔ اجرا را هم تغییر می‌دهد. `--project backend` به‌تنهایی چنین اثری ندارد.
- نسخهٔ پایتون، وابستگی‌ها، lockfile و محتوای migrationها با نسخهٔ ارسالی یکسان‌اند.

## اجرای تست‌ها و بررسی معماری

این پروژه از `unittest` استفاده می‌کند. برای تست‌ها و Import Linter، پوشهٔ `src` باید در مسیر import پایتون قرار بگیرد.

در PowerShell، از داخل `backend`:

```powershell
$env:PYTHONPATH = (Resolve-Path src).Path
uv run python -m unittest discover -s tests -v
uv run lint-imports
uv run pyright
```

در Bash، از داخل `backend`:

```bash
PYTHONPATH=src uv run python -m unittest discover -s tests -v
PYTHONPATH=src uv run lint-imports
uv run pyright
```

## تنظیم PyCharm

- مفسر پایتون: محیط `backend/.venv`؛ در ویندوز فایل `backend/.venv/Scripts/python.exe`.
- پوشهٔ `backend/src` را به‌عنوان Sources Root انتخاب کنید.
- برای اجرای برنامه، Module name را `uvicorn`، پارامترها را `main:app --app-dir src` و Working directory را پوشهٔ `backend` قرار دهید.

## منابع تنظیم مسیر

رفتار مسیرها در [مستندات uv](https://docs.astral.sh/uv/reference/cli/)، [مستندات Alembic](https://alembic.sqlalchemy.org/en/latest/tutorial.html) و [مستندات Pydantic Settings](https://docs.pydantic.dev/latest/concepts/pydantic_settings/) توضیح داده شده است.

## نتیجهٔ بررسی این جابه‌جایی

- پروژه با Python 3.14.6 و همان `uv.lock` نصب شد.
- هر ۵ تست موجود موفق بود و قرارداد Clean Architecture در Import Linter برقرار ماند.
- اجرای دستورهای مستندشده از ریشهٔ مخزن و از داخل `backend` و دریافت `openapi.json` موفق بود.
- انتخاب فایل `.env`، مسیرهای پیش‌فرض/نسبی/مطلق آپلود و اولویت متغیرهای محیطی از سه پوشهٔ اجرای متفاوت بررسی شدند.
- تولید SQL migrationها به‌صورت آفلاین از ریشه و از داخل `backend` موفق بود و خروجی‌ها یکسان بودند. migrationها روی دیتابیس واقعی اجرا نشده‌اند.
- Pyright قبل و بعد از جابه‌جایی همان ۵۴ خطای موجود را گزارش کرد؛ خطای تازه‌ای اضافه نشد. رفع آن خطاهای قبلی در این تغییر انجام نشده است.
- فایل `.env`، فایل‌های آپلودی، منطق کسب‌وکار، تست‌های موجود و migrationها بدون تغییر محتوا منتقل شدند. فایل‌های تولیدشدنی مانند `__pycache__` و محیط مجازی در ZIP قرار نگرفته‌اند.
