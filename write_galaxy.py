content = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class GalaxyScreen extends StatefulWidget {
  const GalaxyScreen({super.key});
  @override
  State<GalaxyScreen> createState() => _GalaxyScreenState();
}

class _GalaxyScreenState extends State<GalaxyScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _starController;
  int _tab = 0;

  @override
  void initState() {
    super.initState();
    _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();
  }

  @override
  void dispose() { _starController.dispose(); super.dispose(); }

  final List<_GalaxyItem> galaxies = [
    _GalaxyItem("Milky Way",    "🌌", Color(0xFF7986CB), "Barred Spiral", "Our home galaxy containing 200–400 billion stars. The Solar System sits 26,000 light years from the center.",     "100,000 ly",       "200-400 billion",  "13.6 billion yrs", "🐟 The Milky Way and Andromeda galaxy are on a collision course — they will merge in about 4.5 billion years into a giant elliptical galaxy."),
    _GalaxyItem("Andromeda",    "🌀", Color(0xFF4FC3F7), "Spiral",        "The nearest large galaxy to us, visible to the naked eye. It is larger than the Milky Way with over a trillion stars.", "220,000 ly",      "1 trillion+",      "10 billion yrs",   "🐟 Andromeda is approaching us at 110 km per second. When it hits, Earth will likely survive because galaxies are mostly empty space."),
    _GalaxyItem("Whirlpool",    "🌊", Color(0xFF80DEEA), "Spiral",        "A classic spiral galaxy interacting with a smaller companion galaxy NGC 5195. A favorite target for astronomers and astrophotographers.", "76,000 ly", "~100 billion",     "400 million yrs",  "🐟 The Whirlpool Galaxy was the first galaxy discovered to have a spiral structure — in 1845 by Lord Rosse using a hand-built telescope in Ireland."),
    _GalaxyItem("Sombrero",     "🎩", Color(0xFFFFE082), "Lenticular",    "A galaxy famous for its bright nucleus, large central bulge, and dark dust lane in its outer edge — resembling a Mexican sombrero hat.", "50,000 ly", "~100 billion",     "13 billion yrs",   "🐟 The Sombrero Galaxy has a supermassive black hole at its center — one BILLION times the mass of our Sun. That's 250x bigger than the Milky Way's own black hole."),
    _GalaxyItem("Triangulum",   "🔺", Color(0xFFEF9A9A), "Spiral",        "The third-largest galaxy in the Local Group after Andromeda and Milky Way. One of the most distant objects visible to the naked eye.", "60,000 ly", "~40 billion",      "10 billion yrs",   "🐟 Unlike most galaxies, Triangulum has no supermassive black hole at its center — making it an anomaly that scientists still don't fully understand."),
    _GalaxyItem("Centaurus A",  "💫", Color(0xFFCE93D8), "Elliptical",    "One of the closest radio galaxies to Earth. It has a massive black hole actively shooting jets of high-energy particles across 13,000 light years.", "60,000 ly", "~100 billion",  "12 billion yrs",   "🐟 Centaurus A's central black hole shoots relativistic jets — streams of particles moving at nearly the speed of light — that extend for 13,000 light years in both directions."),
  ];

  final List<_BlackHoleItem> blackHoles = [
    _BlackHoleItem("Sagittarius A*",   "🕳️", Color(0xFF90A4AE), "Our Galaxy's Core",   "The supermassive black hole at the center of the Milky Way. First imaged in 2022 by the Event Horizon Telescope collaboration.",                                                           "4 million solar masses",       "26,000 light years",     "🐟 Sagittarius A* was finally photographed in 2022. The image took 5 petabytes of data — so much that it had to be physically flown on hard drives from telescopes around the world."),
    _BlackHoleItem("M87*",             "⚫", Color(0xFFFFAB91), "Virgo Cluster",        "The first black hole ever photographed in 2019. Located in the giant elliptical galaxy M87, it powers a relativistic jet visible across millions of light years.",                           "6.5 billion solar masses",     "53.5 million light years","🐟 M87*'s event horizon is so large that our entire Solar System would fit inside it with room to spare. Light takes several days to cross from one side to the other."),
    _BlackHoleItem("Stellar BH",       "💥", Color(0xFFEF9A9A), "Throughout Galaxies",  "Formed when massive stars (20+ solar masses) collapse at the end of their lives in a supernova explosion. The Milky Way contains an estimated 100 million of them.",                        "5–100 solar masses",           "Varies",                  "🐟 Time slows down near a black hole due to gravity. If you hovered near the event horizon for 1 hour, thousands of years could pass on Earth — gravitational time dilation."),
    _BlackHoleItem("Intermediate BH",  "🌑", Color(0xFF80DEEA), "Star Clusters",        "A mysterious middle ground between stellar and supermassive black holes. Rarely observed and poorly understood — they may be the seeds of supermassive black holes.",                         "100–100,000 solar masses",     "Various",                 "🐟 Nobody knows how supermassive black holes got so big so fast after the Big Bang. Intermediate black holes may be the missing link — but we have almost no direct evidence."),
    _BlackHoleItem("Quasar / AGN",     "✨", Color(0xFFFFE082), "Early Universe",        "When a supermassive black hole actively feeds on surrounding matter, it becomes a quasar — the brightest objects in the universe, outshining entire galaxies.",                              "Billions of solar masses",     "Billions of light years", "🐟 The most luminous quasar discovered shines 600 trillion times brighter than our Sun. It devours the equivalent of 2 suns every day to maintain that brightness."),
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
                Padding(
                  padding: const EdgeInsets.fromLTRB(20, 16, 20, 12),
                  child: Row(children: [
                    GestureDetector(onTap: () => Navigator.pop(context), child: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white54, size: 20)),
                    const SizedBox(width: 16),
                    Text("DEEP SPACE", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 3)),
                  ]),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  child: Row(children: [
                    _TabBtn("🌌 Galaxies",   _tab == 0, Color(0xFF7986CB), () => setState(() => _tab = 0)),
                    const SizedBox(width: 10),
                    _TabBtn("🕳️ Black Holes", _tab == 1, Color(0xFF90A4AE), () => setState(() => _tab = 1)),
                  ]),
                ),
                const SizedBox(height: 16),
                Expanded(
                  child: _tab == 0 ? _GalaxyList(galaxies) : _BlackHoleList(blackHoles),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

// ── Tab button ────────────────────────────────────────────────────────────────
Widget _TabBtn(String label, bool active, Color color, VoidCallback onTap) {
  return GestureDetector(
    onTap: onTap,
    child: AnimatedContainer(
      duration: const Duration(milliseconds: 250),
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(12),
        color: active ? color.withOpacity(0.15) : const Color(0xFF040F1F),
        border: Border.all(color: active ? color : Colors.white12, width: active ? 1.5 : 1),
      ),
      child: Text(label, style: GoogleFonts.orbitron(fontSize: 11, color: active ? color : Colors.white38, fontWeight: active ? FontWeight.w700 : FontWeight.w400, letterSpacing: 0.5)),
    ),
  );
}

