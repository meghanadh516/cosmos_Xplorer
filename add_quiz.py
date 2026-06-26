content = open("lib/screens/home_screen.dart").read()

# Add import
content = content.replace(
    "import 'search_screen.dart';",
    "import 'search_screen.dart';\nimport 'quiz_screen.dart';"
)

# Add quiz card before last SizedBox
old = "                      const SizedBox(height: 16),\n                    ],\n                  ),\n                ),"
new = """                      FadeInLeft(
                        delay: Duration(milliseconds: 900),
                        child: GestureDetector(
                          onTap: () => Navigator.push(context, _route(QuizScreen())),
                          child: Container(
                            margin: const EdgeInsets.only(bottom: 12),
                            padding: const EdgeInsets.all(20),
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(16),
                              color: const Color(0xFF040F1F),
                              border: Border.all(color: Color(0xFFFFD700).withOpacity(0.4)),
                              boxShadow: [BoxShadow(color: Color(0xFFFFD700).withOpacity(0.1), blurRadius: 20)],
                            ),
                            child: Row(children: [
                              Text("🧠", style: TextStyle(fontSize: 36)),
                              const SizedBox(width: 16),
                              Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                Text("Cosmic Quiz", style: GoogleFonts.orbitron(fontSize: 16, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 1.5)),
                                const SizedBox(height: 3),
                                Text("Test your space knowledge", style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
                              ])),
                              Icon(Icons.arrow_forward_ios_rounded, color: Color(0xFFFFD700), size: 15),
                            ]),
                          ),
                        ),
                      ),
                      const SizedBox(height: 16),
                    ],
                  ),
                ),"""

result = content.replace(old, new)
open("lib/screens/home_screen.dart", "w").write(result)
print("Done!" if "QuizScreen" in result else "Pattern not matched")
