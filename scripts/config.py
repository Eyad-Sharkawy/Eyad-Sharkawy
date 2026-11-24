"""Everything personal lives here. Edit this file, re-run `python scripts/render_all.py`."""

USERNAME = "Eyad-Sharkawy"
NAME = "Eyad Sharkawy"
PROMPT_USER = "eyad"
PROMPT_HOST = "github"

# Left out of the language bar
HIDE_LANGS = ["Jupyter Notebook", "CMake", "SCSS", "CSS", "HTML"]

# Cycled by the typing animation in header.svg (Java Spring Boot #1, Angular #2)
ROLES = [
    "Java Spring Boot Developer",
    "Angular Frontend Engineer",
    "Open Source @ Apache Fineract & Mifos",
    "Enterprise Systems & Microservices",
    "Modern C++ & Distributed Architectures",
]

TAGLINE = "Cairo, EG  ·  Java Spring Boot & Angular Specialist"

# neofetch-style rows on info-card.svg. "{...}" placeholders are filled from live data.
INFO_ROWS = [
    ("Role", "Java Spring Boot & Angular Developer"),
    ("Primary", "Java 21 · Spring Boot 3 · Microservices"),
    ("Secondary", "Angular · TypeScript · Modern Web"),
    ("OSS", "Apache Fineract (Java) · Mifos (Angular)"),
    ("Uptime", "{uptime} on GitHub"),
    ("Langs", "{top_langs}"),
    ("Backend", "Spring Boot · REST APIs · Modern C++"),
    ("Frontend", "Angular · RxJS · TypeScript · Tailwind"),
    ("Infra", "Docker · PostgreSQL · Nginx · Jenkins"),
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

# tech-sphere.svg: category -> labels (Java Spring Boot #1, Angular #2)
TECH = {
    "backend": ["Java", "Spring Boot", "Microservices", "REST APIs", "Spring Security"],
    "frontend": ["Angular", "TypeScript", "RxJS", "TailwindCSS", "JavaScript"],
    "systems": ["Modern C++", "PostgreSQL", "Docker", "Linux"],
    "infra": ["Nginx", "Jenkins", "Git", "Postman", "Kubernetes"],
    "cloud": ["AWS", "Vitest", "Redis", "Firebase"],
}
