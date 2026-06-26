content = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:animate_do/animate_do.dart';

class BlackHoleScreen extends StatefulWidget {
  const BlackHoleScreen({super.key});
  @override
  State<BlackHoleScreen> createState() => _BlackHoleScreenState();
}

class _BlackHoleScreenState extends State<BlackHoleScreen> with SingleTickerProviderStateMixin {
  late AnimationController _starController;
  @override
  void initState() { super.initState(); _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat(); }
  @override
  void dispose() { _starController.dispose(); super.dispose(); }

  final List<_BHItem> items = [
    _BHItem(name:"Sagittarius A*", emoji:"🕳️", color:Color(0xFF90A4AE), location:"Milky Way Core", imagePath:"assets/images/sagittarius_a.jpg",
      desc:"The supermassive black hole at the center of our Milky Way galaxy. First directly imaged in 2022 by the Event Horizon Telescope after years of effort by 300+ scientists.",
      mass:"4 million solar masses", distance:"26,000 light years",
      fishy:"Photographing Sgr A* took 5 petabytes of data — so much it had to be physically shipped on hard drives from telescopes across 6 continents. Too large to send over the internet."),
    _BHItem(name:"M87*", emoji:"⚫", color:Color(0xFFFFAB91), location:"Virgo Cluster", imagePath:"assets/images/m87.jpg",
      desc:"The first black hole ever photographed in 2019. Located in giant elliptical galaxy M87, it powers a massive relativistic jet visible across millions of light years.",
      mass:"6.5 billion solar masses", distance:"53.5 million light years",
      fishy:"M87's event horizon is so large that our entire Solar System would fit inside it with room to spare. Light takes days to travel from one side to the other."),
    _BHItem(name:"Stellar Black Hole", emoji:"💥", color:Color(0xFFEF9A9A), location:"Throughout Galaxies", imagePath:"assets/images/stellar_bh.jpg",
      desc:"Formed when massive stars (20+ solar masses) die in supernova explosions. The Milky Way contains an estimated 100 million stellar black holes.",
      mass:"5-100 solar masses", distance:"Varies",
      fishy:"Time slows down near a black hole due to gravity. Hover near the event horizon for 1 hour and thousands of years pass on Earth — proven by Einstein's General Relativity."),
    _BHItem(name:"Intermediate BH", emoji:"🌑", color:Color(0xFF80DEEA), location:"Star Clusters", imagePath:"assets/images/intermediate_bh.jpg",
      desc:"A mysterious class between stellar and supermassive black holes. Rarely observed and poorly understood — they may be the missing seeds from which supermassive black holes grew.",
      mass:"100-100,000 solar masses", distance:"Various",
      fishy:"Nobody knows how supermassive black holes grew so huge so fast after the Big Bang. Intermediate black holes may be the answer — but we have almost no direct evidence."),
    _BHItem(name:"Quasar", emoji:"✨", color:Color(0xFFFFE082), location:"Early Universe", imagePath:"assets/images/Quasar.jpg",
      desc:"The most luminous objects in the universe — active galactic nuclei powered by supermassive black holes devouring enormous amounts of matter, outshining entire galaxies.",
      mass:"Billions of solar masses", distance:"Billions of light years",
      fishy:"The most luminous quasar shines 600 TRILLION times brighter than our Sun. Its black hole devours the equivalent of 2 entire suns every single day."),
    _BHItem(name:"Primordial BH", emoji:"🌀", color:Color(0xFFCE93D8), location:"Theoretical", imagePath:"assets/images/primordial_bh.jpg",
      desc:"Hypothetical black holes that may have formed in the first seconds after the Big Bang, before any stars existed. If they exist, they could explain dark matter.",
      mass:"Microscopic to massive", distance:"Unknown",
      fishy:"Some physicists believe microscopic primordial black holes the size of an atom — but with the mass of a mountain — may be constantly passing through Earth right now, undetected."),
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
                Text("BLACK HOLES", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 4, shadows: [Shadow(color: Color(0xFF90A4AE), blurRadius: 15)])),
              ])),
              Expanded(child: ListView(padding: const EdgeInsets.symmetric(horizontal: 16), children: [

                // Hero banner
                FadeInDown(child: ClipRRect(
                  borderRadius: BorderRadius.circular(20),
                  child: SizedBox(height: 170, width: double.infinity, child: Stack(fit: StackFit.expand, children: [
                    Image.asset("assets/images/black_holes.jpg", fit: BoxFit.cover),
                    Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF010914)]))),
                    Positioned(bottom: 14, left: 16, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text("Black Holes", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: Color(0xFF90A4AE), blurRadius: 20)])),
                      Text("Where gravity breaks the laws of physics", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                    ])),
                  ])),
                )),
                const SizedBox(height: 12),

                FadeInUp(child: Container(
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: Colors.white12)),
                  child: Text("A black hole is a region where gravity is so extreme that nothing — not even light — can escape. The boundary of no return is called the event horizon.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white54, height: 1.5)),
                )),
                const SizedBox(height: 16),

                Text("TYPES OF BLACK HOLES", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF90A4AE), letterSpacing: 2)),
                const SizedBox(height: 10),

                ...List.generate(items.length, (i) => FadeInLeft(
                  delay: Duration(milliseconds: 100 + i * 80),
                  child: GestureDetector(
                    onTap: () => showModalBottomSheet(context: context, backgroundColor: Colors.transparent, isScrollControlled: true, builder: (_) => _BHSheet(items[i])),
                    child: Container(
                      margin: const EdgeInsets.only(bottom: 12),
                      height: 110,
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(18),
                        color: const Color(0xFF040F1F),
                        border: Border.all(color: items[i].color.withOpacity(0.25)),
                        boxShadow: [BoxShadow(color: items[i].color.withOpacity(0.08), blurRadius: 16)],
                      ),
                      child: Row(children: [
                        ClipRRect(
                          borderRadius: const BorderRadius.only(topLeft: Radius.circular(18), bottomLeft: Radius.circular(18)),
                          child: SizedBox(width: 110, height: 110, child: Stack(fit: StackFit.expand, children: [
                            Image.asset(items[i].imagePath, fit: BoxFit.cover,
                              errorBuilder: (_, __, ___) => Container(color: items[i].color.withOpacity(0.2),
                                child: Center(child: Text(items[i].emoji, style: const TextStyle(fontSize: 36))))),
                            Positioned(right: 0, child: Container(width: 20, height: 110,
                              decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.transparent, const Color(0xFF040F1F)])))),
                          ])),
                        ),
                        Expanded(child: Padding(
                          padding: const EdgeInsets.all(12),
                          child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.center, children: [
                            Row(children: [
                              Expanded(child: Text(items[i].name, style: GoogleFonts.orbitron(fontSize: 12, fontWeight: FontWeight.w700, color: Colors.white))),
                              Icon(Icons.arrow_forward_ios_rounded, color: items[i].color, size: 13),
                            ]),
                            const SizedBox(height: 3),
                            Text(items[i].location, style: GoogleFonts.rajdhani(fontSize: 12, color: items[i].color)),
                            const SizedBox(height: 2),
                            Text("Mass: ${items[i].mass}", style: GoogleFonts.rajdhani(fontSize: 11, color: Colors.white38)),
                          ]),
                        )),
                      ]),
                    ),
                  ),
                )),

                const SizedBox(height: 8),
                FadeInUp(child: Container(
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: Colors.tealAccent.withOpacity(0.05), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("WILD FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
                    const SizedBox(height: 8),
                    Text("If our Sun suddenly became a black hole, Earth would NOT get sucked in — we'd just freeze in the dark. The gravity would be identical, just concentrated into a tiny point.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
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

class _BHSheet extends StatelessWidget {
  final _BHItem b;
  const _BHSheet(this.b);
  @override
  Widget build(BuildContext context) => DraggableScrollableSheet(
    initialChildSize: 0.75, minChildSize: 0.5, maxChildSize: 0.92,
    builder: (_, ctrl) => Container(
      decoration: BoxDecoration(color: const Color(0xFF040F1F), borderRadius: const BorderRadius.vertical(top: Radius.circular(28)), border: Border.all(color: b.color.withOpacity(0.3))),
      child: ListView(controller: ctrl, padding: EdgeInsets.zero, children: [
        ClipRRect(
          borderRadius: const BorderRadius.vertical(top: Radius.circular(28)),
          child: SizedBox(height: 180, width: double.infinity, child: Stack(fit: StackFit.expand, children: [
            Image.asset(b.imagePath, fit: BoxFit.cover, errorBuilder: (_, __, ___) => Container(color: b.color.withOpacity(0.2))),
            Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF040F1F)]))),
            Positioned(top: 12, left: 0, right: 0, child: Center(child: Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white38, borderRadius: BorderRadius.circular(2))))),
            Positioned(bottom: 14, left: 20, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(b.name, style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: b.color, blurRadius: 20)])),
              Text(b.location, style: GoogleFonts.rajdhani(fontSize: 13, color: b.color)),
            ])),
          ])),
        ),
        Padding(padding: const EdgeInsets.all(20), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(b.desc, style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, height: 1.6)),
          const SizedBox(height: 16),
          Row(children: [_sb("MASS",b.mass,b.color), const SizedBox(width: 10), _sb("DISTANCE",b.distance,b.color)]),
          const SizedBox(height: 14),
          Container(padding: const EdgeInsets.all(14), decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: Colors.tealAccent.withOpacity(0.06), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("MIND-BLOWING FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
              const SizedBox(height: 8),
              Text(b.fishy, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
            ])),
        ])),
      ]),
    ),
  );
}

Widget _sb(String l, String v, Color c) => Expanded(child: Container(
  padding: const EdgeInsets.all(12),
  decoration: BoxDecoration(borderRadius: BorderRadius.circular(12), color: c.withOpacity(0.06), border: Border.all(color: c.withOpacity(0.2))),
  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
    Text(l, style: GoogleFonts.orbitron(fontSize: 7, color: c, letterSpacing: 1.5)),
    const SizedBox(height: 4),
    Text(v, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white, fontWeight: FontWeight.w600, height: 1.3)),
  ]),
));

class _BHItem {
  final String name, emoji, location, desc, mass, distance, fishy, imagePath;
  final Color color;
  const _BHItem({required this.name, required this.emoji, required this.color, required this.location, required this.imagePath, required this.desc, required this.mass, required this.distance, required this.fishy});
}

class _SP extends CustomPainter {
  final double progress;
  static final _rng = Random(33);
  static final _stars = List.generate(150, (_) => Offset(_rng.nextDouble(), _rng.nextDouble()));
  static final _szs = List.generate(150, (_) => _rng.nextDouble() * 1.4 + 0.3);
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

with open("lib/screens/blackhole_screen.dart", "w") as f:
    f.write(content)
print("Black hole screen done!")
