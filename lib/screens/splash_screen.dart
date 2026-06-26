import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'home_screen.dart';

class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});
  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen>
    with TickerProviderStateMixin {
  late AnimationController _logoController;
  late AnimationController _textController;
  late AnimationController _starController;
  late AnimationController _fadeController;

  late Animation<double> _logoScale;
  late Animation<double> _logoOpacity;
  late Animation<double> _textOpacity;
  late Animation<double> _taglineOpacity;
  late Animation<double> _fadeOut;

  @override
  void initState() {
    super.initState();

    _starController = AnimationController(
      vsync: this,
      duration: const Duration(seconds: 20),
    )..repeat();

    _logoController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1200),
    );

    _textController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 1500),
    );

    _fadeController = AnimationController(
      vsync: this,
      duration: const Duration(milliseconds: 800),
    );

    _logoScale = Tween<double>(begin: 0.3, end: 1.0).animate(
      CurvedAnimation(parent: _logoController, curve: Curves.elasticOut),
    );
    _logoOpacity = Tween<double>(begin: 0.0, end: 1.0).animate(
      CurvedAnimation(parent: _logoController, curve: const Interval(0.0, 0.5)),
    );
    _textOpacity = Tween<double>(begin: 0.0, end: 1.0).animate(
      CurvedAnimation(parent: _textController, curve: const Interval(0.0, 0.6)),
    );
    _taglineOpacity = Tween<double>(begin: 0.0, end: 1.0).animate(
      CurvedAnimation(parent: _textController, curve: const Interval(0.4, 1.0)),
    );
    _fadeOut = Tween<double>(begin: 1.0, end: 0.0).animate(_fadeController);

    _runAnimation();
  }

  Future<void> _runAnimation() async {
    await Future.delayed(const Duration(milliseconds: 300));
    await _logoController.forward();
    await Future.delayed(const Duration(milliseconds: 200));
    await _textController.forward();
    await Future.delayed(const Duration(milliseconds: 1500));
    await _fadeController.forward();
    if (mounted) {
      Navigator.of(context).pushReplacement(
        PageRouteBuilder(
          pageBuilder: (_, __, ___) => HomeScreen(),
          transitionsBuilder: (_, anim, __, child) =>
              FadeTransition(opacity: anim, child: child),
          transitionDuration: const Duration(milliseconds: 600),
        ),
      );
    }
  }

  @override
  void dispose() {
    _logoController.dispose();
    _textController.dispose();
    _starController.dispose();
    _fadeController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.black,
      body: AnimatedBuilder(
        animation: Listenable.merge([
          _logoController, _textController,
          _starController, _fadeController,
        ]),
        builder: (_, __) => FadeTransition(
          opacity: _fadeOut,
          child: Stack(
            children: [
              // Background image
              Image.asset("assets/images/space.jpg", fit: BoxFit.cover, width: double.infinity, height: double.infinity),
              // Dark overlay
              Container(color: Colors.black.withOpacity(0.55)),
              // Starfield on top
              CustomPaint(
                painter: _SplashStarPainter(_starController.value),
                child: const SizedBox.expand(),
              ),

              // Nebula glow background
              Center(
                child: Container(
                  width: 300,
                  height: 300,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    gradient: RadialGradient(
                      colors: [
                        Color(0xFF00AAFF).withOpacity(0.08 * _logoOpacity.value),
                        Color(0xFF0044AA).withOpacity(0.05 * _logoOpacity.value),
                        Colors.transparent,
                      ],
                    ),
                  ),
                ),
              ),

              // Main content
              Center(
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    // Animated planet icon
                    Transform.scale(
                      scale: _logoScale.value,
                      child: Opacity(
                        opacity: _logoOpacity.value.clamp(0.0, 1.0),
                        child: Container(
                          width: 100,
                          height: 100,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            gradient: RadialGradient(
                              colors: [
                                Color(0xFF00AAFF),
                                Color(0xFF0044AA),
                                Color(0xFF001133),
                              ],
                              stops: [0.2, 0.6, 1.0],
                            ),
                            boxShadow: [
                              BoxShadow(
                                color: Color(0xFF00AAFF).withOpacity(0.6),
                                blurRadius: 40,
                                spreadRadius: 10,
                              ),
                            ],
                          ),
                          child: const Center(
                            child: Text("🌌", style: TextStyle(fontSize: 48)),
                          ),
                        ),
                      ),
                    ),

                    const SizedBox(height: 32),

                    // COSMOS text
                    Opacity(
                      opacity: _textOpacity.value.clamp(0.0, 1.0),
                      child: Text(
                        "COSMOS",
                        style: GoogleFonts.orbitron(
                          fontSize: 42,
                          fontWeight: FontWeight.w900,
                          color: Colors.white,
                          letterSpacing: 10,
                          shadows: [
                            Shadow(
                              color: Color(0xFF00AAFF),
                              blurRadius: 30,
                            ),
                          ],
                        ),
                      ),
                    ),

                    const SizedBox(height: 6),

                    // XPLORER text
                    Opacity(
                      opacity: _textOpacity.value.clamp(0.0, 1.0),
                      child: Text(
                        "X P L O R E R",
                        style: GoogleFonts.orbitron(
                          fontSize: 14,
                          color: Color(0xFF00AAFF),
                          letterSpacing: 12,
                          fontWeight: FontWeight.w400,
                        ),
                      ),
                    ),

                    const SizedBox(height: 24),

                    // Tagline
                    Opacity(
                      opacity: _taglineOpacity.value.clamp(0.0, 1.0),
                      child: Text(
                        "Journey from planets to the multiverse",
                        style: GoogleFonts.rajdhani(
                          fontSize: 14,
                          color: Colors.white38,
                          letterSpacing: 1.5,
                        ),
                      ),
                    ),

                    const SizedBox(height: 60),

                    // Loading dots
                    Opacity(
                      opacity: _taglineOpacity.value.clamp(0.0, 1.0),
                      child: Row(
                        mainAxisSize: MainAxisSize.min,
                        children: List.generate(3, (i) {
                          final t = (_starController.value * 3 - i * 0.3) % 1.0;
                          final opacity = (0.3 + 0.7 * (0.5 + 0.5 * sin(t * 2 * pi))).clamp(0.0, 1.0);
                          return Container(
                            margin: const EdgeInsets.symmetric(horizontal: 4),
                            width: 6,
                            height: 6,
                            decoration: BoxDecoration(
                              shape: BoxShape.circle,
                              color: Color(0xFF00AAFF).withOpacity(opacity),
                            ),
                          );
                        }),
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class _SplashStarPainter extends CustomPainter {
  final double progress;
  static final _rng = Random(42);
  static final _stars = List.generate(200,
      (_) => Offset(_rng.nextDouble(), _rng.nextDouble()));
  static final _szs = List.generate(200,
      (_) => _rng.nextDouble() * 1.5 + 0.3);

  _SplashStarPainter(this.progress);

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint();
    for (int i = 0; i < _stars.length; i++) {
      final t = 0.2 + 0.8 * (0.5 + 0.5 * sin(progress * 2 * pi * 1.5 + i));
      paint.color = Colors.white.withOpacity(t * 0.8);
      canvas.drawCircle(
        Offset(_stars[i].dx * size.width, _stars[i].dy * size.height),
        _szs[i], paint,
      );
    }
  }

  @override
  bool shouldRepaint(_SplashStarPainter o) => true;
}
