content = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class BlackHolesScreen extends StatefulWidget {
  const BlackHolesScreen({super.key});
  @override
  State<BlackHolesScreen> createState() => _BlackHolesScreenState();
}

class _BlackHolesScreenState extends State<BlackHolesScreen>
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

  final List<_BHType> types = [
    _BHType('💥', 'Stellar Black Hole', Color(0xFFEF9A9A), '5 – 100 solar masses',
        'Born when a massive star (20+ solar masses) exhausts its fuel and collapses in a supernova explosion. The core crushes down to a singularity smaller than an atom.',
        'The Milky Way alone contains an estimated 100 million stellar black holes — but we can barely detect them because they emit no light.',
        ['Born in supernova explosions', 'Most common type', '~100 million in Milky Way', 'Size of a city, mass of a star']),
    _BHType('🌑', 'Intermediate Black Hole', Color(0xFF80DEEA), '100 – 100,000 solar masses',
        'A mysterious middle ground between stellar and supermassive black holes. Rarely observed and poorly understood. They may form in dense star clusters through repeated mergers.',
        'Nobody knows how supermassive black holes grew so large so fast after the Big Bang. Intermediate black holes may be the missing link — but direct evidence is almost nonexistent.',
        ['Extremely rare observations', 'Found in star clusters', 'May seed supermassive BHs', 'Still poorly understood']),
    _BHType('⚫', 'Supermassive Black Hole', Color(0xFFFFAB91), 'Millions – billions of solar masses',
        'Lurking at the centre of nearly every large galaxy, including our own Milky Way. How they formed so early in the universe history is one of the biggest unsolved mysteries in astronomy.',
        'Sagittarius A*, our galaxy own black hole, is 4 million times the mass of the Sun — yet if you stood on the edge of its event horizon, it would look no larger than a full moon in our sky.',
        ['Centre of most galaxies', 'Mass of millions of suns', 'First ones photographed', 'Power quasars and AGN']),
    _BHType('✨', 'Primordial Black Hole', Color(0xFFFFE082), 'Sub-atomic to stellar',
        'Hypothetical black holes that may have formed in the extreme density of the early universe, fractions of a second after the Big Bang — before any stars existed.',
        'Some physicists believe primordial black holes could make up a significant fraction of dark matter. We have never confirmed their existence, but we have not ruled them out either.',
        ['Never directly confirmed', 'Formed in early universe', 'Possible dark matter candidate', 'Can be microscopic']),
  ];

  final List<_FamousBH> famous = [
    _FamousBH('Sagittarius A*', '⚫', Color(0xFF90A4AE), 'Milky Way Centre', '4 million solar masses', '26,000 light years',
        'The supermassive black hole at the heart of our own galaxy. Stars near it orbit at thousands of km/s. First directly imaged in 2022 by the Event Horizon Telescope.',
        'The 2022 image required linking radio telescopes across the entire Earth. The data — 5 petabytes — had to be physically flown on hard drives from Antarctica because the internet there is too slow.'),
    _FamousBH('M87*', '🕳️', Color(0xFFFFAB91), 'Galaxy M87, Virgo Cluster', '6.5 billion solar masses', '53.5 million light years',
        'The first black hole ever photographed, in 2019. Its event horizon is so large our entire Solar System would fit inside it. It powers a relativistic jet stretching 5,000 light years.',
        'The iconic first image of M87* was made possible by Katie Bouman, a 29-year-old scientist who wrote the key algorithm that reconstructed the image from telescope data around the world.'),
    _FamousBH('TON 618', '🌀', Color(0xFFCE93D8), 'Canes Venatici constellation', '66 billion solar masses', '10.4 billion light years',
        'One of the most massive black holes ever discovered. A hyperluminous quasar whose black hole outweighs our entire galaxy. Its event horizon is larger than our Solar System by a factor of 13.',
        'TON 618 event horizon alone would extend 13 times beyond Neptune orbit. The entire Solar System would be swallowed whole inside it.'),
    _FamousBH('Cygnus X-1', '💫', Color(0xFF4FC3F7), 'Cygnus constellation', '~21 solar masses', '7,200 light years',
        'One of the first black hole candidates ever identified. Subject of a famous bet between Stephen Hawking and Kip Thorne. It feeds off a companion blue supergiant star.',
        'Stephen Hawking bet Kip Thorne in 1974 that Cygnus X-1 was NOT a black hole — insuring himself against his own research being wrong. He conceded in 1990. Thorne won a magazine subscription.'),
    _FamousBH('GW150914', '🌊', Color(0xFF80DEEA), 'LIGO detection', '~62 solar masses (merged)', '1.3 billion light years',
        'The first gravitational wave event ever detected. Two black holes spiralled together and merged, releasing more energy in 0.2 seconds than all stars in the observable universe combined.',
        'The gravitational waves stretched space by less than one-thousandth the diameter of a proton as they passed Earth. LIGO detected this — the most precise measurement in the history of science.'),
  ];

  final List<_PhysicsFact> physics = [
    _PhysicsFact('🌀', 'Event Horizon', Color(0xFFEF9A9A),
        'The point of no return — the boundary around a black hole beyond which nothing, not even light, can escape. It is not a physical surface but a mathematical boundary in space.',
        'The event horizon is perfectly invisible. You could cross it without feeling anything — but you could never come back or communicate with the outside universe ever again.'),
    _PhysicsFact('📍', 'Singularity', Color(0xFFFFAB91),
        'At the centre of a black hole, all matter is crushed to an infinitely dense point called a singularity. Here, our known laws of physics completely break down.',
        'The singularity is where general relativity predicts infinite density — physicists believe this means the theory fails at that scale, and a new quantum gravity theory is needed.'),
    _PhysicsFact('🌡️', 'Hawking Radiation', Color(0xFFFFE082),
        'Stephen Hawking theorised that black holes slowly leak energy due to quantum effects near the event horizon. Over incomprehensibly long timescales, this causes black holes to evaporate completely.',
        'A stellar black hole would take 10^67 years to evaporate — far longer than the current age of the universe. The last black holes will not die until ~10^100 years from now.'),
    _PhysicsFact('⏱️', 'Time Dilation', Color(0xFF80DEEA),
        'Near a black hole, gravity is so extreme that time slows down relative to a distant observer. Someone hovering just outside the event horizon would age slower than someone far away.',
        'This was depicted accurately in Interstellar. One hour on the water planet near Gargantua equalled 7 years on Earth. Real gravitational time dilation has been measured even on Earth.'),
    _PhysicsFact('🍝', 'Spaghettification', Color(0xFFCE93D8),
        'If you fell feet-first into a black hole, tidal forces would stretch you into a long thin strand of matter — a process physicists literally call spaghettification.',
        'For supermassive black holes like M87*, tidal forces at the event horizon are actually gentle — you could cross it without immediately noticing. You just could never leave.'),
    _PhysicsFact('🔵', 'Accretion Disc', Color(0xFF4FC3F7),
        'Material falling into a black hole forms a superheated disc of gas and dust. Friction heats it to millions of degrees, making it glow brighter than entire galaxies.',
        'The most luminous quasar known shines 600 trillion times brighter than our Sun — all powered by a single black hole eating about 2 suns worth of matter every day.'),
    _PhysicsFact('🕳️', 'Information Paradox', Color(0xFF90CAF9),
        'If Hawking Radiation causes black holes to evaporate, what happens to the information about everything that fell in? Physics says information cannot be destroyed — but where does it go?',
        'The black hole information paradox is one of the deepest unsolved problems in physics. Current leading theory suggests information is encoded on the event horizon — the holographic principle.'),
    _PhysicsFact('🌉', 'Wormholes', Color(0xFFFFE082),
        'General relativity allows for hypothetical tunnels in spacetime called wormholes that could theoretically connect two separate points in space or time.',
        'No wormhole has ever been observed. Even if they exist, they would likely be too small and too unstable for anything to pass through — unless exotic matter with negative energy exists.'),
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
                    Text('BLACK HOLES', style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 3)),
                  ]),
                ),
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  child: SingleChildScrollView(
                    scrollDirection: Axis.horizontal,
                    child: Row(children: [
                      _TabBtn('🕳️ Types',   _tab == 0, const Color(0xFFEF9A9A), () => setState(() => _tab = 0)),
                      const SizedBox(width: 8),
                      _TabBtn('⚫ Famous',   _tab == 1, const Color(0xFFFFAB91), () => setState(() => _tab = 1)),
                      const SizedBox(width: 8),
                      _TabBtn('🌀 Physics',  _tab == 2, const Color(0xFF80DEEA), () => setState(() => _tab = 2)),
                    ]),
                  ),
                ),
                const SizedBox(height: 16),
                Expanded(
                  child: _tab == 0
                      ? _TypesTab(types: types)
                      : _tab == 1
                          ? _FamousTab(famous: famous)
                          : _PhysicsTab(physics: physics),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

// ── TYPES TAB ────────────────────────────────────────────────────────────────

class _TypesTab extends StatelessWidget {
  final List<_BHType> types;
  const _TypesTab({required this.types});
  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(16, 0, 16, 24),
      children: [
        Text('CLASSIFICATIONS', style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFFEF9A9A), letterSpacing: 2)),
        const SizedBox(height: 4),
        Text('Four known categories of black holes', style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
        const SizedBox(height: 16),
        ...types.map((t) => GestureDetector(
          onTap: () => showModalBottomSheet(context: context, backgroundColor: Colors.transparent, isScrollControlled: true, builder: (_) => _TypeSheet(type: t)),
          child: Container(
            margin: const EdgeInsets.only(bottom: 14),
            padding: const EdgeInsets.all(18),
            decoration: BoxDecoration(borderRadius: BorderRadius.circular(20), color: const Color(0xFF040F1F), border: Border.all(color: t.color.withOpacity(0.3)), boxShadow: [BoxShadow(color: t.color.withOpacity(0.08), blurRadius: 20)]),
            child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Row(children: [
                Container(width: 54, height: 54,
                  decoration: BoxDecoration(shape: BoxShape.circle, gradient: RadialGradient(colors: [Colors.black, t.color.withOpacity(0.5), Colors.transparent], stops: const [0.0, 0.55, 1.0]), boxShadow: [BoxShadow(color: t.color.withOpacity(0.4), blurRadius: 16, spreadRadius: 2)]),
                  child: Center(child: Text(t.icon, style: const TextStyle(fontSize: 22)))),
                const SizedBox(width: 14),
                Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text(t.name, style: GoogleFonts.orbitron(fontSize: 14, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 0.3)),
                  const SizedBox(height: 4),
                  Container(padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 3),
                    decoration: BoxDecoration(borderRadius: BorderRadius.circular(10), color: t.color.withOpacity(0.12), border: Border.all(color: t.color.withOpacity(0.3))),
                    child: Text(t.mass, style: GoogleFonts.orbitron(fontSize: 8, color: t.color, letterSpacing: 0.5))),
                ])),
                const Icon(Icons.arrow_forward_ios_rounded, color: Colors.white24, size: 14),
              ]),
              const SizedBox(height: 12),
              Text(t.description, maxLines: 3, overflow: TextOverflow.ellipsis, style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white54, height: 1.4)),
              const SizedBox(height: 12),
              Wrap(spacing: 8, runSpacing: 6,
                children: t.tags.map((tag) => Container(
                  padding: const EdgeInsets.symmetric(horizontal: 9, vertical: 4),
                  decoration: BoxDecoration(borderRadius: BorderRadius.circular(8), color: t.color.withOpacity(0.07), border: Border.all(color: t.color.withOpacity(0.2))),
                  child: Text(tag, style: GoogleFonts.rajdhani(fontSize: 11, color: t.color)),
                )).toList()),
            ]),
          ),
        )),
      ],
    );
  }
}

