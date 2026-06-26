home = open("lib/screens/home_screen.dart").read()

# Add a second AnimationController for planet rotation
home = home.replace(
    "  late AnimationController _starController;\n\n  @override\n  void initState() {\n    super.initState();\n    _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();",
    """  late AnimationController _starController;
  late AnimationController _planetController;
  late AnimationController _glowController;

  @override
  void initState() {
    super.initState();
    _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();
    _planetController = AnimationController(vsync: this, duration: const Duration(seconds: 8))..repeat();
    _glowController = AnimationController(vsync: this, duration: const Duration(seconds: 3))..repeat(reverse: true);"""
)

# Dispose all controllers
home = home.replace(
    "  @override\n  void dispose() { _starController.dispose(); super.dispose(); }",
    "  @override\n  void dispose() { _starController.dispose(); _planetController.dispose(); _glowController.dispose(); super.dispose(); }"
)

# Replace the title section with planet + title
home = home.replace(
    """                const SizedBox(height: 28),
                FadeInDown(child: Center(child: Text("COSMOS", style: GoogleFonts.orbitron(fontSize: 42, fontWeight: FontWeight.w900, color: Colors.white, letterSpacing: 10, shadows: [Shadow(color: Color(0xFF00AAFF), blurRadius: 40), Shadow(color: Color(0xFF0066FF), blurRadius: 80)])))),
                FadeInDown(delay: Duration(milliseconds: 150), child: Center(child: Text("X P L O R E R", style: GoogleFonts.orbitron(fontSize: 13, color: Color(0xFF00CCFF), letterSpacing: 14, fontWeight: FontWeight.w600)))),
                const SizedBox(height: 6),
                FadeInDown(delay: Duration(milliseconds: 250), child: Center(child: Text("Journey from planets to the multiverse", style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white54, letterSpacing: 1.5, fontWeight: FontWeight.w500)))),""",
    """                const SizedBox(height: 16),
                // 3D Rotating Planet Hero
                AnimatedBuilder(
                  animation: Listenable.merge([_planetController, _glowController]),
                  builder: (_, __) {
                    return Center(
                      child: SizedBox(
                        width: 200, height: 200,
                        child: Stack(
                          alignment: Alignment.center,
                          children: [
                            // Outer glow ring 3
                            Container(
                              width: 200 + _glowController.value * 20,
                              height: 200 + _glowController.value * 20,
                              decoration: BoxDecoration(
                                shape: BoxShape.circle,
                                boxShadow: [BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.05 + 0.05 * _glowController.value), blurRadius: 40, spreadRadius: 20)],
                              ),
                            ),
                            // Orbit ring 1
                            Transform.rotate(
                              angle: _planetController.value * 2 * 3.14159,
                              child: Container(
                                width: 180, height: 60,
                                decoration: BoxDecoration(
                                  border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.3), width: 1),
                                  borderRadius: BorderRadius.circular(100),
                                ),
                              ),
                            ),
                            // Orbit ring 2
                            Transform.rotate(
                              angle: -_planetController.value * 2 * 3.14159 * 0.7,
                              child: Container(
                                width: 160, height: 50,
                                decoration: BoxDecoration(
                                  border: Border.all(color: Color(0xFF00FFCC).withOpacity(0.2), width: 1),
                                  borderRadius: BorderRadius.circular(100),
                                ),
                              ),
                            ),
                            // Planet body
                            Container(
                              width: 110, height: 110,
                              decoration: BoxDecoration(
                                shape: BoxShape.circle,
                                gradient: RadialGradient(
                                  colors: [
                                    Color(0xFF1A6FBF),
                                    Color(0xFF0A3F7F),
                                    Color(0xFF051A3F),
                                  ],
                                  stops: [0.3, 0.7, 1.0],
                                  center: Alignment(-0.3 + _planetController.value * 0.1, -0.2),
                                ),
                                boxShadow: [
                                  BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.5 + 0.2 * _glowController.value), blurRadius: 30, spreadRadius: 5),
                                  BoxShadow(color: Color(0xFF0044FF).withOpacity(0.3), blurRadius: 60, spreadRadius: 10),
                                ],
                              ),
                              child: ClipOval(
                                child: Stack(
                                  children: [
                                    // Surface bands
                                    Positioned(top: 30, left: 0, right: 0,
                                      child: Container(height: 12, color: Colors.white.withOpacity(0.05))),
                                    Positioned(top: 55, left: 0, right: 0,
                                      child: Container(height: 8, color: Colors.white.withOpacity(0.04))),
                                    Positioned(top: 72, left: 0, right: 0,
                                      child: Container(height: 6, color: Colors.white.withOpacity(0.03))),
                                    // Atmosphere glow
                                    Positioned(left: -10, top: -10, right: -10, bottom: -10,
                                      child: Container(
                                        decoration: BoxDecoration(
                                          shape: BoxShape.circle,
                                          gradient: RadialGradient(
                                            colors: [Colors.transparent, Color(0xFF00AAFF).withOpacity(0.15)],
                                            stops: [0.7, 1.0],
                                          ),
                                        ),
                                      ),
                                    ),
                                  ],
                                ),
                              ),
                            ),
                            // Small orbiting moon
                            Transform.rotate(
                              angle: _planetController.value * 2 * 3.14159 * 1.5,
                              child: Transform.translate(
                                offset: Offset(85, 0),
                                child: Container(
                                  width: 14, height: 14,
                                  decoration: BoxDecoration(
                                    shape: BoxShape.circle,
                                    color: Color(0xFF90CAF9),
                                    boxShadow: [BoxShadow(color: Color(0xFF90CAF9).withOpacity(0.6), blurRadius: 8)],
                                  ),
                                ),
                              ),
                            ),
                          ],
                        ),
                      ),
                    );
                  },
                ),
                const SizedBox(height: 12),
                FadeInDown(child: Center(child: Text("COSMOS", style: GoogleFonts.orbitron(fontSize: 38, fontWeight: FontWeight.w900, color: Colors.white, letterSpacing: 8, shadows: [Shadow(color: Color(0xFF00AAFF), blurRadius: 30), Shadow(color: Color(0xFF0066FF), blurRadius: 60)])))),
                FadeInDown(delay: Duration(milliseconds: 150), child: Center(child: Text("X P L O R E R", style: GoogleFonts.orbitron(fontSize: 12, color: Color(0xFF00CCFF), letterSpacing: 12, fontWeight: FontWeight.w600)))),
                const SizedBox(height: 6),
                FadeInDown(delay: Duration(milliseconds: 250), child: Center(child: Text("Journey from planets to the multiverse", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white54, letterSpacing: 1.5, fontWeight: FontWeight.w500)))),"""
)

open("lib/screens/home_screen.dart", "w").write(home)
print("Done!")
