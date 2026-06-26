import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class QuizQuestion {
  final String question, emoji;
  final List<String> options;
  final int correctIndex;
  final String explanation;
  const QuizQuestion({required this.question, required this.emoji, required this.options, required this.correctIndex, required this.explanation});
}

final List<QuizQuestion> allQuestions = [
  QuizQuestion(question: "Which is the hottest planet in our Solar System?", emoji: "🌡️", options: ["Mercury", "Venus", "Mars", "Jupiter"], correctIndex: 1, explanation: "Venus is the hottest despite not being closest to the Sun — its thick CO₂ atmosphere traps heat like a greenhouse."),
  QuizQuestion(question: "How many moons does Jupiter have?", emoji: "🌙", options: ["12", "53", "79", "95"], correctIndex: 3, explanation: "Jupiter has 95 known moons — more than any other planet. The four largest are called the Galilean moons."),
  QuizQuestion(question: "What percentage of the Solar System's mass is the Sun?", emoji: "☀️", options: ["75%", "90%", "99.8%", "85%"], correctIndex: 2, explanation: "The Sun contains 99.8% of all mass in the Solar System — everything else is just 0.2%."),
  QuizQuestion(question: "Which planet has the longest day?", emoji: "⏰", options: ["Mercury", "Venus", "Uranus", "Saturn"], correctIndex: 1, explanation: "A day on Venus (243 Earth days) is longer than its year (225 Earth days) — it spins incredibly slowly."),
  QuizQuestion(question: "What is Sagittarius A*?", emoji: "🕳️", options: ["A star cluster", "A nebula", "The black hole at center of Milky Way", "A satellite galaxy"], correctIndex: 2, explanation: "Sagittarius A* is the supermassive black hole at the center of our Milky Way galaxy, with 4 million solar masses."),
  QuizQuestion(question: "How old is the universe?", emoji: "🌌", options: ["4.6 billion years", "10 billion years", "13.8 billion years", "20 billion years"], correctIndex: 2, explanation: "The universe is 13.8 billion years old, beginning with the Big Bang — a rapid expansion from an incredibly dense state."),
  QuizQuestion(question: "What makes up 68% of the universe?", emoji: "⚡", options: ["Dark Matter", "Dark Energy", "Normal Matter", "Black Holes"], correctIndex: 1, explanation: "Dark energy makes up 68% of the universe and is responsible for its accelerating expansion. We still don't know what it is."),
  QuizQuestion(question: "Which planet rains diamonds?", emoji: "💎", options: ["Saturn", "Jupiter", "Uranus", "Neptune"], correctIndex: 3, explanation: "Neptune's extreme pressure converts carbon into diamond crystals that fall like hailstones toward the core."),
  QuizQuestion(question: "What is the Milky Way?", emoji: "🌌", options: ["A nebula", "Our home galaxy", "A star cluster", "A type of black hole"], correctIndex: 1, explanation: "The Milky Way is our home galaxy — a barred spiral galaxy containing 200–400 billion stars."),
  QuizQuestion(question: "Which planet has blue sunsets?", emoji: "🌅", options: ["Earth", "Venus", "Mars", "Mercury"], correctIndex: 2, explanation: "Mars has blue sunsets because dust particles scatter light in reverse — blue at dusk, red during the day."),
  QuizQuestion(question: "What is the Great Red Spot on Jupiter?", emoji: "🔴", options: ["A volcano", "An ocean", "A storm", "A crater"], correctIndex: 2, explanation: "The Great Red Spot is a massive storm on Jupiter that has been raging for over 400 years."),
  QuizQuestion(question: "How many galaxies are in the observable universe?", emoji: "🔭", options: ["200 million", "2 billion", "2 trillion", "200 trillion"], correctIndex: 2, explanation: "There are approximately 2 trillion galaxies in the observable universe — if you counted one per second, it would take 63 million years."),
  QuizQuestion(question: "What is the closest star to Earth after the Sun?", emoji: "⭐", options: ["Sirius", "Proxima Centauri", "Betelgeuse", "Vega"], correctIndex: 1, explanation: "Proxima Centauri is 4.24 light years away — the closest star to our Solar System after the Sun."),
  QuizQuestion(question: "Which planet could float on water?", emoji: "💧", options: ["Jupiter", "Uranus", "Saturn", "Neptune"], correctIndex: 2, explanation: "Saturn is the least dense planet — it would float on water if you had an ocean large enough to put it in."),
  QuizQuestion(question: "What does Uranus smell like?", emoji: "👃", options: ["Nothing", "Rotten eggs", "Roses", "Ammonia"], correctIndex: 1, explanation: "Uranus's upper atmosphere contains hydrogen sulfide — the same compound responsible for the smell of rotten eggs."),
];

class QuizScreen extends StatefulWidget {
  const QuizScreen({super.key});
  @override
  State<QuizScreen> createState() => _QuizScreenState();
}

class _QuizScreenState extends State<QuizScreen> with TickerProviderStateMixin {
  late AnimationController _starController;
  late AnimationController _progressController;
  late List<QuizQuestion> _questions;
  
