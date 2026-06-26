import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class SettingsScreen extends StatefulWidget {
  const SettingsScreen({super.key});
  @override
  State<SettingsScreen> createState() => _SettingsScreenState();
}

class _SettingsScreenState extends State<SettingsScreen> with SingleTickerProviderStateMixin {
  late AnimationController _starController;
  bool _showFishyFacts = true;
  bool _animationsEnabled = true;
  String _selectedTheme = 'Deep Space';

  @override
  void initState() {
    super.initState();
    _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();
  }

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
              Padding(padding: const EdgeInsets.fromLTRB(20,16,20,12), child: Row(children: [
                GestureDetector(onTap: () => Navigator.pop(context), child: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white54, size: 20)),
                const SizedBox(width: 16),
                Text("SETTINGS", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 4)),
              ])),
              Expanded(child: ListView(padding: const EdgeInsets.symmetric(horizontal: 16), children: [

                // App info card
                Container(
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(borderRadius: BorderRadius.circular(20), color: const Color(0xFF040F1F), border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.2))),
                  child: Row(children: [
                    Container(width: 64, height: 64, decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), gradient: RadialGradient(colors: [Color(0xFF00AAFF), Color(0xFF0044AA), Color(0xFF001133)], stops: [0.2, 0.6, 1.0])),
                      child: const Center(child: Text("🌌", style: TextStyle(fontSize: 32)))),
                    const SizedBox(width: 16),
                    Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text("CosmosXplorer", style: GoogleFonts.orbitron(fontSize: 16, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 1)),
                      const SizedBox(height: 4),
                      Text("Version 1.0.0", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white38)),
                      Text("Journey through the universe", style: GoogleFonts.rajdhani(fontSize: 13, color: Color(0xFF00AAFF))),
                    ])),
                  ]),
                ),
                const SizedBox(height: 24),

                _sectionLabel("PREFERENCES"),
                const SizedBox(height: 10),

                _switchTile("Show Mind-Blowing Facts", "Display the fishy facts on planet cards", "🐟", _showFishyFacts, (v) => setState(() => _showFishyFacts = v)),
                _switchTile("Animations", "Enable screen transition animations", "✨", _animationsEnabled, (v) => setState(() => _animationsEnabled = v)),
                const SizedBox(height: 24),

                _sectionLabel("ABOUT"),
                const SizedBox(height: 10),

                _infoTile("🌍", "Content", "All astronomical data is based on current scientific knowledge and NASA research."),
                _infoTile("📱", "Platform", "Built with Flutter — available on Android & iOS"),
                _infoTile("🔭", "Data Sources", "NASA, ESA, European Southern Observatory"),
                _infoTile("🧑‍💻", "Developer", "Built with passion for space exploration"),
                const SizedBox(height: 24),

                _sectionLabel("EXPLORE"),
                const SizedBox(height: 10),

                _statCard("🪐", "Planets", "8", "Fully documented"),
                _statCard("🌌", "Galaxies", "6", "Notable galaxies"),
                _statCard("🕳️", "Black Holes", "6", "Types covered"),
                _statCard("🧠", "Quiz Questions", "15", "Cosmic trivia"),
                _statCard("🔍", "Searchable Items", "28", "Facts & objects"),
                const SizedBox(height: 24),

                _sectionLabel("FUN COSMIC FACTS"),
                const SizedBox(height: 10),

                ...[ 
                  ["🌟", "There are more stars in the universe than grains of sand on all of Earth's beaches combined."],
                  ["⚡", "A bolt of lightning is 5x hotter than the surface of the Sun."],
                  ["🚀", "If you could drive to the Sun at highway speed, it would take 170 years."],
                  ["🌊", "The Pacific Ocean is larger than all the land on Earth combined."],
                  ["🔭", "The light you see from stars left them thousands of years ago — you're looking into the past."],
                ].map((f) => Container(
                  margin: const EdgeInsets.only(bottom: 10),
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: Colors.white12)),
                  child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                    Text(f[0], style: const TextStyle(fontSize: 20)),
                    const SizedBox(width: 12),
                    Expanded(child: Text(f[1], style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60, height: 1.4))),
                  ]),
                )),

                const SizedBox(height: 24),
                Center(child: Column(children: [
                  Text("Made with ❤️ for space explorers", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white24)),
                  const SizedBox(height: 4),
                  Text("CosmosXplorer © 2025", style: GoogleFonts.orbitron(fontSize: 9, color: Colors.white12, letterSpacing: 2)),
                ])),
                const SizedBox(height: 24),
              ])),
            ]),
          ),
        ],
      ),
    );
  }

  Widget _sectionLabel(String label) => Text(label, style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF00AAFF), letterSpacing: 2));

  Widget _switchTile(String title, String subtitle, String emoji, bool value, Function(bool) onChanged) {
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
      decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: Colors.white12)),
      child: Row(children: [
        Text(emoji, style: const TextStyle(fontSize: 24)),
        const SizedBox(width: 12),
        Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(title, style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white, fontWeight: FontWeight.w600)),
          Text(subtitle, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
        ])),
        Switch(value: value, onChanged: onChanged, activeColor: Color(0xFF00AAFF)),
      ]),
    );
  }

  Widget _infoTile(String emoji, String title, String value) {
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: Colors.white12)),
      child: Row(children: [
        Text(emoji, style: const TextStyle(fontSize: 22)),
        const SizedBox(width: 12),
        Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
          Text(title, style: GoogleFonts.orbitron(fontSize: 9, color: Color(0xFF00AAFF), letterSpacing: 1)),
          const SizedBox(height: 3),
          Text(value, style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white60, height: 1.3)),
        ])),
      ]),
    );
  }

  Widget _statCard(String emoji, String label, String value, String sub) {
    return Container(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: Colors.white12)),
      child: Row(children: [
        Text(emoji, style: const TextStyle(fontSize: 24)),
        const SizedBox(width: 12),
        Expanded(child: Text(label, style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white70, fontWeight: FontWeight.w600))),
        Column(crossAxisAlignment: CrossAxisAlignment.end, children: [
          Text(value, style: GoogleFonts.orbitron(fontSize: 18, color: Color(0xFF00AAFF), fontWeight: FontWeight.w700)),
          Text(sub, style: GoogleFonts.rajdhani(fontSize: 10, color: Colors.white24)),
        ]),
      ]),
    );
  }
}

class _SP extends CustomPainter {
  final double progress;
  static final _rng = Random(33);
  static final _stars = List.generate(120, (_) => Offset(_rng.nextDouble(), _rng.nextDouble()));
  static final _szs = List.generate(120, (_) => _rng.nextDouble() * 1.2 + 0.3);
  _SP(this.progress);
  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint();
    for (int i = 0; i < _stars.length; i++) {
      final t = 0.3+0.7*(0.5+0.5*sin(progress*2*pi*2+i));
      paint.color = Colors.white.withOpacity(t*0.6);
      canvas.drawCircle(Offset(_stars[i].dx*size.width,_stars[i].dy*size.height),_szs[i],paint);
    }
  }
  @override bool shouldRepaint(_) => true;
}
