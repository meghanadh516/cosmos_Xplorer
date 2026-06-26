import 'dart:math';
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
import 'quiz_screen.dart';
import 'settings_screen.dart';
import 'ai_assistant_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> with TickerProviderStateMixin {
  late AnimationController _starController;
  late AnimationController _planetController;
  late AnimationController _glowController;

  @override
  void initState() {
    super.initState();
    _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();
    _planetController = AnimationController(vsync: this, duration: const Duration(seconds: 8))..repeat();
    _glowController = AnimationController(vsync: this, duration: const Duration(seconds: 3))..repeat(reverse: true);
  }

  @override
  void dispose() {
    _starController.dispose();
    _planetController.dispose();
    _glowController.dispose();
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
      body: Stack(
        children: [
          // Starfield background
          AnimatedBuilder(
            animation: _starController,
            builder: (_, __) => CustomPaint(
              painter: _StarPainter(_starController.value),
              child: const SizedBox.expand(),
            ),
          ),

          // Everything in ONE scrollable list
          SafeArea(
            child: Stack(
              children: [
                CustomScrollView(
                  slivers: [
                    SliverList(
                      delegate: SliverChildListDelegate([

                        // Settings icon
                        Align(
                          alignment: Alignment.centerRight,
                          child: Padding(
                            padding: const EdgeInsets.only(right: 16, top: 12),
                            child: GestureDetector(
                              onTap: () => Navigator.push(context, _route(SettingsScreen())),
                              child: Icon(Icons.settings_outlined, color: Colors.white38, size: 22),
                            ),
                          ),
                        ),

                        // 3D Rotating Planet
                        AnimatedBuilder(
                          animation: Listenable.merge([_planetController, _glowController]),
                          builder: (_, __) {
                            return Center(
                              child: SizedBox(
                                width: 180, height: 180,
                                child: Stack(alignment: Alignment.center, children: [
                                  Container(
                                    width: 180 + _glowController.value * 20,
                                    height: 180 + _glowController.value * 20,
                                    decoration: BoxDecoration(shape: BoxShape.circle,
                                      boxShadow: [BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.06 + 0.04 * _glowController.value), blurRadius: 60, spreadRadius: 20)]),
                                  ),
                                  Transform.rotate(
                                    angle: _planetController.value * 2 * pi,
                                    child: Container(width: 170, height: 55,
                                      decoration: BoxDecoration(border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.35), width: 1.5), borderRadius: BorderRadius.circular(100))),
                                  ),
                                  Transform.rotate(
                                    angle: -_planetController.value * 2 * pi * 0.6,
                                    child: Container(width: 150, height: 45,
                                      decoration: BoxDecoration(border: Border.all(color: Color(0xFF00FFCC).withOpacity(0.2), width: 1), borderRadius: BorderRadius.circular(100))),
                                  ),
                                  Container(
                                    width: 100, height: 100,
                                    decoration: BoxDecoration(
                                      shape: BoxShape.circle,
                                      gradient: RadialGradient(
                                        colors: [Color(0xFF1A6FBF), Color(0xFF0A3F7F), Color(0xFF051A3F)],
                                        stops: [0.3, 0.7, 1.0],
                                        center: Alignment(-0.3 + _planetController.value * 0.1, -0.2),
                                      ),
                                      boxShadow: [
                                        BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.5 + 0.2 * _glowController.value), blurRadius: 30, spreadRadius: 5),
                                        BoxShadow(color: Color(0xFF0044FF).withOpacity(0.3), blurRadius: 60, spreadRadius: 10),
                                      ],
                                    ),
                                    child: ClipOval(child: Stack(children: [
                                      Positioned(top: 28, left: 0, right: 0, child: Container(height: 10, color: Colors.white.withOpacity(0.06))),
                                      Positioned(top: 48, left: 0, right: 0, child: Container(height: 7, color: Colors.white.withOpacity(0.04))),
                                      Positioned(top: 65, left: 0, right: 0, child: Container(height: 5, color: Colors.white.withOpacity(0.03))),
                                    ])),
                                  ),
                                  Transform.rotate(
                                    angle: _planetController.value * 2 * pi * 1.5,
                                    child: Transform.translate(offset: Offset(80, 0),
                                      child: Container(width: 12, height: 12,
                                        decoration: BoxDecoration(shape: BoxShape.circle, color: Color(0xFF90CAF9),
                                          boxShadow: [BoxShadow(color: Color(0xFF90CAF9).withOpacity(0.7), blurRadius: 8)]))),
                                  ),
                                ]),
                              ),
                            );
                          },
                        ),

                        const SizedBox(height: 8),

                        // Title
                        FadeInDown(child: Center(child: Text("COSMOS", style: GoogleFonts.orbitron(fontSize: 38, fontWeight: FontWeight.w900, color: Colors.white, letterSpacing: 8, shadows: [Shadow(color: Color(0xFF00AAFF), blurRadius: 30), Shadow(color: Color(0xFF0066FF), blurRadius: 60)])))),
                        FadeInDown(delay: Duration(milliseconds: 150), child: Center(child: Text("X P L O R E R", style: GoogleFonts.orbitron(fontSize: 12, color: Color(0xFF00CCFF), letterSpacing: 12, fontWeight: FontWeight.w600)))),
                        const SizedBox(height: 4),
                        FadeInDown(delay: Duration(milliseconds: 250), child: Center(child: Text("Journey from planets to the multiverse", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white54, letterSpacing: 1.5)))),
                        const SizedBox(height: 12),

                        // Search bar
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 16),
                          child: GestureDetector(
                            onTap: () => Navigator.push(context, _route(SearchScreen())),
                            child: Container(
                              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 11),
                              decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.4), width: 1.5)),
                              child: Row(children: [
                                Icon(Icons.search_rounded, color: Color(0xFF00AAFF), size: 20),
                                const SizedBox(width: 10),
                                Text("Search planets, galaxies, facts...", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white24)),
                              ]),
                            ),
                          ),
                        ),
                        const SizedBox(height: 10),

                        // Daily Fact
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 16),
                          child: _DailyFactBanner(),
                        ),
                        const SizedBox(height: 12),

                        // Solar System featured card
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 16),
                          child: GestureDetector(
                            onTap: () => Navigator.push(context, _route(SolarSystemScreen())),
                            child: Container(
                              margin: const EdgeInsets.only(bottom: 10), height: 140,
                              decoration: BoxDecoration(borderRadius: BorderRadius.circular(20), boxShadow: [BoxShadow(color: Color(0xFFFFB347).withOpacity(0.2), blurRadius: 20)]),
                              child: ClipRRect(borderRadius: BorderRadius.circular(20), child: Stack(fit: StackFit.expand, children: [
                                Image.asset("assets/images/_solar_system.jpg", fit: BoxFit.cover, errorBuilder: (_, __, ___) => Container(color: const Color(0xFF071628))),
                                Container(decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.black.withOpacity(0.1), Colors.black.withOpacity(0.65)], begin: Alignment.topCenter, end: Alignment.bottomCenter))),
                                Positioned(bottom: 14, left: 18, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                  Text("Solar System", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 2)),
                                  Text("Our cosmic neighbourhood", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60)),
                                ])),
                                Positioned(top: 12, right: 12, child: Container(
                                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                                  decoration: BoxDecoration(color: Colors.black38, borderRadius: BorderRadius.circular(20), border: Border.all(color: Colors.white24)),
                                  child: Text("FEATURED", style: GoogleFonts.orbitron(fontSize: 7, color: Colors.white70, letterSpacing: 2)))),
                              ])),
                            ),
                          ),
                        ),

                        // Image cards
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 16),
                          child: Column(children: [
                            ...[
                              ["Planets", "Explore all 8 planets", "assets/images/planets.jpg", Color(0xFF4FC3F7), PlanetsScreen()],
                              ["Galaxies", "Billions of star systems", "assets/images/galaxy.jpg", Color(0xFFCE93D8), GalaxyScreen()],
                              ["Black Holes", "Where gravity breaks reality", "assets/images/black_holes.jpg", Color(0xFF80CBC4), BlackHoleScreen()],
                              ["Universe", "93 billion light years", "assets/images/universe.jpg", Color(0xFF90CAF9), UniverseScreen()],
                              ["Multiverse", "Beyond our universe", "assets/images/multiverse.jpg", Color(0xFFF48FB1), MultiverseScreen()],
                            ].asMap().entries.map((e) {
                              final i = e.key;
                              final d = e.value;
                              return FadeInLeft(
                                delay: Duration(milliseconds: 100 + i * 80),
                                child: GestureDetector(
                                  onTap: () => Navigator.push(context, _route(d[4] as Widget)),
                                  child: Container(
                                    margin: const EdgeInsets.only(bottom: 10), height: 110,
                                    decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), boxShadow: [BoxShadow(color: (d[3] as Color).withOpacity(0.12), blurRadius: 16)]),
                                    child: ClipRRect(borderRadius: BorderRadius.circular(16), child: Stack(fit: StackFit.expand, children: [
                                      Image.asset(d[2] as String, fit: BoxFit.cover, errorBuilder: (_, __, ___) => Container(color: (d[3] as Color).withOpacity(0.3))),
                                      Container(decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.black.withOpacity(0.1), Colors.black.withOpacity(0.7)], begin: Alignment.topCenter, end: Alignment.bottomCenter))),
                                      Positioned(bottom: 12, left: 18, child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                        Text(d[0] as String, style: GoogleFonts.orbitron(fontSize: 16, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 1.5)),
                                        Text(d[1] as String, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white60)),
                                      ])),
                                      Positioned(bottom: 16, right: 14, child: Icon(Icons.arrow_forward_ios_rounded, color: d[3] as Color, size: 14)),
                                    ])),
                                  ),
                                ),
                              );
                            }),
                          ]),
                        ),

                        // Quiz card
                        Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 16),
                          child: GestureDetector(
                            onTap: () => Navigator.push(context, _route(QuizScreen())),
                            child: Container(
                              margin: const EdgeInsets.only(bottom: 100),
                              padding: const EdgeInsets.all(18),
                              decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: const Color(0xFF040F1F), border: Border.all(color: Color(0xFFFFD700).withOpacity(0.4)), boxShadow: [BoxShadow(color: Color(0xFFFFD700).withOpacity(0.08), blurRadius: 20)]),
                              child: Row(children: [
                                Text("🧠", style: TextStyle(fontSize: 34)),
                                const SizedBox(width: 14),
                                Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                  Text("Cosmic Quiz", style: GoogleFonts.orbitron(fontSize: 15, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 1.5)),
                                  const SizedBox(height: 3),
                                  Text("Test your space knowledge", style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
                                ])),
                                Icon(Icons.arrow_forward_ios_rounded, color: Color(0xFFFFD700), size: 14),
                              ]),
                            ),
                          ),
                        ),
                      ]),
                    ),
                  ],
                ),

                // NOVA floating button - always visible
                Positioned(
                  bottom: 24, right: 20,
                  child: GestureDetector(
                    onTap: () => Navigator.push(context, _route(AIAssistantScreen())),
                    child: AnimatedBuilder(
                      animation: _glowController,
                      builder: (_, __) => Column(mainAxisSize: MainAxisSize.min, children: [
                        Container(
                          width: 60, height: 60,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            gradient: RadialGradient(colors: [Color(0xFF00AAFF), Color(0xFF0044AA)]),
                            boxShadow: [BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.4 + 0.2 * _glowController.value), blurRadius: 20 + 10 * _glowController.value, spreadRadius: 2)],
                          ),
                          child: const Center(child: Text("⭐", style: TextStyle(fontSize: 28))),
                        ),
                        const SizedBox(height: 4),
                        Text("NOVA", style: GoogleFonts.orbitron(fontSize: 8, color: Color(0xFF00AAFF), letterSpacing: 2)),
                      ]),
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

