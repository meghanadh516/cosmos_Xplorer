content = open("lib/screens/multiverse_screen.dart").read()

# Add imagePath to each theory
content = content.replace(
    '_MVItem(name:"Bubble Multiverse", emoji:"🫧", color:Color(0xFF90CAF9), theory:"Eternal Inflation",',
    '_MVItem(name:"Bubble Multiverse", emoji:"🫧", color:Color(0xFF90CAF9), theory:"Eternal Inflation", imagePath:"assets/images/Bubble_multiverse.jpg",'
)
content = content.replace(
    '_MVItem(name:"Many-Worlds", emoji:"🌿", color:Color(0xFF80DEEA), theory:"Quantum Mechanics",',
    '_MVItem(name:"Many-Worlds", emoji:"🌿", color:Color(0xFF80DEEA), theory:"Quantum Mechanics", imagePath:"assets/images/many_worlds.jpg",'
)
content = content.replace(
    '_MVItem(name:"Mathematical Universe", emoji:"🔢", color:Color(0xFFFFE082), theory:"Max Tegmark",',
    '_MVItem(name:"Mathematical Universe", emoji:"🔢", color:Color(0xFFFFE082), theory:"Max Tegmark", imagePath:"assets/images/mathematical_universe.jpg",'
)
content = content.replace(
    '_MVItem(name:"String Landscape", emoji:"🎸", color:Color(0xFFCE93D8), theory:"String Theory",',
    '_MVItem(name:"String Landscape", emoji:"🎸", color:Color(0xFFCE93D8), theory:"String Theory", imagePath:"assets/images/string_theory_landscape.jpg",'
)
content = content.replace(
    '_MVItem(name:"Simulation Theory", emoji:"💻", color:Color(0xFF4FC3F7), theory:"Simulation Hypothesis",',
    '_MVItem(name:"Simulation Theory", emoji:"💻", color:Color(0xFF4FC3F7), theory:"Simulation Hypothesis", imagePath:"assets/images/simulated_universe.jpg",'
)
content = content.replace(
    '_MVItem(name:"Cyclic Universe", emoji:"🔄", color:Color(0xFFFFAB91), theory:"Roger Penrose",',
    '_MVItem(name:"Cyclic Universe", emoji:"🔄", color:Color(0xFFFFAB91), theory:"Roger Penrose", imagePath:"assets/images/cyclic_universe.jpg",'
)

# Add imagePath to _MVItem class
content = content.replace(
    "class _MVItem {\n  final String name, emoji, theory, desc, evidence, fishy;\n  final Color color;\n  const _MVItem({required this.name, required this.emoji, required this.color, required this.theory, required this.desc, required this.evidence, required this.fishy});",
    "class _MVItem {\n  final String name, emoji, theory, desc, evidence, fishy, imagePath;\n  final Color color;\n  const _MVItem({required this.name, required this.emoji, required this.color, required this.theory, required this.desc, required this.evidence, required this.fishy, required this.imagePath});"
)

# Update theory card to show image on left
old_card = '''                      child: Container(
                      margin: const EdgeInsets.only(bottom: 12),
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(18),
                        color: const Color(0xFF040F1F),
                        border: Border.all(color: theories[i].color.withOpacity(0.3)),
                        boxShadow: [BoxShadow(color: theories[i].color.withOpacity(0.07), blurRadius: 16)],
                      ),
                      child: Row(children: [
                        Container(
                          width: 60, height: 60,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: theories[i].color.withOpacity(0.12),
                            border: Border.all(color: theories[i].color.withOpacity(0.4), width: 1.5),
                          ),
                          child: Center(child: Text(theories[i].emoji, style: const TextStyle(fontSize: 28))),
                        ),
                        const SizedBox(width: 14),
                        Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                          Row(children: [
                            Expanded(child: Text(theories[i].name, style: GoogleFonts.orbitron(fontSize: 13, fontWeight: FontWeight.w700, color: Colors.white))),
                            Icon(Icons.arrow_forward_ios_rounded, color: theories[i].color, size: 13),
                          ]),
                          const SizedBox(height: 3),
                          Container(padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                            decoration: BoxDecoration(borderRadius: BorderRadius.circular(6), color: theories[i].color.withOpacity(0.12)),
                            child: Text(theories[i].theory, style: GoogleFonts.orbitron(fontSize: 7, color: theories[i].color))),
                          const SizedBox(height: 5),
                          Text(theories[i].desc, maxLines: 2, overflow: TextOverflow.ellipsis,
                            style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38, height: 1.3)),
                        ])),
                      ]),
                    ),'''

