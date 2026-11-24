"""Scrape the public contributions calendar (no token needed) -> data/contributions.json"""
import re
from collections import Counter, defaultdict
from datetime import date, timedelta
import requests
from bs4 import BeautifulSoup

from common import save, load
from config import USERNAME


def main():
    existing = load("contributions.json", {})
    url = f"https://github.com/users/{USERNAME}/contributions"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

    try:
        html = requests.get(url, headers=headers, timeout=15).text
        soup = BeautifulSoup(html, "html.parser")

        tips = {}
        for tip in soup.find_all("tool-tip"):
            m = re.match(r"\s*(\d[\d,]*) contributions?", tip.get_text())
            tips[tip.get("for")] = int(m.group(1).replace(",", "")) if m else 0

        days = []
        for cell in soup.select("td.ContributionCalendar-day[data-date]"):
            days.append({
                "date": cell["data-date"],
                "level": int(cell.get("data-level", 0)),
                "count": tips.get(cell.get("id"), 0),
            })

        if days:
            days.sort(key=lambda d: d["date"])
            counts = [d["count"] for d in days]
            total = sum(counts)

            longest = run = 0
            for c in counts:
                run = run + 1 if c else 0
                longest = max(longest, run)

            current = 0
            tail = counts[:-1] if counts and counts[-1] == 0 else counts
            for c in reversed(tail):
                if not c:
                    break
                current += 1

            best = max(days, key=lambda d: d["count"])
            monthly = defaultdict(int)
            weekday = Counter()
            for d in days:
                monthly[d["date"][:7]] += d["count"]
                weekday[date.fromisoformat(d["date"]).strftime("%A")] += d["count"]

            save("contributions.json", {
                "username": USERNAME,
                "days": days,
                "stats": {
                    "total": total,
                    "current_streak": current,
                    "longest_streak": longest,
                    "best_day": {"date": best["date"], "count": best["count"]},
                    "active_days": sum(1 for c in counts if c),
                    "busiest_weekday": weekday.most_common(1)[0][0] if total else "-",
                    "monthly": dict(monthly),
                    "range": [days[0]["date"], days[-1]["date"]],
                },
            })
            print(f"{len(days)} days, {total} contributions, streak {current}/{longest}, best: {best['count']} on {best['date']}")
            return
    except Exception as e:
        print(f"[Notice] Failed to scrape contributions, using cache/fallback: {e}")

    if existing:
        print("Using existing cached contributions.json")
    else:
        print("[Warning] No existing contributions cache found.")


if __name__ == "__main__":
    main()
