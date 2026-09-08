# تحلیل و راهنمای معماری FSD

## نتیجهٔ بررسی

جهت کلی ساختار اولیه درست بود: استان و دسته‌بندی شغلی اطلاعات دامنه‌اند و جستجوی شغل یک قابلیت کاربر است. مشکل بیشتر در مرز لایه‌ها، قرارداد کامپوننت‌ها و محل زیرساخت مشترک بود. برای اندازهٔ فعلی پروژه، جداسازی مسئولیت‌ها و importهای قابل کنترل از ساخت پوشه‌های خالی یا abstraction اضافی ارزشمندتر است.

نبودن پوشهٔ FSD Pages به‌خودی‌خود نقص عملکردی Next.js نیست؛ `app/page.tsx` همان route صفحهٔ اصلی است. در این بازآرایی، ترکیب UI صفحه از adapter مسیریابی جدا شده تا با رشد پروژه مسئولیت‌ها مخلوط نشوند.

| مورد اولیه | ارزیابی | محل فعلی |
| --- | --- | --- |
| `features/shared` | Shared یک لایهٔ مستقل است؛ Entity نباید برای HTTP یا UI پایه به Features وابسته شود. | `src/shared` |
| `features/widgets/typography.tsx` | Typography ابزار نمایشی عمومی است و مفهوم کسب‌وکار ندارد. | `src/shared/ui/typography` |
| هدر داخل Shared | هدر ساختار سطح سایت را می‌سازد و محل مناسبی برای ترکیب قابلیت‌های سایت است. | `src/widgets/site-header` |
| `features/job-search` | جستجوی شغل یک قصد کاربر است؛ جایگذاری کلی درست بود. | همان slice زیر `src/features` با `model` و `ui` |
| `entities/location` | استان جزئی از مفهوم موقعیت مکانی است؛ نگه‌داشتن آن در Location مناسب است. | `src/entities/location` |
| `entities/job-categories` | دسته‌بندی شغلی Entity مناسبی است؛ نام slice برای هماهنگی مفرد شد. | `src/entities/job-category` |
| `service` | درخواست HTTP بهتر است در segment متداول `api` باشد. کلاس برای این دو سرویس بدون state ضروری نبود. | `api` با factory قابل تزریق |
| queryهای inline فرم | کلید و سیاست cache در مصرف‌کننده تعریف می‌شد و احتمال تکرار داشت. | query options در Entity مربوطه |
| کد صفحه در `app/page.tsx` | مسیریابی و ترکیب صفحه مخلوط بود. | re-export از `_pages/home` |
| `app/providers.tsx` | Provider مسئولیت سطح برنامه است. | `src/_app/providers` |

## نقشهٔ ساختار

| مسیر | مسئولیت |
| --- | --- |
| `app/layout.tsx` | اتصال Root Layout، فونت، metadata، Provider و هدر به Next.js |
| `app/page.tsx` | adapter مسیر `/` |
| `app/jobs/search/page.tsx` | adapter مسیر `/jobs/search` |
| `src/_app/providers` | QueryClient و Provider سراسری |
| `src/_app/styles` | استایل و tokenهای سراسری |
| `src/_pages/home` | ترکیب صفحهٔ اصلی |
| `src/_pages/job-search` | خواندن searchParams و ساخت صفحهٔ مقصد جستجو |
| `src/widgets/site-header` | هدر سایت |
| `src/features/job-search/model` | قرارداد فیلترهای جستجو و تبدیل آن‌ها به/از URL |
| `src/features/job-search/ui` | فرم، state ورودی‌ها و وضعیت درخواست‌ها |
| `src/entities/location` | نوع Province، API استان‌ها، query options و ProvinceSelect |
| `src/entities/job-category` | نوع JobCategory، API، query options و JobCategorySelect |
| `src/shared/api` | Axios instance، timeout و تنظیم عمومی درخواست‌ها |
| `src/shared/ui` | Button، Select، Typography و آیکون‌ها |
| `tooling` | قاعدهٔ محلی ESLint برای مرزهای FSD |
| `tests` | تست URL و قواعد وابستگی |

