import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:animate_do/animate_do.dart';

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

  final List<_Fact> facts = [
    _Fact("⭐", "Type",        "Yellow Dwarf Star",      Color(0xFFFFB300)),
    _Fact("🪐", "Planets",     "8 official",             Color(0xFF4FC3F7)),
    _Fact("🌙", "Moons",       "290+ confirmed",         Color(0xFFCE93D8)),
    _Fact("☄️", "Asteroids",   "1M+ known",              Color(0xFFFF8A65)),
    _Fact("📏", "Size",        "~2 light years",         Color(0xFF80DEEA)),
    _Fact("🕰️", "Age",         "4.6 billion years",      Color(0xFFFFE082)),
    _Fact("🚀", "Speed",       "828,000 km/h",           Color(0xFF90CAF9)),
    _Fact("☀️", "Sun Mass",    "99.8% of system",        Color(0xFFFFB300)),
    _Fact("🌡️", "Sun Temp",    "5,500°C surface",        Color(0xFFEF9A9A)),
    _Fact("💫", "Star Type",   "G-type main seq.",       Color(0xFFFFE082)),
  ];

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF010914),
      body: Stack(
        children: [
          AnimatedBuilder(
            animation: _starController,
            builder: (_, __) => CustomPaint(
              painter: _StarPainter(_starController.value),
              child: const SizedBox.expand(),
            ),
          ),
          SafeArea(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                // Header
                Padding(
                  padding: const EdgeInsets.fromLTRB(20, 16, 20, 12),
                  child: Row(children: [
                    GestureDetector(
                      onTap: () => Navigator.pop(context),
                      child: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white54, size: 20),
                    ),
                    const SizedBox(width: 16),
                    Text("SOLAR SYSTEM", style: GoogleFonts.orbitron(
                      fontSize: 20, fontWeight: FontWeight.w800,
                      color: Colors.white, letterSpacing: 4,
                      shadows: [Shadow(color: Color(0xFFFFB300), blurRadius: 15)],
                    )),
                  ]),
                ),

                // Planet thumbnails
                Padding(
                  padding: const EdgeInsets.only(left: 16, bottom: 6),
                  child: Text("PLANETS & SUN", style: GoogleFonts.orbitron(
                    fontSize: 8, color: Color(0xFF00AAFF), letterSpacing: 2)),
                ),
                SizedBox(
                  height: 82,
                  child: ListView.builder(
                    scrollDirection: Axis.horizontal,
                    padding: const EdgeInsets.symmetric(horizontal: 16),
                    itemCount: thumbs.length,
                    itemBuilder: (ctx, i) {
                      final t = thumbs[i];
                      return FadeInLeft(
                        delay: Duration(milliseconds: i * 60),
                        child: Container(
                          margin: const EdgeInsets.only(right: 10),
                          width: 60,
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(14),
                            color: const Color(0xFF040F1F),
                            border: Border.all(color: t.color.withOpacity(0.35)),
                            boxShadow: [BoxShadow(color: t.color.withOpacity(0.2), blurRadius: 8)],
                          ),
                          child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
                            ClipRRect(
                              borderRadius: BorderRadius.circular(18),
                              child: Image.asset(t.image, width: 36, height: 36, fit: BoxFit.cover,
                                errorBuilder: (_, __, ___) => Container(width: 36, height: 36, color: t.color.withOpacity(0.3))),
                            ),
                            const SizedBox(height: 4),
                            Text(t.name, style: GoogleFonts.orbitron(fontSize: 6.5, color: t.color, letterSpacing: 0.3)),
                          ]),
                        ),
                      );
                    },
                  ),
                ),

                Expanded(
                  child: SingleChildScrollView(
                    padding: const EdgeInsets.all(16),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const SizedBox(height: 8),

                        // Hero image
                        FadeInDown(
                          child: ClipRRect(
                            borderRadius: BorderRadius.circular(20),
                            child: SizedBox(
                              height: 170, width: double.infinity,
                              child: Stack(fit: StackFit.expand, children: [
                                Image.asset("assets/images/_solar_system.jpg", fit: BoxFit.cover,
                                  errorBuilder: (_, __, ___) => Container(color: const Color(0xFF071628))),
                                Container(decoration: BoxDecoration(
                                  gradient: LinearGradient(
                                    begin: Alignment.topCenter, end: Alignment.bottomCenter,
                                    colors: [Colors.transparent, const Color(0xFF010914)],
                                  ),
                                )),
                                Positioned(bottom: 14, left: 18, child: Column(
                                  crossAxisAlignment: CrossAxisAlignment.start, children: [
                                    Text("Our Solar System", style: GoogleFonts.orbitron(
                                      fontSize: 18, fontWeight: FontWeight.w800, color: Colors.white,
                                      shadows: [Shadow(color: Color(0xFFFFB300), blurRadius: 20)],
                                    )),
                                    Text("Milky Way Galaxy · Orion Arm", style: GoogleFonts.rajdhani(
                                      fontSize: 13, color: Colors.white54)),
                                  ])),
                              ]),
                            ),
                          ),
                        ),
                        const SizedBox(height: 16),

                        // About
                        FadeInUp(
                          child: Text("ABOUT", style: GoogleFonts.orbitron(
                            fontSize: 9, color: Color(0xFF00AAFF), letterSpacing: 2)),
                        ),
                        const SizedBox(height: 8),
                        FadeInUp(
                          child: Text(
                            "The Solar System formed 4.6 billion years ago from a giant molecular cloud. The Sun holds 99.8% of all mass. Eight planets, hundreds of moons, millions of asteroids, and countless comets orbit our star — all held together by gravity within a bubble called the heliosphere.",
                            style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.6),
                          ),
                        ),
                        const SizedBox(height: 20),

                        // System Facts - COMPACT GRID
                        FadeInUp(
                          child: Text("SYSTEM FACTS", style: GoogleFonts.orbitron(
                            fontSize: 9, color: Color(0xFF00AAFF), letterSpacing: 2)),
                        ),
                        const SizedBox(height: 10),

                        // 2-column compact fact cards
                        ...List.generate((facts.length / 2).ceil(), (row) {
                          final left = facts[row * 2];
                          final right = (row * 2 + 1 < facts.length) ? facts[row * 2 + 1] : null;
                          return FadeInUp(
                            delay: Duration(milliseconds: row * 60),
                            child: Padding(
                              padding: const EdgeInsets.only(bottom: 8),
                              child: Row(children: [
                                Expanded(child: _FactCard(left)),
                                const SizedBox(width: 8),
                                Expanded(child: right != null ? _FactCard(right) : const SizedBox()),
                              ]),
                            ),
                          );
                        }),
                        const SizedBox(height: 20),

                        // Zones
                        FadeInUp(
                          child: Text("ZONES OF THE SOLAR SYSTEM", style: GoogleFonts.orbitron(
                            fontSize: 9, color: Color(0xFF00AAFF), letterSpacing: 2)),
                        ),
                        const SizedBox(height: 10),

                        ...[ 
                          ["🔥", "Inner Solar System", "Mercury, Venus, Earth, Mars — rocky terrestrial planets.", Color(0xFFEF9A9A)],
                          ["💫", "Asteroid Belt", "Millions of rocky bodies between Mars and Jupiter.", Color(0xFFFFCC80)],
                          ["🌀", "Outer Solar System", "Jupiter, Saturn, Uranus, Neptune — giant planets.", Color(0xFF4FC3F7)],
                          ["❄️", "Kuiper Belt", "Icy bodies beyond Neptune including Pluto.", Color(0xFF80DEEA)],
                          ["☁️", "Oort Cloud", "Vast icy shell at the edge — ~2 light years out.", Color(0xFFCE93D8)],
                        ].asMap().entries.map((e) => FadeInLeft(
                          delay: Duration(milliseconds: e.key * 80),
                          child: Container(
                            margin: const EdgeInsets.only(bottom: 8),
                            padding: const EdgeInsets.all(12),
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(12),
                              color: const Color(0xFF040F1F),
                              border: Border.all(color: (e.value[3] as Color).withOpacity(0.25)),
                            ),
                            child: Row(crossAxisAlignment: CrossAxisAlignment.center, children: [
                              Text(e.value[0] as String, style: const TextStyle(fontSize: 22)),
                              const SizedBox(width: 12),
                              Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                Text(e.value[1] as String, style: GoogleFonts.orbitron(
                                  fontSize: 10, color: e.value[3] as Color,
                                  fontWeight: FontWeight.w600)),
                                const SizedBox(height: 2),
                                Text(e.value[2] as String, style: GoogleFonts.rajdhani(
                                  fontSize: 12, color: Colors.white54)),
                              ])),
                            ]),
                          ),
                        )),
                        const SizedBox(height: 16),

                        // Mind blowing fact
                        FadeInUp(
                          child: Container(
                            padding: const EdgeInsets.all(14),
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(14),
                              color: Colors.tealAccent.withOpacity(0.05),
                              border: Border.all(color: Colors.tealAccent.withOpacity(0.3)),
                            ),
                            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                              Row(children: [
                                const Text("🐟", style: TextStyle(fontSize: 16)),
                                const SizedBox(width: 8),
                                Text("MIND-BLOWING FACT", style: GoogleFonts.orbitron(
                                  fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5)),
                              ]),
                              const SizedBox(height: 8),
                              Text(
                                "If the Sun were the size of a basketball, Earth would be a grain of sand 26 meters away — and Neptune would be a pea 800 meters away. The Solar System is almost entirely empty space.",
                                style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic),
                              ),
                            ]),
                          ),
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

class _FactCard extends StatelessWidget {
  final _Fact f;
  const _FactCard(this.f);
  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(12),
        color: f.color.withOpacity(0.08),
        border: Border.all(color: f.color.withOpacity(0.3)),
      ),
      child: Row(children: [
        Text(f.icon, style: const TextStyle(fontSize: 18)),
        const SizedBox(width: 8),
        Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(f.label, style: GoogleFonts.orbitron(fontSize: 7, color: f.color, letterSpacing: 1)),
          const SizedBox(height: 2),
          Text(f.value, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white, fontWeight: FontWeight.w600)),
        ])),
      ]),
    );
  }
}

class _PlanetThumb {
  final String name, image; final Color color;
  const _PlanetThumb(this.name, this.image, this.color);
}

class _Fact {
  final String icon, label, value; final Color color;
  const _Fact(this.icon, this.label, this.value, this.color);
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
