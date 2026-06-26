content = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:animate_do/animate_do.dart';
import 'planets_screen.dart';
import 'solar_system_screen.dart';
import 'galaxy_screen.dart';
import 'blackhole_screen.dart';
import 'universe_screen.dart';
import 'multiverse_screen.dart';
import 'search_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> with SingleTickerProviderStateMixin {
  late AnimationController _starController;

  @override
  void initState() {
    super.initState();
    _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();
  }

  @override
  void dispose() { _starController.dispose(); super.dispose(); }

  PageRoute _route(Widget screen) => PageRouteBuilder(
    pageBuilder: (_, __, ___) => screen,
    transitionsBuilder: (_, anim, __, child) => FadeTransition(opacity: anim, child: child),
    transitionDuration: const Duration(milliseconds: 500),
  );

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
              children: [
                const SizedBox(height: 28),
                FadeInDown(child: Center(child: Text("COSMOS", style: GoogleFonts.orbitron(fontSize: 36, fontWeight: FontWeight.w900, color: Colors.white, letterSpacing: 8, shadows: [Shadow(color: Color(0xFF00AAFF), blurRadius: 30)])))),
                FadeInDown(delay: Duration(milliseconds: 150), child: Center(child: Text("X P L O R E R", style: GoogleFonts.orbitron(fontSize: 12, color: Color(0xFF00AAFF), letterSpacing: 12)))),
                const SizedBox(height: 6),
                FadeInDown(delay: Duration(milliseconds: 250), child: Center(child: Text("Journey from planets to the multiverse", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white38, letterSpacing: 1.5)))),
                const SizedBox(height: 12),

                // Search bar
                FadeInDown(
                  delay: Duration(milliseconds: 300),
                  child: Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 16),
                    child: GestureDetector(
                      onTap: () => Navigator.push(context, _route(SearchScreen())),
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(14),
                          color: const Color(0xFF040F1F),
                          border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.3)),
                        ),
                        child: Row(children: [
                          Icon(Icons.search_rounded, color: Color(0xFF00AAFF), size: 20),
                          const SizedBox(width: 10),
                          Text("Search planets, galaxies, facts...", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white24)),
                        ]),
                      ),
                    ),
                  ),
                ),
                const SizedBox(height: 12),

                Expanded(
                  child: ListView(
                    padding: const EdgeInsets.symmetric(horizontal: 16),
                    children: [

                      // Solar System featured card
                      FadeInUp(
                        delay: Duration(milliseconds: 350),
                        child: GestureDetector(
                          onTap: () => Navigator.push(context, _route(SolarSystemScreen())),
                          child: Container(
                            margin: const EdgeInsets.only(bottom: 12),
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

                      // Planets card with image
                      FadeInLeft(
                        delay: Duration(milliseconds: 400),
                        child: GestureDetector(
                          onTap: () => Navigator.push(context, _route(PlanetsScreen())),
                          child: Container(
                            margin: const EdgeInsets.only(bottom: 12),
                            height: 120,
                            decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), boxShadow: [BoxShadow(color: Color(0xFF4FC3F7).withOpacity(0.15), blurRadius: 20)]),
                            child: ClipRRect(
                              borderRadius: BorderRadius.circular(16),
                              child: Stack(fit: StackFit.expand, children: [
                                Image.asset("assets/images/planets.jpg", fit: BoxFit.cover),
                                Container(decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.black.withOpacity(0.1), Colors.black.withOpacity(0.65)], begin: Alignment.topCenter, end: Alignment.bottomCenter))),
                                Positioned(bottom: 14, left: 20, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                  Text("Planets", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 2)),
                                  Text("Explore all 8 planets", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                                ])),
                                Positioned(bottom: 18, right: 16, child: Icon(Icons.arrow_forward_ios_rounded, color: Color(0xFF4FC3F7), size: 15)),
                              ]),
                            ),
                          ),
                        ),
                      ),

                      // Galaxies card with image
                      FadeInLeft(
                        delay: Duration(milliseconds: 500),
                        child: GestureDetector(
                          onTap: () => Navigator.push(context, _route(GalaxyScreen())),
                          child: Container(
                            margin: const EdgeInsets.only(bottom: 12),
                            height: 120,
                            decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), boxShadow: [BoxShadow(color: Color(0xFFCE93D8).withOpacity(0.15), blurRadius: 20)]),
                            child: ClipRRect(
                              borderRadius: BorderRadius.circular(16),
                              child: Stack(fit: StackFit.expand, children: [
                                Image.asset("assets/images/galaxy.jpg", fit: BoxFit.cover),
                                Container(decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.black.withOpacity(0.1), Colors.black.withOpacity(0.65)], begin: Alignment.topCenter, end: Alignment.bottomCenter))),
                                Positioned(bottom: 14, left: 20, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                  Text("Galaxies", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 2)),
                                  Text("Billions of star systems", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                                ])),
                                Positioned(bottom: 18, right: 16, child: Icon(Icons.arrow_forward_ios_rounded, color: Color(0xFFCE93D8), size: 15)),
                              ]),
                            ),
                          ),
                        ),
                      ),

                      // Black Holes card with image
                      FadeInLeft(
                        delay: Duration(milliseconds: 600),
                        child: GestureDetector(
                          onTap: () => Navigator.push(context, _route(BlackHoleScreen())),
                          child: Container(
                            margin: const EdgeInsets.only(bottom: 12),
                            height: 120,
                            decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), boxShadow: [BoxShadow(color: Color(0xFF80CBC4).withOpacity(0.15), blurRadius: 20)]),
                            child: ClipRRect(
                              borderRadius: BorderRadius.circular(16),
                              child: Stack(fit: StackFit.expand, children: [
                                Image.asset("assets/images/black_holes.jpg", fit: BoxFit.cover),
                                Container(decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.black.withOpacity(0.1), Colors.black.withOpacity(0.65)], begin: Alignment.topCenter, end: Alignment.bottomCenter))),
                                Positioned(bottom: 14, left: 20, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                  Text("Black Holes", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 2)),
                                  Text("Where gravity breaks reality", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                                ])),
                                Positioned(bottom: 18, right: 16, child: Icon(Icons.arrow_forward_ios_rounded, color: Color(0xFF80CBC4), size: 15)),
                              ]),
                            ),
                          ),
                        ),
                      ),

                      // Universe card with image
                      FadeInLeft(
                        delay: Duration(milliseconds: 700),
                        child: GestureDetector(
                          onTap: () => Navigator.push(context, _route(UniverseScreen())),
                          child: Container(
                            margin: const EdgeInsets.only(bottom: 12),
                            height: 120,
                            decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), boxShadow: [BoxShadow(color: Color(0xFF90CAF9).withOpacity(0.15), blurRadius: 20)]),
                            child: ClipRRect(
                              borderRadius: BorderRadius.circular(16),
                              child: Stack(fit: StackFit.expand, children: [
                                Image.asset("assets/images/universe.jpg", fit: BoxFit.cover),
                                Container(decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.black.withOpacity(0.1), Colors.black.withOpacity(0.65)], begin: Alignment.topCenter, end: Alignment.bottomCenter))),
                                Positioned(bottom: 14, left: 20, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                  Text("Universe", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 2)),
                                  Text("93 billion light years of space", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                                ])),
                                Positioned(bottom: 18, right: 16, child: Icon(Icons.arrow_forward_ios_rounded, color: Color(0xFF90CAF9), size: 15)),
                              ]),
                            ),
                          ),
                        ),
                      ),

                      // Multiverse card with image
                      FadeInLeft(
                        delay: Duration(milliseconds: 800),
                        child: GestureDetector(
                          onTap: () => Navigator.push(context, _route(MultiverseScreen())),
                          child: Container(
                            margin: const EdgeInsets.only(bottom: 12),
                            height: 120,
                            decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), boxShadow: [BoxShadow(color: Color(0xFFF48FB1).withOpacity(0.15), blurRadius: 20)]),
                            child: ClipRRect(
                              borderRadius: BorderRadius.circular(16),
                              child: Stack(fit: StackFit.expand, children: [
                                Image.asset("assets/images/multiverse.jpg", fit: BoxFit.cover),
                                Container(decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.black.withOpacity(0.1), Colors.black.withOpacity(0.65)], begin: Alignment.topCenter, end: Alignment.bottomCenter))),
                                Positioned(bottom: 14, left: 20, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                  Text("Multiverse", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 2)),
                                  Text("Beyond our universe", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                                ])),
                                Positioned(bottom: 18, right: 16, child: Icon(Icons.arrow_forward_ios_rounded, color: Color(0xFFF48FB1), size: 15)),
                              ]),
                            ),
                          ),
                        ),
                      ),

                      const SizedBox(height: 16),
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
