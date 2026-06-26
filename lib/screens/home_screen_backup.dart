import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:animate_do/animate_do.dart';
import 'planets_screen.dart';
import 'solar_system_screen.dart';
import 'galaxy_screen.dart';
import 'universe_screen.dart';
import 'multiverse_screen.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});
  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _starController;

  final List<_Level> levels = [
    _Level('Planets',      '🪐', 'Explore all 8 planets',           Color(0xFF4FC3F7)),
    _Level('Solar System', '☀️', 'Our cosmic neighbourhood',         Color(0xFFFFB347)),
    _Level('Galaxies',     '🌌', 'Billions of star systems',         Color(0xFFCE93D8)),
    _Level('Black Holes',  '🕳️', 'Where gravity breaks reality',     Color(0xFF80CBC4)),
    _Level('Universe',     '🔭', '93 billion light years of space',  Color(0xFF90CAF9)),
    _Level('Multiverse',   '♾️', 'Beyond our universe',              Color(0xFFF48FB1)),
  ];

  @override
  void initState() {
    super.initState();
    _starController = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 20),
    )..repeat();
  }

  @override
  void dispose() {
    _starController.dispose();
    super.dispose();
  }

  void _navigate(BuildContext context, int index) {
    final screens = [
      PlanetsScreen(),
      SolarSystemScreen(),
      GalaxyScreen(),
      GalaxyScreen(),
      UniverseScreen(),
      MultiverseScreen(),
    ];
    Navigator.push(
      context,
      PageRouteBuilder(
        pageBuilder: (_, __, ___) => screens[index],
        transitionsBuilder: (_, anim, __, child) =>
            FadeTransition(opacity: anim, child: child),
        transitionDuration: const Duration(milliseconds: 600),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Stack(
        children: [
          AnimatedBuilder(
            animation: _starController,
            builder: (_, __) => CustomPaint(
              painter: _StarPainter(_starController.value),
              child: const SizedBox.expand(),
            ),
          ),
          SafeArea(
            child: Column(
              children: [
                const SizedBox(height: 40),
                FadeInDown(
                  child: Text('COSMOS',
                    style: GoogleFonts.orbitron(
                      fontSize: 42, fontWeight: FontWeight.w900,
                      color: Colors.white, letterSpacing: 8,
                      shadows: [Shadow(color: Color(0xFF00AAFF), blurRadius: 30)],
                    ),
                  ),
                ),
                FadeInDown(
                  delay: Duration(milliseconds: 200),
                  child: Text('X P L O R E R',
                    style: GoogleFonts.orbitron(
                      fontSize: 14, color: Color(0xFF00AAFF), letterSpacing: 12,
                    ),
                  ),
                ),
                const SizedBox(height: 8),
                FadeInDown(
                  delay: Duration(milliseconds: 300),
                  child: Text('Journey from planets to the multiverse',
                    style: GoogleFonts.rajdhani(
                      fontSize: 14, color: Colors.white38, letterSpacing: 1.5,
                    ),
                  ),
                ),
                const SizedBox(height: 40),
                Expanded(
                  child: ListView.builder(
                    padding: const EdgeInsets.symmetric(horizontal: 20),
                    itemCount: levels.length,
                    itemBuilder: (ctx, i) => FadeInLeft(
                      delay: Duration(milliseconds: 200 + i * 100),
                      child: _LevelCard(
                        level: levels[i],
                        onTap: () => _navigate(context, i),
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

class _Level {
  final String title, emoji, subtitle;
  final Color color;
  const _Level(this.title, this.emoji, this.subtitle, this.color);
}

class _LevelCard extends StatelessWidget {
  final _Level level;
  final VoidCallback onTap;
  const _LevelCard({required this.level, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        margin: const EdgeInsets.only(bottom: 14),
        padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 18),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(16),
          color: const Color(0xFF040F1F),
          border: Border.all(color: level.color.withOpacity(0.3), width: 1),
          boxShadow: [BoxShadow(color: level.color.withOpacity(0.08), blurRadius: 20)],
        ),
        child: Row(
          children: [
            Text(level.emoji, style: const TextStyle(fontSize: 36)),
            const SizedBox(width: 16),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Text(level.title,
                    style: GoogleFonts.orbitron(
                      fontSize: 16, fontWeight: FontWeight.w700,
                      color: Colors.white, letterSpacing: 1.5,
                    ),
                  ),
                  const SizedBox(height: 4),
                  Text(level.subtitle,
                    style: GoogleFonts.rajdhani(
                      fontSize: 13, color: Colors.white38, letterSpacing: 0.5,
                    ),
                  ),
                ],
              ),
            ),
            Icon(Icons.arrow_forward_ios_rounded, color: level.color, size: 16),
          ],
        ),
      ),
    );
  }
}

class _StarPainter extends CustomPainter {
  final double progress;
  static final _rng = Random(42);
  static final _stars = List.generate(150,
    (_) => Offset(_rng.nextDouble(), _rng.nextDouble()));

  _StarPainter(this.progress);

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint();
    for (int i = 0; i < _stars.length; i++) {
      final twinkle = 0.3 + 0.7 * (0.5 + 0.5 * sin(progress * 2 * pi * 2 + i));
      paint.color = Colors.white.withOpacity(twinkle * 0.8);
      canvas.drawCircle(
        Offset(_stars[i].dx * size.width, _stars[i].dy * size.height),
        _rng.nextDouble() * 1.5 + 0.3,
        paint,
      );
    }
  }

  @override
  bool shouldRepaint(_StarPainter old) => true;
}
