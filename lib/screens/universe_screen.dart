import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:animate_do/animate_do.dart';

class UniverseScreen extends StatefulWidget {
  const UniverseScreen({super.key});
  @override
  State<UniverseScreen> createState() => _UniverseScreenState();
}

class _UniverseScreenState extends State<UniverseScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _starController;

  @override
  void initState() {
    super.initState();
    _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();
  }

  @override
  void dispose() { _starController.dispose(); super.dispose(); }

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
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Padding(
                padding: const EdgeInsets.fromLTRB(20, 16, 20, 8),
                child: Row(children: [
                  GestureDetector(
                    onTap: () => Navigator.pop(context),
                    child: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white54, size: 20),
                  ),
                  const SizedBox(width: 16),
                  Text("UNIVERSE", style: GoogleFonts.orbitron(
                    fontSize: 22, fontWeight: FontWeight.w800,
                    color: Colors.white, letterSpacing: 5,
                    shadows: [Shadow(color: Color(0xFF90CAF9), blurRadius: 15)],
                  )),
                ]),
              ),

              Expanded(
                child: ListView(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  children: [

                    // Hero image
                    FadeInDown(
                      child: ClipRRect(
                        borderRadius: BorderRadius.circular(20),
                        child: SizedBox(
                          height: 180, width: double.infinity,
                          child: Stack(fit: StackFit.expand, children: [
                            Image.asset("assets/images/universe.jpg", fit: BoxFit.cover,
                              errorBuilder: (_, __, ___) => Container(color: const Color(0xFF071628))),
                            Container(decoration: BoxDecoration(
                              gradient: LinearGradient(
                                begin: Alignment.topCenter, end: Alignment.bottomCenter,
                                colors: [Colors.transparent, const Color(0xFF010914)],
                              ),
                            )),
                            Positioned(bottom: 14, left: 16, child: Column(
                              crossAxisAlignment: CrossAxisAlignment.start, children: [
                                Text("The Universe", style: GoogleFonts.orbitron(
                                  fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white,
                                  shadows: [Shadow(color: Color(0xFF90CAF9), blurRadius: 20)],
                                )),
                                Text("93 billion light years of everything", style: GoogleFonts.rajdhani(
                                  fontSize: 13, color: Colors.white60)),
                              ])),
                          ]),
                        ),
                      ),
                    ),
                    const SizedBox(height: 16),

                    // About
                    FadeInUp(
                      child: Container(
                        padding: const EdgeInsets.all(14),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(14),
                          color: const Color(0xFF040F1F),
                          border: Border.all(color: Color(0xFF90CAF9).withOpacity(0.2)),
                        ),
                        child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                          Text("WHAT IS THE UNIVERSE?", style: GoogleFonts.orbitron(
                            fontSize: 9, color: Color(0xFF90CAF9), letterSpacing: 2)),
                          const SizedBox(height: 8),
                          Text(
                            "The Universe is everything that exists — all space, time, matter, and energy. It began 13.8 billion years ago with the Big Bang and has been expanding ever since. The expansion is actually accelerating, driven by a mysterious force called dark energy.",
                            style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.6),
                          ),
                        ]),
                      ),
                    ),
                    const SizedBox(height: 20),

                    // ── KEY FACTS SECTION ──
                    FadeInLeft(
                      child: Row(children: [
                        Container(width: 4, height: 20, decoration: BoxDecoration(color: Color(0xFF90CAF9), borderRadius: BorderRadius.circular(2))),
                        const SizedBox(width: 10),
                        Text("KEY FACTS", style: GoogleFonts.orbitron(fontSize: 11, color: Color(0xFF90CAF9), letterSpacing: 2, fontWeight: FontWeight.w700)),
                      ]),
                    ),
                    const SizedBox(height: 10),

                    // Facts in 2 columns compact
                    ...[
                      ["🕰️", "Age",             "13.8 billion years",      Color(0xFFFFE082)],
                      ["📏", "Observable Size", "93 billion light years",  Color(0xFF90CAF9)],
                      ["🌌", "Galaxies",        "~2 trillion",             Color(0xFF7986CB)],
                      ["⭐", "Stars",           "~10²⁴ (septillion)",      Color(0xFFFFB300)],
                      ["🌡️", "Temperature",    "2.7 Kelvin (-270°C)",     Color(0xFF80DEEA)],
                      ["💨", "Expansion",      "~70 km/s/megaparsec",     Color(0xFFCE93D8)],
                      ["🌑", "Dark Matter",    "27% of universe",         Color(0xFF90A4AE)],
                      ["⚡", "Dark Energy",    "68% of universe",         Color(0xFFEF9A9A)],
                      ["⚛️", "Normal Matter",  "Only 5% of universe",     Color(0xFF4FC3F7)],
                      ["🔭", "First Light",    "380,000 years after BB",  Color(0xFFFFCC80)],
                    ].asMap().entries.map((e) {
                      final row = e.key ~/ 2;
                      final col = e.key % 2;
                      if (col == 1) return const SizedBox.shrink();
                      final left = e.value;
                      final rightIdx = e.key + 1;
                      final right = rightIdx < 10 ? [
                        ["🕰️", "Age",             "13.8 billion years",      Color(0xFFFFE082)],
                        ["📏", "Observable Size", "93 billion light years",  Color(0xFF90CAF9)],
                        ["🌌", "Galaxies",        "~2 trillion",             Color(0xFF7986CB)],
                        ["⭐", "Stars",           "~10²⁴ (septillion)",      Color(0xFFFFB300)],
                        ["🌡️", "Temperature",    "2.7 Kelvin (-270°C)",     Color(0xFF80DEEA)],
                        ["💨", "Expansion",      "~70 km/s/megaparsec",     Color(0xFFCE93D8)],
                        ["🌑", "Dark Matter",    "27% of universe",         Color(0xFF90A4AE)],
                        ["⚡", "Dark Energy",    "68% of universe",         Color(0xFFEF9A9A)],
                        ["⚛️", "Normal Matter",  "Only 5% of universe",     Color(0xFF4FC3F7)],
                        ["🔭", "First Light",    "380,000 years after BB",  Color(0xFFFFCC80)],
                      ][rightIdx] : null;

                      return FadeInUp(
                        delay: Duration(milliseconds: row * 60),
                        child: Padding(
                          padding: const EdgeInsets.only(bottom: 8),
                          child: Row(children: [
                            Expanded(child: _FactTile(left[0] as String, left[1] as String, left[2] as String, left[3] as Color)),
                            const SizedBox(width: 8),
                            Expanded(child: right != null
                              ? _FactTile(right[0] as String, right[1] as String, right[2] as String, right[3] as Color)
                              : const SizedBox()),
                          ]),
                        ),
                      );
                    }),
                    const SizedBox(height: 24),

                    // ── BIG BANG TIMELINE SECTION ──
                    FadeInLeft(
                      child: Row(children: [
                        Container(width: 4, height: 20, decoration: BoxDecoration(color: Color(0xFFEF9A9A), borderRadius: BorderRadius.circular(2))),
                        const SizedBox(width: 10),
                        Text("THE BIG BANG TIMELINE", style: GoogleFonts.orbitron(fontSize: 11, color: Color(0xFFEF9A9A), letterSpacing: 2, fontWeight: FontWeight.w700)),
                      ]),
                    ),
                    const SizedBox(height: 14),

                    // Timeline with connecting line
                    Container(
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(20),
                        color: const Color(0xFF040F1F),
                        border: Border.all(color: Color(0xFFEF9A9A).withOpacity(0.2)),
                      ),
                      child: Column(children: [
                        ...[ 
                          ["💥", "10⁻⁴³ seconds", "Planck Epoch — laws of physics break down. Temp: 10³² K", Color(0xFFEF9A9A)],
                          ["⚛️", "First 3 minutes", "Protons and neutrons form. Universe cools enough for nuclei.", Color(0xFFFFAB91)],
                          ["💡", "380,000 years", "First light — atoms form, universe becomes transparent.", Color(0xFFFFE082)],
                          ["⭐", "200M years", "First stars ignite, ending the cosmic dark ages.", Color(0xFF90CAF9)],
                          ["🌌", "1 billion years", "First galaxies form and grow.", Color(0xFF7986CB)],
                          ["☀️", "9.2 billion years", "Our Solar System forms from a molecular cloud.", Color(0xFFFFB300)],
                          ["🧬", "13.5 billion years", "Life emerges on Earth.", Color(0xFF4FC3F7)],
                          ["👁️", "13.8 billion years", "Now — you are reading this.", Color(0xFF80DEEA)],
                        ].asMap().entries.map((e) {
                          final isLast = e.key == 7;
                          final item = e.value;
                          return FadeInLeft(
                            delay: Duration(milliseconds: e.key * 80),
                            child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                              Column(children: [
                                Container(
                                  width: 38, height: 38,
                                  decoration: BoxDecoration(
                                    shape: BoxShape.circle,
                                    color: (item[3] as Color).withOpacity(0.15),
                                    border: Border.all(color: (item[3] as Color).withOpacity(0.5), width: 1.5),
                                  ),
                                  child: Center(child: Text(item[0] as String, style: const TextStyle(fontSize: 16))),
                                ),
                                if (!isLast) Container(width: 2, height: 30,
                                  decoration: BoxDecoration(
                                    gradient: LinearGradient(
                                      begin: Alignment.topCenter, end: Alignment.bottomCenter,
                                      colors: [(item[3] as Color).withOpacity(0.5), Colors.transparent],
                                    ),
                                  )),
                              ]),
                              const SizedBox(width: 14),
                              Expanded(
                                child: Padding(
                                  padding: EdgeInsets.only(bottom: isLast ? 0 : 16),
                                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                    const SizedBox(height: 4),
                                    Text(item[1] as String, style: GoogleFonts.orbitron(
                                      fontSize: 10, color: item[3] as Color, fontWeight: FontWeight.w600)),
                                    const SizedBox(height: 3),
                                    Text(item[2] as String, style: GoogleFonts.rajdhani(
                                      fontSize: 13, color: Colors.white60, height: 1.4)),
                                  ]),
                                ),
                              ),
                            ]),
                          );
                        }),
                      ]),
                    ),
                    const SizedBox(height: 20),

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
                            "95% of the universe is made of dark matter and dark energy — things we cannot see, touch, or directly detect. Everything you have ever seen, touched, or known makes up only 5% of what exists.",
                            style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic),
                          ),
                        ]),
                      ),
                    ),
                    const SizedBox(height: 24),
                  ],
                ),
              ),
            ]),
          ),
        ],
      ),
    );
  }
}

class _FactTile extends StatelessWidget {
  final String icon, label, value;
  final Color color;
  const _FactTile(this.icon, this.label, this.value, this.color);

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 10),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(12),
        color: color.withOpacity(0.08),
        border: Border.all(color: color.withOpacity(0.3)),
      ),
      child: Row(children: [
        Text(icon, style: const TextStyle(fontSize: 18)),
        const SizedBox(width: 8),
        Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(label, style: GoogleFonts.orbitron(fontSize: 7, color: color, letterSpacing: 1)),
          const SizedBox(height: 2),
          Text(value, style: GoogleFonts.rajdhani(fontSize: 11, color: Colors.white, fontWeight: FontWeight.w600)),
        ])),
      ]),
    );
  }
}

class _StarPainter extends CustomPainter {
  final double progress;
  static final _rng = Random(11);
  static final _stars = List.generate(200, (_) => Offset(_rng.nextDouble(), _rng.nextDouble()));
  static final _szs = List.generate(200, (_) => _rng.nextDouble() * 1.5 + 0.3);
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
