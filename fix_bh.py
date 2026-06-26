content = open('lib/screens/blackhole_screen.dart').read()

# Find and remove the duplicate description - keep only the new one from hero banner
old = '''                Container(padding: const EdgeInsets.all(14), decoration: BoxDecoration(borderRadius: BorderRadius.circular(14), color: const Color(0xFF040F1F), border: Border.all(color: Colors.white12)),
                  child: Text("A black hole is a point in space where gravity is so extreme that nothing \u2014 not even light \u2014 can escape. The boundary of no return is called the event horizon.", style: GoogleFonts.rajdhani(fontSize: 14, color: Colors.white54, height: 1.5))),
                const SizedBox(height: 16),
                Text("TYPES OF BLACK HOLES"'''

new = '''                Text("TYPES OF BLACK HOLES"'''

result = content.replace(old, new)

if result != content:
    open('lib/screens/blackhole_screen.dart', 'w').write(result)
    print('Done! Duplicate removed.')
else:
    # Try line-by-line approach
    lines = content.split('\n')
    new_lines = []
    skip = False
    for i, line in enumerate(lines):
        if 'A black hole is a point in space' in line:
            # Remove this line and surrounding container
            new_lines = new_lines[:-2]  # remove previous 2 lines (Container opening)
            skip = True
        elif skip and 'SizedBox(height: 16)' in line:
            skip = False
            continue
        elif not skip:
            new_lines.append(line)
    
    open('lib/screens/blackhole_screen.dart', 'w').write('\n'.join(new_lines))
    print('Done via line approach!')
