import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import requests
from bs4 import BeautifulSoup
import numpy as np
import time
from team_colors import (
    get_team_colors, get_all_teams, local_search_teams,
    TEAM_COLORS, DEFAULT_PRIMARY, DEFAULT_SECONDARY,
)

st.set_page_config(
    page_title="CBB Stats Tracker",
    page_icon="🏀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Constants ──────────────────────────────────────────────────────────────────

BASE_URL = "https://www.sports-reference.com"

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Referer": "https://www.sports-reference.com/cbb/",
}

DNP_STRINGS = {
    "Did Not Play", "Inactive", "Did Not Dress",
    "Not With Team", "Suspended", "Player Suspended",
}

# Player stat groups: (key, label, is_pct, invert_colors)
# invert_colors=True means LOWER is better (tov, pf, opp_pts)
PLAYER_STAT_GROUPS = {
    "Scoring": [
        ("pts",     "Points",       False, False),
        ("fg",      "FG Made",      False, False),
        ("fga",     "FG Attempts",  False, False),
        ("fg_pct",  "FG%",          True,  False),
        ("fg3",     "3PM",          False, False),
        ("fg3a",    "3PA",          False, False),
        ("fg3_pct", "3P%",          True,  False),
        ("fg2",     "2PM",          False, False),
        ("fg2a",    "2PA",          False, False),
        ("fg2_pct", "2P%",          True,  False),
        ("efg_pct", "eFG%",         True,  False),
        ("ft",      "FT Made",      False, False),
        ("fta",     "FT Attempts",  False, False),
        ("ft_pct",  "FT%",          True,  False),
    ],
    "Rebounds": [
        ("trb",  "Total Reb",   False, False),
        ("orb",  "Off. Reb",    False, False),
        ("drb",  "Def. Reb",    False, False),
    ],
    "Playmaking & Defense": [
        ("ast",        "Assists",      False, False),
        ("stl",        "Steals",       False, False),
        ("blk",        "Blocks",       False, False),
        ("tov",        "Turnovers",    False, True),
        ("pf",         "Fouls",        False, True),
        ("mp",         "Minutes",      False, False),
        ("game_score", "Game Score",   False, False),
    ],
}

# Team stat groups — basic (schedule-only)
TEAM_STAT_GROUPS = {
    "Game Results": [
        ("pts",     "Points Scored",  False, False),
        ("opp_pts", "Points Allowed", False, True),
        ("diff",    "Point Diff",     False, False),
    ],
}

# Team stat groups — full (loaded from per-game box scores)
TEAM_FULL_STAT_GROUPS = {
    "Game Results": [
        ("pts",     "Points Scored",  False, False),
        ("opp_pts", "Points Allowed", False, True),
        ("diff",    "Point Diff",     False, False),
    ],
    "Shooting": [
        ("fg_pct",  "FG%",  True,  False),
        ("fg3_pct", "3P%",  True,  False),
        ("ft_pct",  "FT%",  True,  False),
        ("efg_pct", "eFG%", True,  False),
        ("fg3",     "3PM",  False, False),
        ("fg3a",    "3PA",  False, False),
    ],
    "Rebounds": [
        ("trb",  "Total Reb",  False, False),
        ("orb",  "Off. Reb",   False, False),
        ("drb",  "Def. Reb",   False, False),
    ],
    "Playmaking & Defense": [
        ("ast", "Assists",   False, False),
        ("stl", "Steals",    False, False),
        ("blk", "Blocks",    False, False),
        ("tov", "Turnovers", False, True),
        ("pf",  "Fouls",     False, True),
    ],
}

# Default stats checked on load
PLAYER_DEFAULT_ON    = {"pts", "fg_pct", "fg3_pct", "trb", "ast"}
TEAM_DEFAULT_ON      = {"pts", "opp_pts", "diff"}
TEAM_FULL_DEFAULT_ON = {"pts", "opp_pts", "diff", "fg_pct", "fg3_pct", "trb", "ast"}

# Summary metrics shown across the top
PLAYER_SUMMARY = [
    ("pts",     "PPG", False, False),
    ("fg_pct",  "FG%", True,  False),
    ("fg3_pct", "3P%", True,  False),
    ("ft_pct",  "FT%", True,  False),
    ("trb",     "RPG", False, False),
    ("ast",     "APG", False, False),
    ("stl",     "SPG", False, False),
    ("blk",     "BPG", False, False),
]

TEAM_SUMMARY = [
    ("pts",     "PPG",      False, False),
    ("opp_pts", "OPP PPG",  False, True),
    ("diff",    "AVG DIFF", False, False),
]

TEAM_FULL_SUMMARY = [
    ("pts",     "PPG",   False, False),
    ("opp_pts", "OPP",   False, True),
    ("diff",    "DIFF",  False, False),
    ("fg_pct",  "FG%",   True,  False),
    ("fg3_pct", "3P%",   True,  False),
    ("ft_pct",  "FT%",   True,  False),
    ("trb",     "RPG",   False, False),
    ("ast",     "APG",   False, False),
]

