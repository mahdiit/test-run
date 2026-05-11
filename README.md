<p align="center">
  <img src="https://img.shields.io/badge/MRH-G2Ray-0057B3?style=for-the-badge&logo=github&logoColor=white"/>
  <img src="https://img.shields.io/badge/Version-1.0.0--MRH-00C853?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-FFC107?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Platform-GitHub%20Codespaces-181717?style=for-the-badge&logo=github"/>
</p>

<p align="center">
  <a href="#-english-guide">📖 English Guide</a> •
  <a href="#-راهنمای-فارسی">📖 راهنمای فارسی</a>
</p>

---

## 💝 حمایت / Support

اگر این ابزار به شما کمک کرد / If this tool helped you:

**BNB (BEP-20) - Ethereum - Arbitrum - Base:**
`0x3A90B058E51deeA95dd8912b4bA71c4b159Ec582`

**USDT / USDC / DAI (BEP-20 / ERC-20 / Polygon):**
`0x3A90B058E51deeA95dd8912b4bA71c4b159Ec582`

> حمایت مالی کاملاً اختیاری است / Support is optional

---

<h2 align="left">🇬🇧 <a id="-english-guide"></a>English Guide</h2>

<div dir="ltr">

### 🚀 What is this project?

**MRH-G2Ray** is a wrapper around the `g2ray` project that leverages **GitHub Codespaces** to run a VLESS proxy on GitHub's cloud infrastructure.

- All processing and traffic pass through **GitHub servers**.
- No need for a personal VPS or domain.
- Not restricted by geographical limitations or sanctions (provided initial access to GitHub exists).

---

### 📝 Step-by-Step Guide (For Beginners)

