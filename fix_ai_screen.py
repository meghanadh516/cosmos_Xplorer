content = r"""import 'dart:math';
import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart' as http;

class AIAssistantScreen extends StatefulWidget {
  const AIAssistantScreen({super.key});
  @override
  State<AIAssistantScreen> createState() => _AIAssistantScreenState();
}

class _AIAssistantScreenState extends State<AIAssistantScreen>
    with SingleTickerProviderStateMixin {
  late AnimationController _starController;
  final TextEditingController _textController = TextEditingController();
  final ScrollController _scrollController = ScrollController();
  final List<_Message> _messages = [];
  bool _isLoading = false;

  final List<String> _suggestions = [
    "How big is the universe?",
    "What is a black hole?",
    "How many planets exist?",
    "What is dark matter?",
    "Can we live on Mars?",
    "What is the multiverse?",
    "How was the Sun formed?",
    "What happens inside a black hole?",
  ];

  @override
  void initState() {
    super.initState();
    _starController = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();
    _messages.add(_Message(
      text: "Hello! I'm NOVA 🌟 — your personal cosmos guide inside CosmosXplorer.\n\nAsk me anything about planets, black holes, galaxies, the universe, or beyond. The cosmos awaits! 🚀",
      isUser: false,
    ));
  }

  @override
  void dispose() {
    _starController.dispose();
    _textController.dispose();
    _scrollController.dispose();
    super.dispose();
  }

  Future<void> _sendMessage(String text) async {
    if (text.trim().isEmpty) return;
    setState(() {
      _messages.add(_Message(text: text, isUser: true));
      _isLoading = true;
    });
    _textController.clear();
    _scrollToBottom();

    try {
      // Build conversation history (skip welcome message)
      final history = _messages.skip(1).where((m) => m.text != text).map((m) => {
        'role': m.isUser ? 'user' : 'assistant',
        'content': m.text,
      }).toList();
      history.add({'role': 'user', 'content': text});

      final response = await http.post(
        Uri.parse('https://api.anthropic.com/v1/messages'),
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': 'YOUR_API_KEY_HERE',
          'anthropic-version': '2023-06-01',
          'anthropic-dangerous-direct-browser-access': 'true',
        },
        body: jsonEncode({
          'model': 'claude-sonnet-4-20250514',
          'max_tokens': 1024,
          'system': 'You are NOVA, an expert space and astronomy AI assistant inside the CosmosXplorer app. Help users learn about planets, solar system, galaxies, black holes, universe, and multiverse. Keep answers engaging, educational and concise (2-3 paragraphs). Use emojis to make responses fun. Always be scientifically accurate. If asked something unrelated to space/science, politely redirect to cosmos topics.',
          'messages': history,
        }),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final reply = data['content'][0]['text'] as String;
        setState(() {
          _messages.add(_Message(text: reply, isUser: false));
          _isLoading = false;
        });
      } else {
        print('Error: ${response.statusCode} - ${response.body}');
        setState(() {
          _messages.add(_Message(text: "⚠️ Connection lost in deep space! Check your internet and try again.", isUser: false));
          _isLoading = false;
        });
      }
    } catch (e) {
      print('Exception: $e');
      setState(() {
        _messages.add(_Message(text: "⚠️ Connection lost in deep space! Check your internet and try again.", isUser: false));
        _isLoading = false;
      });
    }
    _scrollToBottom();
  }

  void _scrollToBottom() {
    Future.delayed(const Duration(milliseconds: 300), () {
      if (_scrollController.hasClients) {
        _scrollController.animateTo(
          _scrollController.position.maxScrollExtent,
          duration: const Duration(milliseconds: 400),
          curve: Curves.easeOut,
        );
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF010914),
      body: Stack(
        children: [
          AnimatedBuilder(
            animation: _starController,
            builder: (_, __) => CustomPaint(painter: _SP(_starController.value), child: const SizedBox.expand()),
          ),
          SafeArea(
            child: Column(
              children: [
                // Header
                Container(
                  padding: const EdgeInsets.fromLTRB(20, 16, 20, 12),
                  decoration: BoxDecoration(
                    color: const Color(0xFF010914).withOpacity(0.95),
                    border: Border(bottom: BorderSide(color: Color(0xFF00AAFF).withOpacity(0.2))),
                  ),
                  child: Row(children: [
                    GestureDetector(
                      onTap: () => Navigator.pop(context),
                      child: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white54, size: 20),
                    ),
                    const SizedBox(width: 12),
                    Container(
                      width: 42, height: 42,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        gradient: RadialGradient(colors: [Color(0xFF00AAFF), Color(0xFF0044AA)]),
                        boxShadow: [BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.5), blurRadius: 15)],
                      ),
                      child: const Center(child: Text("⭐", style: TextStyle(fontSize: 22))),
                    ),
                    const SizedBox(width: 12),
                    Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                      Text("NOVA", style: GoogleFonts.orbitron(fontSize: 18, fontWeight: FontWeight.w800, color: Colors.white, letterSpacing: 3, shadows: [Shadow(color: Color(0xFF00AAFF), blurRadius: 10)])),
                      Text("AI Cosmos Assistant", style: GoogleFonts.rajdhani(fontSize: 12, color: Color(0xFF00AAFF))),
                    ]),
                    const Spacer(),
                    Container(
                      padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                      decoration: BoxDecoration(borderRadius: BorderRadius.circular(20), color: Color(0xFF00FFCC).withOpacity(0.1), border: Border.all(color: Color(0xFF00FFCC).withOpacity(0.4))),
                      child: Row(children: [
                        Container(width: 6, height: 6, decoration: BoxDecoration(shape: BoxShape.circle, color: Color(0xFF00FFCC))),
                        const SizedBox(width: 5),
                        Text("Online", style: GoogleFonts.orbitron(fontSize: 8, color: Color(0xFF00FFCC))),
                      ]),
                    ),
                  ]),
                ),

                // Messages
                Expanded(
                  child: ListView.builder(
                    controller: _scrollController,
                    padding: const EdgeInsets.all(16),
                    itemCount: _messages.length + (_isLoading ? 1 : 0),
                    itemBuilder: (ctx, i) {
                      if (i == _messages.length && _isLoading) return _TypingIndicator();
                      return _MessageBubble(_messages[i]);
                    },
                  ),
                ),

                // Suggestions
                if (_messages.length <= 1)
                  SizedBox(
                    height: 44,
                    child: ListView.builder(
                      scrollDirection: Axis.horizontal,
                      padding: const EdgeInsets.symmetric(horizontal: 16),
                      itemCount: _suggestions.length,
                      itemBuilder: (ctx, i) => GestureDetector(
                        onTap: () => _sendMessage(_suggestions[i]),
                        child: Container(
                          margin: const EdgeInsets.only(right: 8),
                          padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                          decoration: BoxDecoration(
                            borderRadius: BorderRadius.circular(20),
                            color: const Color(0xFF040F1F),
                            border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.35)),
                          ),
                          child: Text(_suggestions[i], style: GoogleFonts.rajdhani(fontSize: 13, color: Color(0xFF00AAFF))),
                        ),
                      ),
                    ),
                  ),
                const SizedBox(height: 8),

                // Input
                Container(
                  padding: const EdgeInsets.fromLTRB(16, 8, 16, 16),
                  decoration: BoxDecoration(
                    color: const Color(0xFF010914),
                    border: Border(top: BorderSide(color: Color(0xFF00AAFF).withOpacity(0.15))),
                  ),
                  child: Row(children: [
                    Expanded(
                      child: Container(
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(24),
                          color: const Color(0xFF040F1F),
                          border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.35)),
                        ),
                        child: TextField(
                          controller: _textController,
                          style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white),
                          maxLines: null,
                          textInputAction: TextInputAction.send,
                          onSubmitted: _sendMessage,
                          decoration: InputDecoration(
                            hintText: "Ask NOVA anything about space...",
                            hintStyle: GoogleFonts.rajdhani(color: Colors.white24, fontSize: 14),
                            border: InputBorder.none,
                            contentPadding: const EdgeInsets.symmetric(horizontal: 18, vertical: 12),
                          ),
                        ),
                      ),
                    ),
                    const SizedBox(width: 10),
                    GestureDetector(
                      onTap: () => _sendMessage(_textController.text),
                      child: Container(
                        width: 48, height: 48,
                        decoration: BoxDecoration(
                          shape: BoxShape.circle,
                          gradient: LinearGradient(colors: [Color(0xFF00AAFF), Color(0xFF0066FF)]),
                          boxShadow: [BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.5), blurRadius: 15)],
                        ),
                        child: const Icon(Icons.send_rounded, color: Colors.white, size: 22),
                      ),
                    ),
                  ]),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _Message {
  final String text;
  final bool isUser;
  _Message({required this.text, required this.isUser});
}

class _MessageBubble extends StatelessWidget {
  final _Message message;
  const _MessageBubble(this.message);

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 14),
      child: Row(
        mainAxisAlignment: message.isUser ? MainAxisAlignment.end : MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.end,
        children: [
          if (!message.isUser) ...[
            Container(width: 34, height: 34, decoration: BoxDecoration(shape: BoxShape.circle, gradient: RadialGradient(colors: [Color(0xFF00AAFF), Color(0xFF0044AA)]), boxShadow: [BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.3), blurRadius: 8)]),
              child: const Center(child: Text("⭐", style: TextStyle(fontSize: 16)))),
            const SizedBox(width: 8),
          ],
          Flexible(
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.only(
                  topLeft: const Radius.circular(18),
                  topRight: const Radius.circular(18),
                  bottomLeft: Radius.circular(message.isUser ? 18 : 4),
                  bottomRight: Radius.circular(message.isUser ? 4 : 18),
                ),
                color: message.isUser ? Color(0xFF00AAFF).withOpacity(0.2) : const Color(0xFF040F1F),
                border: Border.all(color: message.isUser ? Color(0xFF00AAFF).withOpacity(0.5) : Colors.white12),
              ),
              child: Text(message.text, style: GoogleFonts.rajdhani(fontSize: 15, color: Colors.white, height: 1.5)),
            ),
          ),
          if (message.isUser) ...[
            const SizedBox(width: 8),
            Container(width: 34, height: 34, decoration: BoxDecoration(shape: BoxShape.circle, color: Color(0xFF00AAFF).withOpacity(0.15), border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.4))),
              child: const Center(child: Icon(Icons.person_rounded, color: Color(0xFF00AAFF), size: 20))),
          ],
        ],
      ),
    );
  }
}

class _TypingIndicator extends StatefulWidget {
  @override
  State<_TypingIndicator> createState() => _TypingIndicatorState();
}
class _TypingIndicatorState extends State<_TypingIndicator> with SingleTickerProviderStateMixin {
  late AnimationController _ctrl;
  @override
  void initState() { super.initState(); _ctrl = AnimationController(vsync: this, duration: const Duration(milliseconds: 800))..repeat(); }
  @override
  void dispose() { _ctrl.dispose(); super.dispose(); }
  @override
  Widget build(BuildContext context) => Padding(
    padding: const EdgeInsets.only(bottom: 14),
    child: Row(children: [
      Container(width: 34, height: 34, decoration: BoxDecoration(shape: BoxShape.circle, gradient: RadialGradient(colors: [Color(0xFF00AAFF), Color(0xFF0044AA)])), child: const Center(child: Text("⭐", style: TextStyle(fontSize: 16)))),
      const SizedBox(width: 8),
      Container(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
        decoration: BoxDecoration(borderRadius: BorderRadius.circular(18), color: const Color(0xFF040F1F), border: Border.all(color: Colors.white12)),
        child: AnimatedBuilder(
          animation: _ctrl,
          builder: (_, __) => Row(mainAxisSize: MainAxisSize.min, children: List.generate(3, (i) {
            final t = (_ctrl.value - i * 0.2).clamp(0.0, 1.0);
            return Container(margin: const EdgeInsets.symmetric(horizontal: 3), width: 7, height: 7,
              decoration: BoxDecoration(shape: BoxShape.circle, color: Color(0xFF00AAFF).withOpacity(0.3 + 0.7 * (0.5 + 0.5 * sin(t * 2 * pi)))));
          })),
        ),
      ),
    ]),
  );
}

class _SP extends CustomPainter {
  final double progress;
  static final _rng = Random(55);
  static final _stars = List.generate(150, (_) => Offset(_rng.nextDouble(), _rng.nextDouble()));
  static final _szs = List.generate(150, (_) => _rng.nextDouble() * 1.2 + 0.3);
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

with open("lib/screens/ai_assistant_screen.dart", "w") as f:
    f.write(content)
print("AI screen done!")
