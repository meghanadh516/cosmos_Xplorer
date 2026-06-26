content = open("lib/screens/home_screen.dart").read()

# Fix 1: Add search_screen import
if "search_screen.dart" not in content:
    content = content.replace(
        "import 'blackhole_screen.dart';",
        "import 'blackhole_screen.dart';\nimport 'search_screen.dart';"
    )

# Fix 2: Fix BlackHolesScreen -> BlackHoleScreen
content = content.replace("BlackHolesScreen()", "BlackHoleScreen()")

# Fix 3: Remove the broken Align/search button block that was pasted wrong
import re
content = re.sub(
    r"Align\(\s*alignment: Alignment\.centerRight.*?\),\s*\),\s*\),",
    "",
    content,
    flags=re.DOTALL
)

# Fix 4: Add search icon button properly inside the build method's Column
# Add it after the tagline FadeInDown
old = """                const SizedBox(height: 16),
                Expanded(
                  child: ListView("""
new = """                const SizedBox(height: 8),
                // Search button
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  child: GestureDetector(
                    onTap: () => Navigator.push(context, _route(SearchScreen())),
                    child: Container(
                      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(14),
                        color: const Color(0xFF040F1F),
                        border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.3)),
                      ),
                      child: Row(children: [
                        Icon(Icons.search_rounded, color: Color(0xFF00AAFF), size: 20),
                        const SizedBox(width: 10),
                        Text("Search planets, galaxies, facts...",
                          style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white24, letterSpacing: 0.5)),
                      ]),
                    ),
                  ),
                ),
                const SizedBox(height: 16),
                Expanded(
                  child: ListView("""

content = content.replace(old, new)

with open("lib/screens/home_screen.dart", "w") as f:
    f.write(content)

print("Done!")
print("Has search import:", "search_screen.dart" in content)
print("Has BlackHoleScreen:", "BlackHoleScreen()" in content)
print("Has search button:", "SearchScreen()" in content)
