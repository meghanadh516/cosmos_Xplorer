galaxy = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

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
    _GItem("Milky Way","🌌",Color(0xFF7986CB),"Barred Spiral","Our home galaxy containing 200–400 billion stars. The Solar System sits 26,000 light years from the galactic center, on a minor spiral arm called the Orion Arm.","100,000 ly","200-400B stars","13.6B years","The Milky Way and Andromeda galaxy are on a collision course — they will merge in about 4.5 billion years into a giant elliptical galaxy astronomers call Milkomeda."),
    _GItem("Andromeda","🌀",Color(0xFF4FC3F7),"Spiral","The nearest large galaxy to us, visible to the naked eye on a clear night. It is larger than the Milky Way with over a trillion stars and is heading straight toward us.","220,000 ly","1 trillion+ stars","10B years","Andromeda is approaching us at 110 km per second. When it collides, the night sky will be filled with millions of new stars — but the actual chance of two stars physically colliding is almost zero."),
    _GItem("Whirlpool","🌊",Color(0xFF80DEEA),"Spiral","A classic spiral galaxy interacting with companion galaxy NGC 5195. The gravitational interaction between them is triggering bursts of new star formation.","76,000 ly","~100B stars","400M years","The Whirlpool Galaxy was the first galaxy ever discovered to have a spiral structure — spotted in 1845 by Lord Rosse using a hand-built telescope in a field in Ireland."),
    _GItem("Sombrero","🎩",Color(0xFFFFE082),"Lenticular","Famous for its bright nucleus and dark dust lane resembling a Mexican hat. Located 28 million light years away in the Virgo constellation.","50,000 ly","~100B stars","13B years","The Sombrero Galaxy has a supermassive black hole 1 BILLION times the mass of our Sun at its center — 250 times bigger than the Milky Way's own black hole, Sagittarius A*."),
    _GItem("Triangulum","🔺",Color(0xFFEF9A9A),"Spiral","The third-largest galaxy in the Local Group. One of the most distant objects ever visible to the naked eye — at 2.7 million light years away.","60,000 ly","~40B stars","10B years","Unlike most large galaxies, Triangulum appears to have NO supermassive black hole at its center. Scientists still don't fully understand why — making it one of the biggest mysteries in galaxy formation."),
    _GItem("Centaurus A","💫",Color(0xFFCE93D8),"Elliptical","One of the closest radio galaxies to Earth. A massive black hole at its center shoots jets of high-energy particles that extend 13,000 light years into space.","60,000 ly","~100B stars","12B years","Centaurus A's central black hole shoots relativistic jets — streams of particles moving at nearly the speed of light. These jets extend for 13,000 light years and are visible across the electromagnetic spectrum."),
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
                Text("GALAXIES", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 4)),
              ])),
              Expanded(child: ListView(padding: const EdgeInsets.symmetric(horizontal: 16), children: [
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
                ...items.map((g) => GestureDetector(
                  onTap: () => showModalBottomSheet(context: context, backgroundColor: Colors.transparent, isScrollControlled: true, builder: (_) => _Sheet(g)),
                  child: Container(
                    margin: const EdgeInsets.only(bottom: 12),
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(borderRadius: BorderRadius.circular(18), color: const Color(0xFF040F1F), border: Border.all(color: g.color.withOpacity(0.25))),
                    child: Row(children: [
                      Container(width: 56, height: 56, decoration: BoxDecoration(shape: BoxShape.circle, color: g.color.withOpacity(0.15), border: Border.all(color: g.color.withOpacity(0.4))),
                        child: Center(child: Text(g.emoji, style: const TextStyle(fontSize: 28)))),
                      const SizedBox(width: 14),
                      Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                        Row(children: [Text(g.name, style: GoogleFonts.orbitron(fontSize: 14, fontWeight: FontWeight.w700, color: Colors.white)), const Spacer(), Icon(Icons.arrow_forward_ios_rounded, color: g.color, size: 13)]),
                        const SizedBox(height: 3),
                        Row(children: [
                          Container(padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2), decoration: BoxDecoration(borderRadius: BorderRadius.circular(6), color: g.color.withOpacity(0.12)), child: Text(g.type, style: GoogleFonts.orbitron(fontSize: 7, color: g.color))),
                          const SizedBox(width: 8),
                          Text(g.stars, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
                        ]),
                        const SizedBox(height: 4),
                        Text(g.desc, maxLines: 2, overflow: TextOverflow.ellipsis, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38, height: 1.3)),
                      ])),
                    ]),
                  ),
                )),
                const SizedBox(height: 8),
                Container(padding: const EdgeInsets.all(16), decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: Colors.tealAccent.withOpacity(0.05), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("UNIVERSE FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
                    const SizedBox(height: 8),
                    Text("There are 2 trillion galaxies in the observable universe. If you counted one per second non-stop, it would take 63 million years to count them all.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
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
        const SizedBox(height: 16),
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
  final String name,emoji,type,desc,diameter,stars,age,fishy; final Color color;
  const _GItem(this.name,this.emoji,this.color,this.type,this.desc,this.diameter,this.stars,this.age,this.fishy);
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
      final t = 0.3 + 0.7*(0.5+0.5*sin(progress*2*pi*2+i));
      paint.color = Colors.white.withOpacity(t*0.7);
      canvas.drawCircle(Offset(_stars[i].dx*size.width,_stars[i].dy*size.height),_szs[i],paint);
    }
  }
  @override bool shouldRepaint(_) => true;
}
"""

blackhole = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

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
    _BHItem("Sagittarius A*","🕳️",Color(0xFF90A4AE),"Milky Way Core","The supermassive black hole at the center of our Milky Way galaxy. First directly imaged in 2022 by the Event Horizon Telescope after years of effort by 300+ scientists.","4 million solar masses","26,000 light years","Photographing Sgr A* took 5 petabytes of data — so much that it had to be physically shipped on hard drives from radio telescopes across 6 continents. It could not be sent over the internet."),
    _BHItem("M87*","⚫",Color(0xFFFFAB91),"Virgo Cluster","The first black hole ever photographed in 2019. Located in giant elliptical galaxy M87, it powers a massive relativistic jet visible across millions of light years.","6.5 billion solar masses","53.5 million light years","M87*'s event horizon is so large that our entire Solar System would fit inside it with room to spare. Light takes days to travel from one side of the event horizon to the other."),
    _BHItem("Stellar Black Hole","💥",Color(0xFFEF9A9A),"Throughout Galaxies","Formed when massive stars (20+ solar masses) die in supernova explosions. The Milky Way alone contains an estimated 100 million stellar black holes — we just can't see most of them.","5–100 solar masses","Varies","Time slows down near a black hole due to gravity. If you hovered just outside the event horizon for 1 hour, thousands of years could pass on Earth. This is called gravitational time dilation — proven by Einstein's General Relativity."),
    _BHItem("Intermediate BH","🌑",Color(0xFF80DEEA),"Star Clusters","A mysterious class between stellar and supermassive black holes. Rarely observed and poorly understood — they may be the missing seeds from which supermassive black holes grew.","100–100,000 solar masses","Various","Nobody knows how supermassive black holes grew so enormous so fast after the Big Bang. Intermediate black holes may be the answer — but we have almost no direct evidence of their existence."),
    _BHItem("Quasar","✨",Color(0xFFFFE082),"Early Universe","The most luminous objects in the universe — active galactic nuclei powered by supermassive black holes devouring enormous amounts of matter. They can outshine entire galaxies.","Billions of solar masses","Billions of light years","The most luminous quasar ever discovered shines 600 TRILLION times brighter than our Sun. Its black hole devours the equivalent of 2 entire suns every single day to maintain that brightness."),
    _BHItem("Primordial BH","🌀",Color(0xFFCE93D8),"Theoretical","Hypothetical black holes that may have formed in the first seconds after the Big Bang, before any stars existed. If they exist, they could explain dark matter — one of the universe's biggest mysteries.","Microscopic to massive","Unknown","Some physicists believe microscopic primordial black holes the size of an atom — but with the mass of a mountain — may be constantly passing through Earth right now, completely undetected."),
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
                Text("BLACK HOLES", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 3)),
              ])),
              Expanded(child: ListView(padding: const EdgeInsets.symmetric(horizontal: 16), children: [
                Container(padding: const EdgeInsets.all(14), decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: Colors.white12)),
                  child: Text("A black hole is a point in space where gravity is so extreme that nothing — not even light — can escape. The boundary of no return is called the event horizon.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white54, height: 1.5))),
                const SizedBox(height: 16),
                Text("TYPES OF BLACK HOLES", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF90A4AE), letterSpacing: 2)),
                const SizedBox(height: 10),
                ...items.map((b) => GestureDetector(
                  onTap: () => showModalBottomSheet(context: context, backgroundColor: Colors.transparent, isScrollControlled: true, builder: (_) => _BHSheet(b)),
                  child: Container(
                    margin: const EdgeInsets.only(bottom: 12),
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(borderRadius: BorderRadius.circular(18), color: const Color(0xFF040F1F), border: Border.all(color: b.color.withOpacity(0.25))),
                    child: Row(children: [
                      Container(width: 56, height: 56, decoration: BoxDecoration(shape: BoxShape.circle, color: b.color.withOpacity(0.1), border: Border.all(color: b.color.withOpacity(0.3))),
                        child: Center(child: Text(b.emoji, style: const TextStyle(fontSize: 28)))),
                      const SizedBox(width: 14),
                      Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                        Row(children: [Expanded(child: Text(b.name, style: GoogleFonts.orbitron(fontSize: 13, fontWeight: FontWeight.w700, color: Colors.white))), Icon(Icons.arrow_forward_ios_rounded, color: b.color, size: 13)]),
                        const SizedBox(height: 3),
                        Text(b.location, style: GoogleFonts.rajdhani(fontSize: 12, color: b.color)),
                        Text("Mass: ${b.mass}", style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
                      ])),
                    ]),
                  ),
                )),
                const SizedBox(height: 8),
                Container(padding: const EdgeInsets.all(16), decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: Colors.tealAccent.withOpacity(0.05), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
                  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Row(children: [const Text("🐟", style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text("WILD FACT", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
                    const SizedBox(height: 8),
                    Text("If our Sun suddenly became a black hole, Earth would NOT get sucked in — we'd just freeze in the dark. The gravity would be identical, just concentrated into a tiny point.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
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

class _BHSheet extends StatelessWidget {
  final _BHItem b;
  const _BHSheet(this.b);
  @override
  Widget build(BuildContext context) => DraggableScrollableSheet(
    initialChildSize: 0.75, minChildSize: 0.5, maxChildSize: 0.92,
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
        const SizedBox(height: 16),
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
  final String name,emoji,location,desc,mass,distance,fishy; final Color color;
  const _BHItem(this.name,this.emoji,this.color,this.location,this.desc,this.mass,this.distance,this.fishy);
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

universe = r"""import 'dart:math';
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
                // Hero
                Container(height: 160, decoration: BoxDecoration(borderRadius: BorderRadius.circular(24), gradient: RadialGradient(colors: [Color(0xFF1A237E), Color(0xFF010914)], radius: 1.2)),
                  child: Stack(children: [
                    Center(child: Text("🔭", style: TextStyle(fontSize: 80))),
                    Positioned(bottom: 16, left: 20, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text("Observable Universe", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: Color(0xFF90CAF9), blurRadius: 20)])),
                      Text("93 billion light years across", style: GoogleFonts.rajdhani(fontSize: 13, color: Color(0xFF90CAF9))),
                    ])),
                  ])),
                const SizedBox(height: 20),

                Text("WHAT IS THE UNIVERSE?", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF90CAF9), letterSpacing: 2)),
                const SizedBox(height: 8),
                Text("The Universe is everything that exists — all space, time, matter, and energy. It began 13.8 billion years ago with the Big Bang, a rapid expansion from an incredibly hot and dense state. It has been expanding ever since — and the expansion is accelerating.", style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, height: 1.6)),
                const SizedBox(height: 20),

                Text("KEY FACTS", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF90CAF9), letterSpacing: 2)),
                const SizedBox(height: 10),
                ...[
                  ["🕰️","Age","13.8 billion years",Color(0xFFFFE082)],
                  ["📏","Observable Size","93 billion light years",Color(0xFF90CAF9)],
                  ["🌌","Galaxies","~2 trillion galaxies",Color(0xFF7986CB)],
                  ["⭐","Stars","~10²⁴ (septillion)",Color(0xFFFFB300)],
                  ["🌡️","Avg Temperature","2.7 Kelvin (-270°C)",Color(0xFF80DEEA)],
                  ["💨","Expansion Rate","~70 km/s per megaparsec",Color(0xFFCE93D8)],
                  ["🌑","Dark Matter","27% of universe",Color(0xFF90A4AE)],
                  ["⚡","Dark Energy","68% of universe",Color(0xFFEF9A9A)],
                  ["⚛️","Normal Matter","Only 5% of universe",Color(0xFF4FC3F7)],
                ].map((f) => Container(
                  margin: const EdgeInsets.only(bottom: 8),
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: (f[3] as Color).withOpacity(0.2))),
                  child: Row(children: [
                    Text(f[0] as String, style: const TextStyle(fontSize: 22)),
                    const SizedBox(width: 12),
                    Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text(f[1] as String, style: GoogleFonts.orbitron(fontSize: 8, color: f[3] as Color, letterSpacing: 1.5)),
                      Text(f[2] as String, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white, fontWeight: FontWeight.w600)),
                    ])),
                  ]),
                )),
                const SizedBox(height: 20),

                Text("THE BIG BANG TIMELINE", style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF90CAF9), letterSpacing: 2)),
                const SizedBox(height: 10),
                ...[
                  ["💥","10⁻⁴³ seconds","Planck Epoch — laws of physics break down. Temperature: 10³² K",Color(0xFFEF9A9A)],
                  ["⚛️","First 3 minutes","Protons and neutrons form. Universe cools enough for nuclei.",Color(0xFFFFAB91)],
                  ["💡","380,000 years","First light — atoms form, universe becomes transparent.",Color(0xFFFFE082)],
                  ["⭐","200M years","First stars ignite, ending the cosmic dark ages.",Color(0xFF90CAF9)],
                  ["🌌","1B years","First galaxies form and grow.",Color(0xFF7986CB)],
                  ["☀️","9.2B years","Our Solar System forms.",Color(0xFFFFB300)],
                  ["🧬","13.5B years","Life emerges on Earth.",Color(0xFF4FC3F7)],
                  ["👁️","13.8B years","Now — you are here.",Color(0xFF80DEEA)],
                ].map((e) => Container(
                  margin: const EdgeInsets.only(bottom: 10),
                  child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Column(children: [
                      Container(width: 36, height: 36, decoration: BoxDecoration(shape: BoxShape.circle, color: (e[3] as Color).withOpacity(0.15), border: Border.all(color: (e[3] as Color).withOpacity(0.4))),
                        child: Center(child: Text(e[0] as String, style: const TextStyle(fontSize: 16)))),
                    ]),
                    const SizedBox(width: 12),
                    Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text(e[1] as String, style: GoogleFonts.orbitron(fontSize: 9, color: e[3] as Color, letterSpacing: 1)),
                      const SizedBox(height: 3),
                      Text(e[2] as String, style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60, height: 1.4)),
                    ])),
                  ]),
                )),
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

