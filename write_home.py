content = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:animate_do/animate_do.dart';
import 'planets_screen.dart';
import 'solar_system_screen.dart';
import 'galaxy_screen.dart';
import 'black_holes_screen.dart';
import 'universe_screen.dart';
import 'multiverse_screen.dart';
import 'ai_assistant_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> with TickerProviderStateMixin {
  late AnimationController _starController;
  late AnimationController _pulseController;

  @override
  void initState() {
    super.initState();
    _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();
    _pulseController = AnimationController(vsync: this, duration: const Duration(seconds: 2))..repeat(reverse: true);
  }

  @override
  void dispose() {
    _starController.dispose();
    _pulseController.dispose();
    super.dispose();
  }

  PageRoute _route(Widget screen) => PageRouteBuilder(
    pageBuilder: (_, __, ___) => screen,
    transitionsBuilder: (_, anim, __, child) => FadeTransition(opacity: anim, child: child),
    transitionDuration: const Duration(milliseconds: 500),
  );

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF010914),
      floatingActionButton: AnimatedBuilder(
        animation: _pulseController,
        builder: (_, child) => Transform.scale(scale: 1.0 + 0.06 * _pulseController.value, child: child),
        child: GestureDetector(
          onTap: () => Navigator.push(context, _route(const AiAssistantScreen())),
          child: Container(
            width: 62, height: 62,
            decoration: BoxDecoration(
              shape: BoxShape.circle,
              gradient: const LinearGradient(colors: [Color(0xFF0066FF), Color(0xFF00AAFF)], begin: Alignment.topLeft, end: Alignment.bottomRight),
              boxShadow: [BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.5), blurRadius: 20, spreadRadius: 2)],
            ),
            child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
              const Text("🌟", style: TextStyle(fontSize: 22)),
              Text("NOVA", style: GoogleFonts.orbitron(fontSize: 7, color: Colors.white, letterSpacing: 1, fontWeight: FontWeight.w700)),
            ]),
          ),
        ),
      ),
      body: Stack(
        children: [
          AnimatedBuilder(
            animation: _starController,
            builder: (_, __) => CustomPaint(painter: _StarPainter(_starController.value), child: const SizedBox.expand()),
          ),
          SafeArea(
            child: Column(
              children: [
                const SizedBox(height: 28),
                FadeInDown(child: Center(child: Text("COSMOS", style: GoogleFonts.orbitron(fontSize: 36, fontWeight: FontWeight.w900, color: Colors.white, letterSpacing: 8, shadows: [Shadow(color: Color(0xFF00AAFF), blurRadius: 30)])))),
                FadeInDown(delay: Duration(milliseconds: 150), child: Center(child: Text("X P L O R E R", style: GoogleFonts.orbitron(fontSize: 12, color: Color(0xFF00AAFF), letterSpacing: 12)))),
                const SizedBox(height: 6),
                FadeInDown(delay: Duration(milliseconds: 250), child: Center(child: Text("Journey from planets to the multiverse", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white38, letterSpacing: 1.5)))),
                const SizedBox(height: 24),
                FadeInUp(
                  delay: Duration(milliseconds: 300),
                  child: GestureDetector(
                    onTap: () => Navigator.push(context, _route(SolarSystemScreen())),
                    child: Container(
                      margin: const EdgeInsets.symmetric(horizontal: 16),
                      height: 160,
                      decoration: BoxDecoration(borderRadius: BorderRadius.circular(24), boxShadow: [BoxShadow(color: Color(0xFFFFB347).withOpacity(0.25), blurRadius: 30)]),
                      child: ClipRRect(
                        borderRadius: BorderRadius.circular(24),
                        child: Stack(fit: StackFit.expand, children: [
                          Image.asset("assets/images/_solar_system.jpg", fit: BoxFit.cover, errorBuilder: (_, __, ___) => Container(color: const Color(0xFF071628))),
                          Container(decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.black.withOpacity(0.1), Colors.black.withOpacity(0.65)], begin: Alignment.topCenter, end: Alignment.bottomCenter))),
                          Positioned(bottom: 16, left: 20, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                            Text("Solar System", style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 2)),
                            Text("Our cosmic neighbourhood", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                          ])),
                          Positioned(top: 14, right: 14, child: Container(
                            padding: const EdgeInsets.symmetric(horizontal: 12, vertical: 6),
                            decoration: BoxDecoration(color: Colors.black38, borderRadius: BorderRadius.circular(20), border: Border.all(color: Colors.white24)),
                            child: Text("FEATURED", style: GoogleFonts.orbitron(fontSize: 8, color: Colors.white70, letterSpacing: 2)),
                          )),
                        ]),
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 16),
                Expanded(
                  child: ListView(
                    padding: const EdgeInsets.fromLTRB(16, 0, 16, 80),
                    children: [
                      FadeInLeft(delay: Duration(milliseconds: 400), child: _LevelCard("Planets",     "Explore all 8 planets",            Color(0xFF4FC3F7), () => Navigator.push(context, _route(PlanetsScreen())))),
                      FadeInLeft(delay: Duration(milliseconds: 500), child: _LevelCard("Galaxies",    "Billions of star systems",         Color(0xFFCE93D8), () => Navigator.push(context, _route(GalaxyScreen())))),
                      FadeInLeft(delay: Duration(milliseconds: 600), child: _LevelCard("Black Holes", "Where gravity breaks reality",     Color(0xFF80CBC4), () => Navigator.push(context, _route(BlackHolesScreen())))),
                      FadeInLeft(delay: Duration(milliseconds: 700), child: _LevelCard("Universe",    "93 billion light years of space",  Color(0xFF90CAF9), () => Navigator.push(context, _route(UniverseScreen())))),
                      FadeInLeft(delay: Duration(milliseconds: 800), child: _LevelCard("Multiverse",  "Beyond our universe",              Color(0xFFF48FB1), () => Navigator.push(context, _route(MultiverseScreen())))),
                      const SizedBox(height: 12),
                      FadeInUp(delay: Duration(milliseconds: 900), child: GestureDetector(
                        onTap: () => Navigator.push(context, _route(const AiAssistantScreen())),
                        child: Container(
                          padding: const EdgeInsets.all(16),
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(16),
                            gradient: LinearGradient(colors: [Color(0xFF0066FF).withOpacity(0.15), Color(0xFF00AAFF).withOpacity(0.08)]),
                            border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.4)),
                            boxShadow: [BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.1), blurRadius: 16)],
                          ),
                          child: Row(children: [
                            Container(
                              width: 44, height: 44,
                              decoration: BoxDecoration(shape: BoxShape.circle, gradient: const LinearGradient(colors: [Color(0xFF0066FF), Color(0xFF00AAFF)]), boxShadow: [BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.4), blurRadius: 10)]),
                              child: const Center(child: Text("🌟", style: TextStyle(fontSize: 20))),
                            ),
                            const SizedBox(width: 14),
                            Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                              Text("Ask NOVA", style: GoogleFonts.orbitron(fontSize: 14, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 1.5)),
                              const SizedBox(height: 2),
                              Text("AI-powered cosmos assistant", style: GoogleFonts.rajdhani(fontSize: 12, color: Color(0xFF00AAFF))),
                            ])),
                            Icon(Icons.arrow_forward_ios_rounded, color: Color(0xFF00AAFF), size: 15),
                          ]),
                        ),
                      )),
                    ],
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

