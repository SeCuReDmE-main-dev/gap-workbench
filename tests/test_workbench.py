import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from workbench.lint import lint  # noqa: E402
from workbench.subsidy import compare, load, subsidy  # noqa: E402


class Subsidy(unittest.TestCase):
    def test_cold_climate_pays_2_4_times_energy_star(self):
        self.assertEqual(subsidy("energy-star", 24000), 1200)
        self.assertEqual(subsidy("cold-climate", 24000), 2880)

    def test_geothermal_cap_is_18000(self):
        self.assertEqual(subsidy("geothermal", 24000), 18000)
        self.assertEqual(subsidy("geothermal", 72000), 18000)
        self.assertEqual(subsidy("geothermal-replacement", 36000), 9000)

    def test_compare_puts_the_best_first(self):
        self.assertEqual(compare(36000)[0][0], "geothermal")

    def test_bad_inputs(self):
        for bad in (-1, 300000, 1.5):
            with self.assertRaises(ValueError):
                subsidy("cold-climate", bad)
        with self.assertRaises(ValueError):
            subsidy("solar", 1000)

    def test_every_measure_is_sourced_and_positive(self):
        rules = load()
        self.assertTrue(rules["source"].startswith("https://"))
        for m in rules["measures"]:
            self.assertGreater(m["per_1000_btuh"], 0)


class Lint(unittest.TestCase):
    def test_flags_negation_and_long_opening(self):
        text = "## 6. Money\nWe will sign one partner later, not yet done.\n## 7. Opening\n" + "word " * 151
        issues = lint(text)
        self.assertTrue(any("negation" in i for i in issues))
        self.assertTrue(any("151 words" in i for i in issues))

    def test_clean_text_passes(self):
        self.assertEqual(lint("## 1. Reader\nQuebec homeowners choosing a heat pump.\n"), [])


if __name__ == "__main__":
    unittest.main()
