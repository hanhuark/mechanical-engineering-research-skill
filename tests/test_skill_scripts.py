from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LATEX_AUDIT = ROOT / "skills" / "mechanical-engineering-research" / "scripts" / "audit_latex_project.py"
MANIFEST_AUDIT = ROOT / "skills" / "mechanical-engineering-research" / "scripts" / "audit_data_manifest.py"
STYLE_AUDIT = ROOT / "skills" / "mechanical-engineering-research" / "scripts" / "audit_style_calibration.py"
TECHNICAL_WRITING_AUDIT = (
    ROOT / "skills" / "mechanical-engineering-research" / "scripts" / "audit_technical_writing.py"
)


class SkillScriptTests(unittest.TestCase):
    def test_latex_audit_accepts_consistent_project(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            (project / "figure.png").write_bytes(b"not-a-real-image-but-present")
            (project / "refs.bib").write_text(
                "@article{smith2024, title={Example}, author={Smith, A.}, year={2024}}\n",
                encoding="utf-8",
            )
            (project / "main.tex").write_text(
                r"\documentclass{article}\begin{document}\section{Test}\label{sec:test}"
                r"See Section~\ref{sec:test} and Smith et al.~\cite{smith2024}."
                r"\includegraphics{figure}\bibliography{refs}\end{document}",
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(LATEX_AUDIT), str(project), "--json"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn('"smith2024"', result.stdout)

    def test_latex_audit_flags_missing_citation_key(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            project = Path(folder)
            (project / "refs.bib").write_text("", encoding="utf-8")
            (project / "main.tex").write_text(
                r"\documentclass{article}\begin{document}\cite{missing}\bibliography{refs}\end{document}",
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(LATEX_AUDIT), str(project)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 1)
            self.assertIn("citation key missing from bibliography: missing", result.stdout)

    def test_data_manifest_verifies_checksum(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder)
            artifact = base / "data.csv"
            artifact.write_text("x,y\n1,2\n", encoding="utf-8")
            checksum = hashlib.sha256(artifact.read_bytes()).hexdigest()
            manifest = base / "manifest.csv"
            fields = [
                "artifact_id",
                "path_or_url",
                "evidence_class",
                "source_id",
                "version",
                "units",
                "schema_or_format",
                "transformation",
                "license",
                "redistribution",
                "checksum",
            ]
            with manifest.open("w", encoding="utf-8", newline="") as handle:
                writer = csv.DictWriter(handle, fieldnames=fields)
                writer.writeheader()
                writer.writerow(
                    {
                        "artifact_id": "baseline",
                        "path_or_url": "data.csv",
                        "evidence_class": "measured",
                        "source_id": "test-run-1",
                        "version": "1",
                        "units": "SI; see schema",
                        "schema_or_format": "CSV",
                        "transformation": "none; raw fixture",
                        "license": "test-only",
                        "redistribution": "allowed for test",
                        "checksum": checksum,
                    }
                )
            result = subprocess.run(
                [sys.executable, str(MANIFEST_AUDIT), str(manifest), "--verify-checksums"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Rows: 1", result.stdout)

    def test_style_calibration_audit_accepts_minimal_corpus_and_lints_draft(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "calibration-profile.md").write_text("# Profile\n", encoding="utf-8")
            case = root / "case"
            case.mkdir()
            (root / "corpus-index.json").write_text(
                '{"cases":[{"id":"case-1","relative_case_path":"case","items":[{"id":"P1","status":"verified accepted-after"}]}]}',
                encoding="utf-8",
            )
            draft = root / "draft.md"
            draft.write_text("Fig. 2(a) proves the new panel is novel.", encoding="utf-8")
            result = subprocess.run(
                [sys.executable, str(STYLE_AUDIT), str(root), "--draft", str(draft)],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn("Style-calibration corpus audit passed.", result.stdout)
            self.assertIn("avoid 'panel'", result.stdout)

    def test_technical_writing_audit_reports_lazy_terms_and_dash_forms(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            draft = Path(folder) / "draft.md"
            draft.write_text(
                "The method enables imaging and enabled direct comparison. "
                "This establishes the result unusually quickly. Taken together, "
                "the flow-boiling data support the claim—without a stated baseline. "
                "The tested range was 10 – 20 kPa.",
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(TECHNICAL_WRITING_AUDIT), str(draft), "--json"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(report["lazy_term_counts"]["enable"], 2)
            self.assertEqual(report["lazy_term_counts"]["establish"], 1)
            self.assertEqual(report["lazy_term_counts"]["unusually"], 1)
            self.assertEqual(report["lazy_term_counts"]["together"], 1)
            self.assertEqual(report["dash_forms"]["unspaced_em_dash"], 1)
            self.assertEqual(report["dash_forms"]["spaced_en_dash"], 1)
            self.assertIn("flow-boiling", report["hyphenated_compounds"])

    def test_technical_writing_audit_flags_reader_focus_candidates(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            draft = Path(folder) / "draft.md"
            draft.write_text(
                "# A Critical Review of Physics-Grounded Sensing, Measurement, Diagnostics, and AI-Enabled Interpretation\n\n"
                "The experimentally validated, physics-grounded, stage-resolved framework combines optical, acoustic, "
                "and thermal measurements to provide an integrated characterization of the transient boiling process "
                "across multiple operating conditions, surface states, and diagnostic configurations.\n",
                encoding="utf-8",
            )
            result = subprocess.run(
                [sys.executable, str(TECHNICAL_WRITING_AUDIT), str(draft), "--json"],
                capture_output=True,
                text=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            report = json.loads(result.stdout)
            self.assertEqual(len(report["reader_focus"]["crowded_headings"]), 1)
            self.assertEqual(len(report["reader_focus"]["comma_heavy_sentences"]), 1)
            self.assertEqual(len(report["reader_focus"]["stacked_modifier_sentences"]), 1)


if __name__ == "__main__":
    unittest.main()
