content = r"""import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:http/http.dart' as http;

class AiAssistantScreen extends StatefulWidget {
  const AiAssistantScreen({super.key});
  @override
  State<AiAssistantScreen> createState() => _AiAssistantScreenState();
}

class _AiAssistantScreenState extends State<AiAssistantScreen>
    with TickerProviderStateMixin {
  final TextEditingController _input = TextEditingController();
  final ScrollController _scroll = ScrollController();
  final List<_ChatMsg> _messages = [];
  bool _loading = false;

  // ── Replace with your Anthropic API key ──
  static const _apiKey = 'YOUR_ANTHROPIC_API_KEY';

  static const _system = '''You are NOVA, an AI space assistant inside the Cosmos Xplorer app.
You are an expert on everything in the universe: planets, moons, stars, solar systems, galaxies, black holes, the universe, multiverse theories, space missions, astronomy, astrophysics, and cosmology.
Keep answers engaging, awe-inspiring, and concise (3-5 sentences unless asked for more).
Use occasional space emojis to make responses lively. Always end with a mind-blowing fact if relevant.
If asked something unrelated to space/cosmos, gently redirect: "I'm NOVA, your cosmos guide — ask me anything about space! 🚀"''';

  final List<_QuickPrompt> _quickPrompts = [
    _QuickPrompt("🌍", "How far is Earth from the Sun?"),
    _QuickPrompt("⚫", "What happens inside a black hole?"),
    _QuickPrompt("🌌", "How big is the Milky Way?"),
    _QuickPrompt("🔭", "What is dark matter?"),
    _QuickPrompt("🪐", "How many moons does Saturn have?"),
    _QuickPrompt("💥", "What was the Big Bang?"),
    _QuickPrompt("🌀", "Are there other universes?"),
    _QuickPrompt("☀️", "Will our Sun die?"),
  ];

  @override
  void initState() {
    super.initState();
    _messages.add(_ChatMsg(
      role: 'assistant',
      text: "Hello! I'm NOVA 🌟 — your personal cosmos guide inside Cosmos Xplorer.\n\nAsk me anything about planets, black holes, galaxies, the universe, or beyond. The cosmos awaits! 🚀",
    ));
  }

  @override
  void dispose() {
    _input.dispose();
    _scroll.dispose();
    super.dispose();
  }

  Future<void> _send(String text) async {
    if (text.trim().isEmpty) return;
    _input.clear();
    setState(() {
      _messages.add(_ChatMsg(role: 'user', text: text.trim()));
      _loading = true;
    });
    _scrollToBottom();

    try {
      final history = _messages
          .where((m) => m.role != 'typing')
          .map((m) => {"role": m.role, "content": m.text})
          .toList();

      final response = await http.post(
        Uri.parse('https://api.anthropic.com/v1/messages'),
        headers: {
          'Content-Type': 'application/json',
          'x-api-key': _apiKey,
          'anthropic-version': '2023-06-01',
        },
        body: jsonEncode({
          'model': 'claude-sonnet-4-20250514',
          'max_tokens': 1024,
          'system': _system,
          'messages': history,
        }),
      );

      if (response.statusCode == 200) {
        final data = jsonDecode(response.body);
        final reply = data['content'][0]['text'] as String;
        setState(() {
          _loading = false;
          _messages.add(_ChatMsg(role: 'assistant', text: reply));
        });
      } else {
        setState(() {
          _loading = false;
          _messages.add(_ChatMsg(role: 'assistant', text: "⚠️ Something went wrong reaching the cosmos. Please check your API key and try again."));
        });
      }
    } catch (e) {
      setState(() {
        _loading = false;
        _messages.add(_ChatMsg(role: 'assistant', text: "⚠️ Connection lost in deep space! Check your internet and try again."));
      });
    }
    _scrollToBottom();
  }

  void _scrollToBottom() {
    Future.delayed(const Duration(milliseconds: 150), () {
      if (_scroll.hasClients) {
        _scroll.animateTo(_scroll.position.maxScrollExtent, duration: const Duration(milliseconds: 400), curve: Curves.easeOut);
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFF010914),
      body: SafeArea(
        child: Column(
          children: [
            // ── Header ────────────────────────────────────────────────────
            Container(
              padding: const EdgeInsets.fromLTRB(20, 16, 20, 12),
              decoration: BoxDecoration(
                color: const Color(0xFF010914),
                border: Border(bottom: BorderSide(color: Colors.white.withOpacity(0.06))),
              ),
              child: Row(children: [
                GestureDetector(
                  onTap: () => Navigator.pop(context),
                  child: const Icon(Icons.arrow_back_ios_new_rounded, color: Colors.white54, size: 20),
                ),
                const SizedBox(width: 12),
                Container(
                  width: 38, height: 38,
                  decoration: BoxDecoration(
                    shape: BoxShape.circle,
                    gradient: const RadialGradient(colors: [Color(0xFF1565C0), Color(0xFF0D47A1)]),
                    boxShadow: [BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.4), blurRadius: 12)],
                  ),
                  child: const Center(child: Text("🌟", style: TextStyle(fontSize: 18))),
                ),
                const SizedBox(width: 12),
                Expanded(child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: [
                  Text("NOVA", style: GoogleFonts.orbitron(fontSize: 15, fontWeight: FontWeight.w700, color: Colors.white, letterSpacing: 2)),
                  Text("AI Cosmos Assistant", style: GoogleFonts.rajdhani(fontSize: 11, color: Color(0xFF00AAFF))),
                ])),
                Container(
                  padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                  decoration: BoxDecoration(borderRadius: BorderRadius.circular(20), color: Colors.green.withOpacity(0.12), border: Border.all(color: Colors.green.withOpacity(0.4))),
                  child: Row(mainAxisSize: MainAxisSize.min, children: [
                    Container(width: 6, height: 6, decoration: const BoxDecoration(shape: BoxShape.circle, color: Colors.greenAccent)),
                    const SizedBox(width: 5),
                    Text("Online", style: GoogleFonts.rajdhani(fontSize: 11, color: Colors.greenAccent)),
                  ]),
                ),
              ]),
            ),

            // ── Quick prompts ─────────────────────────────────────────────
            if (_messages.length <= 1)
              Container(
                height: 44,
                margin: const EdgeInsets.only(top: 8),
                child: ListView.builder(
                  scrollDirection: Axis.horizontal,
                  padding: const EdgeInsets.symmetric(horizontal: 16),
                  itemCount: _quickPrompts.length,
                  itemBuilder: (_, i) {
                    final q = _quickPrompts[i];
                    return GestureDetector(
                      onTap: () => _send(q.text),
                      child: Container(
                        margin: const EdgeInsets.only(right: 8),
                        padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                        decoration: BoxDecoration(
                          borderRadius: BorderRadius.circular(20),
                          color: const Color(0xFF040F1F),
                          border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.3)),
                        ),
                        child: Row(mainAxisSize: MainAxisSize.min, children: [
                          Text(q.icon, style: const TextStyle(fontSize: 14)),
                          const SizedBox(width: 6),
                          Text(q.text, style: GoogleFonts.rajdhani(fontSize: 12, color: Colors.white70)),
                        ]),
                      ),
                    );
                  },
                ),
              ),

            // ── Chat messages ─────────────────────────────────────────────
            Expanded(
              child: ListView.builder(
                controller: _scroll,
                padding: const EdgeInsets.fromLTRB(16, 12, 16, 8),
                itemCount: _messages.length + (_loading ? 1 : 0),
                itemBuilder: (_, i) {
                  if (_loading && i == _messages.length) return _TypingIndicator();
                  return _BubbleTile(_messages[i]);
                },
              ),
            ),

            // ── Input bar ────────────────────────────────────────────────
            Container(
              padding: const EdgeInsets.fromLTRB(16, 10, 16, 14),
              decoration: BoxDecoration(
                color: const Color(0xFF010914),
                border: Border(top: BorderSide(color: Colors.white.withOpacity(0.06))),
              ),
              child: Row(children: [
                Expanded(
                  child: Container(
                    decoration: BoxDecoration(
                      borderRadius: BorderRadius.circular(24),
                      color: const Color(0xFF040F1F),
                      border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.25)),
                    ),
                    child: TextField(
                      controller: _input,
                      style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white),
                      maxLines: null,
                      textInputAction: TextInputAction.send,
                      onSubmitted: _send,
                      decoration: InputDecoration(
                        hintText: "Ask NOVA anything about space...",
                        hintStyle: GoogleFonts.rajdhani(fontSize: 13, color: Colors.white24),
                        border: InputBorder.none,
                        contentPadding: const EdgeInsets.symmetric(horizontal: 18, vertical: 12),
                      ),
                    ),
                  ),
                ),
                const SizedBox(width: 10),
                GestureDetector(
                  onTap: () => _send(_input.text),
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 200),
                    width: 46, height: 46,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      gradient: const LinearGradient(colors: [Color(0xFF0066FF), Color(0xFF00AAFF)]),
                      boxShadow: [BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.35), blurRadius: 12)],
                    ),
                    child: const Icon(Icons.send_rounded, color: Colors.white, size: 20),
                  ),
                ),
              ]),
            ),
          ],
        ),
      ),
    );
  }
}

// ── CHAT BUBBLE ──────────────────────────────────────────────────────────────

class _BubbleTile extends StatelessWidget {
  final _ChatMsg msg;
  const _BubbleTile(this.msg);

  @override
  Widget build(BuildContext context) {
    final isUser = msg.role == 'user';
    return Padding(
      padding: const EdgeInsets.only(bottom: 14),
      child: Row(
        mainAxisAlignment: isUser ? MainAxisAlignment.end : MainAxisAlignment.start,
        crossAxisAlignment: CrossAxisAlignment.end,
        children: [
          if (!isUser) ...[
            Container(
              width: 30, height: 30,
              decoration: BoxDecoration(
                shape: BoxShape.circle,
                gradient: const RadialGradient(colors: [Color(0xFF1565C0), Color(0xFF0D47A1)]),
                boxShadow: [BoxShadow(color: Color(0xFF00AAFF).withOpacity(0.3), blurRadius: 8)],
              ),
              child: const Center(child: Text("🌟", style: TextStyle(fontSize: 14))),
            ),
            const SizedBox(width: 8),
          ],
          Flexible(
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              decoration: BoxDecoration(
                borderRadius: BorderRadius.only(
                  topLeft: const Radius.circular(18),
                  topRight: const Radius.circular(18),
                  bottomLeft: Radius.circular(isUser ? 18 : 4),
                  bottomRight: Radius.circular(isUser ? 4 : 18),
                ),
                color: isUser ? const Color(0xFF0066FF) : const Color(0xFF040F1F),
                border: isUser ? null : Border.all(color: Color(0xFF00AAFF).withOpacity(0.2)),
                boxShadow: [
                  BoxShadow(
                    color: isUser ? Color(0xFF0066FF).withOpacity(0.25) : Colors.black26,
                    blurRadius: 10, offset: const Offset(0, 3),
                  ),
                ],
              ),
              child: Text(msg.text, style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white, height: 1.5)),
            ),
          ),
          if (isUser) const SizedBox(width: 8),
        ],
      ),
    );
  }
}

// ── TYPING INDICATOR ──────────────────────────────────────────────────────────

class _TypingIndicator extends StatefulWidget {
  @override
  State<_TypingIndicator> createState() => _TypingIndicatorState();
}

class _TypingIndicatorState extends State<_TypingIndicator> with SingleTickerProviderStateMixin {
  late AnimationController _ctrl;

  @override
  void initState() {
    super.initState();
    _ctrl = AnimationController(vsync: this, duration: const Duration(milliseconds: 900))..repeat();
  }

  @override
  void dispose() { _ctrl.dispose(); super.dispose(); }

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 14),
      child: Row(crossAxisAlignment: CrossAxisAlignment.end, children: [
        Container(
          width: 30, height: 30,
          decoration: BoxDecoration(shape: BoxShape.circle, gradient: const RadialGradient(colors: [Color(0xFF1565C0), Color(0xFF0D47A1)])),
          child: const Center(child: Text("🌟", style: TextStyle(fontSize: 14))),
        ),
        const SizedBox(width: 8),
        Container(
          padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
          decoration: BoxDecoration(
            borderRadius: const BorderRadius.only(topLeft: Radius.circular(18), topRight: Radius.circular(18), bottomRight: Radius.circular(18), bottomLeft: Radius.circular(4)),
            color: const Color(0xFF040F1F),
            border: Border.all(color: Color(0xFF00AAFF).withOpacity(0.2)),
          ),
          child: AnimatedBuilder(
            animation: _ctrl,
            builder: (_, __) => Row(mainAxisSize: MainAxisSize.min, children: List.generate(3, (i) {
              final t = (_ctrl.value - i * 0.2).clamp(0.0, 1.0);
              final opacity = (0.3 + 0.7 * (0.5 + 0.5 * (t < 0.5 ? 2 * t : 2 - 2 * t))).clamp(0.3, 1.0);
              return Container(
                margin: EdgeInsets.only(right: i < 2 ? 4 : 0),
                width: 7, height: 7,
                decoration: BoxDecoration(shape: BoxShape.circle, color: Color(0xFF00AAFF).withOpacity(opacity)),
              );
            })),
          ),
        ),
      ]),
    );
  }
}

// ── MODELS ───────────────────────────────────────────────────────────────────

class _ChatMsg {
  final String role, text;
  const _ChatMsg({required this.role, required this.text});
}

class _QuickPrompt {
  final String icon, text;
  const _QuickPrompt(this.icon, this.text);
}
"""

with open("lib/screens/ai_assistant_screen.dart", "w") as f:
    f.write(content)
print("Done! Lines:", len(content.splitlines()))
