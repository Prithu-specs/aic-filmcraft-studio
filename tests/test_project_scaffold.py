"""Tests for the provider-neutral Filmcraft project scaffold."""
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "create_film_project.py"


class ProjectScaffoldTests(unittest.TestCase):
    def test_creates_same_scene_tree_and_provider_mapping(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "Night Courier", "--scene-count", "2",
                 "--provider", "sample-provider", "--root", tmp],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            project = Path(result.stdout.strip())
            manifest = json.loads((project / "00-admin/project-manifest.json").read_text())
            self.assertEqual(manifest["project_id"], "night-courier")
            self.assertEqual(manifest["scene_ids"], ["scene-01-unassigned", "scene-02-unassigned"])
            self.assertEqual(manifest["provider_adapter"], "sample-provider")
            self.assertTrue((project / "05-production/scene-01-unassigned/02-assets/asset-manifest.json").is_file())
            self.assertTrue((project / "05-production/scene-02-unassigned/07-ledger/attempt-ledger.csv").is_file())
            platform_map = json.loads((project / "04-platform/platform-map.json").read_text())
            self.assertIn("scene-01-unassigned", platform_map["scenes"])
            self.assertIn("scene-02-unassigned", platform_map["scenes"])

    def test_refuses_to_overwrite_existing_project(self):
        with tempfile.TemporaryDirectory() as tmp:
            first = subprocess.run(
                [sys.executable, str(SCRIPT), "Same Project", "--scene-count", "1", "--root", tmp],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(first.returncode, 0, first.stderr)
            second = subprocess.run(
                [sys.executable, str(SCRIPT), "Same Project", "--scene-count", "1", "--root", tmp],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(second.returncode, 2)
            self.assertIn("Refusing to overwrite", second.stderr)

    def test_rejects_invalid_scene_count(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = subprocess.run(
                [sys.executable, str(SCRIPT), "Bad", "--scene-count", "0", "--root", tmp],
                text=True, capture_output=True, check=False,
            )
            self.assertEqual(result.returncode, 2)
            self.assertIn("Scene count must be", result.stderr)
            self.assertFalse((Path(tmp) / "bad").exists())


if __name__ == "__main__":
    unittest.main()