multiverse = r"""import 'dart:math';
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
                Container(height: 140, decoration: BoxDecoration(borderRadius: BorderRadius.circular(24), gradient: RadialGradient(colors: [Color(0xFF4A148C), Color(0xFF010914)], radius: 1.2)),
                  child: Stack(children: [
                    Center(child: Text("♾️", style: TextStyle(fontSize: 72))),
                    Positioned(bottom: 16, left: 20, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text("Beyond Our Universe", style: GoogleFonts.orbitron(fontSize: 16, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: Color(0xFFF48FB1), blurRadius: 20)])),
                      Text("Theoretical · Not yet proven", style: GoogleFonts.rajdhani(fontSize: 13, color: Color(0xFFF48FB1))),
                    ])),
                  ])),
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

with open("lib/screens/galaxy_screen.dart","w") as f: f.write(galaxy)
with open("lib/screens/blackhole_screen.dart","w") as f: f.write(blackhole)
with open("lib/screens/universe_screen.dart","w") as f: f.write(universe)
with open("lib/screens/multiverse_screen.dart","w") as f: f.write(multiverse)
print("galaxy:", len(galaxy.splitlines()), "lines")
print("blackhole:", len(blackhole.splitlines()), "lines")
print("universe:", len(universe.splitlines()), "lines")
print("multiverse:", len(multiverse.splitlines()), "lines")
