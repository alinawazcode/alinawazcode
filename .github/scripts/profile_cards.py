#!/usr/bin/env python3
"""Generate assets/stats.svg and assets/langs.svg from the GitHub GraphQL API.

Stdlib only. Needs GITHUB_TOKEN and GITHUB_USER in the environment.
Counts public, non-fork repositories; private activity is shown only as
"contributions" (the GraphQL contributions calendar includes it when the
account setting allows).
Use `--demo` to render with sample data (no network) for design checks.
"""
import json, os, sys, urllib.request
from html import escape

BG, CARD, LINE = "#0b0f1a", "#0f1527", "#26304f"
RED, IND, SAND, TEAL = "#e03e52", "#5c7cfa", "#f2d7a3", "#38d9a9"
TXT, MUT = "#e8ecf7", "#8b95b3"
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,'DejaVu Sans Mono',monospace"
SANS = "'Segoe UI',-apple-system,Helvetica,Arial,'DejaVu Sans',sans-serif"
FALLBACK = [RED, IND, TEAL, SAND, "#c084fc", "#fb923c", "#22d3ee", "#a3e635"]

QUERY = """
query($login:String!){ user(login:$login){
  followers{totalCount}
  pullRequests{totalCount}
  issues{totalCount}
  contributionsCollection{totalCommitContributions restrictedContributionsCount
    totalPullRequestReviewContributions}
  repositories(ownerAffiliations:OWNER,privacy:PUBLIC,isFork:false,first:100){
    totalCount
    nodes{ stargazerCount forkCount
      languages(first:10,orderBy:{field:SIZE,direction:DESC}){
        edges{ size node{ name color } } } } } } }
"""

def fetch(login, token):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": {"login": login}}).encode(),
        headers={"Authorization": f"bearer {token}", "User-Agent": "profile-cards"})
    with urllib.request.urlopen(req, timeout=30) as r:
        data = json.load(r)
    if "errors" in data:
        raise SystemExit(f"GraphQL error: {data['errors']}")
    return data["data"]["user"]

def summarize(u):
    repos = u["repositories"]["nodes"]
    langs = {}
    for r in repos:
        for e in r["languages"]["edges"]:
            n = e["node"]["name"]
            cur = langs.setdefault(n, [0, e["node"]["color"]])
            cur[0] += e["size"]
    cc = u["contributionsCollection"]
    return {
        "stars": sum(r["stargazerCount"] for r in repos),
        "forks": sum(r["forkCount"] for r in repos),
        "repos": u["repositories"]["totalCount"],
        "followers": u["followers"]["totalCount"],
        "prs": u["pullRequests"]["totalCount"],
        "issues": u["issues"]["totalCount"],
        "commits": cc["totalCommitContributions"] + cc["restrictedContributionsCount"],
        "langs": sorted(langs.items(), key=lambda kv: -kv[1][0]),
    }

def stats_svg(s):
    items = [("Stars earned", s["stars"], SAND), ("Commits (last year)", s["commits"], RED),
             ("Pull requests", s["prs"], IND), ("Issues", s["issues"], TEAL),
             ("Public repos", s["repos"], SAND), ("Followers", s["followers"], RED)]
    cells = ""
    for i, (label, val, col) in enumerate(items):
        x = 28 + (i % 2) * 210; y = 74 + (i // 2) * 50
        cells += (f'<circle cx="{x+5}" cy="{y-5}" r="4" fill="{col}"/>'
                  f'<text x="{x+18}" y="{y}" font-family="{MONO}" font-size="12.5" fill="{MUT}">{escape(label)}</text>'
                  f'<text x="{x+18}" y="{y+22}" font-family="{SANS}" font-size="22" font-weight="800" fill="{TXT}">{val:,}</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="450" height="230" viewBox="0 0 450 230" role="img" aria-label="GitHub stats: {s['stars']} stars, {s['commits']} commits, {s['prs']} pull requests, {s['repos']} public repositories">
  <rect x="1" y="1" width="448" height="228" rx="14" fill="{BG}" stroke="{LINE}"/>
  <path d="M30 22 L40 32 L30 42 L20 32 Z" fill="none" stroke="{RED}" stroke-width="2"/>
  <text x="52" y="38" font-family="{SANS}" font-size="18" font-weight="800" fill="{SAND}">GitHub stats</text>
  <text x="426" y="38" text-anchor="end" font-family="{MONO}" font-size="11" fill="{MUT}">public repos</text>
  {cells}
</svg>
'''

def langs_svg(s):
    langs = s["langs"][:6]
    total = sum(v[0] for _, v in langs) or 1
    bar = ""; x = 28; W = 394
    for i, (name, (size, color)) in enumerate(langs):
        w = max(4, W * size / total)
        col = color or FALLBACK[i % len(FALLBACK)]
        bar += f'<rect x="{x:.1f}" y="62" width="{w:.1f}" height="12" fill="{col}"/>'
        x += w
    legend = ""
    for i, (name, (size, color)) in enumerate(langs):
        col = color or FALLBACK[i % len(FALLBACK)]
        lx = 28 + (i % 2) * 210; ly = 112 + (i // 2) * 30
        legend += (f'<circle cx="{lx+5}" cy="{ly-4}" r="5" fill="{col}"/>'
                   f'<text x="{lx+18}" y="{ly}" font-family="{MONO}" font-size="13" fill="{TXT}">{escape(name)}</text>'
                   f'<text x="{lx+190}" y="{ly}" text-anchor="end" font-family="{MONO}" font-size="12" fill="{MUT}">{100*size/total:.1f}%</text>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="450" height="230" viewBox="0 0 450 230" role="img" aria-label="Most used languages: {', '.join(n for n,_ in langs)}">
  <defs><clipPath id="c"><rect x="28" y="62" width="394" height="12" rx="6"/></clipPath></defs>
  <rect x="1" y="1" width="448" height="228" rx="14" fill="{BG}" stroke="{LINE}"/>
  <path d="M30 22 L40 32 L30 42 L20 32 Z" fill="none" stroke="{IND}" stroke-width="2"/>
  <text x="52" y="38" font-family="{SANS}" font-size="18" font-weight="800" fill="{SAND}">Most used languages</text>
  <g clip-path="url(#c)">{bar}</g>
  {legend}
</svg>
'''

def main():
    out = os.path.join(os.path.dirname(__file__), "..", "..", "assets")
    if "--demo" in sys.argv:
        s = {"stars": 41, "forks": 3, "repos": 12, "followers": 18, "prs": 27, "issues": 9, "commits": 478,
             "langs": [("Python", [90000, "#3572A5"]), ("Jupyter Notebook", [40000, "#DA5B0B"]),
                       ("JavaScript", [15000, "#f1e05a"]), ("HTML", [9000, "#e34c26"]),
                       ("CSS", [6000, "#563d7c"]), ("Java", [3000, "#b07219"])]}
        out = sys.argv[sys.argv.index("--demo") + 1] if len(sys.argv) > 2 else out
    else:
        s = summarize(fetch(os.environ["GITHUB_USER"], os.environ["GITHUB_TOKEN"]))
    open(os.path.join(out, "stats.svg"), "w", encoding="utf-8").write(stats_svg(s))
    open(os.path.join(out, "langs.svg"), "w", encoding="utf-8").write(langs_svg(s))
    print("wrote", os.path.join(out, "stats.svg"), os.path.join(out, "langs.svg"))

if __name__ == "__main__":
    main()
