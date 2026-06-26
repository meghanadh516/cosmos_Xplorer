content = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:animate_do/animate_do.dart';

class MultiverseScreen extends StatefulWidget {
  const MultiverseScreen({super.key});
  @override
  State<MultiverseScreen> createState() => _MultiverseScreenState();
}

class _MultiverseScreenState extends State<MultiverseScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _starController;
  @override
  void initState() { super.initState(); _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat(); }
  @override
  void dispose() { _starController.dispose(); super.dispose(); }

  final List<_MVItem> theories = [
    _MVItem(name:"Bubble Multiverse", emoji:"🫧", color:Color(0xFF90CAF9), theory:"Eternal Inflation",
      desc:"If cosmic inflation never truly stopped, it created countless separate bubble universes — each with their own physical laws, constants, and possibly different forms of matter and energy.",
      evidence:"Supported by string theory and inflationary cosmology. Stephen Hawking's last paper in 2018 addressed this theory.",
      fishy:"There may be a bubble universe where the laws of physics are so different that atoms cannot form — making it an ocean of pure energy with no matter at all."),
    _MVItem(name:"Many-Worlds", emoji:"🌿", color:Color(0xFF80DEEA), theory:"Quantum Mechanics",
      desc:"Every quantum decision creates a branch — a new universe where the other outcome happened. Every time a particle could go left or right, both happen in different universes.",
      evidence:"Proposed by Hugh Everett in 1957. Supported by many quantum physicists including Stephen Hawking.",
      fishy:"Right now, infinite versions of you exist — ones who made every different choice, took different careers, and lived completely different lives."),
    _MVItem(name:"Mathematical Universe", emoji:"🔢", color:Color(0xFFFFE082), theory:"Max Tegmark",
      desc:"All mathematically consistent structures exist as physical realities. Our universe is just one mathematical structure among infinitely many that all physically exist.",
      evidence:"Proposed by MIT physicist Max Tegmark. Controversial but mathematically rigorous.",
      fishy:"In some mathematical universes, 2+2 might not equal 4. The concept of logic itself could be completely different from what we know."),
    _MVItem(name:"String Landscape", emoji:"🎸", color:Color(0xFFCE93D8), theory:"String Theory",
      desc:"String theory predicts 10500 possible universes — each with different physical constants, particle types, and forces. Most would be hostile to life.",
      evidence:"Emerges naturally from string theory mathematics. Supported by Leonard Susskind and others.",
      fishy:"10500 is so large that writing it out would require more digits than there are atoms in the observable universe."),
    _MVItem(name:"Simulation Theory", emoji:"💻", color:Color(0xFF4FC3F7), theory:"Simulation Hypothesis",
      desc:"If advanced civilizations can simulate conscious universes, the number of simulated universes would vastly outnumber real ones — making it statistically likely we are simulated.",
      evidence:"Supported by Nick Bostrom's simulation argument. Elon Musk and many physicists take it seriously.",
      fishy:"If we are simulated, the simulators could pause, rewind, or delete our entire universe at any moment — and we would never know."),
    _MVItem(name:"Cyclic Universe", emoji:"🔄", color:Color(0xFFFFAB91), theory:"Roger Penrose",
      desc:"Our universe is one cycle in an infinite series of Big Bangs and Big Crunches. After each collapse, a new universe is born from the ashes of the old one — forever.",
      evidence:"Roger Penrose claims to have found circular patterns in the cosmic microwave background — echoes from the previous universe.",
      fishy:"If true, our universe is not special — it is one of infinite cycles, and the previous universe may have contained its own stars, planets, and perhaps life."),
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
                Text("MULTIVERSE", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 4, shadows: [Shadow(color: Color(0xFFF48FB1), blurRadius: 15)])),
              ])),
              Expanded(child: ListView(padding: const EdgeInsets.symmetric(horizontal: 16), children: [

                // Hero image
                FadeInDown(child: ClipRRect(
                  borderRadius: BorderRadius.circular(20),
                  child: SizedBox(height: 180, width: double.infinity, child: Stack(fit: StackFit.expand, children: [
                    Image.asset("assets/images/multiverse.jpg", fit: BoxFit.cover),
                    Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF010914)]))),
                    Positioned(bottom: 14, left: 16, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text("Multiverse", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: Color(0xFFF48FB1), blurRadius: 20)])),
                      Text("Beyond our universe — infinite possibilities", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                    ])),
                  ])),
                )),
                const SizedBox(height: 12),

                // What is multiverse
                FadeInUp(child: Container(
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: Color(0xFFF48FB1).withOpacity(0.2))),
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Text("WHAT IS THE MULTIVERSE?", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFFF48FB1), letterSpacing: 2)),
                    const SizedBox(height: 8),
                    Text("The multiverse is a hypothetical collection of universes beyond our own. While not yet proven, multiple independent branches of physics suggest our universe may be just one of infinitely many.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white60, height: 1.5)),
                  ]),
                )),
                const SizedBox(height: 16),

                // Status badges
                FadeInUp(delay: Duration(milliseconds: 100), child: Row(children: [
                  _badge("🔬", "Not Yet Proven", Color(0xFFEF9A9A)),
                  const SizedBox(width: 8),
                  _badge("🧮", "Mathematically Possible", Color(0xFF90CAF9)),
                  const SizedBox(width: 8),
                  _badge("🌌", "Scientifically Serious", Color(0xFF80DEEA)),
                ])),
                const SizedBox(height: 20),

                // Section header
                FadeInLeft(child: Row(children: [
                  Container(width: 4, height: 20, decoration: BoxDecoration(color: Color(0xFFF48FB1), borderRadius: BorderRadius.circular(2))),
                  const SizedBox(width: 10),
                  Text("MULTIVERSE THEORIES", style: GoogleFonts.orbitron(fontSize: 11, color: Color(0xFFF48FB1), letterSpacing: 2, fontWeight: FontWeight.w700)),
                ])),
                const SizedBox(height: 12),

                // Theory cards
                ...List.generate(theories.length, (i) => FadeInLeft(
                  delay: Duration(milliseconds: 100 + i * 80),
                  child: GestureDetector(
                    onTap: () => showModalBottomSheet(context: context, backgroundColor: Colors.transparent, isScrollControlled: true, builder: (_) => _MVSheet(theories[i])),
                    child: Container(
                      margin: const EdgeInsets.only(bottom: 12),
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(18),
                        color: const Color(0xFF040F1F),
                        border: Border.all(color: theories[i].color.withOpacity(0.3)),
                        boxShadow: [BoxShadow(color: theories[i].color.withOpacity(0.07), blurRadius: 16)],
                      ),
                      child: Row(children: [
                        Container(
                          width: 60, height: 60,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: theories[i].color.withOpacity(0.12),
                            border: Border.all(color: theories[i].color.withOpacity(0.4), width: 1.5),
                          ),
                          child: Center(child: Text(theories[i].emoji, style: const TextStyle(fontSize: 28))),
                        ),
                        const SizedBox(width: 14),
                        Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                          Row(children: [
                            Expanded(child: Text(theories[i].name, style: GoogleFonts.orbitron(fontSize: 13, fontWeight: FontWeight.w700, color: Colors.white))),
                            Icon(Icons.arrow_forward_ios_rounded, color: theories[i].color, size: 13),
                          ]),
                          const SizedBox(height: 3),
                          Container(padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                            decoration: BoxDecoration(borderRadius: BorderRadius.circular(6), color: theories[i].color.withOpacity(0.12)),
                            child: Text(theories[i].theory, style: GoogleFonts.orbitron(fontSize: 7, color: theories[i].color))),
                          const SizedBox(height: 5),
                          Text(theories[i].desc, maxLines: 2, overflow: TextOverflow.ellipsis,
                            style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38, height: 1.3)),
                        ])),
                      ]),
                    ),
                  ),
                )),

                const SizedBox(height: 16),

                // Ultimate fact
                FadeInUp(child: Container(
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: Colors.tealAccent.withOpacity(0.05), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("ULTIMATE FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
                    const SizedBox(height: 8),
                    Text("If the multiverse exists, every possible version of your life is being lived somewhere — one where you made every different decision, met different people, and had a completely different existence.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
                  ])),
                ),
                const SizedBox(height: 24),
              ])),
            ]),
          ),
        ],
      ),
    );
  }
}

