from dataclasses import dataclass
from enum import Enum

class PlanetaryAspect(Enum):
    CONJUNCTION = 0
    SEXTILE = 60
    SQUARE = 90
    TRINE = 120
    OPPOSITION = 180

@dataclass
class ZodiacAttributes:
    ruling_planet: str
    element: str
    quality: str
    polarity: str

class EnhancedZodiacalStrategy:
    def __init__(self):
        self.zodiac_signs = {
            'aries': ZodiacAttributes('mars', 'fire', 'cardinal', 'positive'),
            'taurus': ZodiacAttributes('venus', 'earth', 'fixed', 'negative'),
            # Add other signs...
        }
        self.aspect_influences = {
            PlanetaryAspect.CONJUNCTION: 1.0,
            PlanetaryAspect.SEXTILE: 0.5,
            PlanetaryAspect.SQUARE: -0.5,
            PlanetaryAspect.TRINE: 0.8,
            PlanetaryAspect.OPPOSITION: -0.8
        }
        
    def analyze_market_sentiment(self, 
                               planetary_positions: Dict,
                               market_data: pd.DataFrame) -> Dict:
        sentiment = {}
        for sign, attributes in self.zodiac_signs.items():
            aspects = self._calculate_aspects(planetary_positions, attributes.ruling_planet)
            sentiment[sign] = {
                'strength': self._calculate_sign_strength(aspects),
                'element_harmony': self._analyze_element_harmony(planetary_positions, attributes.element),
                'quality_impact': self._analyze_quality_impact(attributes.quality),
                'polarity_bias': self._calculate_polarity_bias(attributes.polarity)
            }
        return sentiment