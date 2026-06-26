// lib/data/cosmos_data.dart

class CosmicObject {
  final String name;
  final String emoji;
  final String description;
  final String diameter;
  final String distanceFromSun;
  final String funFact;
  final String imagePath;

  const CosmicObject({
    required this.name,
    required this.emoji,
    required this.description,
    required this.diameter,
    required this.distanceFromSun,
    required this.funFact,
    this.imagePath = '',
  });
}

final List<CosmicObject> planets = [
  CosmicObject(
    name: 'Mercury',
    emoji: '⚫',
    description: 'The smallest planet and closest to the Sun. Has no atmosphere and extreme temperature swings.',
    diameter: '4,879 km',
    distanceFromSun: '57.9 million km',
    funFact: 'A year on Mercury is just 88 Earth days!',
  ),
  CosmicObject(
    name: 'Venus',
    emoji: '🟡',
    description: 'The hottest planet in our solar system due to its thick CO₂ atmosphere.',
    diameter: '12,104 km',
    distanceFromSun: '108.2 million km',
    funFact: 'Venus spins backwards compared to most planets.',
  ),
  CosmicObject(
    name: 'Earth',
    emoji: '🔵',
    description: 'Our home. The only known planet with life, liquid water, and a protective magnetic field.',
    diameter: '12,742 km',
    distanceFromSun: '149.6 million km',
    funFact: 'Earth is the densest planet in the Solar System.',
  ),
  CosmicObject(
    name: 'Mars',
    emoji: '🔴',
    description: 'The Red Planet with the tallest volcano in the solar system — Olympus Mons.',
    diameter: '6,779 km',
    distanceFromSun: '227.9 million km',
    funFact: 'Mars has two tiny moons: Phobos and Deimos.',
  ),
  CosmicObject(
    name: 'Jupiter',
    emoji: '🟠',
    description: 'The largest planet — a gas giant with a storm (Great Red Spot) raging for 400+ years.',
    diameter: '139,820 km',
    distanceFromSun: '778.5 million km',
    funFact: 'Jupiter has 95 known moons!',
  ),
  CosmicObject(
    name: 'Saturn',
    emoji: '🪐',
    description: 'Famous for its stunning ring system made of ice and rock.',
    diameter: '116,460 km',
    distanceFromSun: '1.43 billion km',
    funFact: 'Saturn is so light it would float on water.',
  ),
  CosmicObject(
    name: 'Uranus',
    emoji: '🔵',
    description: 'An ice giant that rotates on its side with a tilt of 98 degrees.',
    diameter: '50,724 km',
    distanceFromSun: '2.87 billion km',
    funFact: 'Uranus has 13 known rings.',
  ),
  CosmicObject(
    name: 'Neptune',
    emoji: '💙',
    description: 'The windiest planet with storms reaching 2,100 km/h.',
    diameter: '49,244 km',
    distanceFromSun: '4.5 billion km',
    funFact: 'Neptune was predicted mathematically before it was seen.',
  ),
];

final List<CosmicObject> deepSpaceObjects = [
  CosmicObject(
    name: 'Solar System',
    emoji: '☀️',
    description: 'Our Sun and everything bound to it — 8 planets, moons, asteroids, and comets.',
    diameter: '~2 light years across',
    distanceFromSun: 'Center',
    funFact: '99.8% of the Solar System\'s mass is the Sun.',
  ),
  CosmicObject(
    name: 'Milky Way',
    emoji: '🌌',
    description: 'Our home galaxy — a barred spiral galaxy containing 200–400 billion stars.',
    diameter: '100,000 light years',
    distanceFromSun: '26,000 light years from center',
    funFact: 'The Milky Way completes one rotation every 225 million years.',
  ),
  CosmicObject(
    name: 'Black Hole',
    emoji: '🕳️',
    description: 'A region where gravity is so strong that nothing — not even light — can escape.',
    diameter: 'Varies (Singularity)',
    distanceFromSun: 'Nearest: ~1,600 light years',
    funFact: 'Time slows down near a black hole due to gravity.',
  ),
  CosmicObject(
    name: 'Observable Universe',
    emoji: '🔭',
    description: 'Everything we can see — 2 trillion galaxies spanning 93 billion light years.',
    diameter: '93 billion light years',
    distanceFromSun: 'We are inside it',
    funFact: 'The universe is 13.8 billion years old.',
  ),
  CosmicObject(
    name: 'Multiverse',
    emoji: '♾️',
    description: 'A theoretical collection of multiple universes beyond our own, each with different laws of physics.',
    diameter: 'Unknown / Infinite',
    distanceFromSun: 'Beyond observable reality',
    funFact: 'String theory suggests 10⁵⁰⁰ possible universes exist.',
  ),
];