class _LevelCard extends StatelessWidget {
  final String title, subtitle; final Color color; final VoidCallback onTap;
  const _LevelCard(this.title, this.subtitle, this.color, this.onTap);
  @override
  Widget build(BuildContext context) => GestureDetector(
    onTap: onTap,
    child: Container(
      margin: const EdgeInsets.only(bottom: 12),
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 16),
      decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: const Color(0xFF040F1F), border: Border.all(color: color.withOpacity(0.3)), boxShadow: [BoxShadow(color: color.withOpacity(0.07), blurRadius: 16)]),
      child: Row(children: [
        Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(title, style: GoogleFonts.orbitron(fontSize: 14, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 1.5)),
          const SizedBox(height: 3),
          Text(subtitle, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
        ])),
        Icon(Icons.arrow_forward_ios_rounded, color: color, size: 15),
      ]),
    ),
  );
}

class _StarPainter extends CustomPainter {
  final double progress;
  static final _rng = Random(42);
  static final _stars = List.generate(150, (_) => Offset(_rng.nextDouble(), _rng.nextDouble()));
  static final _szs = List.generate(150, (_) => _rng.nextDouble() * 1.5 + 0.3);
  _StarPainter(this.progress);
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint();
    for (int i = 0; i < _stars.length; i++) {
      final t = 0.3 + 0.7 * (0.5 + 0.5 * sin(progress * 2 * pi * 2 + i));
      paint.color = Colors.white.withOpacity(t * 0.8);
      canvas.drawCircle(Offset(_stars[i].dx * size.width, _stars[i].dy * size.height), _szs[i], paint);
    }
  }
  @override
  bool shouldRepaint(_) => true;
}
"""

with open("lib/screens/home_screen.dart", "w") as f:
    f.write(content)
print("Done! Lines:", len(content.splitlines()))
