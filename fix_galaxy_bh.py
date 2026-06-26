# Update galaxy_screen.dart with real images
galaxy = open("lib/screens/galaxy_screen.dart").read()

# Update galaxy items with real image paths
galaxy = galaxy.replace(
    '_GItem("Milky Way","🌌",Color(0xFF7986CB),"Barred Spiral"',
    '_GItem("Milky Way","🌌",Color(0xFF7986CB),"Barred Spiral","assets/images/milky_way.jpg"'
)
galaxy = galaxy.replace(
    '_GItem("Andromeda","🌀",Color(0xFF4FC3F7),"Spiral"',
    '_GItem("Andromeda","🌀",Color(0xFF4FC3F7),"Spiral","assets/images/andromeda.jpg"'
)
galaxy = galaxy.replace(
    '_GItem("Whirlpool","🌊",Color(0xFF80DEEA),"Spiral"',
    '_GItem("Whirlpool","🌊",Color(0xFF80DEEA),"Spiral","assets/images/whirlpool.jpg"'
)
galaxy = galaxy.replace(
    '_GItem("Sombrero","🎩",Color(0xFFFFE082),"Lenticular"',
    '_GItem("Sombrero","🎩",Color(0xFFFFE082),"Lenticular","assets/images/sombrero.jpg"'
)
galaxy = galaxy.replace(
    '_GItem("Triangulum","🔺",Color(0xFFEF9A9A),"Spiral"',
    '_GItem("Triangulum","🔺",Color(0xFFEF9A9A),"Spiral","assets/images/triangulum.jpg"'
)
galaxy = galaxy.replace(
    '_GItem("Centaurus A","💫",Color(0xFFCE93D8),"Elliptical"',
    '_GItem("Centaurus A","💫",Color(0xFFCE93D8),"Elliptical","assets/images/centaurus.jpg"'
)

# Update _GItem class to include imagePath
galaxy = galaxy.replace(
    "class _GItem {\n  final String name,emoji,type,desc,diameter,stars,age,fishy; final Color color;\n  const _GItem(this.name,this.emoji,this.color,this.type,this.desc,this.diameter,this.stars,this.age,this.fishy);",
    "class _GItem {\n  final String name,emoji,type,desc,diameter,stars,age,fishy,imagePath; final Color color;\n  const _GItem(this.name,this.emoji,this.color,this.type,this.desc,this.diameter,this.stars,this.age,this.fishy,this.imagePath);"
)

# Update galaxy card to show image on left
old_card = '''                    child: Container(
                      margin: const EdgeInsets.only(bottom: 12),
                      padding: const EdgeInsets.all(16),
                      decoration: BoxDecoration(borderRadius: BorderRadius.circular(18), color: const Color(0xFF040F1F), border: Border.all(color: items[i].color.withOpacity(0.25))),
                      child: Row(children: [
                        Container(width: 56, height: 56, decoration: BoxDecoration(shape: BoxShape.circle, color: items[i].color.withOpacity(0.15), border: Border.all(color: items[i].color.withOpacity(0.4))),
                          child: Center(child: Text(items[i].emoji, style: const TextStyle(fontSize: 28)))),
                        const SizedBox(width: 14),
                        Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                          Row(children: [Text(items[i].name, style: GoogleFonts.orbitron(fontSize: 14, fontWeight: FontWeight.w700, color: Colors.white)), const Spacer(), Icon(Icons.arrow_forward_ios_rounded, color: items[i].color, size: 13)]),
                          const SizedBox(height: 3),
                          Row(children: [
                            Container(padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2), decoration: BoxDecoration(borderRadius: BorderRadius.circular(6), color: items[i].color.withOpacity(0.12)), child: Text(items[i].type, style: GoogleFonts.orbitron(fontSize: 7, color: items[i].color))),
                            const SizedBox(width: 8),
                            Text(items[i].stars, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
                          ]),
                          const SizedBox(height: 4),
                          Text(items[i].desc, maxLines: 2, overflow: TextOverflow.ellipsis, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38, height: 1.3)),
                        ])),
                      ]),
                    ),'''

