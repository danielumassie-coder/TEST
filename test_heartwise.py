#!/usr/bin/env python3
"""
Tests for Heartwise application
"""

import unittest
import os
import json
from heartwise import HeartHealthTracker


class TestHeartHealthTracker(unittest.TestCase):
    """Test cases for HeartHealthTracker"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_file = "test_heart_data.json"
        self.tracker = HeartHealthTracker(data_file=self.test_file)
    
    def tearDown(self):
        """Clean up test files"""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)
    
    def test_add_reading(self):
        """Test adding a new reading"""
        reading = self.tracker.add_reading(heart_rate=75, blood_pressure="120/80", notes="After exercise")
        
        self.assertEqual(reading["heart_rate"], 75)
        self.assertEqual(reading["blood_pressure"], "120/80")
        self.assertEqual(reading["notes"], "After exercise")
        self.assertIn("timestamp", reading)
    
    def test_add_reading_minimal(self):
        """Test adding a reading with only heart rate"""
        reading = self.tracker.add_reading(heart_rate=72)
        
        self.assertEqual(reading["heart_rate"], 72)
        self.assertIsNone(reading["blood_pressure"])
        self.assertIsNone(reading["notes"])
    
    def test_get_readings(self):
        """Test retrieving readings"""
        self.tracker.add_reading(heart_rate=70)
        self.tracker.add_reading(heart_rate=75)
        self.tracker.add_reading(heart_rate=80)
        
        all_readings = self.tracker.get_readings()
        self.assertEqual(len(all_readings), 3)
        
        recent_readings = self.tracker.get_readings(limit=2)
        self.assertEqual(len(recent_readings), 2)
        self.assertEqual(recent_readings[0]["heart_rate"], 75)
        self.assertEqual(recent_readings[1]["heart_rate"], 80)
    
    def test_average_heart_rate(self):
        """Test calculating average heart rate"""
        # Empty data
        self.assertIsNone(self.tracker.get_average_heart_rate())
        
        # With data
        self.tracker.add_reading(heart_rate=60)
        self.tracker.add_reading(heart_rate=70)
        self.tracker.add_reading(heart_rate=80)
        
        avg = self.tracker.get_average_heart_rate()
        self.assertEqual(avg, 70.0)
    
    def test_get_stats(self):
        """Test statistics calculation"""
        # Empty stats
        stats = self.tracker.get_stats()
        self.assertEqual(stats["total_readings"], 0)
        self.assertIsNone(stats["average_heart_rate"])
        
        # With data
        self.tracker.add_reading(heart_rate=60)
        self.tracker.add_reading(heart_rate=70)
        self.tracker.add_reading(heart_rate=80)
        self.tracker.add_reading(heart_rate=90)
        
        stats = self.tracker.get_stats()
        self.assertEqual(stats["total_readings"], 4)
        self.assertEqual(stats["average_heart_rate"], 75.0)
        self.assertEqual(stats["min_heart_rate"], 60)
        self.assertEqual(stats["max_heart_rate"], 90)
    
    def test_data_persistence(self):
        """Test that data persists across instances"""
        self.tracker.add_reading(heart_rate=75)
        
        # Create new tracker instance with same file
        new_tracker = HeartHealthTracker(data_file=self.test_file)
        readings = new_tracker.get_readings()
        
        self.assertEqual(len(readings), 1)
        self.assertEqual(readings[0]["heart_rate"], 75)


if __name__ == "__main__":
    unittest.main()