  int _current = 0;
  int _score = 0;
  int? _selected;
  bool _answered = false;
  bool _finished = false;

  @override
  void initState() {
    super.initState();
    _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();
    _progressController = AnimationController(vsync: this, duration: const Duration(milliseconds: 400));
    _questions = List.from(allQuestions)..shuffle(Random());
    _questions = _questions.take(10).toList();
  }

  @override
  void dispose() { _starController.dispose(); _progressController.dispose(); super.dispose(); }

  void _answer(int index) {
    if (_answered) return;
    setState(() {
      _selected = index;
      _answered = true;
      if (index == _questions[_current].correctIndex) _score++;
    });
  }

  void _next() {
    if (_current < _questions.length - 1) {
      setState(() {
        _current++;
        _selected = null;
        _answered = false;
      });
    } else {
      setState(() => _finished = true);
    }
  }

  void _restart() {
    setState(() {
      _questions = List.from(allQuestions)..shuffle(Random());
      _questions = _questions.take(10).toList();
      _current = 0;
      _score = 0;
      _selected = null;
      _answered = false;
      _finished = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF010914),
      body: Stack(
        children: [
          AnimatedBuilder(animation: _starController, builder: (_, __) => CustomPaint(painter: _SP(_starController.value), child: const SizedBox.expand())),
          SafeArea(
            child: _finished ? _buildResult() : _buildQuiz(),
          ),
        ],
      ),
    );
  }

