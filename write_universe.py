content = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class UniverseScreen extends StatefulWidget {
  const UniverseScreen({super.key});
  @override
  State<UniverseScreen> createState() => _UniverseScreenState();
}

class _UniverseScreenState extends State<UniverseScreen> with SingleTickerProviderStateMixin {
  late AnimationController _starController;
  @override
  void initState() { super.initState(); _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat(); }
  @override
  void dispose() { _starController.dispose(); super.dispose(); }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF010914),
      body: Stack(
        children: [
          AnimatedBuilder(animation: _starController, builder: (_, __) => CustomPaint(painter: _SP(_starController.value), child: const SizedBox.expand())),
          SafeArea(
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Padding(padding: const EdgeInsets.fromLTRB(20,16,20,8), child: Row(children: [
                GestureDetector(onTap: () => Navigator.pop(context), child: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white54, size: 20)),
                const SizedBox(width: 16),
                Text("UNIVERSE", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 4)),
              ])),
              Expanded(child: ListView(padding: const EdgeInsets.symmetric(horizontal: 16), children: [

                // Hero image
                ClipRRect(
                  borderRadius: BorderRadius.circular(20),
                  child: SizedBox(height: 180, width: double.infinity, child: Stack(fit: StackFit.expand, children: [
                    Image.asset("assets/images/universe.jpg", fit: BoxFit.cover),
                    Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF010914)]))),
                    Positioned(bottom: 14, left: 16, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text("The Universe", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: Color(0xFF90CAF9), blurRadius: 20)])),
                      Text("93 billion light years of everything", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                    ])),
                  ])),
                ),
                const SizedBox(height: 20),

                Text("WHAT IS THE UNIVERSE?", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF90CAF9), letterSpacing: 2)),
                const SizedBox(height: 8),
                Text("The Universe is everything that exists — all space, time, matter, and energy. It began 13.8 billion years ago with the Big Bang, a rapid expansion from an incredibly hot and dense state. It has been expanding ever since — and the expansion is accelerating.", style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, height: 1.6)),
                const SizedBox(height: 20),

                Text("KEY FACTS", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF90CAF9), letterSpacing: 2)),
                const SizedBox(height: 10),

                _fact("🕰️", "Age", "13.8 billion years", Color(0xFFFFE082)),
                _fact("📏", "Observable Size", "93 billion light years", Color(0xFF90CAF9)),
                _fact("🌌", "Galaxies", "~2 trillion galaxies", Color(0xFF7986CB)),
                _fact("⭐", "Stars", "~10²⁴ (septillion)", Color(0xFFFFB300)),
                _fact("🌡️", "Avg Temperature", "2.7 Kelvin (-270°C)", Color(0xFF80DEEA)),
                _fact("💨", "Expansion Rate", "~70 km/s per megaparsec", Color(0xFFCE93D8)),
                _fact("🌑", "Dark Matter", "27% of universe", Color(0xFF90A4AE)),
                _fact("⚡", "Dark Energy", "68% of universe", Color(0xFFEF9A9A)),
                _fact("⚛️", "Normal Matter", "Only 5% of universe", Color(0xFF4FC3F7)),
                const SizedBox(height: 20),

                Text("THE BIG BANG TIMELINE", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF90CAF9), letterSpacing: 2)),
                const SizedBox(height: 10),

                _timeline("💥", "10⁻⁴³ seconds", "Planck Epoch — laws of physics break down. Temperature: 10³² K", Color(0xFFEF9A9A)),
                _timeline("⚛️", "First 3 minutes", "Protons and neutrons form. Universe cools enough for nuclei.", Color(0xFFFFAB91)),
                _timeline("💡", "380,000 years", "First light — atoms form, universe becomes transparent.", Color(0xFFFFE082)),
                _timeline("⭐", "200M years", "First stars ignite, ending the cosmic dark ages.", Color(0xFF90CAF9)),
                _timeline("🌌", "1B years", "First galaxies form and grow.", Color(0xFF7986CB)),
                _timeline("☀️", "9.2B years", "Our Solar System forms.", Color(0xFFFFB300)),
                _timeline("🧬", "13.5B years", "Life emerges on Earth.", Color(0xFF4FC3F7)),
                _timeline("👁️", "13.8B years", "Now — you are here.", Color(0xFF80DEEA)),
                const SizedBox(height: 16),

                Container(padding: const EdgeInsets.all(16), decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: Colors.tealAccent.withOpacity(0.05), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("MIND-BLOWING FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
                    const SizedBox(height: 8),
                    Text("95% of the universe is made of dark matter and dark energy — things we cannot see, touch, or directly detect. Everything you have ever seen, touched, or known makes up only 5% of what exists.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
                  ])),
                const SizedBox(height: 24),
              ])),
            ]),
          ),
        ],
      ),
    );
  }
}

Widget _fact(String icon, String label, String value, Color color) {
  return Container(
    margin: const EdgeInsets.only(bottom: 8),
    padding: const EdgeInsets.all(14),
    decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: color.withOpacity(0.2))),
    child: Row(children: [
      Text(icon, style: const TextStyle(fontSize: 22)),
      const SizedBox(width: 12),
      Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Text(label, style: GoogleFonts.orbitron(fontSize: 8, color: color, letterSpacing: 1.5)),
        Text(value, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white, fontWeight: FontWeight.w600)),
      ])),
    ]),
  );
}

Widget _timeline(String icon, String time, String desc, Color color) {
  return Container(
    margin: const EdgeInsets.only(bottom: 10),
    child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Container(width: 36, height: 36, decoration: BoxDecoration(shape: BoxShape.circle, color: color.withOpacity(0.15), border: Border.all(color: color.withOpacity(0.4))),
        child: Center(child: Text(icon, style: const TextStyle(fontSize: 16)))),
      const SizedBox(width: 12),
      Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
        Text(time, style: GoogleFonts.orbitron(fontSize: 9, color: color, letterSpacing: 1)),
        const SizedBox(height: 3),
        Text(desc, style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60, height: 1.4)),
      ])),
    ]),
  );
}

class _SP extends CustomPainter {
  final double progress;
  static final _rng = Random(11);
  static final _stars = List.generate(200, (_) => Offset(_rng.nextDouble(), _rng.nextDouble()));
  static final _szs = List.generate(200, (_) => _rng.nextDouble() * 1.5 + 0.3);
  _SP(this.progress);
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint();
    for (int i = 0; i < _stars.length; i++) {
      final t = 0.3+0.7*(0.5+0.5*sin(progress*2*pi*2+i));
      paint.color = Colors.white.withOpacity(t*0.7);
      canvas.drawCircle(Offset(_stars[i].dx*size.width,_stars[i].dy*size.height),_szs[i],paint);
    }
  }
  @override bool shouldRepaint(_) => true;
}
"""

with open("lib/screens/universe_screen.dart", "w") as f:
    f.write(content)
print("Done! Lines:", len(content.splitlines()))