نام‌های `_app` و `_pages` همان لایه‌های App و Pages در FSD هستند. پیشوند برای جلوگیری از تداخل با نام‌های رزروشدهٔ Next.js انتخاب شده، مطابق [راهنمای FSD برای Next.js](https://feature-sliced.design/docs/guides/tech/with-nextjs). پروژه همچنان از App Router استفاده می‌کند؛ Pages Router اضافه نشده است.

## قاعدهٔ وابستگی

ترتیب لایه‌ها از بالا به پایین: `_app`، `_pages`، `widgets`، `features`، `entities`، `shared`. یک slice از لایه‌های پایین‌تر استفاده می‌کند؛ sliceهای هم‌لایه یکدیگر را import نمی‌کنند. برای مثال، Entity نمی‌تواند Feature را بشناسد و یک Feature نباید Feature دیگری را مستقیماً import کند. ترکیب آن‌ها در Page یا Widget انجام می‌شود. App و Shared به segment تقسیم می‌شوند و محدودیت sliceهای هم‌لایه برای آن‌ها صدق نمی‌کند. [مرجع لایه‌های FSD](https://feature-sliced.design/docs/reference/layers)

بیرون هر slice، از Public API آن (`index.ts`) استفاده کنید. داخل همان slice import نسبی مناسب است:

```tsx
// از بیرون slice
import { ProvinceSelect, provinceQueries } from "@/entities/location";
import { Select } from "@/shared/ui/select";

// داخل entities/location/api/province-api.ts
import type { Province } from "../model/types";
```

برای Shared یک barrel عظیم ساخته نشده است؛ `shared/api` و هر گروه UI ورودی مشخص خودشان را دارند. قواعد در `tooling/eslint-fsd.mjs` به ESLint متصل‌اند و import خلاف جهت، import بین sliceهای هم‌لایه و دسترسی مصرف‌کننده به فایل داخلی را بررسی می‌کنند. این قاعده برای ساختار همین پروژه نوشته شده است؛ اگر مسیرهای alias یا ساختار Public API عوض شدند، policy و تستش را هم هماهنگ کنید.

## React Query و API

React Query و Devtools حفظ شده‌اند. QueryClient در مرورگر پایدار است و در اجرای سرور cache سراسری مشترک بین درخواست‌ها ساخته نمی‌شود. Provider داخل body قرار دارد و فرزندان Server Component را به‌صورت children می‌گیرد. Client Component بودن Provider به‌معنای تبدیل تمام فرزندان سروری به Client Component نیست. این الگو با [راهنمای TanStack برای App Router](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr) و [مرزهای Server/Client در Next.js](https://nextjs.org/docs/app/getting-started/server-and-client-components) سازگار است.

جریان داده: فرم ← `useQuery` ← query options موجودیت ← API موجودیت ← HTTP client مشترک ← بک‌اند. تعریف queryKey و queryFn کنار API باعث می‌شود مصرف‌کننده‌های بعدی همان cache و قرارداد را به اشتراک بگذارند.

- `provinceQueries.all()` و `jobCategoryQueries.all()` ورودی مستقیم `useQuery` هستند.
- `staleTime` داده‌های مرجع پنج دقیقه و مقدار پیش‌فرض یک دقیقه است. این اعداد سیاست cache هستند و می‌توانید متناسب با تغییرپذیری داده عوضشان کنید.
- خطا یک بار به‌صورت خودکار retry می‌شود؛ فرم تلاش مجدد دستی هم دارد.
- AbortSignal از React Query به Axios منتقل می‌شود تا لغو query به درخواست HTTP برسد.
- فقط لایهٔ HTTP مشترک Axios را پیکربندی می‌کند. URL موجودیت‌ها در خودشان می‌ماند.
- پاسخ Axios با generic تایپ شده و `data` برگردانده می‌شود. این تایپ به‌معنای validation پاسخ JSON در زمان اجرا نیست.
- factoryهای `createProvinceApi(client)` و `createJobCategoryApi(client)` امکان تزریق HTTP client را نگه می‌دارند؛ برای این دو درخواستِ بدون state، کلاس و container سراسری لازم نیست.
- `Content-Type: application/json` عمومی از GETهای بدون body برداشته شده؛ `Accept` باقی است. Axios برای payloadهای JSON رفتار معمول خودش را دارد.

در این نسخه دریافت این دو فهرست با `useQuery` در مرورگر انجام می‌شود. markup اولیهٔ فرم و وضعیت pending می‌توانند روی سرور رندر شوند. برای دو فهرستِ انتخابی، prefetch سرور الزام معماری نیست؛ بنابراین build به در دسترس بودن بک‌اند وابسته نشده است. `isClient`، حذف SSR یا خاموش‌کردن هشدار hydration اضافه نشده‌اند.

اگر بعداً برای صفحه‌ای دادهٔ اولیهٔ سرور لازم شد، همان query options را با QueryClient مستقل در سرور prefetch کنید و با `dehydrate` و `HydrationBoundary` به فرم بدهید. queryKey جدید و موازی نسازید. توابع `server-only` را در Public API سروری جداگانه مثل `index.server.ts` نگه دارید تا وارد گراف کلاینت نشوند. [راهنمای TanStack](https://tanstack.com/query/latest/docs/framework/react/guides/advanced-ssr)

## فرم و کامپوننت‌ها

ProvinceSelect و JobCategorySelect صرفاً داده، value و callback می‌گیرند. به `Dispatch<SetStateAction<...>>` یا نحوهٔ نگهداری state در والد وابسته نیستند. اگر یک فرم دیگر به استان احتیاج داشته باشد، همین Entity را مصرف می‌کند؛ نیازی به import کردن قابلیت جستجوی شغل ندارد.

`value` و `defaultValue` هم‌زمان حذف شده‌اند. گزینهٔ خالی اکنون انتخاب‌پذیر است تا فیلتر پاک شود. اگر شناسه از URL آمده اما داده هنوز نرسیده باشد، یک گزینهٔ موقت مقدار انتخاب‌شده را نگه می‌دارد. این گزینه صحت شناسه را تأیید نمی‌کند؛ validation فیلترهای نتایج با قرارداد بک‌اند تکمیل می‌شود.

`className` نام استاندارد prop است. Select برای حذف border دارای `variant="plain"` است و لازم نیست با کلاس‌های متعارض border کار کنید. `classnames` فقط کلاس‌ها را ترکیب می‌کند و تعارض utilityهای Tailwind را resolve نمی‌کند؛ افزودن یک className تضمین نمی‌کند همهٔ کلاس‌های قبلی را override کند.

فرم با Enter هم submit می‌شود، label قابل دسترس دارد و URL را با URLSearchParams می‌سازد. متن فارسی، علامت `&`، `+` و `#` دیگر query را خراب نمی‌کنند. فیلترهای خالی حذف می‌شوند. نام پارامترهای موجود (`keywords`، `province_id`، `job_category_id`) حفظ شده‌اند؛ قرارداد endpoint نتایج از روی این نام‌ها حدس زده نشده است.

صفحهٔ مقصد searchParams را در سرور می‌خواند و مقدار اولیه می‌دهد. key وابسته به فیلترها باعث می‌شود هنگام تغییر URL، state قدیمی فرم روی مقادیر جدید نماند. دو عنوان ظاهری صفحهٔ اصلی در یک h1 واقعی قرار گرفته‌اند و span به‌جای تحمیل اندازهٔ ۱۴ پیکسل اندازهٔ والد را به ارث می‌برد.

## توسعهٔ بعدی

برای آگهی‌ها، وقتی قرارداد واقعی API موجود شد، نوع Job و درخواست‌ها/queryهای مربوط را در `entities/job` قرار دهید. صفحهٔ `src/_pages/job-search` مسئول ترکیب نتایج و فرم خواهد بود. فقط اگر بلوک فهرست در چند صفحه کاربرد دارد یا خودش بلوکی مستقل و مهم است، Widget جدا برای آن بسازید؛ هر section صفحه لزوماً Widget نیست.

ارسال درخواست استخدام یا ذخیرهٔ آگهی می‌تواند Feature باشد؛ نام Province یا متد getAll به‌تنهایی Feature نیست. کامپوننت‌های ساده‌ای که هیچ مفهوم کسب‌وکار ندارند در Shared می‌مانند. برای هر slice فقط segmentهایی را بسازید که واقعاً محتوا دارند.

**محدودهٔ تحویل:** ساختار و قابلیت‌های موجود بازآرایی شده‌اند و مقصد جستجو یک صفحهٔ مقدماتی دارد. endpoint نتایج، فهرست واقعی آگهی‌ها، احراز هویت و منوی تعاملی در ورودی وجود نداشتند و در این بازآرایی اختراع نشده‌اند.