# Columns in the raw game log table
PLAYER_DISPLAY_COLS = {
    "game_num": "Game", "date": "Date", "opp_name_abbr": "Opp",
    "game_result": "Result", "mp": "Min", "pts": "PTS",
    "fg": "FG", "fga": "FGA", "fg_pct": "FG%",
    "fg3": "3PM", "fg3a": "3PA", "fg3_pct": "3P%",
    "fg2": "2PM", "fg2a": "2PA", "fg2_pct": "2P%",
    "efg_pct": "eFG%",
    "ft": "FT", "fta": "FTA", "ft_pct": "FT%",
    "orb": "ORB", "drb": "DRB", "trb": "TRB",
    "ast": "AST", "stl": "STL", "blk": "BLK",
    "tov": "TOV", "pf": "PF", "game_score": "GmSc",
}

TEAM_DISPLAY_COLS = {
    "game_num": "Game", "date_game": "Date", "opp_name": "Opponent",
    "game_location": "H/A", "game_result": "Result",
    "pts": "Tm Pts", "opp_pts": "Opp Pts", "diff": "Diff",
}


# ── Theme & color helpers ──────────────────────────────────────────────────────

def _hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def _is_too_light(hex_color: str, threshold: int = 200) -> bool:
    """Return True if color is very light (e.g., white secondary colors)."""
    r, g, b = _hex_to_rgb(hex_color)
    return (r + g + b) / 3 > threshold


def _bar_colors(values, avg: float, primary: str, invert: bool) -> list[str]:
    """Return per-bar colors: full primary if 'better', 40%-opacity if 'worse'."""
    r, g, b = _hex_to_rgb(primary)
    faint = f"rgba({r},{g},{b},0.35)"
    result = []
    for v in values:
        better = (v <= avg) if invert else (v >= avg)
        result.append(primary if better else faint)
    return result


def _rolling_line_color(secondary: str) -> str:
    """Return a usable rolling-average line color (fallback if secondary is white/black)."""
    if _is_too_light(secondary):
        return "#2980b9"
    r, g, b = _hex_to_rgb(secondary)
    if r + g + b < 60:    # near-black
        return "#2980b9"
    return secondary


def _compute_trend(series: pd.Series, n_recent: int = 5):
    """Return (season_avg, recent_avg, delta) for the last-N vs full season.
    Returns (None, None, None) if insufficient data."""
    clean = series.dropna()
    if len(clean) < 2:
        return None, None, None
    season_avg = float(clean.mean())
    recent_avg = float(clean.tail(n_recent).mean())
    return season_avg, recent_avg, recent_avg - season_avg


def _trend_emoji(delta: float, avg: float, is_pct: bool, invert: bool) -> str:
    """🔥 if trending meaningfully better, ⚠️ if meaningfully worse, '' if flat."""
    if delta is None or avg is None:
        return ""
    # Threshold: 1.5pp for percentages, 5% relative for counting stats
    threshold = 0.015 if is_pct else (abs(avg) * 0.05 if avg != 0 else 0.5)
    if abs(delta) < threshold:
        return ""
    going_up = delta > 0
    good = going_up if not invert else not going_up
    return "🔥" if good else "⚠️"


