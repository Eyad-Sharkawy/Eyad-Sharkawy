"""Everything personal lives here. Edit this file, re-run `python scripts/render_all.py`."""

USERNAME = "Eyad-Sharkawy"
NAME = "Eyad Sharkawy"
PROMPT_USER = "eyad"
PROMPT_HOST = "github"

# Left out of the language bar
HIDE_LANGS = ["Jupyter Notebook", "CMake", "SCSS", "CSS", "HTML"]

# Cycled by the typing animation in header.svg (simple & direct, no buzzwords)
ROLES = [
    "Java & Spring Boot Developer",
    "Angular Frontend Developer",
    "Open Source @ Apache Fineract & Mifos",
    "C++ & Systems Programming",
]

TAGLINE = "Cairo, EG  ·  Java, Angular & C++"

# neofetch-style rows on info-card.svg. "{...}" placeholders are filled from live data.
INFO_ROWS = [
    ("Role", "Software Developer"),
    ("Backend", "Java · Spring Boot"),
    ("Frontend", "Angular · TypeScript"),
    ("Systems", "C++"),
    ("OSS", "Apache Fineract · Mifos"),
    ("Uptime", "{uptime} on GitHub"),
    ("Langs", "{top_langs}"),
    ("Databases", "PostgreSQL"),
    ("Tools", "Docker · Git · Linux"),
    ("Repos", "{public_repos} public  ·  {stars} stars"),
    ("Contribs", "{total} in the last year"),
    ("Projects", "Agency OS · Omni Sync · Phoenix"),
]

# globe.svg: home pin + arcs to the open-source projects you contribute to (lat, lon)
HOME = ("Cairo", 30.04, 31.23)
GLOBE_CMD = "./open-source --from cairo"

REGIONS = [
    ("Apache Fineract", 39.74, -75.55),
    ("Mifos Initiative", 47.60, -122.33),
    ("Cloud & OSS Hub", 52.36, 4.90),
]

# tech-sphere.svg: category -> labels
TECH = {
    "backend": ["Java", "Spring Boot", "REST APIs", "PostgreSQL"],
    "frontend": ["Angular", "TypeScript", "TailwindCSS", "JavaScript"],
    "systems": ["C++", "Docker", "Linux", "Git"],
    "tools": ["Postman", "Kubernetes", "Vitest", "AWS"],
}
