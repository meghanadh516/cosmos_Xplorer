content = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class MultiverseScreen extends StatefulWidget {
  const MultiverseScreen({super.key});
  @override
  State<MultiverseScreen> createState() => _MultiverseScreenState();
}

class _MultiverseScreenState extends State<MultiverseScreen> with SingleTickerProviderStateMixin {
  late AnimationController _starController;
  @override
  void initState() { super.initState(); _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat(); }
  @override
  void dispose() { _starController.dispose(); super.dispose(); }

  final List<_MVItem> theories = [
    _MVItem("Bubble Multiverse","🫧",Color(0xFF90CAF9),"Eternal Inflation Theory","If cosmic inflation never truly stopped, it created countless separate bubble universes — each with their own physical laws, constants, and possibly different forms of matter and energy.","Theoretical — Stephen Hawking's last paper addressed this theory in 2018, just days before his death."),
    _MVItem("Many-Worlds","🌿",Color(0xFF80DEEA),"Quantum Mechanics","Every quantum decision creates a branch — a new universe where the other outcome happened. Every time a particle could go left or right, both happen — in different universes.","This means there may be a universe where you made every different choice in your life. Every decision branches reality."),
    _MVItem("Mathematical Universe","🔢",Color(0xFFFFE082),"Max Tegmark's Hypothesis","All mathematically consistent structures exist as physical realities. Our universe is just one mathematical structure among infinitely many that all physically exist.","If true, there are universes with completely different mathematics — where 2+2 might not equal 4, and the concept of logic itself is different."),
    _MVItem("String Theory Landscape","🎸",Color(0xFFCE93D8),"String Theory","String theory predicts 10⁵⁰⁰ possible universes — each with different physical constants, particle types, and forces. Most would be hostile to life; we exist in one of the rare habitable ones.","10⁵⁰⁰ is a number so incomprehensibly large that writing it out would require more digits than there are atoms in the observable universe."),
    _MVItem("Simulated Universe","💻",Color(0xFF4FC3F7),"Simulation Hypothesis","If advanced civilizations can simulate conscious universes, and if this is possible, the number of simulated universes would vastly outnumber real ones — making it statistically likely we are simulated.","Elon Musk, Neil deGrasse Tyson, and many physicists believe the probability we are NOT in a simulation is less than 1 in a billion."),
    _MVItem("Cyclic Universe","🔄",Color(0xFFFFAB91),"Conformal Cyclic Cosmology","Our universe is just one cycle in an infinite series of Big Bangs and Big Crunches. After each collapse, a new universe is born from the ashes of the old one — forever.","Roger Penrose claims to have found evidence of the previous universe in the cosmic microwave background — circular patterns that may be echoes of black holes from before our Big Bang."),
  ];

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
                Text("MULTIVERSE", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 3)),
              ])),
              Expanded(child: ListView(padding: const EdgeInsets.symmetric(horizontal: 16), children: [

                // Hero image
                ClipRRect(
                  borderRadius: BorderRadius.circular(20),
                  child: SizedBox(height: 180, width: double.infinity, child: Stack(fit: StackFit.expand, children: [
                    Image.asset("assets/images/multiverse.jpg", fit: BoxFit.cover),
                    Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF010914)]))),
                    Positioned(bottom: 14, left: 16, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text("Multiverse", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: Color(0xFFF48FB1), blurRadius: 20)])),
                      Text("Beyond our universe — infinite possibilities", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                    ])),
                  ])),
                ),
                const SizedBox(height: 16),

                Container(padding: const EdgeInsets.all(14), decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: Colors.white12)),
                  child: Text("The multiverse is a hypothetical set of universes beyond our own. While not yet proven, multiple branches of physics independently suggest our universe may not be the only one.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white54, height: 1.5))),
                const SizedBox(height: 20),

                Text("MULTIVERSE THEORIES", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFFF48FB1), letterSpacing: 2)),
                const SizedBox(height: 10),

                ...theories.map((t) => GestureDetector(
                  onTap: () => showModalBottomSheet(context: context, backgroundColor: Colors.transparent, isScrollControlled: true, builder: (_) => _MVSheet(t)),
                  child: Container(
                    margin: const EdgeInsets.only(bottom: 12),
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(borderRadius: BorderRadius.circular(18), color: const Color(0xFF040F1F), border: Border.all(color: t.color.withOpacity(0.25))),
                    child: Row(children: [
                      Container(width: 56, height: 56, decoration: BoxDecoration(shape: BoxShape.circle, color: t.color.withOpacity(0.12), border: Border.all(color: t.color.withOpacity(0.35))),
                        child: Center(child: Text(t.emoji, style: const TextStyle(fontSize: 28)))),
                      const SizedBox(width: 14),
                      Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                        Row(children: [Expanded(child: Text(t.name, style: GoogleFonts.orbitron(fontSize: 13, fontWeight: FontWeight.w700, color: Colors.white))), Icon(Icons.arrow_forward_ios_rounded, color: t.color, size: 13)]),
                        const SizedBox(height: 3),
                        Text(t.theory, style: GoogleFonts.rajdhani(fontSize: 11, color: t.color)),
                        const SizedBox(height: 4),
                        Text(t.desc, maxLines: 2, overflow: TextOverflow.ellipsis, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38, height: 1.3)),
                      ])),
                    ]),
                  ),
                )),

                const SizedBox(height: 8),
                Container(padding: const EdgeInsets.all(16), decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: Colors.tealAccent.withOpacity(0.05), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("ULTIMATE FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
                    const SizedBox(height: 8),
                    Text("If the multiverse exists, then every possible version of your life is being lived somewhere — one where you made every different decision, met different people, and had a completely different existence.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
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

class _MVSheet extends StatelessWidget {
  final _MVItem t;
  const _MVSheet(this.t);
  @override
  Widget build(BuildContext context) => DraggableScrollableSheet(
    initialChildSize: 0.72, minChildSize: 0.5, maxChildSize: 0.92,
    builder: (_, ctrl) => Container(
      decoration: BoxDecoration(color: const Color(0xFF040F1F), borderRadius: const BorderRadius.vertical(top: Radius.circular(28)), border: Border.all(color: t.color.withOpacity(0.3))),
      child: ListView(controller: ctrl, padding: const EdgeInsets.all(24), children: [
        Center(child: Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white24, borderRadius: BorderRadius.circular(2)))),
        const SizedBox(height: 20),
        Center(child: Text(t.emoji, style: const TextStyle(fontSize: 72))),
        const SizedBox(height: 12),
        Center(child: Text(t.name, style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: t.color, blurRadius: 20)]))),
        Center(child: Text(t.theory, style: GoogleFonts.rajdhani(fontSize: 14, color: t.color))),
        const SizedBox(height: 20),
        Text("THE THEORY", style: GoogleFonts.orbitron(fontSize: 9, color: t.color, letterSpacing: 2)),
        const SizedBox(height: 8),
        Text(t.desc, style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, height: 1.6)),
        const SizedBox(height: 16),
        Container(padding: const EdgeInsets.all(14), decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: Colors.tealAccent.withOpacity(0.06), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("MIND-BLOWING FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
            const SizedBox(height: 8),
            Text(t.fishy, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
          ])),
        const SizedBox(height: 16),
      ]),
    ),
  );
}

class _MVItem {
  final String name,emoji,theory,desc,fishy; final Color color;
  const _MVItem(this.name,this.emoji,this.color,this.theory,this.desc,this.fishy);
}

class _SP extends CustomPainter {
  final double progress;
  static final _rng = Random(99);
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

with open("lib/screens/multiverse_screen.dart", "w") as f:
    f.write(content)
print("Done! Lines:", len(content.splitlines()))
