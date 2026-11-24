"""info-card.svg: neofetch-style card, refreshed daily with live stats + language bar."""
import os
from datetime import datetime, timezone

from common import BORDER, CYAN, FG, GREEN, MUTED, ORANGE, PINK, PURPLE, esc, load, window, write_svg
from config import HIDE_LANGS, INFO_ROWS, PROMPT_HOST, PROMPT_USER

W, H = 490, 420
STATIC = os.environ.get("STATIC") == "1"

# Language colors matching GitHub linguist, with Spring green / Java orange
LANG_COLORS = {
    "Java": "#b07219",
    "TypeScript": "#3178c6",
    "C++": "#f34b7d",
    "SQL": "#e38c00",
    "JavaScript": "#f1e05a",
    "HTML": "#e34c26",
    "CSS": "#663399",
    "Python": "#3572A5",
    "Docker": "#384d54",
    "Shell": "#89e051",
}
KEY_COLORS = [GREEN, CYAN, PURPLE, ORANGE, PINK]


def plural(n, unit):
    return f"{n} {unit}" if n == 1 else f"{n} {unit}s"


def uptime(created):
    c = datetime.fromisoformat(created.replace("Z", "+00:00"))
    months = (datetime.now(timezone.utc) - c).days * 12 // 365
    y, m = divmod(months, 12)
    parts = ([plural(y, "yr")] if y else []) + ([plural(m, "mo")] if m or not y else [])
    return ", ".join(parts)


def main():
    st = load("contributions.json", {}).get("stats", {})
    prof = load("profile.json", {})
    langs = {k: v for k, v in prof.get("languages", {}).items() if k not in HIDE_LANGS}
    total_bytes = sum(langs.values()) or 1

    fill = {
        "uptime": uptime(prof["created_at"]) if prof.get("created_at") else "2 yrs on GitHub",
        "top_langs": "Java · TypeScript · C++",
        "public_repos": prof.get("public_repos", 23),
        "stars": prof.get("stars", 2),
        "total": f"{st.get('total', 847):,}",
        "current_streak": st.get("current_streak", 0),
        "longest_streak": st.get("longest_streak", 0),
        "fineract_prs": prof.get("fineract_prs", 4),
        "mifos_prs": prof.get("mifos_prs", 2),
    }

    def anim(k):
        return "" if STATIC else f' class="ln" style="animation-delay:{0.5 + k * 0.09:.2f}s"'

    x, y = 24, 60

    # Calculate exact monospace text positioning for user@host to avoid any font overlap
    char_w = 9.1
    x_at = x + len(PROMPT_USER) * char_w
    x_host = x_at + char_w
    dashes = "-" * (len(PROMPT_USER) + 1 + len(PROMPT_HOST))

    lines = [
        f'<g{anim(0)}><text x="{x}" y="{y}" font-size="13" fill="{FG}"><tspan fill="{GREEN}">$</tspan> neofetch</text></g>',
        f'<g{anim(1)}>'
        f'<text font-size="15" font-weight="700">'
        f'<tspan x="{x}" y="{y + 28}" fill="{GREEN}">{esc(PROMPT_USER)}</tspan>'
        f'<tspan x="{x_at:.1f}" y="{y + 28}" fill="{FG}">@</tspan>'
        f'<tspan x="{x_host:.1f}" y="{y + 28}" fill="{CYAN}">{esc(PROMPT_HOST)}</tspan>'
        f'</text>'
        f'<text x="{x}" y="{y + 42}" font-size="13" fill="{MUTED}">{dashes}</text></g>',
    ]

    ry = y + 64
    for k, (key, val) in enumerate(INFO_ROWS):
        color = KEY_COLORS[k % len(KEY_COLORS)]
        formatted_val = val
        for fkey, fval in fill.items():
            formatted_val = formatted_val.replace(f"{{{fkey}}}", str(fval))
        lines.append(
            f'<g{anim(k + 2)}><text x="{x}" y="{ry + k * 20}" font-size="13"><tspan fill="{color}" font-weight="700">{esc(key)}</tspan>'
            f'<tspan x="{x + 92}" fill="{FG}">{esc(formatted_val)}</tspan></text></g>'
        )

    # language bar: Java #1, TypeScript (Angular) #2
    by = ry + len(INFO_ROWS) * 20 + 4
    bar_w = W - 2 * x
    segs, legend, cx, lx, ly = [], [], x, x, by + 28
    for k, (lang, size) in enumerate(list(langs.items())[:5]):
        w = bar_w * size / total_bytes
        c = LANG_COLORS.get(lang, MUTED)
        segs.append(f'<rect x="{cx:.1f}" y="{by}" width="{max(w, 1):.1f}" height="8" fill="{c}"/>')
        cx += w
        label = f"{lang} {100 * size / total_bytes:.1f}%"
        if lx + len(label) * 6.6 + 18 > W - x:
            lx, ly = x, ly + 17
        legend.append(f'<circle cx="{lx + 4}" cy="{ly - 4}" r="4" fill="{c}"/><text x="{lx + 13}" y="{ly}" font-size="11" fill="{MUTED}">{esc(label)}</text>')
        lx += len(label) * 6.6 + 30

    bar_anim = "" if STATIC else '<animate attributeName="width" from="0" to="{0}" begin="1.6s" dur="1.2s" fill="freeze" calcMode="spline" keySplines=".2 .8 .2 1" keyTimes="0;1"/>'.format(bar_w)
    lines.append(
        f'<clipPath id="barClip"><rect x="{x}" y="{by}" width="{0 if not STATIC else bar_w}" height="8" rx="4">{bar_anim}</rect></clipPath>'
        f'<rect x="{x}" y="{by}" width="{bar_w}" height="8" rx="4" fill="{BORDER}"/>'
        f'<g clip-path="url(#barClip)">{"".join(segs)}</g>'
        f'<g{anim(len(INFO_ROWS) + 4)}>{"".join(legend)}</g>'
    )

    defs = "" if STATIC else """<style>
  .ln { opacity: 0; animation: ln .5s ease-out forwards; }
  @keyframes ln { from { opacity: 0; transform: translateX(-10px); } to { opacity: 1; transform: none; } }
</style>"""
    write_svg("info-card.svg", window(W, H, f"{PROMPT_USER}@{PROMPT_HOST}: ~", "\n".join(lines), defs))


if __name__ == "__main__":
    main()