#### Step 1: Create a GitHub Account
1. Go to [GitHub.com](https://github.com)
2. Click **Sign up**
3. Choose email, password, and username
4. Enter the verification code

> ⚠️ **Security Recommendation:** Use a secondary (burner) GitHub account to protect your main account.

#### Step 2: Fork This Repository
1. Click **Fork** at the top of this page
2. Choose a name (e.g., `My-Proxy`)
3. Click **Create fork**

#### Step 3: Set Up a Codespace
1. In your forked repo, click the green **Code** button
2. Select **Codespaces** tab → **Create codespace on main**
3. Wait a few minutes

#### Step 4: Get Your VLESS Link
- Open Admin GUI in browser:
  - `https://<YOUR-CODESPACE-NAME>-8080.app.github.dev`
- Login is protected by HTTP Basic Auth:
  - Username: `admin`
  - Password: `Sample@Sample`
- For safety, change these defaults by setting environment variables `MRH_ADMIN_USER` and `MRH_ADMIN_PASS`.
- Copy your generated `vless://` link from the panel
- UUID is generated automatically per Codespace and shown in the GUI

#### Step 5: Connect
Paste the link into one of these:
- **V2rayNG** (Android)
- **Hiddify** (Android, Windows, Mac)
- **Streisand** (Windows, Mac)
- **Nekobox** (Windows)

> If you cannot access the GUI URL directly, make sure port `8080` is available in Codespaces (recommended: **Private**).

---

### ⏰ Managing Quotas (Technical)

Free GitHub accounts receive **60 hours per month** on the default 2-core machine. **1-core machines are NOT available.**

#### How to Avoid Wasting Quota (Hours & Storage):

| Action | Effect on Hours | Effect on Storage |
| :--- | :---: | :---: |
| **Stop** | ✅ Stops | ❌ Still consumed |
| **Delete** | ✅ Stops | ✅ Stops |

- **Stop:** Halts the machine. Your files remain on GitHub's disk, consuming your 15 GB storage quota.
- **Delete:** Completely removes the cloud environment, freeing both compute hours and storage space.

> ✅ **Best Practice:** Delete your Codespace after each session and recreate it next time.

---

### 🛠️ Pro Section (Advanced Users)

#### Change Minimum Machine Requirements (If Needed):
Edit `.devcontainer/devcontainer.json` and add:
```json
"hostRequirements": {
   "cpus": 4,
   "memory": "8gb",
   "storage": "64gb"
}
```
> Note: More powerful machines have lower free quotas (e.g., 4-core = 30 hours/month).

#### Sync with Upstream (Get Updates):
Click **Sync fork** on your forked repository's page.

---

### ⚠️ Limitations

| Item | Value |
| :--- | :---: |
| Free monthly hours (2-core) | 60 hours |
| Free storage | 15 GB |
| Minimum available machine | 2 cores |

---

<p align="center">
  <b>MRH-G2Ray</b><br/>
  <sub>Version 1.0.0</sub>
</p>

</div>

---

<h2 dir="rtl" align="right">🇮🇷 <a id="-راهنمای-فارسی"></a>راهنمای فارسی</h2>

<div dir="rtl">

### 🚀 این پروژه چیست؟

**MRH-G2Ray** پوسته‌ای (Wrapper) بر روی پروژه `g2ray` است که با استفاده از **زیرساخت ابری GitHub Codespaces**، یک Proxy مبتنی بر پروتکل VLESS را در محیط ابری گیت‌هاب راه‌اندازی می‌کند.

- تمام پردازش‌ها و ترافیک از طریق **سرورهای گیت‌هاب** عبور می‌کند.
- نیازی به تهیه سرور یا دامنه شخصی نیست.
- اجرای آن محدود به مناطق جغرافیایی خاص یا تحریم‌ها نمی‌شود (به شرط دسترسی اولیه به گیت‌هاب).

---

### 📝 راهنمای گام به گام (برای مبتدیان)

#### مرحله ۱: ساخت اکانت گیت‌هاب
1. به [GitHub.com](https://github.com) بروید
2. روی **Sign up** کلیک کنید
3. ایمیل، رمز عبور و نام کاربری انتخاب کنید
4. کد تأیید ارسال‌شده را وارد کنید

> ⚠️ **توصیه امنیتی:** از یک اکانت دوم (فرعی) استفاده کنید.

#### مرحله ۲: فورک (کپی) کردن این مخزن
1. روی دکمه **Fork** در بالای صفحه کلیک کنید
2. نام دلخواه (مثلاً `My-Proxy`) انتخاب کنید
3. **Create fork** را بزنید

#### مرحله ۳: راه‌اندازی Codespace
1. در مخزن فورک‌شده، دکمه سبز **Code** را بزنید
2. برگه **Codespaces** → **Create codespace on main**
3. چند دقیقه صبر کنید

#### مرحله ۴: دریافت لینک VLESS
- پنل گرافیکی را در مرورگر باز کنید:
  - `https://<YOUR-CODESPACE-NAME>-8080.app.github.dev`
- ورود پنل با احراز هویت Basic محافظت شده است:
  - نام کاربری: `admin`
  - رمز عبور: `Sample@Sample`
- برای امنیت بیشتر، این مقادیر پیش‌فرض را با تنظیم متغیرهای محیطی `MRH_ADMIN_USER` و `MRH_ADMIN_PASS` تغییر دهید.
- لینک `vless://` تولیدشده را از پنل کپی کنید
- مقدار UUID به‌صورت خودکار برای هر Codespace ساخته می‌شود و داخل پنل نمایش داده می‌شود

#### مرحله ۵: اتصال
لینک را در یکی از نرم‌افزارهای زیر وارد کنید:
- **V2rayNG** (اندروید)
- **Hiddify** (اندروید، ویندوز، مک)
- **Streisand** (ویندوز، مک)
- **Nekobox** (ویندوز)

> اگر پنل گرافیکی باز نشد، در Codespaces بررسی کنید پورت `8080` در دسترس باشد (پیشنهاد: حالت **Private**).

---

### ⏰ مدیریت ساعات و حجم (بخش فنی)

GitHub Codespaces برای حساب‌های رایگان، **ماهیانه ۶۰ ساعت** (با ماشین ۲ هسته‌ای) ارائه می‌دهد. **امکان دریافت ماشین ۱ هسته وجود ندارد.**

#### نحوه جلوگیری از هدررفت سهمیه (ساعت و فضا):

| عملیات | تأثیر بر ساعت | تأثیر بر فضای ذخیره‌سازی |
| :--- | :---: | :---: |
| **Stop** (متوقف کردن) | ✅ متوقف می‌شود | ❌ همچنان مصرف می‌شود |
| **Delete** (حذف کامل) | ✅ متوقف می‌شود | ✅ متوقف می‌شود |

- **Stop** فقط اجرای ماشین را متوقف می‌کند، اما فایل‌های شما روی دیسک گیت‌هاب باقی می‌مانند و از سهمیه ۱۵ گیگابایت شما کم می‌شوند.
- **Delete** کل محیط را حذف می‌کند و هم ساعت و هم فضا را آزاد می‌سازد.

> ✅ **نکته:** برای استفاده بهینه، پس از هر بار کار، Codespace را **Delete** کنید و دفعه بعد دوباره بسازید.

---

### 🛠️ بخش تخصصی (برای کاربران حرفه‌ای)

#### تغییر حداقل منابع (در صورت نیاز):
در فایل `.devcontainer/devcontainer.json` می‌توانید حداقل نیازمندی را افزایش دهید:
```json
"hostRequirements": {
   "cpus": 4,
   "memory": "8gb",
   "storage": "64gb"
}
```
> توجه: ماشین‌های قوی‌تر سهمیه ماهانه کمتری دارند (مثلاً ماشین ۴ هسته = ۳۰ ساعت).

#### همگام‌سازی با پروژه اصلی (دریافت آپدیت):
در صفحه فورک خود، دکمه **Sync fork** را بزنید.

---

### ⚠️ محدودیت‌ها

| مورد | مقدار |
| :--- | :---: |
| ساعات رایگان ماهانه (ماشین ۲ هسته) | ۶۰ ساعت |
| فضای ذخیره‌سازی رایگان | ۱۵ گیگابایت |
| حداقل ماشین در دسترس | ۲ هسته |

---

<p align="center">
  <b>MRH-G2Ray</b><br/>
  <sub>نسخه ۱.۰.۰</sub>
</p>

</div>
