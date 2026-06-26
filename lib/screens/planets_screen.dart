import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:animate_do/animate_do.dart';

class PlanetData {
  final String name, description, diameter, distance, funFact, fishyFact, imagePath;
  final Color color;
  const PlanetData({required this.name, required this.description, required this.diameter, required this.distance, required this.funFact, required this.fishyFact, required this.imagePath, required this.color});
}

final List<PlanetData> planetList = [
  PlanetData(name: "Mercury", description: "The smallest planet and closest to the Sun. Extreme temperatures swing from -180C at night to 430C during the day.", diameter: "4,879 km", distance: "57.9 million km", funFact: "A year on Mercury is just 88 Earth days!", fishyFact: "Mercury's core takes up 85% of its radius — if Earth's core was that big, it would poke out of the surface.", color: Color(0xFF90A4AE), imagePath: "assets/images/mercury.jpg"),
  PlanetData(name: "Venus", description: "The hottest planet despite not being closest to the Sun. Its thick CO2 atmosphere traps heat like a pressure cooker.", diameter: "12,104 km", distance: "108.2 million km", funFact: "Venus spins backwards — the Sun rises in the west there.", fishyFact: "A day on Venus is longer than its year. It rotates so slowly that you could walk faster than its rotation speed.", color: Color(0xFFFFCC80), imagePath: "assets/images/venus.jpg"),
  PlanetData(name: "Earth", description: "Our home. The only known planet with liquid water on the surface and life as we know it.", diameter: "12,742 km", distance: "149.6 million km", funFact: "Earth is the densest planet in the Solar System.", fishyFact: "Earth is not a perfect sphere — people in Ecuador are farther from Earth's center than people at the North Pole.", color: Color(0xFF4FC3F7), imagePath: "assets/images/earth.jpg"),
  PlanetData(name: "Mars", description: "The Red Planet with the tallest volcano and longest canyon in the solar system.", diameter: "6,779 km", distance: "227.9 million km", funFact: "Olympus Mons on Mars is 3x taller than Mount Everest.", fishyFact: "Mars has BLUE sunsets. Dust scatters light in reverse — blue at dusk, red during the day. Opposite of Earth.", color: Color(0xFFEF9A9A), imagePath: "assets/images/mars.jpg"),
  PlanetData(name: "Jupiter", description: "The largest planet — so massive all other planets could fit inside it twice over.", diameter: "139,820 km", distance: "778.5 million km", funFact: "Jupiter's Great Red Spot is a storm older than 400 years.", fishyFact: "Jupiter has no solid surface. If you tried to land, you'd just sink deeper until pressure crushed you into nothing.", color: Color(0xFFFFAB91), imagePath: "assets/images/jupiter.jpg"),
  PlanetData(name: "Saturn", description: "The ringed beauty of the solar system. Its rings are made of billions of ice and rock particles.", diameter: "116,460 km", distance: "1.43 billion km", funFact: "Saturn is so light it would float on water.", fishyFact: "Saturn's rings are only 10 meters thick on average. If Saturn were a basketball, the rings would be thinner than paper.", color: Color(0xFFFFE082), imagePath: "assets/images/saturn.jpg"),
  PlanetData(name: "Uranus", description: "An ice giant that rotates on its side — its poles get more sunlight than its equator.", diameter: "50,724 km", distance: "2.87 billion km", funFact: "Uranus's tilt is 98 degrees — it literally rolls around the Sun.", fishyFact: "Uranus smells like rotten eggs. Its atmosphere contains hydrogen sulfide — same compound that makes farts smell bad.", color: Color(0xFF80DEEA), imagePath: "assets/images/uranus.jpg"),
  PlanetData(name: "Neptune", description: "The windiest planet with storms reaching 2,100 km/h — faster than the speed of sound on Earth.", diameter: "49,244 km", distance: "4.5 billion km", funFact: "Neptune was predicted by math before anyone saw it through a telescope.", fishyFact: "It rains DIAMONDS on Neptune. Extreme pressure converts carbon into diamond crystals that fall like hailstones.", color: Color(0xFF90CAF9), imagePath: "assets/images/neptune.jpg"),
];

class PlanetsScreen extends StatefulWidget {
  const PlanetsScreen({super.key});
  @override
  State<PlanetsScreen> createState() => _PlanetsScreenState();
}

