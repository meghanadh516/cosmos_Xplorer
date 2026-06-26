content = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class SolarSystemScreen extends StatefulWidget {
  const SolarSystemScreen({super.key});
  @override
  State<SolarSystemScreen> createState() => _SolarSystemScreenState();
}

class _SolarSystemScreenState extends State<SolarSystemScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _starController;

  @override
  void initState() {
    super.initState();
    _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();
  }

  @override
  void dispose() { _starController.dispose(); super.dispose(); }

  final List<_PlanetThumb> thumbs = [
    _PlanetThumb("Sun",     "assets/images/sun.jpg",     Color(0xFFFFB300)),
    _PlanetThumb("Mercury", "assets/images/mercury.jpg", Color(0xFF90A4AE)),
    _PlanetThumb("Venus",   "assets/images/venus.jpg",   Color(0xFFFFCC80)),
    _PlanetThumb("Earth",   "assets/images/earth.jpg",   Color(0xFF4FC3F7)),
    _PlanetThumb("Mars",    "assets/images/mars.jpg",    Color(0xFFEF9A9A)),
    _PlanetThumb("Jupiter", "assets/images/jupiter.jpg", Color(0xFFFFAB91)),
    _PlanetThumb("Saturn",  "assets/images/saturn.jpg",  Color(0xFFFFE082)),
    _PlanetThumb("Uranus",  "assets/images/uranus.jpg",  Color(0xFF80DEEA)),
    _PlanetThumb("Neptune", "assets/images/neptune.jpg", Color(0xFF90CAF9)),
  ];

  final List<_SystemFact> facts = [
    _SystemFact("⭐", "Type", "Yellow Dwarf Star System", Color(0xFFFFB300)),
    _SystemFact("🪐", "Planets", "8 official planets", Color(0xFF4FC3F7)),
    _SystemFact("🌙", "Known Moons", "290+ confirmed moons", Color(0xFFCE93D8)),
    _SystemFact("☄️", "Asteroids", "1+ million known asteroids", Color(0xFFFF8A65)),
    _SystemFact("📏", "Size", "~2 light years across", Color(0xFF80DEEA)),
    _SystemFact("🕰️", "Age", "4.6 billion years old", Color(0xFFFFE082)),
    _SystemFact("🚀", "Speed", "828,000 km/h around galaxy", Color(0xFF90CAF9)),
    _SystemFact("☀️", "Sun Mass", "99.8% of all system mass", Color(0xFFFFB300)),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF010914),
      body: Stack(
        children: [
          AnimatedBuilder(
            animation: _starController,
            builder: (_, __) => CustomPaint(painter: _StarPainter(_starController.value), child: const SizedBox.expand()),
          ),
          SafeArea(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Header
                Padding(
                  padding: const EdgeInsets.fromLTRB(20, 16, 20, 12),
                  child: Row(children: [
                    GestureDetector(onTap: () => Navigator.pop(context), child: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white54, size: 20)),
                    const SizedBox(width: 16),
                    Text("SOLAR SYSTEM", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 3)),
                  ]),
                ),

                // Planet thumbnails row at top
                Padding(
                  padding: const EdgeInsets.only(left: 16, bottom: 4),
                  child: Text("PLANETS & SUN", style: GoogleFonts.orbitron(fontSize: 8, color: Color(0xFF00AAFF), letterSpacing: 2)),
                ),
                SizedBox(
                  height: 86,
                  child: ListView.builder(
                    scrollDirection: Axis.horizontal,
                    padding: const EdgeInsets.symmetric(horizontal: 16),
                    itemCount: thumbs.length,
                    itemBuilder: (ctx, i) {
                      final t = thumbs[i];
                      return Container(
                        margin: const EdgeInsets.only(right: 10),
                        width: 62,
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(14),
                          color: const Color(0xFF040F1F),
                          border: Border.all(color: t.color.withOpacity(0.3)),
                          boxShadow: [BoxShadow(color: t.color.withOpacity(0.15), blurRadius: 8)],
                        ),
                        child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
                          ClipRRect(
                            borderRadius: BorderRadius.circular(18),
                            child: Image.asset(t.image, width: 38, height: 38, fit: BoxFit.cover,
                              errorBuilder: (_, __, ___) => Container(width: 38, height: 38, color: t.color.withOpacity(0.3))),
                          ),
                          const SizedBox(height: 4),
                          Text(t.name, style: GoogleFonts.orbitron(fontSize: 7, color: t.color, letterSpacing: 0.3)),
                        ]),
                      );
                    },
                  ),
                ),

                // Scrollable content
                Expanded(
                  child: SingleChildScrollView(
                    padding: const EdgeInsets.all(16),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const SizedBox(height: 8),

                        // Hero solar system image
                        ClipRRect(
                          borderRadius: BorderRadius.circular(24),
                          child: SizedBox(
                            height: 190,
                            width: double.infinity,
                            child: Stack(fit: StackFit.expand, children: [
                              Image.asset("assets/images/_solar_system.jpg", fit: BoxFit.cover,
                                errorBuilder: (_, __, ___) => Container(color: const Color(0xFF071628))),
                              Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF010914)]))),
                              Positioned(bottom: 16, left: 20, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                Text("Our Solar System", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 1, shadows: [Shadow(color: Color(0xFFFFB300), blurRadius: 20)])),
                                Text("Milky Way Galaxy · Orion Arm", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white54)),
                              ])),
                            ]),
                          ),
                        ),
                        const SizedBox(height: 20),

                        // About section
                        Text("ABOUT", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF00AAFF), letterSpacing: 2)),
                        const SizedBox(height: 8),
                        Text(
                          "The Solar System formed 4.6 billion years ago from a giant molecular cloud. The Sun holds 99.8% of all mass. Eight planets, hundreds of moons, millions of asteroids, and countless comets orbit our star — all held together by gravity within a bubble called the heliosphere.",
                          style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, height: 1.6),
                        ),
                        const SizedBox(height: 20),

                        // System facts grid
                        Text("SYSTEM FACTS", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF00AAFF), letterSpacing: 2)),
                        const SizedBox(height: 10),
                        GridView.builder(
                          shrinkWrap: true,
                          physics: const NeverScrollableScrollPhysics(),
                          gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 2, childAspectRatio: 2.4, crossAxisSpacing: 10, mainAxisSpacing: 10),
                          itemCount: facts.length,
                          itemBuilder: (ctx, i) {
                            final f = facts[i];
                            return Container(
                              padding: const EdgeInsets.all(12),
                              decoration: BoxDecoration(
                                borderRadius: BorderRadius.circular(14),
                                color: const Color(0xFF040F1F),
                                border: Border.all(color: f.color.withOpacity(0.25)),
                              ),
                              child: Row(children: [
                                Text(f.icon, style: const TextStyle(fontSize: 20)),
                                const SizedBox(width: 10),
                                Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.center, children: [
                                  Text(f.label, style: GoogleFonts.orbitron(fontSize: 7, color: f.color, letterSpacing: 1)),
                                  Text(f.value, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white, fontWeight: FontWeight.w600, height: 1.2)),
                                ])),
                              ]),
                            );
                          },
                        ),
                        const SizedBox(height: 20),

                        // Zones section
                        Text("ZONES OF THE SOLAR SYSTEM", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF00AAFF), letterSpacing: 2)),
                        const SizedBox(height: 10),
                        _ZoneCard("🔥", "Inner Solar System", "Mercury, Venus, Earth, Mars — rocky terrestrial planets close to the Sun.", Color(0xFFEF9A9A)),
                        _ZoneCard("💫", "Asteroid Belt", "A ring of millions of rocky bodies between Mars and Jupiter. Ceres is the largest.", Color(0xFFFFCC80)),
                        _ZoneCard("🌀", "Outer Solar System", "Jupiter, Saturn, Uranus, Neptune — giant planets with rings and many moons.", Color(0xFF4FC3F7)),
                        _ZoneCard("❄️", "Kuiper Belt", "A region beyond Neptune filled with icy bodies including Pluto.", Color(0xFF80DEEA)),
                        _ZoneCard("☁️", "Oort Cloud", "A vast shell of icy objects at the very edge of the Solar System — ~2 light years out.", Color(0xFFCE93D8)),
                        const SizedBox(height: 20),

                        // Mind blowing fact
                        Container(
                          padding: const EdgeInsets.all(16),
                          decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: Colors.tealAccent.withOpacity(0.05), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
                          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                            Row(children: [
                              const Text("🐟", style: TextStyle(fontSize: 16)),
                              const SizedBox(width: 8),
                              Text("MIND-BLOWING FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5)),
                            ]),
                            const SizedBox(height: 8),
                            Text("If the Sun were the size of a basketball, Earth would be a grain of sand 26 meters away — and Neptune would be a pea 800 meters away. The Solar System is almost entirely empty space.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
                          ]),
                        ),
                        const SizedBox(height: 24),
                      ],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _PlanetThumb {
  final String name, image; final Color color;
  const _PlanetThumb(this.name, this.image, this.color);
}