// ── FAMOUS TAB ───────────────────────────────────────────────────────────────

class _FamousTab extends StatelessWidget {
  final List<_FamousBH> famous;
  const _FamousTab({required this.famous});
  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(16, 0, 16, 24),
      children: [
        Text('NOTABLE BLACK HOLES', style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFFFFAB91), letterSpacing: 2)),
        const SizedBox(height: 4),
        Text('The most significant black holes ever discovered', style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
        const SizedBox(height: 16),
        ...famous.map((b) => GestureDetector(
          onTap: () => showModalBottomSheet(context: context, backgroundColor: Colors.transparent, isScrollControlled: true, builder: (_) => _FamousSheet(bh: b)),
          child: Container(
            margin: const EdgeInsets.only(bottom: 12),
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(borderRadius: BorderRadius.circular(18), color: const Color(0xFF040F1F), border: Border.all(color: b.color.withOpacity(0.25))),
            child: Row(children: [
              Container(width: 52, height: 52,
                decoration: BoxDecoration(shape: BoxShape.circle, gradient: RadialGradient(colors: [Colors.black, b.color.withOpacity(0.45), Colors.transparent], stops: const [0.0, 0.6, 1.0]), boxShadow: [BoxShadow(color: b.color.withOpacity(0.35), blurRadius: 14)]),
                child: Center(child: Text(b.icon, style: const TextStyle(fontSize: 20)))),
              const SizedBox(width: 14),
              Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Row(children: [
                  Expanded(child: Text(b.name, style: GoogleFonts.orbitron(fontSize: 13, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 0.3))),
                  const Icon(Icons.arrow_forward_ios_rounded, color: Colors.white24, size: 13),
                ]),
                const SizedBox(height: 4),
                Text(b.location, style: GoogleFonts.rajdhani(fontSize: 12, color: b.color)),
                const SizedBox(height: 4),
                Text('Mass: ${b.mass}', style: GoogleFonts.orbitron(fontSize: 8, color: Colors.white38, letterSpacing: 0.3)),
                Text('Distance: ${b.distance}', style: GoogleFonts.orbitron(fontSize: 8, color: Colors.white38, letterSpacing: 0.3)),
              ])),
            ]),
          ),
        )),
      ],
    );
  }
}

