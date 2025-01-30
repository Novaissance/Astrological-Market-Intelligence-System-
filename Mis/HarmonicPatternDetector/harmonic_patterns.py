import numpy as np
import pandas as pd
from typing import Dict, List
from scipy.signal import find_peaks

class AdvancedHarmonicPatternDetector:
    def __init__(self):
        self.fibonacci_levels = [0.382, 0.5, 0.618, 0.786, 1.272, 1.618, 2.618, 4.236]
        self.patterns = {
            'gartley': {'XA': 0.618, 'AB': 0.382, 'BC': 0.886, 'CD': 1.272},
            'butterfly': {'XA': 0.786, 'AB': 0.382, 'BC': 0.886, 'CD': 1.618},
            'bat': {'XA': 0.886, 'AB': 0.382, 'BC': 0.886, 'CD': 2.0},
            'crab': {'XA': 0.886, 'AB': 0.382, 'BC': 0.886, 'CD': 3.618},
            'shark': {'XA': 0.886, 'AB': 1.13, 'BC': 1.618, 'CD': 0.886},
            'cypher': {'XA': 0.786, 'AB': 1.272, 'BC': 0.786, 'CD': 1.272}
        }
        
    def detect_advanced_patterns(self, price_data: pd.DataFrame) -> List[Dict]:
        swing_points = self._identify_swing_points(price_data)
        patterns_found = []
        
        for i in range(len(swing_points) - 4):
            points = swing_points[i:i+5]
            for pattern_name, ratios in self.patterns.items():
                confidence = self._validate_pattern_with_tolerance(points, ratios)
                if confidence > 0.8:  # 80% confidence threshold
                    patterns_found.append({
                        'pattern': pattern_name,
                        'points': points,
                        'confidence': confidence,
                        'completion_zone': self._calculate_completion_zone(points, pattern_name)
                    })
        return patterns_found

    def _identify_swing_points(self, price_data: pd.DataFrame) -> np.array:
        highs, _ = find_peaks(price_data['high'].values)
        lows, _ = find_peaks(-price_data['low'].values)
        return np.sort(np.concatenate([highs, lows]))
