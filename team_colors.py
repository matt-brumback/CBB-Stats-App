"""
College basketball team colors, keyed by Sports-Reference.com school ID.

primary   = main brand color (used for bars, accents, borders)
secondary = alternate/accent color (used for rolling-average line)
name      = human-readable display name
"""

TEAM_COLORS = {

    # ── ACC ───────────────────────────────────────────────────────────────────
    "boston-college":        {"primary": "#98002E", "secondary": "#C4B7A6", "name": "Boston College"},
    "clemson":               {"primary": "#F56600", "secondary": "#522D80", "name": "Clemson"},
    "duke":                  {"primary": "#003087", "secondary": "#CDA323", "name": "Duke"},
    "florida-state":         {"primary": "#782F40", "secondary": "#CEB888", "name": "Florida State"},
    "georgia-tech":          {"primary": "#003057", "secondary": "#B3A369", "name": "Georgia Tech"},
    "louisville":            {"primary": "#AD0000", "secondary": "#000000", "name": "Louisville"},
    "miami-fl":              {"primary": "#005030", "secondary": "#F47321", "name": "Miami (FL)"},
    "north-carolina-state":  {"primary": "#CC0000", "secondary": "#000000", "name": "NC State"},
    "north-carolina":        {"primary": "#7BAFD4", "secondary": "#13294B", "name": "North Carolina"},
    "notre-dame":            {"primary": "#0C2340", "secondary": "#C99700", "name": "Notre Dame"},
    "pittsburgh":            {"primary": "#003594", "secondary": "#FFB81C", "name": "Pittsburgh"},
    "syracuse":              {"primary": "#F76900", "secondary": "#002147", "name": "Syracuse"},
    "virginia":              {"primary": "#F84C1E", "secondary": "#232D4B", "name": "Virginia"},
    "virginia-tech":         {"primary": "#630031", "secondary": "#CF4420", "name": "Virginia Tech"},
    "wake-forest":           {"primary": "#9E7E38", "secondary": "#000000", "name": "Wake Forest"},
    "california":            {"primary": "#003262", "secondary": "#FDB515", "name": "California"},
    "stanford":              {"primary": "#8C1515", "secondary": "#2D2D2D", "name": "Stanford"},
    "washington-state":      {"primary": "#981E32", "secondary": "#5E6A71", "name": "Washington State"},

    # ── Big Ten ───────────────────────────────────────────────────────────────
    "illinois":              {"primary": "#E84A27", "secondary": "#13294B", "name": "Illinois"},
    "indiana":               {"primary": "#990000", "secondary": "#DFBF60", "name": "Indiana"},
    "iowa":                  {"primary": "#FFCD00", "secondary": "#000000", "name": "Iowa"},
    "maryland":              {"primary": "#E03A3E", "secondary": "#FFD520", "name": "Maryland"},
    "michigan":              {"primary": "#00274C", "secondary": "#FFCB05", "name": "Michigan"},
    "michigan-state":        {"primary": "#18453B", "secondary": "#FFFFFF", "name": "Michigan State"},
    "minnesota":             {"primary": "#7A0019", "secondary": "#FFCC33", "name": "Minnesota"},
    "nebraska":              {"primary": "#E41C38", "secondary": "#F5F1E7", "name": "Nebraska"},
    "northwestern":          {"primary": "#4E2A84", "secondary": "#FFFFFF", "name": "Northwestern"},
    "ohio-state":            {"primary": "#BB0000", "secondary": "#666666", "name": "Ohio State"},
    "penn-state":            {"primary": "#1E407C", "secondary": "#FFFFFF", "name": "Penn State"},
    "purdue":                {"primary": "#CEB888", "secondary": "#000000", "name": "Purdue"},
    "rutgers":               {"primary": "#CC0033", "secondary": "#5F6A72", "name": "Rutgers"},
    "wisconsin":             {"primary": "#C5050C", "secondary": "#FFFFFF", "name": "Wisconsin"},
    "ucla":                  {"primary": "#2D68C4", "secondary": "#F2A900", "name": "UCLA"},
    "usc":                   {"primary": "#990000", "secondary": "#FFC72C", "name": "USC"},
    "washington":            {"primary": "#4B2E83", "secondary": "#B7A57A", "name": "Washington"},
    "oregon":                {"primary": "#154733", "secondary": "#FEE123", "name": "Oregon"},
    "oregon-state":          {"primary": "#DC4405", "secondary": "#000000", "name": "Oregon State"},

    # ── Big 12 ────────────────────────────────────────────────────────────────
    "arizona":               {"primary": "#AB0520", "secondary": "#0C234B", "name": "Arizona"},
    "arizona-state":         {"primary": "#8C1D40", "secondary": "#FFC627", "name": "Arizona State"},
    "baylor":                {"primary": "#154734", "secondary": "#FFB81C", "name": "Baylor"},
    "brigham-young":         {"primary": "#002E5D", "secondary": "#FFFFFF", "name": "BYU"},
    "cincinnati":            {"primary": "#E00122", "secondary": "#000000", "name": "Cincinnati"},
    "colorado":              {"primary": "#CFB87C", "secondary": "#000000", "name": "Colorado"},
    "iowa-state":            {"primary": "#C8102E", "secondary": "#F1BE48", "name": "Iowa State"},
    "kansas":                {"primary": "#0051A5", "secondary": "#E8000D", "name": "Kansas"},
    "kansas-state":          {"primary": "#512888", "secondary": "#D1A827", "name": "Kansas State"},
    "oklahoma":              {"primary": "#841617", "secondary": "#FDF9D8", "name": "Oklahoma"},
    "oklahoma-state":        {"primary": "#FF6600", "secondary": "#000000", "name": "Oklahoma State"},
    "texas-christian":       {"primary": "#4D1979", "secondary": "#A3A3A3", "name": "TCU"},
    "texas":                 {"primary": "#BF5700", "secondary": "#FFFFFF", "name": "Texas"},
    "texas-tech":            {"primary": "#CC0000", "secondary": "#000000", "name": "Texas Tech"},
    "central-florida":       {"primary": "#BA9B37", "secondary": "#000000", "name": "UCF"},
    "utah":                  {"primary": "#BE0000", "secondary": "#000000", "name": "Utah"},
    "west-virginia":         {"primary": "#002855", "secondary": "#EAAA00", "name": "West Virginia"},

    # ── SEC ───────────────────────────────────────────────────────────────────
    "alabama":               {"primary": "#9E1B32", "secondary": "#828A8F", "name": "Alabama"},
    "arkansas":              {"primary": "#9D2235", "secondary": "#000000", "name": "Arkansas"},
    "auburn":                {"primary": "#E87722", "secondary": "#03244D", "name": "Auburn"},
    "florida":               {"primary": "#0021A5", "secondary": "#FA4616", "name": "Florida"},
    "georgia":               {"primary": "#BA0C2F", "secondary": "#000000", "name": "Georgia"},
    "kentucky":              {"primary": "#0033A0", "secondary": "#FFFFFF", "name": "Kentucky"},
    "lsu":                   {"primary": "#461D7C", "secondary": "#FDD023", "name": "LSU"},
    "mississippi-state":     {"primary": "#660000", "secondary": "#FFFFFF", "name": "Mississippi State"},
    "mississippi":           {"primary": "#CE1126", "secondary": "#14213D", "name": "Ole Miss"},
    "missouri":              {"primary": "#F1B82D", "secondary": "#000000", "name": "Missouri"},
    "south-carolina":        {"primary": "#73000A", "secondary": "#000000", "name": "South Carolina"},
    "tennessee":             {"primary": "#FF8200", "secondary": "#FFFFFF", "name": "Tennessee"},
    "texas-am":              {"primary": "#500000", "secondary": "#FFFFFF", "name": "Texas A&M"},
    "vanderbilt":            {"primary": "#866D4B", "secondary": "#000000", "name": "Vanderbilt"},

    # ── Big East ──────────────────────────────────────────────────────────────
    "butler":                {"primary": "#13294B", "secondary": "#807B78", "name": "Butler"},
    "connecticut":           {"primary": "#000E2F", "secondary": "#A2AAAD", "name": "UConn"},
    "creighton":             {"primary": "#005CA9", "secondary": "#FFFFFF", "name": "Creighton"},
    "depaul":                {"primary": "#00539F", "secondary": "#D22630", "name": "DePaul"},
    "georgetown":            {"primary": "#041E42", "secondary": "#73777B", "name": "Georgetown"},
    "marquette":             {"primary": "#003366", "secondary": "#FFCC00", "name": "Marquette"},
    "providence":            {"primary": "#321E6D", "secondary": "#FFFFFF", "name": "Providence"},
    "seton-hall":            {"primary": "#004B8D", "secondary": "#FFFFFF", "name": "Seton Hall"},
    "st-johns-ny":           {"primary": "#CC0000", "secondary": "#FFFFFF", "name": "St. John's"},
    "villanova":             {"primary": "#003189", "secondary": "#13B5EA", "name": "Villanova"},
    "xavier":                {"primary": "#0D5257", "secondary": "#B9975B", "name": "Xavier"},

    # ── Other Notable Programs ─────────────────────────────────────────────────
    "dayton":                {"primary": "#CC0000", "secondary": "#004B8D", "name": "Dayton"},
    "davidson":              {"primary": "#CC0000", "secondary": "#000000", "name": "Davidson"},
    "drake":                 {"primary": "#004B8D", "secondary": "#FFFFFF", "name": "Drake"},
    "gonzaga":               {"primary": "#002060", "secondary": "#CF0A2C", "name": "Gonzaga"},
    "loyola-il":             {"primary": "#822433", "secondary": "#DBC98E", "name": "Loyola Chicago"},
    "memphis":               {"primary": "#003087", "secondary": "#898D8D", "name": "Memphis"},
    "murray-state":          {"primary": "#002144", "secondary": "#9D9795", "name": "Murray State"},
    "nevada":                {"primary": "#003366", "secondary": "#807B77", "name": "Nevada"},
    "new-mexico":            {"primary": "#BA0C2F", "secondary": "#888B8D", "name": "New Mexico"},
    "saint-louis":           {"primary": "#003DA5", "secondary": "#FFFFFF", "name": "Saint Louis"},
    "saint-marys-ca":        {"primary": "#0F3B7E", "secondary": "#BB9753", "name": "Saint Mary's"},
    "san-diego-state":       {"primary": "#C41230", "secondary": "#000000", "name": "San Diego State"},
    "utah-state":            {"primary": "#00263A", "secondary": "#8A8D8F", "name": "Utah State"},
    "vcu":                   {"primary": "#000000", "secondary": "#F9A01B", "name": "VCU"},
    "wichita-state":         {"primary": "#000000", "secondary": "#FFD100", "name": "Wichita State"},
}