// ── PHYSICS TAB ──────────────────────────────────────────────────────────────

class _PhysicsTab extends StatelessWidget {
  final List<_PhysicsFact> physics;
  const _PhysicsTab({required this.physics});
  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(16, 0, 16, 24),
      children: [
        Text('THE PHYSICS OF BLACK HOLES', style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF80DEEA), letterSpacing: 2)),
        const SizedBox(height: 4),
        Text('How they warp space, time, and reality', style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
        const SizedBox(height: 16),
        ...physics.map((p) => GestureDetector(
          onTap: () => showModalBottomSheet(context: context, backgroundColor: Colors.transparent, isScrollControlled: true, builder: (_) => _PhysicsSheet(fact: p)),
          child: Container(
            margin: const EdgeInsets.only(bottom: 12),
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: const Color(0xFF040F1F), border: Border.all(color: p.color.withOpacity(0.22))),
            child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Container(width: 44, height: 44,
                decoration: BoxDecoration(shape: BoxShape.circle, color: p.color.withOpacity(0.12), border: Border.all(color: p.color.withOpacity(0.3))),
                child: Center(child: Text(p.icon, style: const TextStyle(fontSize: 20)))),
              const SizedBox(width: 14),
              Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Row(children: [
                  Expanded(child: Text(p.title, style: GoogleFonts.orbitron(fontSize: 12, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 0.3))),
                  const Icon(Icons.arrow_forward_ios_rounded, color: Colors.white24, size: 13),
                ]),
                const SizedBox(height: 6),
                Text(p.summary, maxLines: 2, overflow: TextOverflow.ellipsis, style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white38, height: 1.4)),
              ])),
            ]),
          ),
        )),
        const SizedBox(height: 8),
        Container(
          padding: const EdgeInsets.all(16),
          decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: Colors.tealAccent.withOpacity(0.05), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(children: [const Text('🐟', style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text('THE ULTIMATE FACT', style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
            const SizedBox(height: 8),
            Text('Black holes are not cosmic vacuum cleaners. If our Sun were replaced by a black hole of the same mass, Earth would not be sucked in — it would continue orbiting normally in the dark.',
                style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
          ]),
        ),
      ],
    );
  }
}

