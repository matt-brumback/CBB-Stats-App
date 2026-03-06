"""
College basketball team colors, keyed by Sports-Reference.com school ID.

primary   = main brand color (used for bars, accents, borders)
secondary = alternate/accent color (used for rolling-average line)
name      = human-readable display name (city/school name only)
nickname  = team nickname / mascot (used to build full name like "Kansas Jayhawks")
"""

TEAM_COLORS = {

    # ── ACC ───────────────────────────────────────────────────────────────────
    "boston-college":        {"primary": "#98002E", "secondary": "#C4B7A6", "name": "Boston College",  "nickname": "Eagles"},
    "clemson":               {"primary": "#F56600", "secondary": "#522D80", "name": "Clemson",          "nickname": "Tigers"},
    "duke":                  {"primary": "#003087", "secondary": "#CDA323", "name": "Duke",             "nickname": "Blue Devils"},
    "florida-state":         {"primary": "#782F40", "secondary": "#CEB888", "name": "Florida State",   "nickname": "Seminoles"},
    "georgia-tech":          {"primary": "#003057", "secondary": "#B3A369", "name": "Georgia Tech",    "nickname": "Yellow Jackets"},
    "louisville":            {"primary": "#AD0000", "secondary": "#000000", "name": "Louisville",       "nickname": "Cardinals"},
    "miami-fl":              {"primary": "#005030", "secondary": "#F47321", "name": "Miami (FL)",       "nickname": "Hurricanes"},
    "north-carolina-state":  {"primary": "#CC0000", "secondary": "#000000", "name": "NC State",         "nickname": "Wolfpack"},
    "north-carolina":        {"primary": "#7BAFD4", "secondary": "#13294B", "name": "North Carolina",  "nickname": "Tar Heels"},
    "notre-dame":            {"primary": "#0C2340", "secondary": "#C99700", "name": "Notre Dame",       "nickname": "Fighting Irish"},
    "pittsburgh":            {"primary": "#003594", "secondary": "#FFB81C", "name": "Pittsburgh",       "nickname": "Panthers"},
    "syracuse":              {"primary": "#F76900", "secondary": "#002147", "name": "Syracuse",         "nickname": "Orange"},
    "virginia":              {"primary": "#F84C1E", "secondary": "#232D4B", "name": "Virginia",         "nickname": "Cavaliers"},
    "virginia-tech":         {"primary": "#630031", "secondary": "#CF4420", "name": "Virginia Tech",   "nickname": "Hokies"},
    "wake-forest":           {"primary": "#9E7E38", "secondary": "#000000", "name": "Wake Forest",     "nickname": "Demon Deacons"},
    "california":            {"primary": "#003262", "secondary": "#FDB515", "name": "California",      "nickname": "Golden Bears"},
    "stanford":              {"primary": "#8C1515", "secondary": "#2D2D2D", "name": "Stanford",         "nickname": "Cardinal"},
    "washington-state":      {"primary": "#981E32", "secondary": "#5E6A71", "name": "Washington State","nickname": "Cougars"},

    # ── Big Ten ───────────────────────────────────────────────────────────────
    "illinois":              {"primary": "#E84A27", "secondary": "#13294B", "name": "Illinois",         "nickname": "Fighting Illini"},
    "indiana":               {"primary": "#990000", "secondary": "#DFBF60", "name": "Indiana",          "nickname": "Hoosiers"},
    "iowa":                  {"primary": "#FFCD00", "secondary": "#000000", "name": "Iowa",             "nickname": "Hawkeyes"},
    "maryland":              {"primary": "#E03A3E", "secondary": "#FFD520", "name": "Maryland",         "nickname": "Terrapins"},
    "michigan":              {"primary": "#00274C", "secondary": "#FFCB05", "name": "Michigan",         "nickname": "Wolverines"},
    "michigan-state":        {"primary": "#18453B", "secondary": "#FFFFFF", "name": "Michigan State",  "nickname": "Spartans"},
    "minnesota":             {"primary": "#7A0019", "secondary": "#FFCC33", "name": "Minnesota",        "nickname": "Golden Gophers"},
    "nebraska":              {"primary": "#E41C38", "secondary": "#F5F1E7", "name": "Nebraska",         "nickname": "Cornhuskers"},
    "northwestern":          {"primary": "#4E2A84", "secondary": "#FFFFFF", "name": "Northwestern",     "nickname": "Wildcats"},
    "ohio-state":            {"primary": "#BB0000", "secondary": "#666666", "name": "Ohio State",       "nickname": "Buckeyes"},
    "penn-state":            {"primary": "#1E407C", "secondary": "#FFFFFF", "name": "Penn State",       "nickname": "Nittany Lions"},
    "purdue":                {"primary": "#CEB888", "secondary": "#000000", "name": "Purdue",           "nickname": "Boilermakers"},
    "rutgers":               {"primary": "#CC0033", "secondary": "#5F6A72", "name": "Rutgers",          "nickname": "Scarlet Knights"},
    "wisconsin":             {"primary": "#C5050C", "secondary": "#FFFFFF", "name": "Wisconsin",        "nickname": "Badgers"},
    "ucla":                  {"primary": "#2D68C4", "secondary": "#F2A900", "name": "UCLA",             "nickname": "Bruins"},
    "usc":                   {"primary": "#990000", "secondary": "#FFC72C", "name": "USC",              "nickname": "Trojans"},
    "washington":            {"primary": "#4B2E83", "secondary": "#B7A57A", "name": "Washington",       "nickname": "Huskies"},
    "oregon":                {"primary": "#154733", "secondary": "#FEE123", "name": "Oregon",           "nickname": "Ducks"},
    "oregon-state":          {"primary": "#DC4405", "secondary": "#000000", "name": "Oregon State",    "nickname": "Beavers"},

    # ── Big 12 ────────────────────────────────────────────────────────────────
    "arizona":               {"primary": "#AB0520", "secondary": "#0C234B", "name": "Arizona",          "nickname": "Wildcats"},
    "arizona-state":         {"primary": "#8C1D40", "secondary": "#FFC627", "name": "Arizona State",   "nickname": "Sun Devils"},
    "baylor":                {"primary": "#154734", "secondary": "#FFB81C", "name": "Baylor",           "nickname": "Bears"},
    "brigham-young":         {"primary": "#002E5D", "secondary": "#FFFFFF", "name": "BYU",              "nickname": "Cougars"},
    "cincinnati":            {"primary": "#E00122", "secondary": "#000000", "name": "Cincinnati",       "nickname": "Bearcats"},
    "colorado":              {"primary": "#CFB87C", "secondary": "#000000", "name": "Colorado",         "nickname": "Buffaloes"},
    "iowa-state":            {"primary": "#C8102E", "secondary": "#F1BE48", "name": "Iowa State",      "nickname": "Cyclones"},
    "kansas":                {"primary": "#0051A5", "secondary": "#E8000D", "name": "Kansas",           "nickname": "Jayhawks"},
    "kansas-state":          {"primary": "#512888", "secondary": "#D1A827", "name": "Kansas State",    "nickname": "Wildcats"},
    "oklahoma":              {"primary": "#841617", "secondary": "#FDF9D8", "name": "Oklahoma",         "nickname": "Sooners"},
    "oklahoma-state":        {"primary": "#FF6600", "secondary": "#000000", "name": "Oklahoma State",  "nickname": "Cowboys"},
    "texas-christian":       {"primary": "#4D1979", "secondary": "#A3A3A3", "name": "TCU",              "nickname": "Horned Frogs"},
    "texas":                 {"primary": "#BF5700", "secondary": "#FFFFFF", "name": "Texas",            "nickname": "Longhorns"},
    "texas-tech":            {"primary": "#CC0000", "secondary": "#000000", "name": "Texas Tech",      "nickname": "Red Raiders"},
    "central-florida":       {"primary": "#BA9B37", "secondary": "#000000", "name": "UCF",              "nickname": "Knights"},
    "utah":                  {"primary": "#BE0000", "secondary": "#000000", "name": "Utah",             "nickname": "Utes"},
    "west-virginia":         {"primary": "#002855", "secondary": "#EAAA00", "name": "West Virginia",   "nickname": "Mountaineers"},

    # ── SEC ───────────────────────────────────────────────────────────────────
    "alabama":               {"primary": "#9E1B32", "secondary": "#828A8F", "name": "Alabama",          "nickname": "Crimson Tide"},
    "arkansas":              {"primary": "#9D2235", "secondary": "#000000", "name": "Arkansas",         "nickname": "Razorbacks"},
    "auburn":                {"primary": "#E87722", "secondary": "#03244D", "name": "Auburn",           "nickname": "Tigers"},
    "florida":               {"primary": "#0021A5", "secondary": "#FA4616", "name": "Florida",          "nickname": "Gators"},
    "georgia":               {"primary": "#BA0C2F", "secondary": "#000000", "name": "Georgia",          "nickname": "Bulldogs"},
    "kentucky":              {"primary": "#0033A0", "secondary": "#FFFFFF", "name": "Kentucky",         "nickname": "Wildcats"},
    "lsu":                   {"primary": "#461D7C", "secondary": "#FDD023", "name": "LSU",              "nickname": "Tigers"},
    "mississippi-state":     {"primary": "#660000", "secondary": "#FFFFFF", "name": "Mississippi State","nickname": "Bulldogs"},
    "mississippi":           {"primary": "#CE1126", "secondary": "#14213D", "name": "Ole Miss",         "nickname": "Rebels"},
    "missouri":              {"primary": "#F1B82D", "secondary": "#000000", "name": "Missouri",         "nickname": "Tigers"},
    "south-carolina":        {"primary": "#73000A", "secondary": "#000000", "name": "South Carolina",  "nickname": "Gamecocks"},
    "tennessee":             {"primary": "#FF8200", "secondary": "#FFFFFF", "name": "Tennessee",        "nickname": "Volunteers"},
    "texas-am":              {"primary": "#500000", "secondary": "#FFFFFF", "name": "Texas A&M",        "nickname": "Aggies"},
    "vanderbilt":            {"primary": "#866D4B", "secondary": "#000000", "name": "Vanderbilt",       "nickname": "Commodores"},

    # ── Big East ──────────────────────────────────────────────────────────────
    "butler":                {"primary": "#13294B", "secondary": "#807B78", "name": "Butler",           "nickname": "Bulldogs"},
    "connecticut":           {"primary": "#000E2F", "secondary": "#A2AAAD", "name": "UConn",            "nickname": "Huskies"},
    "creighton":             {"primary": "#005CA9", "secondary": "#FFFFFF", "name": "Creighton",        "nickname": "Bluejays"},
    "depaul":                {"primary": "#00539F", "secondary": "#D22630", "name": "DePaul",           "nickname": "Blue Demons"},
    "georgetown":            {"primary": "#041E42", "secondary": "#73777B", "name": "Georgetown",       "nickname": "Hoyas"},
    "marquette":             {"primary": "#003366", "secondary": "#FFCC00", "name": "Marquette",        "nickname": "Golden Eagles"},
    "providence":            {"primary": "#321E6D", "secondary": "#FFFFFF", "name": "Providence",       "nickname": "Friars"},
    "seton-hall":            {"primary": "#004B8D", "secondary": "#FFFFFF", "name": "Seton Hall",       "nickname": "Pirates"},
    "st-johns-ny":           {"primary": "#CC0000", "secondary": "#FFFFFF", "name": "St. John's",       "nickname": "Red Storm"},
    "villanova":             {"primary": "#003189", "secondary": "#13B5EA", "name": "Villanova",        "nickname": "Wildcats"},
    "xavier":                {"primary": "#0D5257", "secondary": "#B9975B", "name": "Xavier",           "nickname": "Musketeers"},

    # ── Other Notable Programs ─────────────────────────────────────────────────
    "dayton":                {"primary": "#CC0000", "secondary": "#004B8D", "name": "Dayton",           "nickname": "Flyers"},
    "davidson":              {"primary": "#CC0000", "secondary": "#000000", "name": "Davidson",         "nickname": "Wildcats"},
    "drake":                 {"primary": "#004B8D", "secondary": "#FFFFFF", "name": "Drake",            "nickname": "Bulldogs"},
    "gonzaga":               {"primary": "#002060", "secondary": "#CF0A2C", "name": "Gonzaga",          "nickname": "Bulldogs"},
    "loyola-il":             {"primary": "#822433", "secondary": "#DBC98E", "name": "Loyola Chicago",  "nickname": "Ramblers"},
    "memphis":               {"primary": "#003087", "secondary": "#898D8D", "name": "Memphis",          "nickname": "Tigers"},
    "murray-state":          {"primary": "#002144", "secondary": "#9D9795", "name": "Murray State",    "nickname": "Racers"},
    "nevada":                {"primary": "#003366", "secondary": "#807B77", "name": "Nevada",           "nickname": "Wolf Pack"},
    "new-mexico":            {"primary": "#BA0C2F", "secondary": "#888B8D", "name": "New Mexico",       "nickname": "Lobos"},
    "saint-louis":           {"primary": "#003DA5", "secondary": "#FFFFFF", "name": "Saint Louis",     "nickname": "Billikens"},
    "saint-marys-ca":        {"primary": "#0F3B7E", "secondary": "#BB9753", "name": "Saint Mary's",    "nickname": "Gaels"},
    "san-diego-state":       {"primary": "#C41230", "secondary": "#000000", "name": "San Diego State", "nickname": "Aztecs"},
    "utah-state":            {"primary": "#00263A", "secondary": "#8A8D8F", "name": "Utah State",      "nickname": "Aggies"},
    "vcu":                   {"primary": "#000000", "secondary": "#F9A01B", "name": "VCU",              "nickname": "Rams"},
    "wichita-state":         {"primary": "#000000", "secondary": "#FFD100", "name": "Wichita State",   "nickname": "Shockers"},
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


def get_team_display_name(school_id: str) -> str:
    """Return the short display name (e.g. 'Kansas') for a school_id."""
    team = TEAM_COLORS.get(school_id)
    return team["name"] if team else school_id.replace("-", " ").title()


def get_team_full_name(school_id: str) -> str:
    """Return the full display name including nickname (e.g. 'Kansas Jayhawks')."""
    team = TEAM_COLORS.get(school_id)
    if not team:
        return school_id.replace("-", " ").title()
    nickname = team.get("nickname", "")
    if nickname:
        return f"{team['name']} {nickname}"
    return team["name"]


def get_all_teams() -> list[tuple[str, str]]:
    """Return list of (display_name, school_id) sorted alphabetically by name."""
    return sorted(
        [(v["name"], k) for k, v in TEAM_COLORS.items()],
        key=lambda x: x[0],
    )


# ── Conference mapping (fallback when live scraping fails) ─────────────────────
TEAM_CONFERENCES: dict[str, str] = {
    # ACC
    "boston-college":        "ACC",
    "clemson":               "ACC",
    "duke":                  "ACC",
    "florida-state":         "ACC",
    "georgia-tech":          "ACC",
    "louisville":            "ACC",
    "miami-fl":              "ACC",
    "north-carolina-state":  "ACC",
    "north-carolina":        "ACC",
    "notre-dame":            "ACC",
    "pittsburgh":            "ACC",
    "syracuse":              "ACC",
    "virginia":              "ACC",
    "virginia-tech":         "ACC",
    "wake-forest":           "ACC",
    "california":            "ACC",
    "stanford":              "ACC",
    "washington-state":      "ACC",
    # Big Ten
    "illinois":              "Big Ten",
    "indiana":               "Big Ten",
    "iowa":                  "Big Ten",
    "maryland":              "Big Ten",
    "michigan":              "Big Ten",
    "michigan-state":        "Big Ten",
    "minnesota":             "Big Ten",
    "nebraska":              "Big Ten",
    "northwestern":          "Big Ten",
    "ohio-state":            "Big Ten",
    "penn-state":            "Big Ten",
    "purdue":                "Big Ten",
    "rutgers":               "Big Ten",
    "wisconsin":             "Big Ten",
    "ucla":                  "Big Ten",
    "usc":                   "Big Ten",
    "washington":            "Big Ten",
    "oregon":                "Big Ten",
    "oregon-state":          "Big Ten",
    # Big 12
    "arizona":               "Big 12",
    "arizona-state":         "Big 12",
    "baylor":                "Big 12",
    "brigham-young":         "Big 12",
    "cincinnati":            "Big 12",
    "colorado":              "Big 12",
    "iowa-state":            "Big 12",
    "kansas":                "Big 12",
    "kansas-state":          "Big 12",
    "oklahoma-state":        "Big 12",
    "texas-christian":       "Big 12",
    "texas-tech":            "Big 12",
    "central-florida":       "Big 12",
    "utah":                  "Big 12",
    "west-virginia":         "Big 12",
    # SEC
    "alabama":               "SEC",
    "arkansas":              "SEC",
    "auburn":                "SEC",
    "florida":               "SEC",
    "georgia":               "SEC",
    "kentucky":              "SEC",
    "lsu":                   "SEC",
    "mississippi-state":     "SEC",
    "mississippi":           "SEC",
    "missouri":              "SEC",
    "oklahoma":              "SEC",
    "south-carolina":        "SEC",
    "tennessee":             "SEC",
    "texas":                 "SEC",
    "texas-am":              "SEC",
    "vanderbilt":            "SEC",
    # Big East
    "butler":                "Big East",
    "connecticut":           "Big East",
    "creighton":             "Big East",
    "depaul":                "Big East",
    "georgetown":            "Big East",
    "marquette":             "Big East",
    "providence":            "Big East",
    "seton-hall":            "Big East",
    "st-johns-ny":           "Big East",
    "villanova":             "Big East",
    "xavier":                "Big East",
    # Other notable programs
    "gonzaga":               "WCC",
    "saint-marys-ca":        "WCC",
    "san-diego-state":       "Mountain West",
    "nevada":                "Mountain West",
    "utah-state":            "Mountain West",
    "new-mexico":            "Mountain West",
    "memphis":               "AAC",
    "dayton":                "Atlantic 10",
    "saint-louis":           "Atlantic 10",
    "vcu":                   "Atlantic 10",
    "davidson":              "Atlantic 10",
    "loyola-il":             "Missouri Valley",
    "drake":                 "Missouri Valley",
    "wichita-state":         "AAC",
    "murray-state":          "Missouri Valley",
}


def get_team_conference(school_id: str) -> str | None:
    """Return the conference name for a school_id (fallback when scraping fails)."""
    return TEAM_CONFERENCES.get(school_id)


# ── ESPN numeric team IDs (for logo CDN) ──────────────────────────────────────
# Used by _check_logo in app.py: https://a.espncdn.com/i/teamlogos/ncaa/500/{id}.png
TEAM_ESPN_IDS: dict[str, int] = {
    # ACC
    "boston-college":        103,
    "clemson":               228,
    "duke":                  150,
    "florida-state":         52,
    "georgia-tech":          59,
    "louisville":            97,
    "miami-fl":              2390,
    "north-carolina-state":  152,
    "north-carolina":        153,
    "notre-dame":            87,
    "pittsburgh":            221,
    "syracuse":              183,
    "virginia":              258,
    "virginia-tech":         259,
    "wake-forest":           154,
    "california":            25,
    "stanford":              24,
    "washington-state":      265,
    # Big Ten
    "illinois":              356,
    "indiana":               84,
    "iowa":                  2294,
    "maryland":              120,
    "michigan":              130,
    "michigan-state":        127,
    "minnesota":             135,
    "nebraska":              158,
    "northwestern":          77,
    "ohio-state":            194,
    "penn-state":            213,
    "purdue":                2509,
    "rutgers":               164,
    "wisconsin":             275,
    "ucla":                  26,
    "usc":                   30,
    "washington":            264,
    "oregon":                2483,
    "oregon-state":          204,
    # Big 12
    "arizona":               12,
    "arizona-state":         9,
    "baylor":                239,
    "brigham-young":         252,
    "cincinnati":            2132,
    "colorado":              38,
    "iowa-state":            66,
    "kansas":                2305,
    "kansas-state":          2306,
    "oklahoma":              201,
    "oklahoma-state":        197,
    "texas-christian":       2628,
    "texas":                 251,
    "texas-tech":            2641,
    "central-florida":       2116,
    "utah":                  254,
    "west-virginia":         277,
    # SEC
    "alabama":               333,
    "arkansas":              8,
    "auburn":                2,
    "florida":               57,
    "georgia":               61,
    "kentucky":              96,
    "lsu":                   99,
    "mississippi-state":     344,
    "mississippi":           145,
    "missouri":              142,
    "south-carolina":        2579,
    "tennessee":             2633,
    "texas-am":              245,
    "vanderbilt":            238,
    # Big East
    "butler":                2086,
    "connecticut":           41,
    "creighton":             156,
    "depaul":                305,
    "georgetown":            46,
    "marquette":             269,
    "providence":            2507,
    "seton-hall":            2550,
    "st-johns-ny":           2599,
    "villanova":             222,
    "xavier":                2708,
    # Other notable programs
    "dayton":                2168,
    "davidson":              2166,
    "drake":                 2181,
    "gonzaga":               2250,
    "loyola-il":             2350,
    "memphis":               235,
    "murray-state":          93,
    "nevada":                2440,
    "new-mexico":            167,
    "saint-louis":           139,
    "saint-marys-ca":        2608,
    "san-diego-state":       21,
    "utah-state":            2393,
    "vcu":                   2670,
    "wichita-state":         2691,
}
