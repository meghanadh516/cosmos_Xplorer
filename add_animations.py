import os

# Add animations to planets_screen.dart
planets = open("lib/screens/planets_screen.dart").read()

# Add animate_do import if not there
if "animate_do" not in planets:
    planets = planets.replace(
        "import 'package:google_fonts/google_fonts.dart';",
        "import 'package:google_fonts/google_fonts.dart';\nimport 'package:animate_do/animate_do.dart';"
    )

# Animate planet cards with FadeInLeft + delay
old_card = "        return GestureDetector(\n      onTap: onTap,"
# won't work - use itemBuilder approach
planets = planets.replace(
    "itemBuilder: (ctx, i) => _PlanetCard(planet: planetList[i], onTap: () => _showInfo(context, planetList[i])),",
    """itemBuilder: (ctx, i) => FadeInLeft(
                      delay: Duration(milliseconds: 100 + i * 80),
                      child: FadeInUp(
                        delay: Duration(milliseconds: 100 + i * 80),
                        child: _PlanetCard(planet: planetList[i], onTap: () => _showInfo(context, planetList[i])),
                      ),
                    ),"""
)
open("lib/screens/planets_screen.dart", "w").write(planets)
print("planets_screen: animations added")

# Add animations to galaxy_screen.dart
galaxy = open("lib/screens/galaxy_screen.dart").read()
if "animate_do" not in galaxy:
    galaxy = galaxy.replace(
        "import 'package:google_fonts/google_fonts.dart';",
        "import 'package:google_fonts/google_fonts.dart';\nimport 'package:animate_do/animate_do.dart';"
    )
# Wrap hero banner
galaxy = galaxy.replace(
    "                ClipRRect(\n                  borderRadius: BorderRadius.circular(20),\n                  child: SizedBox(height: 170",
    "                FadeInDown(\n                  child: ClipRRect(\n                  borderRadius: BorderRadius.circular(20),\n                  child: SizedBox(height: 170"
)
open("lib/screens/galaxy_screen.dart", "w").write(galaxy)
print("galaxy_screen: animations added")

# Add animations to blackhole_screen.dart
bh = open("lib/screens/blackhole_screen.dart").read()
if "animate_do" not in bh:
    bh = bh.replace(
        "import 'package:google_fonts/google_fonts.dart';",
        "import 'package:google_fonts/google_fonts.dart';\nimport 'package:animate_do/animate_do.dart';"
    )
open("lib/screens/blackhole_screen.dart", "w").write(bh)
print("blackhole_screen: done")

# Add animations to solar_system_screen.dart  
solar = open("lib/screens/solar_system_screen.dart").read()
if "animate_do" not in solar:
    solar = solar.replace(
        "import 'package:google_fonts/google_fonts.dart';",
        "import 'package:google_fonts/google_fonts.dart';\nimport 'package:animate_do/animate_do.dart';"
    )
open("lib/screens/solar_system_screen.dart", "w").write(solar)
print("solar_system_screen: done")

print("\nAll done! Now upgrading home screen with pulse animations...")

# Upgrade home screen - add pulsing glow to cards
home = open("lib/screens/home_screen.dart").read()

# Add a daily fact widget and better animations - inject after search bar
old_search_end = """                const SizedBox(height: 12),

                Expanded(
                  child: ListView("""

new_search_end = """                const SizedBox(height: 12),

                // Daily cosmic fact banner
                FadeInUp(
                  delay: Duration(milliseconds: 350),
                  child: Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 16),
                    child: _DailyFactBanner(),
                  ),
                ),
                const SizedBox(height: 12),

                Expanded(
                  child: ListView("""

home = home.replace(old_search_end, new_search_end)

# Add _DailyFactBanner class before _StarPainter
daily_fact_widget = '''
class _DailyFactBanner extends StatefulWidget {
  const _DailyFactBanner();
  @override
  State<_DailyFactBanner> createState() => _DailyFactBannerState();
}

class _DailyFactBannerState extends State<_DailyFactBanner>
    with SingleTickerProviderStateMixin {
  late AnimationController _pulse;
  final List<Map<String,String>> facts = [
    {"emoji":"🌌","fact":"The Milky Way has 200–400 billion stars — and there are 2 trillion galaxies in the universe."},
    {"emoji":"💎","fact":"It rains diamonds on Neptune. Extreme pressure turns carbon into gem crystals."},
    {"emoji":"⏰","fact":"A day on Venus is longer than its year. It spins that slowly."},
    {"emoji":"🕳️","fact":"Time slows down near a black hole due to extreme gravity — proven by Einstein."},
    {"emoji":"🌅","fact":"Mars has blue sunsets and red skies — the opposite of Earth."},
    {"emoji":"☀️","fact":"The Sun makes up 99.8% of all mass in the Solar System."},
    {"emoji":"🌍","fact":"You are made of stardust — every atom in your body was forged in a star."},
  ];
  late int _factIndex;

  @override
  void initState() {
    super.initState();
    _factIndex = DateTime.now().day % facts.length;
    _pulse = AnimationController(vsync: this, duration: const Duration(seconds: 3))..repeat(reverse: true);
  }

  @override
  void dispose() { _pulse.dispose(); super.dispose(); }

  @override
  Widget build(BuildContext context) {
    final f = facts[_factIndex];
    return AnimatedBuilder(
      animation: _pulse,
      builder: (_, __) => Container(
        padding: const EdgeInsets.all(14),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(16),
          color: const Color(0xFF040F1F),
          border: Border.all(
            color: Color(0xFF00FFCC).withOpacity(0.2 + 0.2 * _pulse.value),
            width: 1.5,
          ),
          boxShadow: [BoxShadow(
            color: Color(0xFF00FFCC).withOpacity(0.05 + 0.05 * _pulse.value),
            blurRadius: 20,
          )],
        ),
        child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Column(children: [
            Text(f["emoji"]!, style: const TextStyle(fontSize: 24)),
            const SizedBox(height: 4),
            Text("TODAY", style: GoogleFonts.orbitron(fontSize: 6, color: Color(0xFF00FFCC), letterSpacing: 1)),
          ]),
          const SizedBox(width: 12),
          Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text("COSMIC FACT OF THE DAY", style: GoogleFonts.orbitron(fontSize: 8, color: Color(0xFF00FFCC), letterSpacing: 1.5)),
            const SizedBox(height: 6),
            Text(f["fact"]!, style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white70, height: 1.4)),
          ])),
        ]),
      ),
    );
  }
}

'''

home = home.replace("class _StarPainter extends CustomPainter {", daily_fact_widget + "class _StarPainter extends CustomPainter {")

open("lib/screens/home_screen.dart", "w").write(home)
print("home_screen: daily fact + pulse animation added")
print("\nAll animations done!")