// ── BOTTOM SHEETS ─────────────────────────────────────────────────────────────

class _TypeSheet extends StatelessWidget {
  final _BHType type;
  const _TypeSheet({required this.type});
  @override
  Widget build(BuildContext context) => DraggableScrollableSheet(
    initialChildSize: 0.75, minChildSize: 0.5, maxChildSize: 0.93,
    builder: (_, ctrl) => Container(
      decoration: BoxDecoration(color: const Color(0xFF040F1F), borderRadius: const BorderRadius.vertical(top: Radius.circular(28)), border: Border.all(color: type.color.withOpacity(0.3))),
      child: ListView(controller: ctrl, padding: const EdgeInsets.all(24), children: [
        Center(child: Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white24, borderRadius: BorderRadius.circular(2)))),
        const SizedBox(height: 24),
        Center(child: Container(width: 110, height: 110,
          decoration: BoxDecoration(shape: BoxShape.circle, gradient: RadialGradient(colors: [Colors.black, type.color.withOpacity(0.55), Colors.transparent], stops: const [0.0, 0.55, 1.0]), boxShadow: [BoxShadow(color: type.color.withOpacity(0.45), blurRadius: 40, spreadRadius: 4)]),
          child: Center(child: Text(type.icon, style: const TextStyle(fontSize: 42))))),
        const SizedBox(height: 18),
        Center(child: Text(type.name, textAlign: TextAlign.center, style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: type.color, blurRadius: 20)]))),
        const SizedBox(height: 6),
        Center(child: Container(padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 4),
          decoration: BoxDecoration(borderRadius: BorderRadius.circular(12), color: type.color.withOpacity(0.12), border: Border.all(color: type.color.withOpacity(0.35))),
          child: Text(type.mass, style: GoogleFonts.orbitron(fontSize: 10, color: type.color, letterSpacing: 1)))),
        const SizedBox(height: 20),
        Text(type.description, style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, height: 1.6)),
        const SizedBox(height: 16),
        Wrap(spacing: 8, runSpacing: 8,
          children: type.tags.map((tag) => Container(
            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
            decoration: BoxDecoration(borderRadius: BorderRadius.circular(10), color: type.color.withOpacity(0.08), border: Border.all(color: type.color.withOpacity(0.25))),
            child: Text(tag, style: GoogleFonts.rajdhani(fontSize: 12, color: type.color)),
          )).toList()),
        const SizedBox(height: 16),
        Container(padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: Colors.tealAccent.withOpacity(0.06), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(children: [const Text('🐟', style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text('MIND-BLOWING FACT', style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
            const SizedBox(height: 8),
            Text(type.fishyFact, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
          ])),
        const SizedBox(height: 16),
      ]),
    ),
  );
}

