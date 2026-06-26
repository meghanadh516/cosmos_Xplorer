# Polish the home screen with better gradients and typography

home = open("lib/screens/home_screen.dart").read()

# Make title bigger and more impactful
home = home.replace(
    'Text("COSMOS", style: GoogleFonts.orbitron(fontSize: 36, fontWeight: FontWeight.w900, color: Colors.white, letterSpacing: 8, shadows: [Shadow(color: Color(0xFF00AAFF), blurRadius: 30)]))',
    'Text("COSMOS", style: GoogleFonts.orbitron(fontSize: 42, fontWeight: FontWeight.w900, color: Colors.white, letterSpacing: 10, shadows: [Shadow(color: Color(0xFF00AAFF), blurRadius: 40), Shadow(color: Color(0xFF0066FF), blurRadius: 80)]))'
)

# Make XPLORER more visible
home = home.replace(
    'Text("X P L O R E R", style: GoogleFonts.orbitron(fontSize: 12, color: Color(0xFF00AAFF), letterSpacing: 12))',
    'Text("X P L O R E R", style: GoogleFonts.orbitron(fontSize: 13, color: Color(0xFF00CCFF), letterSpacing: 14, fontWeight: FontWeight.w600))'
)

# Make tagline more visible
home = home.replace(
    'Text("Journey from planets to the multiverse", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white38, letterSpacing: 1.5))',
    'Text("Journey from planets to the multiverse", style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white54, letterSpacing: 1.5, fontWeight: FontWeight.w500))'
)

# Make search bar more prominent
home = home.replace(
    'border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.3)),',
    'border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.5), width: 1.5),'
)

open("lib/screens/home_screen.dart", "w").write(home)
print("home_screen polished!")

# Polish planets screen
planets = open("lib/screens/planets_screen.dart").read()

# Better header
planets = planets.replace(
    'Text("PLANETS", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 4))',
    'Text("PLANETS", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 5, shadows: [Shadow(color: Color(0xFF4FC3F7), blurRadius: 15)]))'
)

# Better planet name in card
planets = planets.replace(
    'Text(planet.name, style: GoogleFonts.orbitron(fontSize: 16, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 1))',
    'Text(planet.name, style: GoogleFonts.orbitron(fontSize: 17, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 1.5))'
)

open("lib/screens/planets_screen.dart", "w").write(planets)
print("planets_screen polished!")

# Polish solar system screen
solar = open("lib/screens/solar_system_screen.dart").read()
solar = solar.replace(
    'Text("SOLAR SYSTEM", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 3))',
    'Text("SOLAR SYSTEM", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 4, shadows: [Shadow(color: Color(0xFFFFB300), blurRadius: 15)]))'
)
open("lib/screens/solar_system_screen.dart", "w").write(solar)
print("solar_system_screen polished!")

# Polish galaxy screen
galaxy = open("lib/screens/galaxy_screen.dart").read()
galaxy = galaxy.replace(
    'Text("GALAXIES", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 4))',
    'Text("GALAXIES", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 5, shadows: [Shadow(color: Color(0xFF7986CB), blurRadius: 15)]))'
)
open("lib/screens/galaxy_screen.dart", "w").write(galaxy)
print("galaxy_screen polished!")

# Polish blackhole screen
bh = open("lib/screens/blackhole_screen.dart").read()
bh = bh.replace(
    'Text("BLACK HOLES", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 3))',
    'Text("BLACK HOLES", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 4, shadows: [Shadow(color: Color(0xFF90A4AE), blurRadius: 15)]))'
)
open("lib/screens/blackhole_screen.dart", "w").write(bh)
print("blackhole_screen polished!")

# Polish universe screen
universe = open("lib/screens/universe_screen.dart").read()
universe = universe.replace(
    'Text("UNIVERSE", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 4))',
    'Text("UNIVERSE", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 5, shadows: [Shadow(color: Color(0xFF90CAF9), blurRadius: 15)]))'
)
open("lib/screens/universe_screen.dart", "w").write(universe)
print("universe_screen polished!")

# Polish multiverse screen
multi = open("lib/screens/multiverse_screen.dart").read()
multi = multi.replace(
    'Text("MULTIVERSE", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 3))',
    'Text("MULTIVERSE", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 4, shadows: [Shadow(color: Color(0xFFF48FB1), blurRadius: 15)]))'
)
open("lib/screens/multiverse_screen.dart", "w").write(multi)
print("multiverse_screen polished!")

# Polish quiz screen
quiz = open("lib/screens/quiz_screen.dart").read()
quiz = quiz.replace(
    'Text("COSMIC QUIZ", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 3))',
    'Text("COSMIC QUIZ", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 4, shadows: [Shadow(color: Color(0xFF00AAFF), blurRadius: 15)]))'
)
open("lib/screens/quiz_screen.dart", "w").write(quiz)
print("quiz_screen polished!")

# Polish search screen
search = open("lib/screens/search_screen.dart").read()
search = search.replace(
    'Text("SEARCH", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 4))',
    'Text("SEARCH", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 5, shadows: [Shadow(color: Color(0xFF00AAFF), blurRadius: 15)]))'
)
open("lib/screens/search_screen.dart", "w").write(search)
print("search_screen polished!")

print("\nAll screens polished! Run flutter run")
