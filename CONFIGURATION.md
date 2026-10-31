# Configuration & Setup Guide

This repository is a **GitHub Profile README** for [@alinawazcode](https://github.com/alinawazcode).
Follow the steps below to install it. Total setup time: ~5 minutes.

---

## 1. Repository Layout

```
alinawazcode/                     ← your profile repo (alinawazcode/alinawazcode)
├── README.md                     ← the profile README
├── CONFIGURATION.md              ← this file
├── assets/
│   ├── banner.svg                ← hero banner (dark, animated accent line)
│   └── divider.svg               ← section divider
└── .github/
    └── workflows/
        ├── snake.yml             ← generates the contribution snake (every 12 h)
        └── recent-activity.yml   ← updates the Recent Activity section (every 6 h)
```

The snake workflow publishes generated SVGs to a separate **`output` branch**,
which is created automatically on the first run — you do not need to create it.

---

## 2. Installation

1. Extract this ZIP **into the root** of your `alinawazcode/alinawazcode` profile repository.
2. Commit and push:

   ```bash
   git add -A
   git commit -m "Set up animated profile README"
   git push origin main
   ```

3. Enable the workflows (next section).

---

## 3. Enabling GitHub Actions

Both workflows use only the built-in `GITHUB_TOKEN` — **no personal access
tokens or extra secrets are required**.

### Required repository settings

Go to **Settings → Actions → General**:

1. Under **Actions permissions**, choose **"Allow all actions and reusable workflows"**
   (or at minimum allow actions from GitHub and verified creators — `Platane/snk`
   and `jamesgeorge007/github-activity-readme` are both widely used and verified).
2. Under **Workflow permissions**, select **"Read and write permissions"**.
   This is required so the workflows can commit the updated README and push the
   snake SVGs to the `output` branch. The workflows themselves only request
   `contents: write` — nothing broader.

### First run

The snake animation is not visible until its first run:

1. Go to the **Actions** tab.
2. Select **"Generate Contribution Snake"** → **"Run workflow"** → Run on `main`.
3. Wait ~1 minute. The workflow creates the `output` branch with two SVGs:
   - `github-contribution-grid-snake.svg` (light)
   - `github-contribution-grid-snake-dark.svg` (dark)

The README's `<picture>` element automatically serves the right one based on the
viewer's GitHub theme.

You can also manually trigger **"Update Recent Activity"** the same way; it will
fill the section between the `<!--START_SECTION:activity-->` markers.

---

## 4. What Each Feature Depends On

| Feature | Type | Dependency |
|---|---|---|
| Hero banner, dividers | Local SVG assets | None — fully self-hosted in `assets/` |
| Typing headline | External service | `readme-typing-svg.demolab.com` (Demolab) |
| Social & tech badges | External service | `shields.io` |
| Profile views counter | External service | `komarev.com/ghpvc` |
| Project cards, stats, languages | External service | `github-readme-stats.vercel.app` |
| Streak stats | External service | `streak-stats.demolab.com` |
| Contribution snake | GitHub Actions | `snake.yml` → pushes to `output` branch |
| Recent activity | GitHub Actions | `recent-activity.yml` → commits to README |

---

## 5. Optional: Hardening the Stats Cards

The public `github-readme-stats.vercel.app` instance is best-effort and can be
rate-limited at traffic spikes. If a card ever shows an error, you have two
options (both documented in the project's README):

1. **Self-host on Vercel** — fork `anuraghazra/github-readme-stats`, deploy to
   Vercel with a read-only PAT, and replace the base URL in `README.md`.
2. **GitHub Actions generation** — use `readme-tools/github-readme-stats-action`
   to bake static SVGs into this repo on a schedule (no external requests).

Everything else (badges, typing SVG, streak, counter) is served by stable
community instances.

---

## 6. Maintenance Notes

- **Scheduled runs are skipped after 60 days of repo inactivity** (GitHub policy).
  Since the activity workflow itself commits changes, the repo stays active on
  its own as long as you have public GitHub activity.
- To change the typing headline, edit the `lines=` parameter in `README.md`
  (separate lines with `;`, URL-encode spaces as `+`).
- To change featured projects, swap the `repo=` parameters in the pin-card URLs.
- The snake and activity schedules can be adjusted via the `cron:` lines in each
  workflow file.
