content = r"""import 'dart:math';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class SearchItem {
  final String title, subtitle, category, emoji, fact;
  final Color color;
  const SearchItem({required this.title, required this.subtitle, required this.category, required this.emoji, required this.fact, required this.color});
}

final List<SearchItem> allItems = [
  // Planets
  SearchItem(title:"Mercury", subtitle:"Smallest planet, closest to Sun", category:"Planet", emoji:"⚫", fact:"A year on Mercury is just 88 Earth days!", color:Color(0xFF90A4AE)),
  SearchItem(title:"Venus", subtitle:"Hottest planet in the solar system", category:"Planet", emoji:"🟡", fact:"Venus spins backwards — Sun rises in the west.", color:Color(0xFFFFCC80)),
  SearchItem(title:"Earth", subtitle:"Our home, only known planet with life", category:"Planet", emoji:"🔵", fact:"Earth is the densest planet in the Solar System.", color:Color(0xFF4FC3F7)),
  SearchItem(title:"Mars", subtitle:"The Red Planet with blue sunsets", category:"Planet", emoji:"🔴", fact:"Olympus Mons is 3x taller than Mount Everest.", color:Color(0xFFEF9A9A)),
  SearchItem(title:"Jupiter", subtitle:"Largest planet, 95 known moons", category:"Planet", emoji:"🟠", fact:"Jupiter's storm has raged for 400+ years.", color:Color(0xFFFFAB91)),
  SearchItem(title:"Saturn", subtitle:"Ringed giant, floats on water", category:"Planet", emoji:"🪐", fact:"Saturn's rings are only ~10 meters thick.", color:Color(0xFFFFE082)),
  SearchItem(title:"Uranus", subtitle:"Ice giant, rotates on its side", category:"Planet", emoji:"🔵", fact:"Uranus smells like rotten eggs.", color:Color(0xFF80DEEA)),
  SearchItem(title:"Neptune", subtitle:"Windiest planet, diamond rain", category:"Planet", emoji:"💙", fact:"It rains diamonds on Neptune.", color:Color(0xFF90CAF9)),
  // Galaxies
  SearchItem(title:"Milky Way", subtitle:"Our home galaxy, 200-400 billion stars", category:"Galaxy", emoji:"🌌", fact:"The Milky Way completes one rotation every 225 million years.", color:Color(0xFF7986CB)),
  SearchItem(title:"Andromeda", subtitle:"Nearest large galaxy, heading toward us", category:"Galaxy", emoji:"🌀", fact:"Andromeda will collide with Milky Way in 4.5 billion years.", color:Color(0xFF4FC3F7)),
  SearchItem(title:"Whirlpool", subtitle:"Classic spiral with companion galaxy", category:"Galaxy", emoji:"🌊", fact:"First galaxy discovered to have spiral structure.", color:Color(0xFF80DEEA)),
  SearchItem(title:"Sombrero", subtitle:"Famous for its dark dust lane", category:"Galaxy", emoji:"🎩", fact:"Has a black hole 1 billion times mass of our Sun.", color:Color(0xFFFFE082)),
  SearchItem(title:"Triangulum", subtitle:"Third largest in Local Group", category:"Galaxy", emoji:"🔺", fact:"Has no supermassive black hole — a mystery!", color:Color(0xFFEF9A9A)),
  SearchItem(title:"Centaurus A", subtitle:"Closest radio galaxy to Earth", category:"Galaxy", emoji:"💫", fact:"Shoots jets of particles 13,000 light years long.", color:Color(0xFFCE93D8)),
  // Black Holes
  SearchItem(title:"Sagittarius A*", subtitle:"Black hole at Milky Way center", category:"Black Hole", emoji:"🕳️", fact:"First imaged in 2022 using 5 petabytes of data.", color:Color(0xFF90A4AE)),
  SearchItem(title:"M87*", subtitle:"First ever photographed black hole", category:"Black Hole", emoji:"⚫", fact:"6.5 billion solar masses — Solar System fits inside.", color:Color(0xFFFFAB91)),
  SearchItem(title:"Quasar", subtitle:"Brightest objects in the universe", category:"Black Hole", emoji:"✨", fact:"Shines 600 trillion times brighter than our Sun.", color:Color(0xFFFFE082)),
  // Universe
  SearchItem(title:"Big Bang", subtitle:"Origin of the universe 13.8B years ago", category:"Universe", emoji:"💥", fact:"The universe was smaller than an atom at t=0.", color:Color(0xFFEF9A9A)),
  SearchItem(title:"Dark Matter", subtitle:"27% of the universe, invisible", category:"Universe", emoji:"🌑", fact:"We know it exists only from its gravitational effects.", color:Color(0xFF90A4AE)),
  SearchItem(title:"Dark Energy", subtitle:"68% of the universe, causing expansion", category:"Universe", emoji:"⚡", fact:"Dark energy is accelerating the universe's expansion.", color:Color(0xFF90CAF9)),
  SearchItem(title:"Observable Universe", subtitle:"93 billion light years across", category:"Universe", emoji:"🔭", fact:"Contains ~2 trillion galaxies.", color:Color(0xFF4FC3F7)),
  // Multiverse
  SearchItem(title:"Bubble Multiverse", subtitle:"Infinite bubble universes from inflation", category:"Multiverse", emoji:"🫧", fact:"Hawking's last paper was about this theory.", color:Color(0xFF90CAF9)),
  SearchItem(title:"Many-Worlds", subtitle:"Every quantum event creates a new universe", category:"Multiverse", emoji:"🌿", fact:"There may be a universe where you made every different choice.", color:Color(0xFF80DEEA)),
  SearchItem(title:"String Theory", subtitle:"10⁵⁰⁰ possible universes predicted", category:"Multiverse", emoji:"🎸", fact:"10⁵⁰⁰ universes — more than atoms in our universe.", color:Color(0xFFCE93D8)),
  SearchItem(title:"Simulation Theory", subtitle:"We may be living in a simulation", category:"Multiverse", emoji:"💻", fact:"Elon Musk thinks chance we're NOT simulated is 1 in a billion.", color:Color(0xFF4FC3F7)),
  // Solar System facts
  SearchItem(title:"Asteroid Belt", subtitle:"Millions of rocks between Mars and Jupiter", category:"Solar System", emoji:"☄️", fact:"Ceres is the largest object in the asteroid belt.", color:Color(0xFFFF8A65)),
  SearchItem(title:"Oort Cloud", subtitle:"Icy shell at edge of Solar System", category:"Solar System", emoji:"☁️", fact:"~2 light years across — edge of Sun's gravity.", color:Color(0xFFCE93D8)),
  SearchItem(title:"Kuiper Belt", subtitle:"Icy region beyond Neptune", category:"Solar System", emoji:"❄️", fact:"Pluto lives here — it's not lonely.", color:Color(0xFF80DEEA)),
  SearchItem(title:"The Sun", subtitle:"Star at center of Solar System", category:"Solar System", emoji:"☀️", fact:"99.8% of all Solar System mass is the Sun.", color:Color(0xFFFFB300)),
];

class SearchScreen extends StatefulWidget {
  const SearchScreen({super.key});
  @override
  State<SearchScreen> createState() => _SearchScreenState();
}

class _SearchScreenState extends State<SearchScreen> with SingleTickerProviderStateMixin {
  late AnimationController _starController;
  final TextEditingController _searchController = TextEditingController();
  List<SearchItem> _results = [];
  String _query = '';
  String _selectedCategory = 'All';

  final List<String> categories = ['All', 'Planet', 'Galaxy', 'Black Hole', 'Universe', 'Multiverse', 'Solar System'];

  @override
  void initState() {
    super.initState();
    _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();
    _results = allItems;
  }

  @override
  void dispose() { _starController.dispose(); _searchController.dispose(); super.dispose(); }

  void _search(String query) {
    setState(() {
      _query = query;
      _filter();
    });
  }

  void _filter() {
    _results = allItems.where((item) {
      final matchQuery = _query.isEmpty ||
          item.title.toLowerCase().contains(_query.toLowerCase()) ||
          item.subtitle.toLowerCase().contains(_query.toLowerCase()) ||
          item.fact.toLowerCase().contains(_query.toLowerCase());
      final matchCategory = _selectedCategory == 'All' || item.category == _selectedCategory;
      return matchQuery && matchCategory;
    }).toList();
  }

  void _selectCategory(String cat) {
    setState(() {
      _selectedCategory = cat;
      _filter();
    });
  }

  void _showDetail(BuildContext context, SearchItem item) {
    showModalBottomSheet(
      context: context,
      backgroundColor: Colors.transparent,
      isScrollControlled: true,
      builder: (_) => Container(
        margin: const EdgeInsets.all(16),
        padding: const EdgeInsets.all(24),
        decoration: BoxDecoration(
          borderRadius: BorderRadius.circular(24),
          color: const Color(0xFF040F1F),
          border: Border.all(color: item.color.withOpacity(0.4)),
          boxShadow: [BoxShadow(color: item.color.withOpacity(0.15), blurRadius: 40)],
        ),
        child: Column(mainAxisSize: MainAxisSize.min, crossAxisAlignment: CrossAxisAlignment.start, children: [
          Center(child: Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.white24, borderRadius: BorderRadius.circular(2)))),
          const SizedBox(height: 20),
          Row(children: [
            Text(item.emoji, style: const TextStyle(fontSize: 48)),
            const SizedBox(width: 16),
            Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
              Text(item.title, style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w800, color: Colors.white)),
              Container(margin: const EdgeInsets.only(top: 4), padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 3),
                decoration: BoxDecoration(borderRadius: BorderRadius.circular(8), color: item.color.withOpacity(0.15)),
                child: Text(item.category, style: GoogleFonts.orbitron(fontSize: 8, color: item.color, letterSpacing: 1))),
            ])),
          ]),
          const SizedBox(height: 16),
          Text(item.subtitle, style: GoogleFonts.rajdhani(fontSize: 16, color: Colors.white70, height: 1.5)),
          const SizedBox(height: 16),
          Container(padding: const EdgeInsets.all(14), decoration: BoxDecoration(borderRadius: BorderRadius.circular(12), color: item.color.withOpacity(0.08), border: Border.all(color: item.color.withOpacity(0.3))),
            child: Row(children: [
              const Text("💡", style: TextStyle(fontSize: 20)),
              const SizedBox(width: 10),
              Expanded(child: Text(item.fact, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white70, fontStyle: FontStyle.italic))),
            ])),
          const SizedBox(height: 8),
        ]),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF010914),
      body: Stack(
        children: [
          AnimatedBuilder(animation: _starController, builder: (_, __) => CustomPaint(painter: _SP(_starController.value), child: const SizedBox.expand())),
          SafeArea(
            child: Column(children: [
              // Header
              Padding(padding: const EdgeInsets.fromLTRB(20,16,20,12), child: Row(children: [
                GestureDetector(onTap: () => Navigator.pop(context), child: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white54, size: 20)),
                const SizedBox(width: 16),
                Text("SEARCH", style: GoogleFonts.orbitron(fontSize: 20, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 4)),
              ])),

              // Search bar
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 16),
                child: Container(
                  decoration: BoxDecoration(borderRadius: BorderRadius.circular(16), color: const Color(0xFF040F1F), border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.3))),
                  child: TextField(
                    controller: _searchController,
                    onChanged: _search,
                    autofocus: true,
                    style: GoogleFonts.rajdhani(fontSize: 16, color: Colors.white),
                    decoration: InputDecoration(
                      hintText: "Search planets, galaxies, black holes...",
                      hintStyle: GoogleFonts.rajdhani(color: Colors.white24, fontSize: 14),
                      prefixIcon: const Icon(Icons.search_rounded, color: Color(0xFF00AAFF)),
                      suffixIcon: _query.isNotEmpty ? GestureDetector(
                        onTap: () { _searchController.clear(); _search(''); },
                        child: const Icon(Icons.close_rounded, color: Colors.white38),
                      ) : null,
                      border: InputBorder.none,
                      contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 12),

              // Category chips
              SizedBox(
                height: 36,
                child: ListView.builder(
                  scrollDirection: Axis.horizontal,
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  itemCount: categories.length,
                  itemBuilder: (ctx, i) {
                    final cat = categories[i];
                    final selected = cat == _selectedCategory;
                    return GestureDetector(
                      onTap: () => _selectCategory(cat),
                      child: AnimatedContainer(
                        duration: const Duration(milliseconds: 200),
                        margin: const EdgeInsets.only(right: 8),
                        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 6),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(20),
                          color: selected ? Color(0xFF00AAFF).withOpacity(0.2) : const Color(0xFF040F1F),
                          border: Border.all(color: selected ? Color(0xFF00AAFF) : Colors.white12),
                        ),
                        child: Text(cat, style: GoogleFonts.orbitron(fontSize: 9, color: selected ? Color(0xFF00AAFF) : Colors.white38, letterSpacing: 0.5)),
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(height: 8),

              // Results count
              Padding(
                padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 4),
                child: Row(children: [
                  Text("${_results.length} results", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white38)),
                ]),
              ),

              // Results list
              Expanded(
                child: _results.isEmpty
                  ? Center(child: Column(mainAxisSize: MainAxisSize.min, children: [
                      const Text("🔭", style: TextStyle(fontSize: 48)),
                      const SizedBox(height: 12),
                      Text("No results found", style: GoogleFonts.orbitron(fontSize: 14, color: Colors.white38)),
                      const SizedBox(height: 6),
                      Text("Try a different search term", style: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white24)),
                    ]))
                  : ListView.builder(
                      padding: const EdgeInsets.symmetric(horizontal: 16),
                      itemCount: _results.length,
                      itemBuilder: (ctx, i) {
                        final item = _results[i];
                        return GestureDetector(
                          onTap: () => _showDetail(context, item),
                          child: Container(
                            margin: const EdgeInsets.only(bottom: 10),
                            padding: const EdgeInsets.all(14),
                            decoration: BoxDecoration(
                              borderRadius: BorderRadius.circular(16),
                              color: const Color(0xFF040F1F),
                              border: Border.all(color: item.color.withOpacity(0.2)),
                            ),
                            child: Row(children: [
                              Container(width: 46, height: 46, decoration: BoxDecoration(shape: BoxShape.circle, color: item.color.withOpacity(0.12), border: Border.all(color: item.color.withOpacity(0.3))),
                                child: Center(child: Text(item.emoji, style: const TextStyle(fontSize: 22)))),
                              const SizedBox(width: 12),
                              Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                                Row(children: [
                                  Text(item.title, style: GoogleFonts.orbitron(fontSize: 13, fontWeight: FontWeight.w700, color: Colors.white)),
                                  const Spacer(),
                                  Container(padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 2),
                                    decoration: BoxDecoration(borderRadius: BorderRadius.circular(6), color: item.color.withOpacity(0.12)),
                                    child: Text(item.category, style: GoogleFonts.orbitron(fontSize: 7, color: item.color))),
                                ]),
                                const SizedBox(height: 3),
                                Text(item.subtitle, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white38, height: 1.3)),
                              ])),
                              const SizedBox(width: 8),
                              Icon(Icons.arrow_forward_ios_rounded, color: item.color.withOpacity(0.5), size: 13),
                            ]),
                          ),
                        );
                      },
                    ),
              ),
            ]),
          ),
        ],
      ),
    );
  }
}

class _SP extends CustomPainter {
  final double progress;
  static final _rng = Random(55);
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
"""

with open("lib/screens/search_screen.dart", "w") as f:
    f.write(content)
print("Done! Lines:", len(content.splitlines()))
