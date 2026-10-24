"""Regressions for the public HTML parser: malformed data must never become zeros."""
import unittest
from unittest.mock import patch, Mock
from pathlib import Path
import datetime
import fetch_contributions as fetch
import build_profile as art

def calendar(tooltip='1 contribution'):
    start=datetime.date(2025, 10, 19)
    cells=[]
    for i in range(371):
        date=start+datetime.timedelta(days=i)
        cells.append(f'<td class="ContributionCalendar-day" id="d{i}" data-date="{date}" data-level="1"></td><tool-tip for="d{i}">{tooltip}</tool-tip>')
    return ''.join(cells)

class ParserTests(unittest.TestCase):
    def parse(self, html):
        with patch.object(fetch.requests, 'get', return_value=Mock(text=html)):
            return fetch.fetch_days()

    def test_counts_and_thousands(self):
        self.assertEqual(self.parse(calendar('1,234 contributions'))[0]['count'], 1234)
        self.assertEqual(self.parse(calendar('No contributions'))[0]['count'], 0)

    def test_missing_tooltip_fails_closed(self):
        with self.assertRaises(ValueError):
            self.parse(calendar('Calendar changed'))

    def test_incomplete_calendar_fails_closed(self):
        with self.assertRaises(ValueError):
            self.parse('<td class="ContributionCalendar-day" data-date="2026-10-24"></td>')

    def test_streak_does_not_count_empty_today(self):
        days=[{'date':'2026-10-23','count':2}, {'date':'2026-10-24','count':0}]
        self.assertEqual(fetch.compute_current_streak(days), (1,'2026-10-23','2026-10-23'))

if __name__ == '__main__':
    unittest.main()