// ── Galaxy list ───────────────────────────────────────────────────────────────
class _GalaxyList extends StatelessWidget {
  final List<_GalaxyItem> items;
  const _GalaxyList(this.items);

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.symmetric(horizontal: 16),
      children: [
        Text("TYPES OF GALAXIES", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF7986CB), letterSpacing: 2)),
        const SizedBox(height: 6),
        Wrap(spacing: 8, runSpacing: 8, children: [
          _TypeChip("🌀", "Spiral",     Color(0xFF4FC3F7)),
          _TypeChip("⭕", "Elliptical", Color(0xFFFFE082)),
          _TypeChip("🔷", "Lenticular", Color(0xFFCE93D8)),
          _TypeChip("🔶", "Irregular",  Color(0xFFFF8A65)),
        ]),
        const SizedBox(height: 20),
        Text("NOTABLE GALAXIES", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF7986CB), letterSpacing: 2)),
        const SizedBox(height: 10),
        ...items.map((g) => _GalaxyCard(g, context)),
        const SizedBox(height: 16),
        Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: Colors.tealAccent.withOpacity(0.05), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("UNIVERSE FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
            const SizedBox(height: 8),
            Text("There are an estimated 2 trillion galaxies in the observable universe. If you counted one per second, it would take 63 million years to count them all.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
          ]),
        ),
        const SizedBox(height: 24),
      ],
    );
  }
}

Widget _TypeChip(String icon, String label, Color color) => Container(
  padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 7),
  decoration: BoxDecoration(borderRadius: BorderRadius.circular(10), color: color.withOpacity(0.08), border: Border.all(color: color.withOpacity(0.3))),
  child: Row(mainAxisSize: MainAxisSize.min, children: [
    Text(icon, style: const TextStyle(fontSize: 14)),
    const SizedBox(width: 6),
    Text(label, style: GoogleFonts.rajdhani(fontSize: 13, color: color, fontWeight: FontWeight.w600)),
  ]),
);