def apply_theme(primary: str, secondary: str):
    """Inject CSS that colors metric cards, sidebar, and headings with team palette."""
    r, g, b = _hex_to_rgb(primary)
    st.markdown(
        f"""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

        /* ── Global typography ── */
        html, body, [class*="css"], .stApp {{
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif !important;
        }}

        /* ── Main container padding ── */
        .main .block-container {{
            padding-top: 1.8rem !important;
            padding-bottom: 2rem !important;
        }}

        /* ── Metric cards ── */
        div[data-testid="metric-container"] {{
            border-left: 4px solid {primary};
            background: linear-gradient(135deg, rgba({r},{g},{b},0.07) 0%, rgba({r},{g},{b},0.02) 100%);
            border-radius: 0 12px 12px 0;
            padding: 14px 18px !important;
            margin-bottom: 6px;
            box-shadow: 0 1px 4px rgba(0,0,0,0.06);
            transition: transform 0.15s ease, box-shadow 0.15s ease;
        }}
        div[data-testid="metric-container"]:hover {{
            transform: translateX(3px);
            box-shadow: 0 2px 8px rgba({r},{g},{b},0.15);
        }}
        /* Metric label — small caps style */
        div[data-testid="metric-container"] label {{
            font-size: 0.68rem !important;
            font-weight: 700 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.08em !important;
            color: #6b7280 !important;
        }}
        /* Metric value */
        div[data-testid="stMetricValue"] > div {{
            font-size: 1.55rem !important;
            font-weight: 700 !important;
            font-variant-numeric: tabular-nums !important;
            letter-spacing: -0.02em !important;
            color: #111827 !important;
        }}
        /* Metric delta */
        div[data-testid="stMetricDelta"] svg {{ display: none; }}
        div[data-testid="stMetricDelta"] > div {{
            font-size: 0.78rem !important;
            font-weight: 600 !important;
        }}

        /* ── Sidebar ── */
        section[data-testid="stSidebar"] > div:first-child {{
            border-right: 3px solid rgba({r},{g},{b},0.15);
            background: #f9fafb;
        }}
        section[data-testid="stSidebar"] h1 {{
            font-size: 1.2rem !important;
            font-weight: 800 !important;
            letter-spacing: -0.02em !important;
        }}
        section[data-testid="stSidebar"] .stRadio label {{
            font-weight: 600 !important;
            font-size: 0.88rem !important;
        }}
        section[data-testid="stSidebar"] .stCheckbox label {{
            font-size: 0.82rem !important;
            color: #374151 !important;
        }}
        /* Sidebar text input */
        section[data-testid="stSidebar"] input {{
            border-radius: 8px !important;
            font-size: 0.88rem !important;
            border-color: rgba({r},{g},{b},0.25) !important;
        }}
        section[data-testid="stSidebar"] input:focus {{
            border-color: {primary} !important;
            box-shadow: 0 0 0 3px rgba({r},{g},{b},0.12) !important;
        }}

        /* ── Headings ── */
        h1 {{
            font-weight: 800 !important;
            letter-spacing: -0.03em !important;
            color: #111827 !important;
            line-height: 1.15 !important;
        }}
        h2, h3 {{
            color: {primary} !important;
            font-weight: 700 !important;
            letter-spacing: -0.01em !important;
        }}

        /* ── Dividers ── */
        hr {{
            border: none !important;
            border-top: 1px solid rgba({r},{g},{b},0.15) !important;
            margin: 1.4rem 0 !important;
        }}

        /* ── Caption ── */
        [data-testid="stCaptionContainer"] p {{
            color: #6b7280;
            font-size: 0.76rem;
            font-weight: 500;
            letter-spacing: 0.01em;
        }}

        /* ── Plotly chart wrapper ── */
        div[data-testid="stPlotlyChart"] > div {{
            border-radius: 12px !important;
            box-shadow: 0 1px 4px rgba(0,0,0,0.06), 0 0 0 1px rgba(0,0,0,0.04) !important;
            overflow: hidden;
            background: white !important;
        }}

        /* ── Expanders ── */
        details summary p {{
            font-weight: 600 !important;
            font-size: 0.85rem !important;
            color: #374151 !important;
        }}

        /* ── Dataframe ── */
        div[data-testid="stDataFrame"] {{
            border-radius: 10px !important;
            overflow: hidden;
            box-shadow: 0 1px 4px rgba(0,0,0,0.06) !important;
        }}

        /* ── Info/warning ── */
        div[data-testid="stAlert"] {{
            border-radius: 10px !important;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


# ── HTTP session ───────────────────────────────────────────────────────────────

def _make_session() -> requests.Session:
    """Return a Session warmed up with sports-reference cookies."""
    s = requests.Session()
    s.headers.update(HEADERS)
    try:
        s.get(f"{BASE_URL}/cbb/", timeout=10)
    except Exception:
        pass
    return s


# ── Player data ────────────────────────────────────────────────────────────────

@st.cache_data(ttl=3600, show_spinner=False)
def search_players(query: str) -> list:
    session = _make_session()
    resp = session.get(
        f"{BASE_URL}/cbb/search/search.fcgi",
        params={"search": query},
        timeout=10,
    )
    soup = BeautifulSoup(resp.text, "lxml")

    if "/cbb/players/" in resp.url and "search.fcgi" not in resp.url:
        h1 = soup.find("h1")
        name = h1.get_text(" ", strip=True) if h1 else query
        pid = resp.url.split("/cbb/players/")[-1].rstrip("/").replace(".html", "").split("/")[0]
        return [{"name": name, "id": pid, "info": ""}]

    players = []
    div = soup.find("div", id="players")
    if div:
        for p in div.find_all("p"):
            a = p.find("a", href=lambda h: h and "/cbb/players/" in h)
            if not a:
                continue
            pid = a["href"].split("/cbb/players/")[-1].rstrip("/").replace(".html", "")
            info = p.get_text(" ", strip=True).replace(a.get_text(strip=True), "").strip(" ()")
            players.append({"name": a.get_text(strip=True), "id": pid, "info": info})
    return players


@st.cache_data(ttl=3600, show_spinner=False)
def get_player_seasons(player_id: str) -> list:
    session = _make_session()
    resp = session.get(f"{BASE_URL}/cbb/players/{player_id}.html", timeout=10)
    soup = BeautifulSoup(resp.text, "lxml")

    years = set()
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if f"/cbb/players/{player_id}/gamelog/" in href:
            yr = href.split("/gamelog/")[-1].rstrip("/")
            if yr.isdigit():
                years.add(int(yr))
    return sorted(years, reverse=True)


@st.cache_data(ttl=3600, show_spinner=False)
def get_player_school_id(player_id: str) -> str | None:
    """Return the sports-reference school ID for a player by reading their bio section."""
    session = _make_session()
    resp = session.get(f"{BASE_URL}/cbb/players/{player_id}.html", timeout=10)
    soup = BeautifulSoup(resp.text, "lxml")
    info_div = soup.find("div", id="info")
    if info_div:
        for a in info_div.find_all("a", href=True):
            href = a["href"]
            if "/cbb/schools/" in href:
                parts = href.rstrip("/").split("/")
                # /cbb/schools/{sid}/{gender}/
                if len(parts) >= 4:
                    return parts[3]
    return None


@st.cache_data(ttl=3600, show_spinner=False)
def get_player_game_log(player_id: str, year: int):
    session = _make_session()
    resp = session.get(
        f"{BASE_URL}/cbb/players/{player_id}/gamelog/{year}/",
        timeout=10,
    )
    soup = BeautifulSoup(resp.text, "lxml")

    table = soup.find("table", id="player_game_log")
    if not table:
        return None

    rows = []
    for tr in table.select("tbody tr"):
        if "thead" in tr.get("class", []):
            continue
        cells = {
            td["data-stat"]: td.get_text(strip=True)
            for td in tr.find_all(["td", "th"])
            if td.get("data-stat")
        }
        if not cells:
            continue
        pts = cells.get("pts", "")
        if not pts or pts in DNP_STRINGS:
            continue
        if cells.get("reason", "") in DNP_STRINGS:
            continue
        rows.append(cells)

    if not rows:
        return None

    df = pd.DataFrame(rows)

    count_cols = ["fg", "fga", "fg2", "fg2a", "fg3", "fg3a", "ft", "fta",
                  "orb", "drb", "trb", "ast", "stl", "blk", "tov", "pf", "pts", "game_score"]
    pct_cols   = ["fg_pct", "fg2_pct", "fg3_pct", "ft_pct", "efg_pct"]

    for col in count_cols + pct_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    if "mp" in df.columns:
        def _parse_mp(v):
            s = str(v).strip()
            if ":" in s:
                try:
                    m, sec = s.split(":")
                    return float(m) + float(sec) / 60
                except ValueError:
                    return np.nan
            return pd.to_numeric(s, errors="coerce")
        df["mp"] = df["mp"].apply(_parse_mp)

    df = df.reset_index(drop=True)
    df["game_num"] = df.index + 1

    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    return df


# ── Team data ──────────────────────────────────────────────────────────────────

@st.cache_data(ttl=3600, show_spinner=False)
def search_teams(query: str) -> list:
    """
    Return list of {name, id, info} dicts for matching schools.

    Strategy:
      1. Local alias/fuzzy search (instant, handles UNC/UVA/nicknames)
      2. Fall back to sports-reference search (catches programs not in our color dict)
    Results are deduplicated by school ID.
    """
    # ── Step 1: local search ──────────────────────────────────────────────────
    local = local_search_teams(query)
    local_ids = {r["id"] for r in local}

    # ── Step 2: sports-reference fallback for unknown programs ────────────────
    sr_teams = []
    try:
        session = _make_session()
        resp = session.get(
            f"{BASE_URL}/cbb/search/search.fcgi",
            params={"search": query},
            timeout=10,
        )
        soup = BeautifulSoup(resp.text, "lxml")

        # Direct redirect to a single school page
        if "/cbb/schools/" in resp.url and "search.fcgi" not in resp.url:
            h1 = soup.find("h1")
            name = h1.get_text(" ", strip=True) if h1 else query
            sid  = resp.url.split("/cbb/schools/")[-1].rstrip("/").split("/")[0]
            if sid not in local_ids:
                sr_teams.append({"name": name, "id": sid, "info": ""})
        else:
            div = soup.find("div", id="schools")
            if div:
                seen = set()
                for a in div.find_all("a", href=True):
                    href = a["href"]
                    if "/cbb/schools/" not in href:
                        continue
                    parts = href.rstrip("/").split("/")
                    if len(parts) < 5:
                        continue
                    sid, gender = parts[3], parts[4]
                    if gender not in ("men", "women"):
                        continue
                    key = (sid, gender)
                    if key in seen or sid in local_ids:
                        continue
                    seen.add(key)
                    label = a.get_text(strip=True)
                    if gender == "women":
                        label += " (W)"
                    sr_teams.append({"name": label, "id": sid, "info": gender})
    except Exception:
        pass  # local results still returned even if SR is unreachable

    return local + sr_teams


@st.cache_data(ttl=3600, show_spinner=False)
def get_team_seasons(team_id: str) -> list:
    """Return list of season-end years available for this team, newest first.

    The school index page (/cbb/schools/{id}/men/) contains a table whose rows
    link to individual season pages at /cbb/schools/{id}/men/{YEAR}.html.
    We extract the year from those links.
    """
    session = _make_session()
    resp = session.get(f"{BASE_URL}/cbb/schools/{team_id}/men/", timeout=10)
    soup = BeautifulSoup(resp.text, "lxml")

    years = set()
    pattern = f"/cbb/schools/{team_id}/men/"
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith(pattern):
            # href looks like /cbb/schools/duke/men/2024.html
            tail = href[len(pattern):]          # "2024.html"
            yr_str = tail.replace(".html", "").split("-")[0]
            if yr_str.isdigit() and 1980 <= int(yr_str) <= 2030:
                years.add(int(yr_str))

    return sorted(years, reverse=True)


@st.cache_data(ttl=3600, show_spinner=False)
def get_team_schedule(team_id: str, year: int):
    """Fetch team schedule and return per-game DataFrame with pts/opp_pts/diff."""
    session = _make_session()
    url = f"{BASE_URL}/cbb/schools/{team_id}/men/{year}-schedule.html"
    resp = session.get(url, timeout=10)
    soup = BeautifulSoup(resp.text, "lxml")

    table = soup.find("table", id="schedule")
    if not table:
        return None

    rows = []
    for tr in table.select("tbody tr"):
        if "thead" in tr.get("class", []):
            continue
        cells = {
            td["data-stat"]: td.get_text(strip=True)
            for td in tr.find_all(["td", "th"])
            if td.get("data-stat")
        }
        if not cells:
            continue
        # Skip rows without a real date (section headers, future games)
        date_val = cells.get("date_game", "")
        if not date_val or date_val in ("Date", ""):
            continue
        pts_val = cells.get("pts", "")
        if not pts_val:
            continue  # game not yet played
        rows.append(cells)

    if not rows:
        return None

    df = pd.DataFrame(rows)

    for col in ["pts", "opp_pts", "wins", "losses"]:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Compute point differential
    if "pts" in df.columns and "opp_pts" in df.columns:
        df["diff"] = df["pts"] - df["opp_pts"]

    if "date_game" in df.columns:
        df["date_game"] = pd.to_datetime(df["date_game"], errors="coerce")

    df = df.dropna(subset=["pts", "opp_pts"]).reset_index(drop=True)
    df["game_num"] = df.index + 1

    return df


@st.cache_data(ttl=86400, show_spinner=False)
def get_team_game_log(team_id: str, year: int):
    """Fetch per-game team shooting stats from individual box score pages.

    Scrapes N+1 pages (schedule + one per game played).
    Results are cached for 24 hrs since historical data doesn't change.
    Returns a DataFrame with full team box score stats merged with schedule info.
    """
    session = _make_session()

    # ── Step 1: pull schedule to get box score URLs ───────────────────────────
    url = f"{BASE_URL}/cbb/schools/{team_id}/men/{year}-schedule.html"
    try:
        resp = session.get(url, timeout=10)
    except Exception:
        return None
    soup = BeautifulSoup(resp.text, "lxml")
    table = soup.find("table", id="schedule")
    if not table:
        return None

    games = []
    for tr in table.select("tbody tr"):
        if "thead" in tr.get("class", []):
            continue
        date_td = tr.find("td", {"data-stat": "date_game"})
        if not date_td:
            continue
        pts_td = tr.find("td", {"data-stat": "pts"})
        if not pts_td or not pts_td.get_text(strip=True):
            continue  # not yet played

        a = date_td.find("a")
        if not a:
            continue

        def _cell(stat):
            td = tr.find("td", {"data-stat": stat})
            return td.get_text(strip=True) if td else ""

        games.append({
            "box_url":      a["href"],
            "date_game":    _cell("date_game"),
            "opp_name":     _cell("opp_name"),
            "game_location": _cell("game_location"),
            "game_result":  _cell("game_result"),
            "pts":          _cell("pts"),
            "opp_pts":      _cell("opp_pts"),
        })

    if not games:
        return None

    # ── Step 2: fetch each box score ──────────────────────────────────────────
    table_id = f"box-score-basic-{team_id}"
    rows = []
    for game in games:
        time.sleep(2.5)
        try:
            box_resp = session.get(f"{BASE_URL}{game['box_url']}", timeout=10)
            box_soup = BeautifulSoup(box_resp.text, "lxml")
            box_table = box_soup.find("table", id=table_id)
            if not box_table:
                continue
            tfoot = box_table.find("tfoot")
            if not tfoot:
                continue
            row = tfoot.find("tr")
            if not row:
                continue
            cells = {
                td.get("data-stat"): td.get_text(strip=True)
                for td in row.find_all(["td", "th"])
                if td.get("data-stat") and td.get("data-stat") != "player"
            }
            cells.update(game)
            rows.append(cells)
        except Exception:
            continue

    if not rows:
        return None

    df = pd.DataFrame(rows)

    count_cols = ["fg", "fga", "fg2", "fg2a", "fg3", "fg3a", "ft", "fta",
                  "orb", "drb", "trb", "ast", "stl", "blk", "tov", "pf", "pts", "opp_pts"]
    pct_cols   = ["fg_pct", "fg2_pct", "fg3_pct", "ft_pct"]

    for col in count_cols + pct_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")

    # Compute derived stats
    if "fg" in df.columns and "fg3" in df.columns and "fga" in df.columns:
        df["efg_pct"] = (df["fg"] + 0.5 * df["fg3"]) / df["fga"]
    if "pts" in df.columns and "opp_pts" in df.columns:
        df["diff"] = df["pts"] - df["opp_pts"]
    if "date_game" in df.columns:
        df["date_game"] = pd.to_datetime(df["date_game"], errors="coerce")

    df = df.dropna(subset=["pts"]).reset_index(drop=True)
    df["game_num"] = df.index + 1
    return df


# ── Chart builder (shared) ─────────────────────────────────────────────────────

def make_chart(
    df: pd.DataFrame,
    key: str,
    label: str,
    is_pct: bool,
    invert: bool,
    primary: str,
    secondary: str,
    date_col: str = "date",
    opp_col: str = "opp_name_abbr",
) -> go.Figure | None:
    """
    Bar chart per game + 5-game rolling avg + season avg dashed line.

    Bar color:  team primary  when the game value is "better" than avg
                team primary @ 35% opacity when "worse"
    invert=True means lower values are better (tov, opp_pts, pf).
    """
    if key not in df.columns:
        return None

    extra = [c for c in [date_col, opp_col, "game_result"] if c in df.columns]
    data = df[["game_num", key] + extra].dropna(subset=[key]).copy()
    if data.empty:
        return None

    avg     = data[key].mean()
    rolling = data[key].rolling(5, min_periods=1).mean()
    colors  = _bar_colors(data[key], avg, primary, invert)
    line_color = _rolling_line_color(secondary)

    # Trend emoji for chart title
    _, _, trend_delta = _compute_trend(data[key])
    trend_icon = _trend_emoji(trend_delta, avg, is_pct, invert) if trend_delta is not None else ""
    chart_title = f"{label}  {trend_icon}" if trend_icon else label

    fmt     = ".1%" if is_pct else ".1f"
    avg_str = f"{avg:.1%}" if is_pct else f"{avg:.1f}"

    # Hover text
    hover = []
    for _, row in data.iterrows():
        parts = []
        if date_col in data.columns and pd.notna(row.get(date_col)):
            parts.append(row[date_col].strftime("%b %d"))
        if opp_col in data.columns and row.get(opp_col):
            parts.append(f"vs {row[opp_col]}")
        if "game_result" in data.columns and row.get("game_result"):
            parts.append(row["game_result"])
        parts.append(f"<b>{label}: {row[key]:{fmt}}</b>")
        hover.append("<br>".join(parts))

    fig = go.Figure()

    # Per-game bars
    fig.add_trace(go.Bar(
        x=data["game_num"],
        y=data[key],
        marker_color=colors,
        opacity=0.85,
        name="Per Game",
        hovertext=hover,
        hovertemplate="%{hovertext}<extra></extra>",
    ))

    # 5-game rolling average
    fig.add_trace(go.Scatter(
        x=data["game_num"],
        y=rolling,
        mode="lines",
        line=dict(color=line_color, width=2.5, dash="solid"),
        name="5-Game Avg",
        hovertemplate=f"Game %{{x}}<br>5-Game Avg: %{{y:{fmt}}}<extra></extra>",
    ))

    # Season average reference
    fig.add_hline(
        y=avg,
        line_dash="dot",
        line_color="#f39c12",
        line_width=1.8,
        annotation_text=f"Season avg  {avg_str}",
        annotation_position="top right",
        annotation_font=dict(color="#f39c12", size=11),
    )

    n = len(data)
    fig.update_layout(
        title=dict(
            text=chart_title,
            font=dict(size=13, color="#111827", family="Inter, sans-serif"),
            x=0, xanchor="left",
            pad=dict(b=10),
        ),
        height=290,
        margin=dict(l=10, r=20, t=44, b=56),
        plot_bgcolor="#ffffff",
        paper_bgcolor="#ffffff",
        xaxis=dict(
            title=dict(text="Game", font=dict(size=10, color="#9ca3af")),
            showgrid=False,
            tick0=1,
            dtick=max(1, round(n / 10)),
            tickfont=dict(size=10, color="#6b7280"),
            linecolor="#e5e7eb",
            linewidth=1,
            showline=True,
        ),
        yaxis=dict(
            tickformat=".0%" if is_pct else None,
            gridcolor="#f3f4f6",
            gridwidth=1,
            tickfont=dict(size=10, color="#6b7280"),
            zeroline=False,
        ),
        legend=dict(
            orientation="h",
            y=-0.22,
            x=0,
            xanchor="left",
            font=dict(size=10, color="#6b7280"),
            bgcolor="rgba(0,0,0,0)",
            itemsizing="constant",
            traceorder="normal",
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="white",
            font_size=12,
            font_family="Inter, sans-serif",
            bordercolor="#e5e7eb",
        ),
    )
    return fig


# ── Shared UI helpers ──────────────────────────────────────────────────────────

def _render_summary(df, stat_list, primary):
    """Row of st.metric tiles with last-5 trend delta."""
    cols = st.columns(len(stat_list))
    for col, stat in zip(cols, stat_list):
        key, lbl, is_pct = stat[0], stat[1], stat[2]
        invert = stat[3] if len(stat) > 3 else False
        if key not in df.columns or not df[key].notna().any():
            continue
        series = df[key].dropna()
        val = series.mean()
        val_str = f"{val:.1%}" if is_pct else f"{val:.1f}"

        delta_str = None
        delta_color = "normal"
        if len(series) >= 3:
            _, _, delta = _compute_trend(series)
            if delta is not None and abs(delta) > 1e-9:
                delta_str = f"{delta:+.1%} L5" if is_pct else f"{delta:+.1f} L5"
                delta_color = "inverse" if invert else "normal"

        col.metric(lbl, val_str, delta=delta_str, delta_color=delta_color)


def _render_charts(df, stat_groups, defaults, primary, secondary,
                   date_col="date", opp_col="opp_name_abbr"):
    """Sidebar checkboxes + 2-column chart grid."""
    selected = {}
    for group_name, stats in stat_groups.items():
        with st.expander(group_name, expanded=(group_name in ("Scoring", "Game Results"))):
            for key, label, _, _ in stats:
                selected[key] = st.checkbox(label, value=(key in defaults), key=f"chk_{key}")

    return selected  # caller handles rendering


def _draw_charts(df, stat_groups, selected, primary, secondary,
                 date_col="date", opp_col="opp_name_abbr"):
    active = [
        (key, label, is_pct, inv)
        for group in stat_groups.values()
        for key, label, is_pct, inv in group
        if selected.get(key)
    ]
    if not active:
        st.info("Select at least one stat in the sidebar.")
        return

    for i in range(0, len(active), 2):
        pair = active[i: i + 2]
        cols = st.columns(len(pair))
        for col, (key, label, is_pct, inv) in zip(cols, pair):
            fig = make_chart(df, key, label, is_pct, inv, primary, secondary,
                             date_col=date_col, opp_col=opp_col)
            if fig:
                col.plotly_chart(fig, use_container_width=True)
            else:
                col.caption(f"No data for {label}")


# ── Main app ───────────────────────────────────────────────────────────────────

def main():
    # ── Sidebar ───────────────────────────────────────────────────────────────
    with st.sidebar:
        st.title("🏀 CBB Stats")

        mode = st.radio("View", ["Player", "Team"], horizontal=True)
        st.divider()

        # ── PLAYER MODE CONTROLS ──────────────────────────────────────────────
        if mode == "Player":
            st.subheader("Find a Player")
            query = st.text_input("Name", placeholder="e.g. Zach Edey", key="player_query")

            player_id = None
            player_label = ""
            selected_year = None
            school_id = None   # auto-populated by get_player_school_id() below

            if query and len(query) >= 2:
                with st.spinner("Searching…"):
                    results = search_players(query)
                if not results:
                    st.warning("No players found.")
                else:
                    display_map = {
                        (r["name"] + (f"  ({r['info']})" if r["info"] else "")): r["id"]
                        for r in results
                    }
                    chosen = st.selectbox("Select player", list(display_map.keys()))
                    player_id    = display_map[chosen]
                    player_label = chosen.split("  (")[0]

            if player_id:
                with st.spinner("Loading seasons…"):
                    seasons = get_player_seasons(player_id)
                    school_id = get_player_school_id(player_id)
                if not seasons:
                    st.warning("No seasons found.")
                    player_id = None
                else:
                    selected_year = st.selectbox(
                        "Season",
                        seasons,
                        format_func=lambda y: f"{y - 1}–{str(y)[-2:]}",
                    )

            st.divider()
            st.subheader("Stats to Display")
            selected_stats = {}
            for group_name, stats in PLAYER_STAT_GROUPS.items():
                with st.expander(group_name, expanded=(group_name == "Scoring")):
                    for key, label, _, _ in stats:
                        selected_stats[key] = st.checkbox(
                            label, value=(key in PLAYER_DEFAULT_ON), key=f"chk_{key}"
                        )

        # ── TEAM MODE CONTROLS ────────────────────────────────────────────────
        else:
            st.subheader("Find a Team")
            query = st.text_input("Team name", placeholder="e.g. Virginia, LIU", key="team_query")

            team_id = None
            team_label = ""
            selected_year = None

            if query and len(query) >= 2:
                with st.spinner("Searching…"):
                    results = search_teams(query)
                if not results:
                    st.warning("No teams found.")
                else:
                    display_map = {
                        (r["name"] + (f"  ({r['info']})" if r["info"] else "")): r["id"]
                        for r in results
                    }
                    chosen = st.selectbox("Select team", list(display_map.keys()))
                    team_id    = display_map[chosen]
                    team_label = chosen.split("  (")[0]

            if team_id:
                with st.spinner("Loading seasons…"):
                    seasons = get_team_seasons(team_id)
                if not seasons:
                    st.warning("No seasons found.")
                    team_id = None
                else:
                    selected_year = st.selectbox(
                        "Season",
                        seasons,
                        format_func=lambda y: f"{y - 1}–{str(y)[-2:]}",
                    )
                school_id = team_id
            else:
                school_id = "__default__"

            st.divider()

            # Full stats toggle — persisted in session state
            full_key = f"team_full_{team_id}_{selected_year}" if (team_id and selected_year) else None
            use_full = st.session_state.get("use_full_team_stats", False)

            if team_id and selected_year:
                use_full = st.toggle(
                    "Full team stats",
                    value=use_full,
                    key="use_full_team_stats",
                    help="Loads per-game shooting, rebounding & more from individual box scores. First load takes ~1 min; cached after.",
                )

            st.subheader("Stats to Display")
            stat_groups_to_use = TEAM_FULL_STAT_GROUPS if use_full else TEAM_STAT_GROUPS
            defaults_to_use    = TEAM_FULL_DEFAULT_ON   if use_full else TEAM_DEFAULT_ON
            selected_stats = {}
            for group_name, stats in stat_groups_to_use.items():
                with st.expander(group_name, expanded=(group_name in ("Game Results", "Shooting"))):
                    for key, label, _, _ in stats:
                        selected_stats[key] = st.checkbox(
                            label, value=(key in defaults_to_use), key=f"chk_{key}"
                        )

    # ── Resolve team colors (auto-detected; no manual picker) ─────────────────
    # Player mode: school_id comes from get_player_school_id()
    # Team mode:   school_id == team_id set in the sidebar block above
    resolved_school = school_id if (school_id and school_id != "__default__") else None
    if resolved_school:
        primary, secondary = get_team_colors(resolved_school)
    else:
        primary, secondary = DEFAULT_PRIMARY, DEFAULT_SECONDARY

    apply_theme(primary, secondary)

    # ── PLAYER MAIN CONTENT ────────────────────────────────────────────────────
    if mode == "Player":
        if not player_id or not selected_year:
            st.title("College Basketball Stats")
            st.markdown(
                f"""
                Search for any college basketball **player** in the sidebar and pick a season.

                **Each chart shows:**
                - Bars colored by team palette — full color = **better** than season avg, faded = below
                - **Blue/secondary line** — 5-game rolling trend
                - **Orange dotted line** — season average reference

                **Data source:** [Sports-Reference.com / CBB](https://www.sports-reference.com/cbb)

                ---
                **Sites worth exploring for design inspiration:**
                - [EvanMiya CBB Analytics](https://evanmiya.com) — college hoops advanced metrics
                - [Cleaning the Glass](https://cleaningtheglass.com) — efficiency-focused basketball analytics
                - [Stathead](https://stathead.com/basketball) — sports-reference's analytics layer
                - [Hoopsalytics](https://hoopsalytics.com) — timeline & goal-based basketball viz
                - [CourtSketch / NBAVisuals](https://nbavisuals.com) — modern shot chart + player viz
                """
            )
            return

        with st.spinner(f"Loading {player_label} {selected_year - 1}–{str(selected_year)[-2:]}…"):
            df = get_player_game_log(player_id, selected_year)

        if df is None or df.empty:
            st.error("No game log data found for this player and season.")
            return

        season_str = f"{selected_year - 1}–{str(selected_year)[-2:]}"
        r2, g2, b2 = _hex_to_rgb(primary)
        st.markdown(
            f"""<div style="margin-bottom:0.2rem">
            <h1 style="margin-bottom:6px;font-size:2.1rem">{player_label}</h1>
            <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:4px">
              <span style="background:rgba({r2},{g2},{b2},0.12);color:{primary};
                           padding:4px 12px;border-radius:20px;font-size:0.8rem;
                           font-weight:700;letter-spacing:0.03em">{season_str}</span>
              <span style="color:#6b7280;font-size:0.88rem;font-weight:500">
                {len(df)} games played</span>
            </div></div>""",
            unsafe_allow_html=True,
        )

        _render_summary(df, PLAYER_SUMMARY, primary)
        st.divider()

        _draw_charts(df, PLAYER_STAT_GROUPS, selected_stats, primary, secondary,
                     date_col="date", opp_col="opp_name_abbr")

        with st.expander("View raw game log"):
            available = {k: v for k, v in PLAYER_DISPLAY_COLS.items() if k in df.columns}
            st.dataframe(
                df[list(available.keys())].rename(columns=available),
                use_container_width=True,
                hide_index=True,
            )

    # ── TEAM MAIN CONTENT ──────────────────────────────────────────────────────
    else:
        if not team_id or not selected_year:
            st.title("College Basketball Stats")
            st.markdown(
                """
                Search for any college basketball **team** in the sidebar and pick a season.

                The dashboard shows **game-by-game scoring results** — points scored, points allowed,
                and point differential — plotted as a time series with season average and 5-game rolling trend.
                """
            )
            return

        use_full = st.session_state.get("use_full_team_stats", False)

        if use_full:
            n_games_hint = ""
            with st.spinner(
                f"Loading full stats for {team_label} {selected_year - 1}–{str(selected_year)[-2:]}… "
                f"(fetching box scores — first load ~1–2 min, cached after)"
            ):
                df = get_team_game_log(team_id, selected_year)
            date_col, opp_col = "date_game", "opp_name"
            stat_groups_used  = TEAM_FULL_STAT_GROUPS
            summary_used      = TEAM_FULL_SUMMARY
        else:
            with st.spinner(f"Loading {team_label} {selected_year - 1}–{str(selected_year)[-2:]} schedule…"):
                df = get_team_schedule(team_id, selected_year)
            date_col, opp_col = "date_game", "opp_name"
            stat_groups_used  = TEAM_STAT_GROUPS
            summary_used      = TEAM_SUMMARY

        if df is None or df.empty:
            st.error("No schedule data found for this team and season.")
            return

        season_str = f"{selected_year - 1}–{str(selected_year)[-2:]}"
        wins   = int((df["diff"] > 0).sum()) if "diff" in df.columns else "—"
        losses = int((df["diff"] < 0).sum()) if "diff" in df.columns else "—"
        r2, g2, b2 = _hex_to_rgb(primary)
        st.markdown(
            f"""<div style="margin-bottom:0.2rem">
            <h1 style="margin-bottom:6px;font-size:2.1rem">{team_label}</h1>
            <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:4px">
              <span style="background:rgba({r2},{g2},{b2},0.12);color:{primary};
                           padding:4px 12px;border-radius:20px;font-size:0.8rem;
                           font-weight:700;letter-spacing:0.03em">{season_str}</span>
              <span style="background:#f0fdf4;color:#16a34a;padding:4px 12px;
                           border-radius:20px;font-size:0.8rem;font-weight:700">{wins}W</span>
              <span style="background:#fef2f2;color:#dc2626;padding:4px 12px;
                           border-radius:20px;font-size:0.8rem;font-weight:700">{losses}L</span>
              <span style="color:#6b7280;font-size:0.88rem;font-weight:500">
                {len(df)} games</span>
            </div></div>""",
            unsafe_allow_html=True,
        )

        _render_summary(df, summary_used, primary)
        st.divider()

        _draw_charts(df, stat_groups_used, selected_stats, primary, secondary,
                     date_col=date_col, opp_col=opp_col)

        with st.expander("View full schedule"):
            available = {k: v for k, v in TEAM_DISPLAY_COLS.items() if k in df.columns}
            st.dataframe(
                df[list(available.keys())].rename(columns=available),
                use_container_width=True,
                hide_index=True,
            )


if __name__ == "__main__":
    main()