class _FamousSheet extends StatelessWidget {
  final _FamousBH bh;
  const _FamousSheet({required this.bh});
  @override
  Widget build(BuildContext context) => DraggableScrollableSheet(
    initialChildSize: 0.75, minChildSize: 0.5, maxChildSize: 0.93,
    builder: (_, ctrl) => Container(
      decoration: BoxDecoration(color: const Color(0xFF040F1F), borderRadius: const BorderRadius.vertical(top: Radius.circular(28)), border: Border.all(color: bh.color.withOpacity(0.3))),
      child: ListView(controller: ctrl, padding: const EdgeInsets.all(24), children: [
        Center(child: Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white24, borderRadius: BorderRadius.circular(2)))),
        const SizedBox(height: 24),
        Center(child: Container(width: 100, height: 100,
          decoration: BoxDecoration(shape: BoxShape.circle, gradient: RadialGradient(colors: [Colors.black, bh.color.withOpacity(0.5), Colors.transparent], stops: const [0.0, 0.55, 1.0]), boxShadow: [BoxShadow(color: bh.color.withOpacity(0.45), blurRadius: 36)]),
          child: Center(child: Text(bh.icon, style: const TextStyle(fontSize: 38))))),
        const SizedBox(height: 16),
        Center(child: Text(bh.name, textAlign: TextAlign.center, style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: bh.color, blurRadius: 20)]))),
        Center(child: Text(bh.location, style: GoogleFonts.rajdhani(fontSize: 14, color: bh.color))),
        const SizedBox(height: 16),
        Row(children: [_S('MASS', bh.mass, bh.color), const SizedBox(width: 10), _S('DISTANCE', bh.distance, bh.color)]),
        const SizedBox(height: 16),
        Text(bh.description, style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, height: 1.6)),
        const SizedBox(height: 16),
        Container(padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: Colors.tealAccent.withOpacity(0.06), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(children: [const Text('🐟', style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text('MIND-BLOWING FACT', style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
            const SizedBox(height: 8),
            Text(bh.fishyFact, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
          ])),
        const SizedBox(height: 16),
      ]),
    ),
  );
}