// Galaxy card — shows only galaxy info
Widget _GalaxyCard(_GalaxyItem g, BuildContext context) {
  return GestureDetector(
    onTap: () => showModalBottomSheet(
      context: context, backgroundColor: Colors.transparent, isScrollControlled: true,
      builder: (_) => _GalaxySheet(g),
    ),
    child: Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(borderRadius: BorderRadius.circular(18), color: const Color(0xFF040F1F), border: Border.all(color: g.color.withOpacity(0.25)), boxShadow: [BoxShadow(color: g.color.withOpacity(0.07), blurRadius: 16)]),
      child: Row(children: [
        Container(width: 56, height: 56, decoration: BoxDecoration(shape: BoxShape.circle, color: g.color.withOpacity(0.15), border: Border.all(color: g.color.withOpacity(0.4))),
          child: Center(child: Text(g.emoji, style: const TextStyle(fontSize: 28)))),
        const SizedBox(width: 14),
        Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Row(children: [
            Text(g.name, style: GoogleFonts.orbitron(fontSize: 14, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 1)),
            const Spacer(),
            Icon(Icons.arrow_forward_ios_rounded, color: g.color, size: 13),
          ]),
          const SizedBox(height: 3),
          Row(children: [
            Container(padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2), decoration: BoxDecoration(borderRadius: BorderRadius.circular(6), color: g.color.withOpacity(0.12)), child: Text(g.type, style: GoogleFonts.orbitron(fontSize: 7, color: g.color, letterSpacing: 0.5))),
            const SizedBox(width: 8),
            Text("${g.stars} stars", style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
          ]),
          const SizedBox(height: 5),
          Text(g.description, maxLines: 2, overflow: TextOverflow.ellipsis, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38, height: 1.3)),
        ])),
      ]),
    ),
  );
}

// ── Black hole list ───────────────────────────────────────────────────────────
class _BlackHoleList extends StatelessWidget {
  final List<_BlackHoleItem> items;
  const _BlackHoleList(this.items);

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.symmetric(horizontal: 16),
      children: [
        Container(
          padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: Colors.white12)),
          child: Text("A black hole is a region where gravity is so extreme that nothing — not even light — can escape. They form when massive stars collapse, or when matter accumulates at galactic centers.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white54, height: 1.5)),
        ),
        const SizedBox(height: 16),
        Text("TYPES OF BLACK HOLES", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF90A4AE), letterSpacing: 2)),
        const SizedBox(height: 10),
        ...items.map((b) => _BlackHoleCard(b, context)),
        const SizedBox(height: 24),
      ],
    );
  }
}

// Black hole card — shows only black hole info
Widget _BlackHoleCard(_BlackHoleItem b, BuildContext context) {
  return GestureDetector(
    onTap: () => showModalBottomSheet(
      context: context, backgroundColor: Colors.transparent, isScrollControlled: true,
      builder: (_) => _BlackHoleSheet(b),
    ),
    child: Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(borderRadius: BorderRadius.circular(18), color: const Color(0xFF040F1F), border: Border.all(color: b.color.withOpacity(0.25)), boxShadow: [BoxShadow(color: b.color.withOpacity(0.07), blurRadius: 16)]),
      child: Row(children: [
        Container(width: 56, height: 56, decoration: BoxDecoration(shape: BoxShape.circle, color: b.color.withOpacity(0.1), border: Border.all(color: b.color.withOpacity(0.3))),
          child: Center(child: Text(b.emoji, style: const TextStyle(fontSize: 28)))),
        const SizedBox(width: 14),
        Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Row(children: [
            Expanded(child: Text(b.name, style: GoogleFonts.orbitron(fontSize: 13, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 0.5))),
            Icon(Icons.arrow_forward_ios_rounded, color: b.color, size: 13),
          ]),
          const SizedBox(height: 3),
          Text(b.location, style: GoogleFonts.rajdhani(fontSize: 12, color: b.color)),
          const SizedBox(height: 4),
          Text("Mass: ${b.mass}", style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
        ])),
      ]),
    ),
  );
}