  Widget _buildQuiz() {
    final q = _questions[_current];
    final progress = (_current + 1) / _questions.length;

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        // Header
        Padding(padding: const EdgeInsets.fromLTRB(20,16,20,12), child: Row(children: [
          GestureDetector(onTap: () => Navigator.pop(context), child: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white54, size: 20)),
          const SizedBox(width: 16),
          Text("COSMIC QUIZ", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 4, shadows: [Shadow(color: Color(0xFF00AAFF), blurRadius: 15)])),
          const Spacer(),
          Text("${_current + 1}/${_questions.length}", style: GoogleFonts.orbitron(fontSize: 13, color: Color(0xFF00AAFF))),
        ])),

        // Progress bar
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 20),
          child: ClipRRect(
            borderRadius: BorderRadius.circular(4),
            child: LinearProgressIndicator(
              value: progress,
              backgroundColor: Colors.white12,
              valueColor: AlwaysStoppedAnimation(Color(0xFF00AAFF)),
              minHeight: 4,
            ),
          ),
        ),
        const SizedBox(height: 8),

        // Score
        Padding(
          padding: const EdgeInsets.symmetric(horizontal: 20),
          child: Row(children: [
            Text("Score: ", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white38)),
            Text("$_score", style: GoogleFonts.orbitron(fontSize: 13, color: Color(0xFF00FFCC))),
          ]),
        ),

        // Question
        Expanded(
          child: SingleChildScrollView(
            padding: const EdgeInsets.all(20),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                const SizedBox(height: 12),
                Center(child: Text(q.emoji, style: const TextStyle(fontSize: 64))),
                const SizedBox(height: 20),
                Text(q.question, style: GoogleFonts.orbitron(fontSize: 16, fontWeight: FontWeight.w700, color: Colors.white, height: 1.4)),
                const SizedBox(height: 24),

                // Options
                ...List.generate(q.options.length, (i) {
                  Color borderColor = Colors.white12;
                  Color bgColor = const Color(0xFF040F1F);
                  Color textColor = Colors.white70;
                  Widget? trailing;

                  if (_answered) {
                    if (i == q.correctIndex) {
                      borderColor = Color(0xFF00FFCC);
                      bgColor = Color(0xFF00FFCC).withOpacity(0.08);
                      textColor = Color(0xFF00FFCC);
                      trailing = Icon(Icons.check_circle_rounded, color: Color(0xFF00FFCC), size: 20);
                    } else if (i == _selected && i != q.correctIndex) {
                      borderColor = Color(0xFFEF5350);
                      bgColor = Color(0xFFEF5350).withOpacity(0.08);
                      textColor = Color(0xFFEF5350);
                      trailing = Icon(Icons.cancel_rounded, color: Color(0xFFEF5350), size: 20);
                    }
                  } else if (_selected == i) {
                    borderColor = Color(0xFF00AAFF);
                    bgColor = Color(0xFF00AAFF).withOpacity(0.08);
                    textColor = Color(0xFF00AAFF);
                  }

                  return GestureDetector(
                    onTap: () => _answer(i),
                    child: AnimatedContainer(
                      duration: const Duration(milliseconds: 250),
                      margin: const EdgeInsets.only(bottom: 12),
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: bgColor, border: Border.all(color: borderColor, width: 1.5)),
                      child: Row(children: [
                        Container(width: 28, height: 28, decoration: BoxDecoration(shape: BoxShape.circle, border: Border.all(color: borderColor)),
                          child: Center(child: Text(["A","B","C","D"][i], style: GoogleFonts.orbitron(fontSize: 10, color: textColor, fontWeight: FontWeight.w700)))),
                        const SizedBox(width: 12),
                        Expanded(child: Text(q.options[i], style: GoogleFonts.rajdhani(fontSize: 15, color: textColor, fontWeight: FontWeight.w600))),
                        if (trailing != null) trailing,
                      ]),
                    ),
                  );
                }),

                // Explanation
                if (_answered) ...[
                  const SizedBox(height: 8),
                  Container(
                    padding: const EdgeInsets.all(14),
                    decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: Colors.tealAccent.withOpacity(0.06), border: Border.all(color: Colors.tealAccent.withOpacity(0.3))),
                    child: Row(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      const Text("💡", style: TextStyle(fontSize: 16)),
                      const SizedBox(width: 8),
                      Expanded(child: Text(q.explanation, style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white70, height: 1.5))),
                    ]),
                  ),
                  const SizedBox(height: 16),
                  SizedBox(
                    width: double.infinity,
                    child: GestureDetector(
                      onTap: _next,
                      child: Container(
                        padding: const EdgeInsets.symmetric(vertical: 16),
                        decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: Color(0xFF00AAFF).withOpacity(0.15), border: Border.all(color: Color(0xFF00AAFF))),
                        child: Center(child: Text(
                          _current < _questions.length - 1 ? "NEXT QUESTION →" : "SEE RESULTS",
                          style: GoogleFonts.orbitron(fontSize: 13, color: Color(0xFF00AAFF), fontWeight: FontWeight.w700, letterSpacing: 1),
                        )),
                      ),
                    ),
                  ),
                ],
              ],
            ),
          ),
        ),
      ],
    );
  }

  Widget _buildResult() {
    final pct = (_score / _questions.length * 100).round();
    String grade, emoji, msg;
    Color gradeColor;

    if (pct >= 90) { grade = "COSMIC GENIUS"; emoji = "🏆"; msg = "Outstanding! You know the universe inside out."; gradeColor = Color(0xFFFFD700); }
    else if (pct >= 70) { grade = "STAR EXPLORER"; emoji = "⭐"; msg = "Great job! You really know your cosmic facts."; gradeColor = Color(0xFF00FFCC); }
    else if (pct >= 50) { grade = "SPACE CADET"; emoji = "🚀"; msg = "Good effort! Keep exploring the cosmos."; gradeColor = Color(0xFF00AAFF); }
    else { grade = "EARTHLING"; emoji = "🌍"; msg = "Keep learning! The universe has much to teach."; gradeColor = Color(0xFFCE93D8); }

    return Center(
      child: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(mainAxisAlignment: MainAxisAlignment.center, children: [
          Text(emoji, style: const TextStyle(fontSize: 80)),
          const SizedBox(height: 16),
          Text(grade, style: GoogleFonts.orbitron(fontSize: 22, fontWeight: FontWeight.w900, color: gradeColor, letterSpacing: 2, shadows: [Shadow(color: gradeColor, blurRadius: 20)])),
          const SizedBox(height: 12),
          Text(msg, style: GoogleFonts.rajdhani(fontSize: 16, color: Colors.white70, height: 1.5), textAlign: TextAlign.center),
          const SizedBox(height: 32),
          Container(
            padding: const EdgeInsets.all(24),
            decoration: BoxDecoration(borderRadius: BorderRadius.circular(20), color: const Color(0xFF040F1F), border: Border.all(color: gradeColor.withOpacity(0.3))),
            child: Column(children: [
              Text("$_score / ${_questions.length}", style: GoogleFonts.orbitron(fontSize: 48, fontWeight: FontWeight.w900, color: gradeColor)),
              Text("$pct% correct", style: GoogleFonts.rajdhani(fontSize: 18, color: Colors.white54)),
            ]),
          ),
          const SizedBox(height: 32),
          GestureDetector(
            onTap: _restart,
            child: Container(
              width: double.infinity,
              padding: const EdgeInsets.symmetric(vertical: 16),
              decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: Color(0xFF00AAFF).withOpacity(0.15), border: Border.all(color: Color(0xFF00AAFF))),
              child: Center(child: Text("PLAY AGAIN 🔄", style: GoogleFonts.orbitron(fontSize: 14, color: Color(0xFF00AAFF), fontWeight: FontWeight.w700, letterSpacing: 1))),
            ),
          ),
          const SizedBox(height: 12),
          GestureDetector(
            onTap: () => Navigator.pop(context),
            child: Container(
              width: double.infinity,
              padding: const EdgeInsets.symmetric(vertical: 16),
              decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: Colors.white.withOpacity(0.05), border: Border.all(color: Colors.white12)),
              child: Center(child: Text("BACK TO HOME", style: GoogleFonts.orbitron(fontSize: 14, color: Colors.white38, letterSpacing: 1))),
            ),
          ),
        ]),
      ),
    );
  }
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
      final t = 0.3+0.7*(0.5+0.5*sin(progress*2*pi*2+i));
      paint.color = Colors.white.withOpacity(t*0.7);
      canvas.drawCircle(Offset(_stars[i].dx*size.width,_stars[i].dy*size.height),_szs[i],paint);
    }
  }
  @override bool shouldRepaint(_) => true;
}