class _DailyFactBanner extends StatefulWidget {
  const _DailyFactBanner();
  @override
  State<_DailyFactBanner> createState() => _DailyFactBannerState();
}
class _DailyFactBannerState extends State<_DailyFactBanner> with SingleTickerProviderStateMixin {
  late AnimationController _pulse;
  final List<Map<String,String>> facts = [
    {"emoji":"🌌","fact":"The Milky Way has 200-400 billion stars — and there are 2 trillion galaxies in the universe."},
    {"emoji":"💎","fact":"It rains diamonds on Neptune. Extreme pressure turns carbon into gem crystals."},
    {"emoji":"⏰","fact":"A day on Venus is longer than its year. It spins that slowly."},
    {"emoji":"🕳️","fact":"Time slows down near a black hole due to extreme gravity — proven by Einstein."},
    {"emoji":"🌅","fact":"Mars has blue sunsets and red skies — the opposite of Earth."},
    {"emoji":"☀️","fact":"The Sun makes up 99.8% of all mass in the Solar System."},
    {"emoji":"🌍","fact":"You are made of stardust — every atom in your body was forged in a star."},
  ];
  late int _factIndex;
  @override
  void initState() {
    super.initState();
    _factIndex = DateTime.now().day % facts.length;
    _pulse = AnimationController(vsync: this, duration: const Duration(seconds: 3))..repeat(reverse: true);
  }
  @override
  void dispose() { _pulse.dispose(); super.dispose(); }
  @override
  Widget build(BuildContext context) {
    final f = facts[_factIndex];
    return AnimatedBuilder(
      animation: _pulse,
      builder: (_, __) => Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F),
          border: Border.all(color: Color(0xFF00FFCC).withOpacity(0.2 + 0.15 * _pulse.value), width: 1.5),
          boxShadow: [BoxShadow(color: Color(0xFF00FFCC).withOpacity(0.04 + 0.04 * _pulse.value), blurRadius: 20)],
        ),
        child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Column(children: [
            Text(f["emoji"]!, style: const TextStyle(fontSize: 22)),
            const SizedBox(height: 2),
            Text("TODAY", style: GoogleFonts.orbitron(fontSize: 6, color: Color(0xFF00FFCC), letterSpacing: 1)),
          ]),
          const SizedBox(width: 10),
          Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
            Text("COSMIC FACT OF THE DAY", style: GoogleFonts.orbitron(fontSize: 7, color: Color(0xFF00FFCC), letterSpacing: 1.5)),
            const SizedBox(height: 4),
            Text(f["fact"]!, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white70, height: 1.4)),
          ])),
        ]),
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
  @override bool shouldRepaint(_) => true;
}