new_card = '''                    child: Container(
                      margin: const EdgeInsets.only(bottom: 12),
                      height: 110,
                      decoration: BoxDecoration(
                        borderRadius: BorderRadius.circular(18),
                        color: const Color(0xFF040F1F),
                        border: Border.all(color: items[i].color.withOpacity(0.25)),
                        boxShadow: [BoxShadow(color: items[i].color.withOpacity(0.08), blurRadius: 16)],
                      ),
                      child: Row(children: [
                        ClipRRect(
                          borderRadius: const BorderRadius.only(topLeft: Radius.circular(18), bottomLeft: Radius.circular(18)),
                          child: SizedBox(width: 110, height: 110, child: Stack(fit: StackFit.expand, children: [
                            Image.asset(items[i].imagePath, fit: BoxFit.cover,
                              errorBuilder: (_, __, ___) => Container(color: items[i].color.withOpacity(0.3),
                                child: Center(child: Text(items[i].emoji, style: const TextStyle(fontSize: 36))))),
                            Positioned(right: 0, child: Container(width: 20, height: 110,
                              decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.transparent, const Color(0xFF040F1F)])))),
                          ])),
                        ),
                        Expanded(child: Padding(
                          padding: const EdgeInsets.all(12),
                          child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.center, children: [
                            Row(children: [
                              Expanded(child: Text(items[i].name, style: GoogleFonts.orbitron(fontSize: 13, fontWeight: FontWeight.w700, color: Colors.white))),
                              Icon(Icons.arrow_forward_ios_rounded, color: items[i].color, size: 13),
                            ]),
                            const SizedBox(height: 4),
                            Container(padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                              decoration: BoxDecoration(borderRadius: BorderRadius.circular(6), color: items[i].color.withOpacity(0.12)),
                              child: Text(items[i].type, style: GoogleFonts.orbitron(fontSize: 7, color: items[i].color))),
                            const SizedBox(height: 4),
                            Text(items[i].desc, maxLines: 2, overflow: TextOverflow.ellipsis,
                              style: GoogleFonts.rajdhani(fontSize: 11, color: Colors.white38, height: 1.3)),
                          ]),
                        )),
                      ]),
                    ),'''

galaxy = galaxy.replace(old_card, new_card)

# Update sheet to show image
old_sheet_emoji = "        Center(child: Text(g.emoji, style: const TextStyle(fontSize: 72))),"
new_sheet_emoji = """        ClipRRect(
          borderRadius: BorderRadius.circular(16),
          child: SizedBox(height: 160, width: double.infinity, child: Stack(fit: StackFit.expand, children: [
            Image.asset(g.imagePath, fit: BoxFit.cover,
              errorBuilder: (_, __, ___) => Center(child: Text(g.emoji, style: const TextStyle(fontSize: 72)))),
            Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF040F1F)]))),
          ])),
        ),"""
galaxy = galaxy.replace(old_sheet_emoji, new_sheet_emoji)

open("lib/screens/galaxy_screen.dart", "w").write(galaxy)
print("Galaxy screen updated!")

# Now update blackhole_screen.dart with real images
bh = open("lib/screens/blackhole_screen.dart").read()

# Update BH items with image paths
bh = bh.replace(
    '_BHItem("Sagittarius A*","🕳️",Color(0xFF90A4AE),"Milky Way Core"',
    '_BHItem("Sagittarius A*","🕳️",Color(0xFF90A4AE),"Milky Way Core","assets/images/sagittarius_a.jpg"'
)
bh = bh.replace(
    '_BHItem("M87*","⚫",Color(0xFFFFAB91),"Virgo Cluster"',
    '_BHItem("M87*","⚫",Color(0xFFFFAB91),"Virgo Cluster","assets/images/m87.jpg"'
)
bh = bh.replace(
    '_BHItem("Stellar Black Hole","💥",Color(0xFFEF9A9A),"Throughout Galaxies"',
    '_BHItem("Stellar Black Hole","💥",Color(0xFFEF9A9A),"Throughout Galaxies","assets/images/stellar_bh.jpg"'
)
bh = bh.replace(
    '_BHItem("Intermediate BH","🌑",Color(0xFF80DEEA),"Star Clusters"',
    '_BHItem("Intermediate BH","🌑",Color(0xFF80DEEA),"Star Clusters","assets/images/intermediate_bh.jpg"'
)
bh = bh.replace(
    '_BHItem("Quasar","✨",Color(0xFFFFE082),"Early Universe"',
    '_BHItem("Quasar","✨",Color(0xFFFFE082),"Early Universe","assets/images/Quasar.jpg"'
)
bh = bh.replace(
    '_BHItem("Primordial BH","🌀",Color(0xFFCE93D8),"Theoretical"',
    '_BHItem("Primordial BH","🌀",Color(0xFFCE93D8),"Theoretical","assets/images/primordial_bh.jpg"'
)