class _SystemFact {
  final String icon, label, value; final Color color;
  const _SystemFact(this.icon, this.label, this.value, this.color);
}

Widget _ZoneCard(String icon, String title, String desc, Color color) {
  return Container(
    margin: const EdgeInsets.only(bottom: 10),
    padding: const EdgeInsets.all(14),
    decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: color.withOpacity(0.25))),
    child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Text(icon, style: const TextStyle(fontSize: 24)),
      const SizedBox(width: 12),
      Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Text(title, style: GoogleFonts.orbitron(fontSize: 11, color: color, fontWeight: FontWeight.w600, letterSpacing: 0.5)),
        const SizedBox(height: 4),
        Text(desc, style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white54, height: 1.4)),
      ])),
    ]),
  );
}

class _StarPainter extends CustomPainter {
  final double progress;
  static final _rng = Random(55);
  static final _stars = List.generate(120, (_) => Offset(_rng.nextDouble(), _rng.nextDouble()));
  static final _szs = List.generate(120, (_) => _rng.nextDouble() * 1.2 + 0.3);
  _StarPainter(this.progress);
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint();
    for (int i = 0; i < _stars.length; i++) {
      final t = 0.3 + 0.7 * (0.5 + 0.5 * sin(progress * 2 * pi * 2 + i));
      paint.color = Colors.white.withOpacity(t * 0.7);
      canvas.drawCircle(Offset(_stars[i].dx * size.width, _stars[i].dy * size.height), _szs[i], paint);
    }
  }
  @override
  bool shouldRepaint(_) => true;
}
"""

with open("lib/screens/solar_system_screen.dart", "w") as f:
    f.write(content)
print("Done! Lines:", len(content.splitlines()))
