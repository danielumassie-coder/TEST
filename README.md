# TEST

## Heartwise - Heart Health Tracker

A simple Python application for tracking heart health metrics including heart rate and blood pressure.

### Features

- Track heart rate readings
- Record blood pressure measurements
- Add notes to readings
- View reading history
- Calculate statistics (average, min, max heart rate)
- Data persistence using JSON storage

### Quick Start

```bash
# Run the application
python3 heartwise.py

# Run tests
python3 test_heartwise.py
```

### Usage

The application provides an interactive CLI with the following options:

1. **Add new reading** - Record heart rate, blood pressure, and notes
2. **View recent readings** - Display reading history
3. **View statistics** - See heart health statistics
4. **Exit** - Close the application

### Example

```python
from heartwise import HeartHealthTracker

# Create tracker instance
tracker = HeartHealthTracker()

# Add a reading
tracker.add_reading(heart_rate=72, blood_pressure="120/80", notes="Morning reading")

# Get statistics
stats = tracker.get_stats()
print(f"Average heart rate: {stats['average_heart_rate']:.1f} bpm")
```

---

## PhD Documentation System

This repository also includes a systematic approach for extracting and organizing PhD-relevant content from all documentation.

### Quick Start

1. **Review the extraction guide**: See [PHD_EXTRACTION_GUIDE.md](PHD_EXTRACTION_GUIDE.md) for detailed instructions on how to extract PhD-relevant content from documentation.

2. **Check the documentation index**: View [DOCUMENTATION_INDEX.md](DOCUMENTATION_INDEX.md) to see all available documentation files and their review status.

3. **Access research notes**: All extracted PhD-relevant content is organized in [PHD_RESEARCH_NOTES.md](PHD_RESEARCH_NOTES.md).

### Files

- **PHD_RESEARCH_NOTES.md** - Central repository for all PhD-relevant content extracted from documentation
- **DOCUMENTATION_INDEX.md** - Inventory of all documentation files with relevance ratings and review status
- **PHD_EXTRACTION_GUIDE.md** - Step-by-step guide for systematically extracting PhD-relevant content

### Workflow

1. Identify new documentation files
2. Add them to the DOCUMENTATION_INDEX.md
3. Review each file following the PHD_EXTRACTION_GUIDE.md
4. Extract relevant content into PHD_RESEARCH_NOTES.md
5. Update review status in DOCUMENTATION_INDEX.md

### Current Status

- ✅ Documentation system established
- ✅ README.md reviewed
- ⏳ Awaiting additional documentation for review

---

For questions or suggestions about the PhD documentation system, please create an issue.