DEFAULT_PRIMARY   = "#2c3e50"
DEFAULT_SECONDARY = "#7f8c8d"

# ── Aliases & nicknames ────────────────────────────────────────────────────────
# Maps common abbreviations / nicknames (lowercase) → school_id
# Covers the cases that fuzzy name search can't catch on its own.
TEAM_ALIASES: dict[str, str] = {
    # Abbreviations
    "unc":              "north-carolina",
    "uva":              "virginia",
    "vt":               "virginia-tech",
    "uk":               "kentucky",
    "ku":               "kansas",
    "ksu":              "kansas-state",
    "k-state":          "kansas-state",
    "wvu":              "west-virginia",
    "osu":              "ohio-state",
    "msu":              "michigan-state",
    "psu":              "penn-state",
    "uconn":            "connecticut",
    "ucf":              "central-florida",
    "tcu":              "texas-christian",
    "byu":              "brigham-young",
    "fsu":              "florida-state",
    "ncsu":             "north-carolina-state",
    "sdsu":             "san-diego-state",
    "gt":               "georgia-tech",
    "bc":               "boston-college",
    "nd":               "notre-dame",
    "pitt":             "pittsburgh",
    "cal":              "california",
    "lsu":              "lsu",
    "vcu":              "vcu",
    "ucla":             "ucla",
    "usc":              "usc",
    # Nicknames (unambiguous)
    "tar heels":        "north-carolina",
    "cavaliers":        "virginia",
    "hokies":           "virginia-tech",
    "jayhawks":         "kansas",
    "mountaineers":     "west-virginia",
    "buckeyes":         "ohio-state",
    "spartans":         "michigan-state",
    "nittany lions":    "penn-state",
    "boilermakers":     "purdue",
    "hoosiers":         "indiana",
    "hawkeyes":         "iowa",
    "cyclones":         "iowa-state",
    "illini":           "illinois",
    "fighting illini":  "illinois",
    "huskers":          "nebraska",
    "cornhuskers":      "nebraska",
    "gophers":          "minnesota",
    "terps":            "maryland",
    "terrapins":        "maryland",
    "wolverines":       "michigan",
    "badgers":          "wisconsin",
    "scarlet knights":  "rutgers",
    "zags":             "gonzaga",
    "nova":             "villanova",
    "hoyas":            "georgetown",
    "blue demons":      "depaul",
    "musketeers":       "xavier",
    "friars":           "providence",
    "ramblers":         "loyola-il",
    "flyers":           "dayton",
    "blue devils":      "duke",
    "orange":           "syracuse",
    "ducks":            "oregon",
    "beavers":          "oregon-state",
    "bruins":           "ucla",
    "trojans":          "usc",
    "fighting irish":   "notre-dame",
    "demon deacons":    "wake-forest",
    "wake":             "wake-forest",
    "yellow jackets":   "georgia-tech",
    "seminoles":        "florida-state",
    "crimson tide":     "alabama",
    "bama":             "alabama",
    "razorbacks":       "arkansas",
    "hogs":             "arkansas",
    "gators":           "florida",
    "vols":             "tennessee",
    "volunteers":       "tennessee",
    "tigers":           "lsu",
    "hurricanes":       "miami-fl",
    "canes":            "miami-fl",
    "longhorns":        "texas",
    "red raiders":      "texas-tech",
    "cowboys":          "oklahoma-state",
    "sooners":          "oklahoma",
    "bears":            "baylor",
    "aztecs":           "san-diego-state",
    "shockers":         "wichita-state",
    "rams":             "vcu",
    "lobos":            "new-mexico",
    "utes":             "utah",
    "buffs":            "colorado",
    "buffaloes":        "colorado",
    "commodores":       "vanderbilt",
    "vandy":            "vanderbilt",
    "ole miss":         "mississippi",
    "rebels":           "mississippi",
    "nc state":         "north-carolina-state",
    "wolfpack":         "north-carolina-state",
    "a&m":              "texas-am",
    "aggie":            "texas-am",
    "aggies":           "texas-am",
    "cards":            "louisville",
    "cardinals":        "louisville",
    "cats":             "kentucky",
    "wildcats":         "kentucky",
    "panthers":         "pittsburgh",
}