# Update _BHItem class
bh = bh.replace(
    "class _BHItem {\n  final String name,emoji,location,desc,mass,distance,fishy; final Color color;\n  const _BHItem(this.name,this.emoji,this.color,this.location,this.desc,this.mass,this.distance,this.fishy);",
    "class _BHItem {\n  final String name,emoji,location,desc,mass,distance,fishy,imagePath; final Color color;\n  const _BHItem(this.name,this.emoji,this.color,this.location,this.desc,this.mass,this.distance,this.fishy,this.imagePath);"
)

# Update BH card to show image
old_bh_card = '''                    child: Container(
                    margin: const EdgeInsets.only(bottom: 12),
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(borderRadius: BorderRadius.circular(18), color: const Color(0xFF040F1F), border: Border.all(color: b.color.withOpacity(0.25))),
                    child: Row(children: [
                      Container(width: 56, height: 56, decoration: BoxDecoration(shape: BoxShape.circle, color: b.color.withOpacity(0.1), border: Border.all(color: b.color.withOpacity(0.3))),
                        child: Center(child: Text(b.emoji, style: const TextStyle(fontSize: 28)))),
                      const SizedBox(width: 14),
                      Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                        Row(children: [Expanded(child: Text(b.name, style: GoogleFonts.orbitron(fontSize: 13, fontWeight: FontWeight.w700, color: Colors.white))), Icon(Icons.arrow_forward_ios_rounded, color: b.color, size: 13)]),
                        const SizedBox(height: 3),
                        Text(b.location, style: GoogleFonts.rajdhani(fontSize: 12, color: b.color)),
                        Text("Mass: ${b.mass}", style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38)),
                      ])),
                    ]),
                  ),'''

new_bh_card = '''                    child: Container(
                    margin: const EdgeInsets.only(bottom: 12),
                    height: 110,
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(18),
                      color: const Color(0xFF040F1F),
                      border: Border.all(color: b.color.withOpacity(0.25)),
                      boxShadow: [BoxShadow(color: b.color.withOpacity(0.08), blurRadius: 16)],
                    ),
                    child: Row(children: [
                      ClipRRect(
                        borderRadius: const BorderRadius.only(topLeft: Radius.circular(18), bottomLeft: Radius.circular(18)),
                        child: SizedBox(width: 110, height: 110, child: Stack(fit: StackFit.expand, children: [
                          Image.asset(b.imagePath, fit: BoxFit.cover,
                            errorBuilder: (_, __, ___) => Container(color: b.color.withOpacity(0.2),
                              child: Center(child: Text(b.emoji, style: const TextStyle(fontSize: 36))))),
                          Positioned(right: 0, child: Container(width: 20, height: 110,
                            decoration: BoxDecoration(gradient: LinearGradient(colors: [Colors.transparent, const Color(0xFF040F1F)])))),
                        ])),
                      ),
                      Expanded(child: Padding(
                        padding: const EdgeInsets.all(12),
                        child: Column(crossAxisAlignment: CrossAxisAlignment.start, mainAxisAlignment: MainAxisAlignment.center, children: [
                          Row(children: [
                            Expanded(child: Text(b.name, style: GoogleFonts.orbitron(fontSize: 13, fontWeight: FontWeight.w700, color: Colors.white))),
                            Icon(Icons.arrow_forward_ios_rounded, color: b.color, size: 13),
                          ]),
                          const SizedBox(height: 4),
                          Text(b.location, style: GoogleFonts.rajdhani(fontSize: 12, color: b.color)),
                          const SizedBox(height: 2),
                          Text("Mass: ${b.mass}", style: GoogleFonts.rajdhani(fontSize: 11, color: Colors.white38)),
                        ]),
                      )),
                    ]),
                  ),'''

bh = bh.replace(old_bh_card, new_bh_card)

# Update BH sheet to show image
old_bh_sheet = "        Center(child: Text(b.emoji, style: const TextStyle(fontSize: 72))),"
new_bh_sheet = """        ClipRRect(
          borderRadius: BorderRadius.circular(16),
          child: SizedBox(height: 160, width: double.infinity, child: Stack(fit: StackFit.expand, children: [
            Image.asset(b.imagePath, fit: BoxFit.cover,
              errorBuilder: (_, __, ___) => Center(child: Text(b.emoji, style: const TextStyle(fontSize: 72)))),
            Container(decoration: BoxDecoration(gradient: LinearGradient(begin: Alignment.topCenter, end: Alignment.bottomCenter, colors: [Colors.transparent, const Color(0xFF040F1F)]))),
          ])),
        ),"""
bh = bh.replace(old_bh_sheet, new_bh_sheet)

open("lib/screens/blackhole_screen.dart", "w").write(bh)
print("Black hole screen updated!")
print("Both done! Run flutter run")