// ── Galaxy detail sheet — ONLY galaxy fields ──────────────────────────────────
class _GalaxySheet extends StatelessWidget {
  final _GalaxyItem g;
  const _GalaxySheet(this.g);
  @override
  Widget build(BuildContext context) => DraggableScrollableSheet(
    initialChildSize: 0.72, minChildSize: 0.5, maxChildSize: 0.92,
    builder: (_, ctrl) => Container(
      decoration: BoxDecoration(color: const Color(0xFF040F1F), borderRadius: const BorderRadius.vertical(top: Radius.circular(28)), border: Border.all(color: g.color.withOpacity(0.3))),
      child: ListView(controller: ctrl, padding: const EdgeInsets.all(24), children: [
        Center(child: Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white24, borderRadius: BorderRadius.circular(2)))),
        const SizedBox(height: 20),
        Center(child: Text(g.emoji, style: const TextStyle(fontSize: 72))),
        const SizedBox(height: 12),
        Center(child: Text(g.name, style: GoogleFonts.orbitron(fontSize: 26, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: g.color, blurRadius: 20)]))),
        Center(child: Text(g.type, style: GoogleFonts.rajdhani(fontSize: 14, color: g.color))),
        const SizedBox(height: 20),
        Text(g.description, style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, height: 1.6)),
        const SizedBox(height: 16),
        // Galaxy-only stats: diameter, stars, age
        Row(children: [
          _StatBox("DIAMETER", g.diameter, g.color),
          const SizedBox(width: 8),
          _StatBox("STARS", g.stars, g.color),
          const SizedBox(width: 8),
          _StatBox("AGE", g.age, g.color),
        ]),
        const SizedBox(height: 14),
        Container(padding: const EdgeInsets.all(14), decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: Colors.tealAccent.withOpacity(0.06), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("MIND-BLOWING FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
            const SizedBox(height: 8),
            Text(g.fishyFact, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
          ])),
        const SizedBox(height: 16),
      ]),
    ),
  );
}

// ── Black hole detail sheet — ONLY black hole fields ─────────────────────────
class _BlackHoleSheet extends StatelessWidget {
  final _BlackHoleItem b;
  const _BlackHoleSheet(this.b);
  @override
  Widget build(BuildContext context) => DraggableScrollableSheet(
    initialChildSize: 0.72, minChildSize: 0.5, maxChildSize: 0.92,
    builder: (_, ctrl) => Container(
      decoration: BoxDecoration(color: const Color(0xFF040F1F), borderRadius: const BorderRadius.vertical(top: Radius.circular(28)), border: Border.all(color: b.color.withOpacity(0.3))),
      child: ListView(controller: ctrl, padding: const EdgeInsets.all(24), children: [
        Center(child: Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white24, borderRadius: BorderRadius.circular(2)))),
        const SizedBox(height: 20),
        Center(child: Text(b.emoji, style: const TextStyle(fontSize: 72))),
        const SizedBox(height: 12),
        Center(child: Text(b.name, style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: b.color, blurRadius: 20)]))),
        Center(child: Text(b.location, style: GoogleFonts.rajdhani(fontSize: 14, color: b.color))),
        const SizedBox(height: 20),
        Text(b.description, style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, height: 1.6)),
        const SizedBox(height: 16),
        // Black hole-only stats: mass, distance
        Row(children: [
          _StatBox("MASS",     b.mass,     b.color),
          const SizedBox(width: 8),
          _StatBox("DISTANCE", b.distance, b.color),
        ]),
        const SizedBox(height: 14),
        Container(padding: const EdgeInsets.all(14), decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: Colors.tealAccent.withOpacity(0.06), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("MIND-BLOWING FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
            const SizedBox(height: 8),
            Text(b.fishyFact, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
          ])),
        const SizedBox(height: 16),
      ]),
    ),
  );
}

// ── Shared stat box ───────────────────────────────────────────────────────────
Widget _StatBox(String label, String value, Color color) => Expanded(child: Container(
  padding: const EdgeInsets.all(12),
  decoration: BoxDecoration(borderRadius: BorderRadius.circular(12), color: color.withOpacity(0.06), border: Border.all(color: color.withOpacity(0.2))),
  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
    Text(label, style: GoogleFonts.orbitron(fontSize: 7, color: color, letterSpacing: 1.5)),
    const SizedBox(height: 4),
    Text(value, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white, fontWeight: FontWeight.w600, height: 1.3)),
  ]),
));

// ── Data models ───────────────────────────────────────────────────────────────
class _GalaxyItem {
  final String name, emoji, type, description, diameter, stars, age, fishyFact;
  final Color color;
  const _GalaxyItem(this.name, this.emoji, this.color, this.type, this.description, this.diameter, this.stars, this.age, this.fishyFact);
}

class _BlackHoleItem {
  final String name, emoji, location, description, mass, distance, fishyFact;
  final Color color;
  const _BlackHoleItem(this.name, this.emoji, this.color, this.location, this.description, this.mass, this.distance, this.fishyFact);
}

// ── Star painter ──────────────────────────────────────────────────────────────
class _StarPainter extends CustomPainter {
  final double progress;
  static final _rng = Random(77);
  static final _stars = List.generate(150, (_) => Offset(_rng.nextDouble(), _rng.nextDouble()));
  static final _szs = List.generate(150, (_) => _rng.nextDouble() * 1.4 + 0.3);
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

with open("lib/screens/galaxy_screen.dart", "w") as f:
    f.write(content)
print("Done! Lines:", len(content.splitlines()))
