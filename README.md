# Couple Conflict Log ♡

> A soft, cartoon-style journal for two hearts to reflect together after conflicts.
> Record disagreements, write your own side, mark them reconciled, and grow with your partner.

---

## ✨ Features

- **Two preset accounts only** — `loverA` (Little Bear 🐻) and `loverB` (Sweet Bunny 🐰). No sign-up, no external service.
- **Dual-column reflection layout** — left panel is the Bear's side, right panel is the Bunny's. Each account can only edit **its own** panel; the partner's panel is read-only.
- **Conflict records** with date, custom tags (e.g. money, habits, family), two reflections, and two mood ratings (heart stars).
- **Mark as Reconciled** — flip the record from "still hugging out" to "made up 💗".
- **Soft, healing, cartoon-kawaii UI** — pink, lavender, and sky-blue palette with round shapes, pastel gradients, SVG cartoon avatars and floating heart decorations.
- **Fully responsive** — works beautifully on phones (single column), tablets, and desktops (two-column layout).
- **100% local storage** — everything lives in the browser's `indexedDB` on the device you're using. **No backend, no network calls, no tracking.** Privacy-first by design.
- **Wipe-all** — one click to permanently remove all local records.

---

## 🚀 Getting Started

```bash
# Install dependencies
npm install

# Start local dev server (http://localhost:5173)
npm run dev

# Build for production (outputs to ./dist)
npm run build

# Preview the production build locally
npm run preview
```

### Default accounts

| Username | Password          | Who it is           |
| -------- | ----------------- | ------------------- |
| `loverA` | `together4ever`   | Little Bear 🐻 (boy) |
| `loverB` | `myheartforyou`   | Sweet Bunny 🐰 (girl) |

> 💡 On the login screen you can also use the **Quick entry** buttons for one-tap login.

---

## 🏗 Project Structure

```
/
├── index.html                # Entry HTML
├── vite.config.js            # Vite + Vue config
├── package.json
└── src/
    ├── main.js               # App bootstrap
    ├── App.vue               # Root component (RouterView)
    ├── router/
    │   └── index.js          # Routes + auth guard
    ├── utils/
    │   ├── auth.js           # Two preset accounts, reactive login state
    │   └── storage.js        # IndexedDB CRUD for conflict records
    ├── views/
    │   ├── Login.vue         # Soft, animated login page
    │   └── Home.vue          # Dashboard, filters, stats, list of records
    ├── components/
    │   ├── Header.vue        # Top bar with user chip + logout
    │   ├── CoupleAvatar.vue  # SVG cartoon couple (bear + bunny)
    │   ├── ConflictForm.vue  # New record form with tags + dual panels
    │   ├── ConflictCard.vue  # One record (view / edit / reconcile / delete)
    │   ├── TagInput.vue      # Press Enter to add a tag, Backspace to remove
    │   └── MoodStars.vue     # 1-5 heart rating, read-only or interactive
    └── styles/
        └── global.css        # Theme variables, buttons, typography
```

---

## 🛡 Privacy & Data

- **No server.** No network calls are made by the app.
- **IndexedDB only.** Your conflict records are stored in the browser's `indexedDB` under the store name `conflicts` in the `CoupleConflictLog` database.
- **Shared-device note.** Because this is a local web app, if two people use the same browser on the same device, they will see each other's records. For full separation, use two different devices / browsers / private windows, or bookmark the app on each person's own phone.
- **Wipe** — use the "Erase all local data" button at the bottom of the home page to delete everything at once.

---

## 🎨 Design notes (how the cartoon theme was built)

- Palette derived from warm pinks, lavender, soft blues, cream, and cocoa text — designed to feel healing rather than clinical.
- The couple avatars in [CoupleAvatar.vue](src/components/CoupleAvatar.vue) are **inline SVG**, matching the cute, soft character style:
  - **Bear (loverA)** — dark fluffy hair with bangs, round cheeks, small nose, gentle smile, blue shirt with a tiny heart pocket.
  - **Bunny (loverB)** — long wavy dark hair, larger kawaii eyes with multiple highlights, pinker cheeks, cream shirt, little heart necklace.
- Animated floating hearts (`♡ ✿ ☆`) behind the login hero for a playful feel.
- Pill-shaped buttons, rounded cards, and subtle drop shadows give a "soft sticker" aesthetic.

---

## 🧭 User-flow at a glance

1. Open the app → login screen.
2. Tap **Little Bear** / **Sweet Bunny** (or type credentials).
3. Home screen shows the cute couple avatar, stats (total memories / open / reconciled), and the list of past conflicts.
4. Tap **+ New Conflict Log** → pick a date, add tags, write *only* your side, and rate your mood. Your partner's panel is disabled on your account.
5. Save → your record shows up in the list. Your partner, when logged in as their account, can then write their side.
6. Either of you can tap **Mark as Reconciled** once you've made up.
7. Delete individual records, or erase everything, anytime.

---

## 📦 Tech Stack

- Vue 3 (`<script setup>` composition API)
- Vue Router 4 (with a simple auth guard)
- Vite 5 (dev server + build)
- Native **IndexedDB** (no external DB, no ORM dependency)
- Pure CSS, no UI library — keeping the kawaii look lightweight and consistent.

---

May every conflict end with a hug. ♡
