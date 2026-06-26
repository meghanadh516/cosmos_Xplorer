content = open("lib/screens/home_screen.dart").read()

# Add import
content = content.replace(
    "import 'quiz_screen.dart';",
    "import 'quiz_screen.dart';\nimport 'settings_screen.dart';"
)

# Add settings icon in header area - after XPLORER text
content = content.replace(
    'FadeInDown(delay: Duration(milliseconds: 150), child: Center(child: Text("X P L O R E R", style: GoogleFonts.orbitron(fontSize: 12, color: Color(0xFF00AAFF), letterSpacing: 12)))),',
    '''FadeInDown(delay: Duration(milliseconds: 150), child: Center(child: Text("X P L O R E R", style: GoogleFonts.orbitron(fontSize: 12, color: Color(0xFF00AAFF), letterSpacing: 12)))),
                // Settings icon top right
                Align(
                  alignment: Alignment.centerRight,
                  child: Padding(
                    padding: const EdgeInsets.only(right: 16, top: 4),
                    child: GestureDetector(
                      onTap: () => Navigator.push(context, _route(SettingsScreen())),
                      child: Icon(Icons.settings_outlined, color: Colors.white38, size: 22),
                    ),
                  ),
                ),'''
)

open("lib/screens/home_screen.dart", "w").write(content)
print("Done!" if "SettingsScreen" in content else "Pattern not matched")