class _PlanetsScreenState extends State<PlanetsScreen> with SingleTickerProviderStateMixin {
  late AnimationController _starController;
  @override
  void initState() { super.initState(); _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat(); }
  @override
  void dispose() { _starController.dispose(); super.dispose(); }

  void _showInfo(BuildContext context, PlanetData p) {
    showModalBottomSheet(context: context, backgroundColor: Colors.transparent, isScrollControlled: true, builder: (_) => _InfoSheet(planet: p));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF010914),
      body: Stack(
        children: [
          AnimatedBuilder(animation: _starController, builder: (_, __) => CustomPaint(painter: _StarPainter(_starController.value), child: const SizedBox.expand())),
          SafeArea(
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Padding(
                  padding: const EdgeInsets.fromLTRB(20, 16, 20, 4),
                  child: Row(children: [
                    GestureDetector(onTap: () => Navigator.pop(context), child: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white54, size: 20)),
                    const SizedBox(width: 16),
                    Text("PLANETS", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 5, shadows: [Shadow(color: Color(0xFF4FC3F7), blurRadius: 15)])),
                  ]),
                ),
                
                
                Padding(
                  padding: const EdgeInsets.fromLTRB(16, 0, 16, 12),
                  child: ClipRRect(
                    borderRadius: BorderRadius.circular(20),
                    child: SizedBox(
                      height: 160, width: double.infinity,
                      child: Stack(fit: StackFit.expand, children: [
                        Image.asset("assets/images/planets.jpg", fit: BoxFit.cover),
                        Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF010914)]))),
                        Positioned(bottom: 14, left: 16, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                          Text("8 Planets", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w800, color: Colors.white, shadows: [Shadow(color: Color(0xFF4FC3F7), blurRadius: 20)])),
                          Text("Tap any planet to explore", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                        ])),
                      ]),
                    ),
                  ),
                ),
                Expanded(
                  child: ListView.builder(
                    padding: const EdgeInsets.symmetric(horizontal: 16),
                    itemCount: planetList.length,
                    itemBuilder: (ctx, i) => FadeInLeft(
                      delay: Duration(milliseconds: 100 + i * 80),
                      child: FadeInUp(
                        delay: Duration(milliseconds: 100 + i * 80),
                        child: _PlanetCard(planet: planetList[i], onTap: () => _showInfo(context, planetList[i])),
                      ),
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

class _PlanetCard extends StatelessWidget {
  final PlanetData planet; final VoidCallback onTap;
  const _PlanetCard({required this.planet, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        margin: const EdgeInsets.only(bottom: 16),
        height: 140,
        decoration: BoxDecoration(borderRadius: BorderRadius.circular(24), color: const Color(0xFF040F1F), border: Border.all(color: planet.color.withOpacity(0.25)), boxShadow: [BoxShadow(color: planet.color.withOpacity(0.08), blurRadius: 20)]),
        child: Row(
          children: [
            ClipRRect(
              borderRadius: const BorderRadius.only(topLeft: Radius.circular(24), bottomLeft: Radius.circular(24)),
              child: SizedBox(width: 140, height: 140, child: Stack(fit: StackFit.expand, children: [
                Image.asset(planet.imagePath, fit: BoxFit.cover, errorBuilder: (_, __, ___) => Container(color: planet.color.withOpacity(0.3), child: Center(child: Text(planet.name[0], style: GoogleFonts.orbitron(fontSize: 40, color: planet.color))))),
                Positioned(right: 0, child: Container(width: 30, height: 140, decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.transparent, const Color(0xFF040F1F)])))),
              ])),
            ),
            Expanded(
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.center, children: [
                  Row(children: [
                    Expanded(child: Text(planet.name, style: GoogleFonts.orbitron(fontSize: 17, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 1.5))),
                    Icon(Icons.arrow_forward_ios_rounded, color: planet.color.withOpacity(0.7), size: 14),
                  ]),
                  const SizedBox(height: 6),
                  Text(planet.description, maxLines: 2, overflow: TextOverflow.ellipsis, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38, height: 1.4)),
                  const SizedBox(height: 10),
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                    decoration: BoxDecoration(borderRadius: BorderRadius.circular(20), color: planet.color.withOpacity(0.1), border: Border.all(color: planet.color.withOpacity(0.3))),
                    child: Text(planet.distance, style: GoogleFonts.orbitron(fontSize: 8, color: planet.color, letterSpacing: 0.5)),
                  ),
                ]),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _InfoSheet extends StatelessWidget {
  final PlanetData planet;
  const _InfoSheet({required this.planet});

  @override
  Widget build(BuildContext context) {
    return DraggableScrollableSheet(
      initialChildSize: 0.78, minChildSize: 0.5, maxChildSize: 0.95,
      builder: (_, controller) => Container(
        decoration: BoxDecoration(color: const Color(0xFF040F1F), borderRadius: const BorderRadius.vertical(top: Radius.circular(28)), border: Border.all(color: planet.color.withOpacity(0.3))),
        child: ListView(controller: controller, padding: EdgeInsets.zero, children: [
          ClipRRect(
            borderRadius: const BorderRadius.vertical(top: Radius.circular(28)),
            child: SizedBox(height: 220, width: double.infinity, child: Stack(fit: StackFit.expand, children: [
              Image.asset(planet.imagePath, fit: BoxFit.cover, errorBuilder: (_, __, ___) => Container(color: planet.color.withOpacity(0.2))),
              Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF040F1F)]))),
              Positioned(top: 12, left: 0, right: 0, child: Center(child: Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white38, borderRadius: BorderRadius.circular(2))))),
              Positioned(bottom: 16, left: 24, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                Text(planet.name, style: GoogleFonts.orbitron(fontSize: 32, fontWeight: FontWeight.w900, color: Colors.white, letterSpacing: 2, shadows: [Shadow(color: planet.color, blurRadius: 20)])),
                Text("Planet · Solar System", style: GoogleFonts.rajdhani(fontSize: 13, color: planet.color)),
              ])),
            ])),
          ),
          Padding(padding: const EdgeInsets.all(24), child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text("ABOUT", style: GoogleFonts.orbitron(fontSize: 9, color: planet.color, letterSpacing: 2)),
            const SizedBox(height: 8),
            Text(planet.description, style: GoogleFonts.rajdhani(fontSize: 16, color: Colors.white70, height: 1.6)),
            const SizedBox(height: 20),
            Row(children: [
              _StatBox("DIAMETER", planet.diameter, planet.color),
              const SizedBox(width: 10),
              _StatBox("DISTANCE", planet.distance, planet.color),
            ]),
            const SizedBox(height: 16),
            _FactBox(icon: "💡", label: "FUN FACT", text: planet.funFact, color: planet.color),
            const SizedBox(height: 12),
            _FactBox(icon: "🐟", label: "MIND-BLOWING FACT", text: planet.fishyFact, color: Colors.tealAccent, isWild: true),
            const SizedBox(height: 24),
          ])),
        ]),
      ),
    );
  }
}

