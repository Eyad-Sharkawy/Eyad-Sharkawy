"""Everything personal lives here. Edit this file, re-run `python scripts/render_all.py`."""

USERNAME = "Eyad-Sharkawy"
NAME = "Eyad Sharkawy"
PROMPT_USER = "eyad"
PROMPT_HOST = "github"

# Left out of the language bar
HIDE_LANGS = ["Jupyter Notebook", "CMake"]

# Cycled by the typing animation in header.svg
ROLES = [
    "Full-Stack Software Developer",
    "Open Source @ Apache Fineract & Mifos",
    "Java Spring Boot & Angular Specialist",
    "Applied Software Solutions @ FCAI-CU",
    "Modern C++ & Distributed Systems",
]

TAGLINE = "Cairo, EG  ·  Java, Angular, C++ & Open Source Fintech Systems"

# neofetch-style rows on info-card.svg. "{...}" placeholders are filled from live data.
INFO_ROWS = [
    ("Role", "Full-Stack Software Developer"),
    ("Track", "Applied Software Solutions @ FCAI-CU"),
    ("OSS", "Apache Fineract · Mifos Initiative"),
    ("Uptime", "{uptime} on GitHub"),
    ("Langs", "{top_langs}"),
    ("Backend", "Java · Spring Boot · Modern C++"),
    ("Frontend", "Angular · TypeScript · Tailwind"),
    ("Infra", "Docker · PostgreSQL · Nginx · Jenkins"),
    ("Repos", "{public_repos} public  ·  {stars} stars"),
    ("Contribs", "{total} in the last year"),
    ("Streak", "{current_streak}d current  ·  {longest_streak}d best"),
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

# tech-sphere.svg: category -> labels (each category gets its own colour)
TECH = {
    "languages": ["Java", "TypeScript", "C++", "JavaScript", "Python"],
    "frontend": ["Angular", "Tailwind", "HTML5", "CSS3", "React"],
    "backend": ["Spring Boot", "REST APIs", "Microservices", "Postman"],
    "infra": ["Docker", "PostgreSQL", "Nginx", "Jenkins", "Git"],
    "tools": ["Kubernetes", "Linux", "AWS", "Vitest", "Firebase"],
}
