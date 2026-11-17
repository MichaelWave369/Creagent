"""Regression tests for the Creagent TOE knowledge graph."""

import importlib.util
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "skills" / "creagent-toe" / "scripts" / "explore.py"
spec = importlib.util.spec_from_file_location("creagent_explore", SCRIPT)
explore = importlib.util.module_from_spec(spec)
spec.loader.exec_module(explore)


class OntologyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.graph = explore.load_graph()

    def test_valid(self):
        self.assertEqual(explore.validate(self.graph), [])

    def test_color_order(self):
        self.assertEqual([x["label"] for x in self.graph["layers"]],
                         ["Reality", "Dreamspace", "Limbo", "Quantum", "Astral"])

    def test_moon_sun_inward_outward_route(self):
        route = explore.find_path(self.graph, "moon", "sun")
        self.assertEqual([x["from"] for x in route] + [route[-1]["to"]],
                         ["moon", "viewer", "sun"])
        self.assertTrue(all(x["epistemic"] == "model-inference" for x in route))

    def test_upward_route(self):
        route = explore.find_path(self.graph, "viewer", "one")
        labels = [x["from"] for x in route] + [route[-1]["to"]]
        self.assertEqual(labels, ["viewer", "yggdrasil", "eden", "one"])

    def test_bardo_astral_relationship_is_source(self):
        edges = [e for e in self.graph["edges"] if e["source"] == "bardo" and e["target"] == "astral"]
        self.assertEqual(len(edges), 1)
        self.assertEqual(edges[0]["type"], "boundary-to")
        self.assertEqual(edges[0]["epistemic"], "source")

    def test_unknown_node(self):
        with self.assertRaises(ValueError):
            explore.find_path(self.graph, "moon", "unicorn")

    def test_invalid_edge_rejected(self):
        clone = {**self.graph, "edges": [*self.graph["edges"],
                 {"source": "missing", "target": "sun", "type": "nonsense", "epistemic": "source", "note": "bad"}]}
        self.assertTrue(any("unknown node" in err for err in explore.validate(clone)))


if __name__ == "__main__":
    unittest.main()