new_card = '''                      child: Container(
                      margin: const EdgeInsets.only(bottom: 12),
                      height: 110,
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(18),
                        color: const Color(0xFF040F1F),
                        border: Border.all(color: theories[i].color.withOpacity(0.3)),
                        boxShadow: [BoxShadow(color: theories[i].color.withOpacity(0.08), blurRadius: 16)],
                      ),
                      child: Row(children: [
                        ClipRRect(
                          borderRadius: const BorderRadius.only(topLeft: Radius.circular(18), bottomLeft: Radius.circular(18)),
                          child: SizedBox(width: 110, height: 110, child: Stack(fit: StackFit.expand, children: [
                            Image.asset(theories[i].imagePath, fit: BoxFit.cover,
                              errorBuilder: (_, __, ___) => Container(color: theories[i].color.withOpacity(0.2),
                                child: Center(child: Text(theories[i].emoji, style: const TextStyle(fontSize: 36))))),
                            Positioned(right: 0, child: Container(width: 20, height: 110,
                              decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.transparent, const Color(0xFF040F1F)])))),
                          ])),
                        ),
                        Expanded(child: Padding(
                          padding: const EdgeInsets.all(12),
                          child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.center, children: [
                            Row(children: [
                              Expanded(child: Text(theories[i].name, style: GoogleFonts.orbitron(fontSize: 12, fontWeight: FontWeight.w700, color: Colors.white))),
                              Icon(Icons.arrow_forward_ios_rounded, color: theories[i].color, size: 13),
                            ]),
                            const SizedBox(height: 4),
                            Container(padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                              decoration: BoxDecoration(borderRadius: BorderRadius.circular(6), color: theories[i].color.withOpacity(0.12)),
                              child: Text(theories[i].theory, style: GoogleFonts.orbitron(fontSize: 7, color: theories[i].color))),
                            const SizedBox(height: 4),
                            Text(theories[i].desc, maxLines: 2, overflow: TextOverflow.ellipsis,
                              style: GoogleFonts.rajdhani(fontSize: 11, color: Colors.white38, height: 1.3)),
                          ]),
                        )),
                      ]),
                    ),'''

content = content.replace(old_card, new_card)

# Update sheet to show image at top
old_sheet = '''        Center(child: Container(
          width: 90, height: 90,
          decoration: BoxDecoration(shape: BoxShape.circle, color: t.color.withOpacity(0.12), border: Border.all(color: t.color.withOpacity(0.4), width: 2)),
          child: Center(child: Text(t.emoji, style: const TextStyle(fontSize: 44))),
        )),
        const SizedBox(height: 16),
        Center(child: Text(t.name,'''

new_sheet = '''        ClipRRect(
          borderRadius: BorderRadius.circular(16),
          child: SizedBox(height: 160, width: double.infinity, child: Stack(fit: StackFit.expand, children: [
            Image.asset(t.imagePath, fit: BoxFit.cover,
              errorBuilder: (_, __, ___) => Container(color: t.color.withOpacity(0.2),
                child: Center(child: Text(t.emoji, style: const TextStyle(fontSize: 72))))),
            Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF040F1F)]))),
          ])),
        ),
        const SizedBox(height: 16),
        Center(child: Text(t.name,'''

content = content.replace(old_sheet, new_sheet)

open("lib/screens/multiverse_screen.dart", "w").write(content)
print("Done!" if "imagePath" in content else "Error")