def local_search_teams(query: str) -> list:
    """
    Search our local TEAM_COLORS dict by alias, team name, or school ID.
    Returns list of {name, id, info} dicts, sorted by match quality.
    """
    q = query.strip().lower()
    if not q or len(q) < 2:
        return []

    # 1. Alias exact match → single definitive result
    if q in TEAM_ALIASES:
        sid = TEAM_ALIASES[q]
        if sid and sid in TEAM_COLORS:
            t = TEAM_COLORS[sid]
            return [{"name": t["name"], "id": sid, "info": ""}]

    # 2. Fuzzy match on team name and hyphenated school ID
    scored = []
    for sid, info in TEAM_COLORS.items():
        name_lower = info["name"].lower()
        id_words   = sid.replace("-", " ")
        if q not in name_lower and q not in id_words:
            continue
        # Score: 0 = exact, 1 = starts-with, 2 = substring
        if name_lower == q or id_words == q:
            score = 0
        elif name_lower.startswith(q) or id_words.startswith(q):
            score = 1
        else:
            score = 2
        scored.append((score, info["name"], sid))

    scored.sort()
    return [{"name": name, "id": sid, "info": ""} for _, name, sid in scored]


def get_team_colors(school_id: str) -> tuple[str, str]:
    """Return (primary, secondary) hex strings for a given school_id."""
    team = TEAM_COLORS.get(school_id)
    if team:
        return team["primary"], team["secondary"]
    return DEFAULT_PRIMARY, DEFAULT_SECONDARY


def get_all_teams() -> list[tuple[str, str]]:
    """Return list of (display_name, school_id) sorted alphabetically by name."""
    return sorted(
        [(v["name"], k) for k, v in TEAM_COLORS.items()],
        key=lambda x: x[0],
    )
