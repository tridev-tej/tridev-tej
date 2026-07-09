import html

ART = """\
                  ###*   +***##
               ****##%%%%%%%%&%#*++
            ==*####%&@@@&&&&%%%&####*
           =*###%%%&&&@&&%%%&&&&&%%%%%*
          +*####%%&&&&@@@&%&&@@@@&%&%%%#+
         *#%&&&%&&@@&&&@@@@@&@@@@@&&@&@&*=
        +%%&%&&@@@@%***##&@@@@@@@@@@@@@@%+
        +#&&&&&@@&*=~--~~~==~~+%%%@@@@@@%
         **&&@@@@~-***##*::~+#####&@@@@&+
           #&@@@#.-#&@@&%::=#@@&&%~&&%@#
            *#+**.:=####+..:~####*.++**
             ===+.....-:...::::....-+=
              ~~+~~~+#*+%%%%%**#+==++~
               -+===#&%*+===++%&*****
                ##**+*=~~~=====##%%&#
                 %&&&%*=+*###**%&&@%
                  #&&&&%###&%%&&@@%
                  -+#&&@@@@@@@@@%*
                *=:~=+#%&@@@&&%*+=~
              ##%+.-==++*####*++==+-
          *###%%%%~.:===++++++===+%:%###
     **##%%%%%%%%%%:..-=+++++===+*~.%%%%%%%#*
***###%%%%%%&&%&&&&+...:-~=======~-=*&&&&&&&&%%###
#%%%%%%%%%%%%&&&&&%%:.-~-::~~~~~--~=+&&&&&&&&&&&%%%%
%%%%%%%%%&&&&&&&&&&&*-:::::::-~::::-=&&&&&&&&&&&&&&&
&&&&&&%&&&&&&&&&&&%&&-.........:::::~%&&&&&&&&&&&&&&"""

C_ART = "#b1bac4"
C_KEY = "#ff7b72"
C_VAL = "#e3b341"
C_DIM = "#484f58"
C_HDR = "#c9d1d9"
C_NUM = "#79c0ff"
C_OK = "#3fb950"

INFO_COLS = 66


def kv(key, *segs):
    val_len = sum(len(t) for t, _ in segs)
    dots = INFO_COLS - 2 - len(key) - 1 - val_len - 1
    return [(". ", C_DIM), (key, C_KEY), (" " + "." * dots + " ", C_DIM)] + list(segs)


def header(name):
    dashes = INFO_COLS - len(name) - 1
    return [(name, C_HDR), (" " + "─" * dashes, C_DIM)]


INFO = [
    header("tejesh@tridev-tej"),
    kv("OS:", ("macOS, Ubuntu", C_VAL)),
    kv("Host:", ("Lumian.ai", C_VAL)),
    kv("Kernel:", ("Senior AI Engineer", C_VAL)),
    kv("IDE:", ("VS Code, Claude Code", C_VAL)),
    [],
    header("- Runtime"),
    kv("Languages.Programming:", ("Python, C++, TypeScript, SQL", C_VAL)),
    kv("Languages.Computer:", ("HTML, CSS, JSON, LaTeX, YAML", C_VAL)),
    kv("Languages.Real:", ("English, Hindi", C_VAL)),
    kv("Education:", ("IIT Kanpur, B.Tech CSE", C_VAL)),
    kv("History:", ("Simbian, Abacus.AI, TI", C_VAL)),
    kv("Hobbies.Software:", ("AI Agents, Comp. Programming", C_VAL)),
    [],
    header("- Contact"),
    kv("Email.Work:", ("tejesh@lumian.ai", C_VAL)),
    kv("LinkedIn:", ("tejeshvaish", C_VAL)),
    kv("Website:", ("tejeshvaish.com", C_VAL)),
    kv("GitHub.Personal:", ("tejeshvaish", C_VAL)),
    [],
    header("- GitHub Stats"),
    kv("Repos:", ("92", C_NUM), (" {tridev-tej + tejeshvaish}", C_VAL)),
    kv("Stars:", ("14", C_NUM), (" | Followers: ", C_VAL), ("21", C_NUM)),
    kv("Committing since:", ("Sep 2019", C_OK)),
]

art_lines = ART.split("\n")
n = max(len(art_lines), len(INFO))
CHAR_W = 7.25
LINE_H = 16.5
PAD_X, PAD_Y = 22, 24
ART_COLS = 55
width = round(PAD_X * 2 + (ART_COLS + INFO_COLS) * CHAR_W)
height = round(PAD_Y * 2 + n * LINE_H)

rows = []
for i in range(n):
    y = PAD_Y + (i + 1) * LINE_H - 4
    tspans = ""
    art = art_lines[i] if i < len(art_lines) else ""
    tspans += '<tspan fill="%s">%s</tspan>' % (C_ART, html.escape(art.ljust(ART_COLS)))
    for text, color in (INFO[i] if i < len(INFO) else []):
        tspans += '<tspan fill="%s">%s</tspan>' % (color, html.escape(text))
    rows.append(
        '<text x="%d" y="%.1f" xml:space="preserve">%s</text>' % (PAD_X, y, tspans)
    )

svg = """<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" font-family="'SFMono-Regular',Consolas,'Liberation Mono',Menlo,monospace" font-size="12.2px">
<rect width="{w}" height="{h}" rx="8" fill="#0d1117" stroke="#30363d"/>
{rows}
</svg>
""".format(w=width, h=height, rows="\n".join(rows))

out = "profile.svg"
open(out, "w").write(svg)
print("wrote", out, width, "x", height)
