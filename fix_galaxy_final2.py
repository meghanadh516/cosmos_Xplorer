content = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:animate_do/animate_do.dart';

class GalaxyScreen extends StatefulWidget {
  const GalaxyScreen({super.key});
  @override
  State<GalaxyScreen> createState() => _GalaxyScreenState();
}

class _GalaxyScreenState extends State<GalaxyScreen> with SingleTickerProviderStateMixin {
  late AnimationController _starController;
  @override
  void initState() { super.initState(); _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat(); }
  @override
  void dispose() { _starController.dispose(); super.dispose(); }

  final List<_GItem> items = [
    _GItem(name:"Milky Way", emoji:"🌌", color:Color(0xFF7986CB), type:"Barred Spiral", imagePath:"assets/images/milky_way.jpg",
      desc:"Our home galaxy containing 200-400 billion stars. The Solar System sits 26,000 light years from the galactic center.",
      diameter:"100,000 ly", stars:"200-400B stars", age:"13.6B years",
      fishy:"The Milky Way and Andromeda are on a collision course — they will merge in 4.5 billion years into a galaxy called Milkomeda."),
    _GItem(name:"Andromeda", emoji:"🌀", color:Color(0xFF4FC3F7), type:"Spiral", imagePath:"assets/images/andromeda.jpg",
      desc:"The nearest large galaxy to us, visible to the naked eye. It is larger than the Milky Way with over a trillion stars.",
      diameter:"220,000 ly", stars:"1 trillion+ stars", age:"10B years",
      fishy:"Andromeda approaches at 110 km/s. When it hits, the night sky fills with new stars — but the chance of two stars colliding is almost zero."),
    _GItem(name:"Whirlpool", emoji:"🌊", color:Color(0xFF80DEEA), type:"Spiral", imagePath:"assets/images/whirlpool.jpg",
      desc:"A classic spiral galaxy interacting with companion galaxy NGC 5195, triggering bursts of new star formation.",
      diameter:"76,000 ly", stars:"~100B stars", age:"400M years",
      fishy:"The Whirlpool was the first galaxy discovered to have a spiral structure — spotted in 1845 by Lord Rosse in Ireland."),
    _GItem(name:"Sombrero", emoji:"🎩", color:Color(0xFFFFE082), type:"Lenticular", imagePath:"assets/images/sombrero.jpg",
      desc:"Famous for its bright nucleus and dark dust lane resembling a Mexican hat. Located 28 million light years away.",
      diameter:"50,000 ly", stars:"~100B stars", age:"13B years",
      fishy:"The Sombrero has a black hole 1 BILLION times the mass of our Sun — 250x bigger than the Milky Way's own black hole."),
    _GItem(name:"Triangulum", emoji:"🔺", color:Color(0xFFEF9A9A), type:"Spiral", imagePath:"assets/images/triangulum.jpg",
      desc:"Third-largest galaxy in the Local Group. One of the most distant objects visible to the naked eye at 2.7 million light years.",
      diameter:"60,000 ly", stars:"~40B stars", age:"10B years",
      fishy:"Triangulum has NO supermassive black hole at its center — scientists still don't fully understand why."),
    _GItem(name:"Centaurus A", emoji:"💫", color:Color(0xFFCE93D8), type:"Elliptical", imagePath:"assets/images/centaurus.jpg",
      desc:"One of the closest radio galaxies to Earth. A massive black hole shoots jets of particles 13,000 light years into space.",
      diameter:"60,000 ly", stars:"~100B stars", age:"12B years",
      fishy:"Centaurus A shoots relativistic jets at nearly the speed of light — extending 13,000 light years in both directions."),
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
              Padding(padding: const EdgeInsets.fromLTRB(20,16,20,12), child: Row(children: [
                GestureDetector(onTap: () => Navigator.pop(context), child: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white54, size: 20)),
                const SizedBox(width: 16),
                Text("GALAXIES", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 5, shadows: [Shadow(color: Color(0xFF7986CB), blurRadius: 15)])),
              ])),
              Expanded(child: ListView(padding: const EdgeInsets.symmetric(horizontal: 16), children: [

                // Hero banner
                FadeInDown(child: ClipRRect(
                  borderRadius: BorderRadius.circular(20),
                  child: SizedBox(height: 170, width: double.infinity, child: Stack(fit: StackFit.expand, children: [
                    Image.asset("assets/images/galaxy.jpg", fit: BoxFit.cover),
                    Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF010914)]))),
                    Positioned(bottom: 14, left: 16, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text("Galaxies", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: Color(0xFF7986CB), blurRadius: 20)])),
                      Text("2 trillion galaxies in the observable universe", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                    ])),
                  ])),
                )),
                const SizedBox(height: 12),

                FadeInUp(child: Container(
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: Color(0xFF7986CB).withOpacity(0.2))),
                  child: Text("A galaxy is a massive system of stars, gas, dust, and dark matter bound together by gravity. They range from dwarf galaxies with a few million stars to giants with hundreds of trillions.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white60, height: 1.5)),
                )),
                const SizedBox(height: 16),

                Text("TYPES", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF7986CB), letterSpacing: 2)),
                const SizedBox(height: 8),
                Wrap(spacing: 8, runSpacing: 8, children: [
                  _chip("🌀","Spiral",Color(0xFF4FC3F7)),
                  _chip("⭕","Elliptical",Color(0xFFFFE082)),
                  _chip("🔷","Lenticular",Color(0xFFCE93D8)),
                  _chip("🔶","Irregular",Color(0xFFFF8A65)),
                ]),
                const SizedBox(height: 20),

                Text("NOTABLE GALAXIES", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF7986CB), letterSpacing: 2)),
                const SizedBox(height: 10),

                ...List.generate(items.length, (i) => FadeInLeft(
                  delay: Duration(milliseconds: 100 + i * 80),
                  child: GestureDetector(
                    onTap: () => showModalBottomSheet(context: context, backgroundColor: Colors.transparent, isScrollControlled: true, builder: (_) => _Sheet(items[i])),
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
                              errorBuilder: (_, __, ___) => Container(color: items[i].color.withOpacity(0.3),
                                child: Center(child: Text(items[i].emoji, style: const TextStyle(fontSize: 36))))),
                            Positioned(right: 0, child: Container(width: 20, height: 110,
                              decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.transparent, const Color(0xFF040F1F)])))),
                          ])),
                        ),
                        Expanded(child: Padding(
                          padding: const EdgeInsets.all(12),
                          child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.center, children: [
                            Row(children: [
                              Expanded(child: Text(items[i].name, style: GoogleFonts.orbitron(fontSize: 13, fontWeight: FontWeight.w700, color: Colors.white))),
                              Icon(Icons.arrow_forward_ios_rounded, color: items[i].color, size: 13),
                            ]),
                            const SizedBox(height: 4),
                            Container(padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                              decoration: BoxDecoration(borderRadius: BorderRadius.circular(6), color: items[i].color.withOpacity(0.12)),
                              child: Text(items[i].type, style: GoogleFonts.orbitron(fontSize: 7, color: items[i].color))),
                            const SizedBox(height: 4),
                            Text(items[i].desc, maxLines: 2, overflow: TextOverflow.ellipsis,
                              style: GoogleFonts.rajdhani(fontSize: 11, color: Colors.white38, height: 1.3)),
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
                    Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("UNIVERSE FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
                    const SizedBox(height: 8),
                    Text("There are 2 trillion galaxies in the observable universe. If you counted one per second, it would take 63 million years.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
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

Widget _chip(String icon, String label, Color color) => Container(
  padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 7),
  decoration: BoxDecoration(borderRadius: BorderRadius.circular(10), color: color.withOpacity(0.08), border: Border.all(color: color.withOpacity(0.3))),
  child: Row(mainAxisSize: MainAxisSize.min, children: [Text(icon, style: const TextStyle(fontSize: 14)), const SizedBox(width: 6), Text(label, style: GoogleFonts.rajdhani(fontSize: 13, color: color, fontWeight: FontWeight.w600))]),
);

class _Sheet extends StatelessWidget {
  final _GItem g;
  const _Sheet(this.g);
  @override
  Widget build(BuildContext context) => DraggableScrollableSheet(
    initialChildSize: 0.75, minChildSize: 0.5, maxChildSize: 0.92,
    builder: (_, ctrl) => Container(
      decoration: BoxDecoration(color: const Color(0xFF040F1F), borderRadius: const BorderRadius.vertical(top: Radius.circular(28)), border: Border.all(color: g.color.withOpacity(0.3))),
      child: ListView(controller: ctrl, padding: EdgeInsets.zero, children: [
        ClipRRect(
          borderRadius: const BorderRadius.vertical(top: Radius.circular(28)),
          child: SizedBox(height: 180, width: double.infinity, child: Stack(fit: StackFit.expand, children: [
            Image.asset(g.imagePath, fit: BoxFit.cover, errorBuilder: (_, __, ___) => Container(color: g.color.withOpacity(0.2))),
            Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF040F1F)]))),
            Positioned(top: 12, left: 0, right: 0, child: Center(child: Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white38, borderRadius: BorderRadius.circular(2))))),
            Positioned(bottom: 14, left: 20, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(g.name, style: GoogleFonts.orbitron(fontSize: 26, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: g.color, blurRadius: 20)])),
              Text(g.type, style: GoogleFonts.rajdhani(fontSize: 14, color: g.color)),
            ])),
          ])),
        ),
        Padding(padding: const EdgeInsets.all(20), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(g.desc, style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, height: 1.6)),
          const SizedBox(height: 16),
          Row(children: [_sb("DIAMETER",g.diameter,g.color), const SizedBox(width: 8), _sb("STARS",g.stars,g.color), const SizedBox(width: 8), _sb("AGE",g.age,g.color)]),
          const SizedBox(height: 14),
          Container(padding: const EdgeInsets.all(14), decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: Colors.tealAccent.withOpacity(0.06), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("MIND-BLOWING FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
              const SizedBox(height: 8),
              Text(g.fishy, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
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

class _GItem {
  final String name, emoji, type, desc, diameter, stars, age, fishy, imagePath;
  final Color color;
  const _GItem({required this.name, required this.emoji, required this.color, required this.type, required this.imagePath, required this.desc, required this.diameter, required this.stars, required this.age, required this.fishy});
}

class _SP extends CustomPainter {
  final double progress;
  static final _rng = Random(77);
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

with open("lib/screens/galaxy_screen.dart", "w") as f:
    f.write(content)
print("Galaxy done!")
