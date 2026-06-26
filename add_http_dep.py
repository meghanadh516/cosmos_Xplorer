import re

with open("pubspec.yaml", "r") as f:
    content = f.read()

# Add http dependency if not already there
if "http:" not in content:
    content = content.replace(
        "  smooth_page_indicator: ^1.1.0",
        "  smooth_page_indicator: ^1.1.0\n  http: ^1.1.0"
    )
    with open("pubspec.yaml", "w") as f:
        f.write(content)
    print("http dependency added to pubspec.yaml")
else:
    print("http already in pubspec.yaml")