Widget _badge(String icon, String label, Color color) => Expanded(child: Container(
  padding: const EdgeInsets.symmetric(vertical: 8),
  decoration: BoxDecoration(borderRadius: BorderRadius.circular(10), color: color.withOpacity(0.08), border: Border.all(color: color.withOpacity(0.3))),
  child: Column(children: [
    Text(icon, style: const TextStyle(fontSize: 18)),
    const SizedBox(height: 4),
    Text(label, style: GoogleFonts.orbitron(fontSize: 6.5, color: color, letterSpacing: 0.5), textAlign: TextAlign.center),
  ]),
));

class _MVSheet extends StatelessWidget {
  final _MVItem t;
  const _MVSheet(this.t);
  @override
  Widget build(BuildContext context) => DraggableScrollableSheet(
    initialChildSize: 0.75, minChildSize: 0.5, maxChildSize: 0.92,
    builder: (_, ctrl) => Container(
      decoration: BoxDecoration(color: const Color(0xFF040F1F), borderRadius: const BorderRadius.vertical(top: Radius.circular(28)), border: Border.all(color: t.color.withOpacity(0.3))),
      child: ListView(controller: ctrl, padding: const EdgeInsets.all(24), children: [
        Center(child: Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white24, borderRadius: BorderRadius.circular(2)))),
        const SizedBox(height: 20),
        Center(child: Container(
          width: 90, height: 90,
          decoration: BoxDecoration(shape: BoxShape.circle, color: t.color.withOpacity(0.12), border: Border.all(color: t.color.withOpacity(0.4), width: 2)),
          child: Center(child: Text(t.emoji, style: const TextStyle(fontSize: 44))),
        )),
        const SizedBox(height: 16),
        Center(child: Text(t.name, style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: t.color, blurRadius: 20)]))),
        Center(child: Container(margin: const EdgeInsets.only(top: 6), padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 4),
          decoration: BoxDecoration(borderRadius: BorderRadius.circular(8), color: t.color.withOpacity(0.15)),
          child: Text(t.theory, style: GoogleFonts.orbitron(fontSize: 9, color: t.color, letterSpacing: 1)))),
        const SizedBox(height: 20),

        Text("THE THEORY", style: GoogleFonts.orbitron(fontSize: 9, color: t.color, letterSpacing: 2)),
        const SizedBox(height: 8),
        Text(t.desc, style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, height: 1.6)),
        const SizedBox(height: 16),

        Text("SCIENTIFIC BASIS", style: GoogleFonts.orbitron(fontSize: 9, color: t.color, letterSpacing: 2)),
        const SizedBox(height: 8),
        Container(padding: const EdgeInsets.all(12), decoration: BoxDecoration(borderRadius: BorderRadius.circular(12), color: t.color.withOpacity(0.06), border: Border.all(color: t.color.withOpacity(0.2))),
          child: Text(t.evidence, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white60, height: 1.5))),
        const SizedBox(height: 14),

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
  final String name, emoji, theory, desc, evidence, fishy;
  final Color color;
  const _MVItem({required this.name, required this.emoji, required this.color, required this.theory, required this.desc, required this.evidence, required this.fishy});
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