class _PhysicsSheet extends StatelessWidget {
  final _PhysicsFact fact;
  const _PhysicsSheet({required this.fact});
  @override
  Widget build(BuildContext context) => DraggableScrollableSheet(
    initialChildSize: 0.65, minChildSize: 0.4, maxChildSize: 0.9,
    builder: (_, ctrl) => Container(
      decoration: BoxDecoration(color: const Color(0xFF040F1F), borderRadius: const BorderRadius.vertical(top: Radius.circular(28)), border: Border.all(color: fact.color.withOpacity(0.3))),
      child: ListView(controller: ctrl, padding: const EdgeInsets.all(24), children: [
        Center(child: Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white24, borderRadius: BorderRadius.circular(2)))),
        const SizedBox(height: 20),
        Center(child: Container(width: 80, height: 80,
          decoration: BoxDecoration(shape: BoxShape.circle, color: fact.color.withOpacity(0.12), border: Border.all(color: fact.color.withOpacity(0.4)), boxShadow: [BoxShadow(color: fact.color.withOpacity(0.25), blurRadius: 24)]),
          child: Center(child: Text(fact.icon, style: const TextStyle(fontSize: 36))))),
        const SizedBox(height: 14),
        Center(child: Text(fact.title, textAlign: TextAlign.center, style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: fact.color, blurRadius: 18)]))),
        const SizedBox(height: 20),
        Text(fact.summary, style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, height: 1.6)),
        const SizedBox(height: 16),
        Container(padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: Colors.tealAccent.withOpacity(0.06), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
          child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Row(children: [const Text('🐟', style: TextStyle(fontSize: 16)), const SizedBox(width: 8), Text('MIND-BLOWING FACT', style: GoogleFonts.orbitron(fontSize: 8, color: Colors.tealAccent, letterSpacing: 1.5))]),
            const SizedBox(height: 8),
            Text(fact.fishyFact, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: FontStyle.italic)),
          ])),
        const SizedBox(height: 16),
      ]),
    ),
  );
}

// ── HELPERS & MODELS ──────────────────────────────────────────────────────────

Widget _TabBtn(String label, bool active, Color color, VoidCallback onTap) {
  return GestureDetector(
    onTap: onTap,
    child: AnimatedContainer(
      duration: const Duration(milliseconds: 250),
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
      decoration: BoxDecoration(borderRadius: BorderRadius.circular(12), color: active ? color.withOpacity(0.15) : const Color(0xFF040F1F), border: Border.all(color: active ? color : Colors.white12, width: active ? 1.5 : 1)),
      child: Text(label, style: GoogleFonts.orbitron(fontSize: 11, color: active ? color : Colors.white38, fontWeight: active ? FontWeight.w700 : FontWeight.w400, letterSpacing: 0.5)),
    ),
  );
}

Widget _S(String l, String v, Color c) => Expanded(child: Container(
  padding: const EdgeInsets.all(12),
  decoration: BoxDecoration(borderRadius: BorderRadius.circular(12), color: c.withOpacity(0.06), border: Border.all(color: c.withOpacity(0.2))),
  child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
    Text(l, style: GoogleFonts.orbitron(fontSize: 7, color: c, letterSpacing: 1.5)),
    const SizedBox(height: 4),
    Text(v, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white, fontWeight: FontWeight.w600, height: 1.3)),
  ]),
));

class _BHType {
  final String icon, name, mass, description, fishyFact; final Color color; final List<String> tags;
  const _BHType(this.icon, this.name, this.color, this.mass, this.description, this.fishyFact, this.tags);
}
class _FamousBH {
  final String name, icon, location, mass, distance, description, fishyFact; final Color color;
  const _FamousBH(this.name, this.icon, this.color, this.location, this.mass, this.distance, this.description, this.fishyFact);
}
class _PhysicsFact {
  final String icon, title, summary, fishyFact; final Color color;
  const _PhysicsFact(this.icon, this.title, this.color, this.summary, this.fishyFact);
}

class _StarPainter extends CustomPainter {
  final double progress;
  static final _rng = Random(66);
  static final _stars = List.generate(140, (_) => Offset(_rng.nextDouble(), _rng.nextDouble()));
  static final _szs = List.generate(140, (_) => _rng.nextDouble() * 1.3 + 0.3);
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

with open("lib/screens/black_holes_screen.dart", "w") as f:
    f.write(content)
print("Done! Lines:", len(content.splitlines()))