class _StatBox extends StatelessWidget {
  final String label, value; final Color color;
  const _StatBox(this.label, this.value, this.color);
  @override
  Widget build(BuildContext context) => Expanded(child: Container(
    padding: const EdgeInsets.all(14),
    decoration: BoxDecoration(borderRadius: BorderRadius.circular(12), color: color.withOpacity(0.06), border: Border.all(color: color.withOpacity(0.2))),
    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Text(label, style: GoogleFonts.orbitron(fontSize: 8, color: color, letterSpacing: 1.5)),
      const SizedBox(height: 6),
      Text(value, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white, fontWeight: FontWeight.w600)),
    ]),
  ));
}

class _FactBox extends StatelessWidget {
  final String icon, label, text; final Color color; final bool isWild;
  const _FactBox({required this.icon, required this.label, required this.text, required this.color, this.isWild = false});
  @override
  Widget build(BuildContext context) => Container(
    padding: const EdgeInsets.all(16),
    decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: color.withOpacity(isWild ? 0.06 : 0.05), border: Border.all(color: color.withOpacity(isWild ? 0.35 : 0.2))),
    child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
      Row(children: [Text(icon, style: const TextStyle(fontSize: 16)), const SizedBox(width: 8), Text(label, style: GoogleFonts.orbitron(fontSize: 8, color: color, letterSpacing: 1.5))]),
      const SizedBox(height: 8),
      Text(text, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, height: 1.5, fontStyle: isWild ? FontStyle.italic : FontStyle.normal)),
    ]),
  );
}

class _StarPainter extends CustomPainter {
  final double progress;
  static final _rng = Random(99);
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
