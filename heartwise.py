#!/usr/bin/env python3
"""
Heartwise - A simple heart health monitoring application
"""

import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class HeartHealthTracker:
    """Main class for tracking heart health metrics"""
    
    def __init__(self, data_file: str = "heart_data.json"):
        self.data_file = data_file
        self.data = self._load_data()
    
    def _load_data(self) -> List[Dict]:
        """Load existing data from file"""
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return []
        return []
    
    def _save_data(self) -> None:
        """Save data to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.data, f, indent=2)
    
    def add_reading(self, heart_rate: int, blood_pressure: Optional[str] = None, 
                   notes: Optional[str] = None) -> Dict:
        """
        Add a new heart health reading
        
        Args:
            heart_rate: Heart rate in beats per minute
            blood_pressure: Blood pressure reading (e.g., "120/80")
            notes: Optional notes about the reading
        
        Returns:
            The created reading record
        """
        reading = {
            "timestamp": datetime.now().isoformat(),
            "heart_rate": heart_rate,
            "blood_pressure": blood_pressure,
            "notes": notes
        }
        self.data.append(reading)
        self._save_data()
        return reading
    
    def get_readings(self, limit: Optional[int] = None) -> List[Dict]:
        """
        Get all readings, optionally limited to most recent
        
        Args:
            limit: Number of most recent readings to return
        
        Returns:
            List of reading records
        """
        if limit:
            return self.data[-limit:]
        return self.data
    
    def get_average_heart_rate(self) -> Optional[float]:
        """Calculate average heart rate from all readings"""
        if not self.data:
            return None
        
        total = sum(reading["heart_rate"] for reading in self.data)
        return total / len(self.data)
    
    def get_stats(self) -> Dict:
        """Get statistics about heart health readings"""
        if not self.data:
            return {
                "total_readings": 0,
                "average_heart_rate": None,
                "min_heart_rate": None,
                "max_heart_rate": None
            }
        
        heart_rates = [reading["heart_rate"] for reading in self.data]
        
        return {
            "total_readings": len(self.data),
            "average_heart_rate": sum(heart_rates) / len(heart_rates),
            "min_heart_rate": min(heart_rates),
            "max_heart_rate": max(heart_rates)
        }


def main():
    """Main CLI interface"""
    tracker = HeartHealthTracker()
    
    print("=" * 50)
    print("Welcome to Heartwise - Heart Health Tracker")
    print("=" * 50)
    
    while True:
        print("\nOptions:")
        print("1. Add new reading")
        print("2. View recent readings")
        print("3. View statistics")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            try:
                heart_rate = int(input("Enter heart rate (bpm): "))
                blood_pressure = input("Enter blood pressure (optional, e.g., 120/80): ").strip()
                notes = input("Enter notes (optional): ").strip()
                
                reading = tracker.add_reading(
                    heart_rate=heart_rate,
                    blood_pressure=blood_pressure if blood_pressure else None,
                    notes=notes if notes else None
                )
                print(f"\n✓ Reading added at {reading['timestamp']}")
            except ValueError:
                print("\n✗ Invalid heart rate. Please enter a number.")
        
        elif choice == "2":
            try:
                limit = input("How many recent readings? (press Enter for all): ").strip()
                limit = int(limit) if limit else None
                readings = tracker.get_readings(limit)
                
                if not readings:
                    print("\nNo readings found.")
                else:
                    print(f"\n{'='*70}")
                    print(f"{'Timestamp':<20} {'Heart Rate':<12} {'Blood Pressure':<15} {'Notes'}")
                    print(f"{'='*70}")
                    for reading in readings:
                        timestamp = reading['timestamp'][:19]  # Remove microseconds
                        hr = f"{reading['heart_rate']} bpm"
                        bp = reading.get('blood_pressure') or '-'
                        notes = reading.get('notes') or '-'
                        print(f"{timestamp:<20} {hr:<12} {bp:<15} {notes}")
            except ValueError:
                print("\n✗ Invalid number.")
        
        elif choice == "3":
            stats = tracker.get_stats()
            print("\n" + "="*40)
            print("Heart Health Statistics")
            print("="*40)
            print(f"Total readings: {stats['total_readings']}")
            if stats['average_heart_rate']:
                print(f"Average heart rate: {stats['average_heart_rate']:.1f} bpm")
                print(f"Min heart rate: {stats['min_heart_rate']} bpm")
                print(f"Max heart rate: {stats['max_heart_rate']} bpm")
            else:
                print("No data available yet.")
        
        elif choice == "4":
            print("\nThank you for using Heartwise!")
            break
        
        else:
            print("\n✗ Invalid choice. Please enter 1-4.")


if __name__ == "__main__":
    main()
