import os
from unittest.mock import patch

from hn_search.feed.lenses import load_settings
from tests.feed_helpers import CONFIG, TOKEN, FeedCase


class LensTests(FeedCase):
    def test_defaults_digest_ignores_order_and_tracks_descriptions(self):
        self.config.write_text(CONFIG + 'evals = "Model evaluations"\n')
        first = self.settings()
        self.assertEqual((first.model, first.effort), ("gpt-6-luna", "high"))
        self.config.write_text(CONFIG.replace('agents = "AI agents, agent frameworks, and tool use"',
                                            'evals = "Model evaluations"\nagents = "AI agents, agent frameworks, and tool use"'))
        self.assertEqual(first.lenses[0].categories_digest, self.settings().lenses[0].categories_digest)
        self.config.write_text(self.config.read_text().replace("Model evaluations", "Language model benchmarks"))
        self.assertNotEqual(first.lenses[0].categories_digest, self.settings().lenses[0].categories_digest)
        self.assertNotIn(TOKEN, repr(first))

    def test_invalid_config_fails_before_requests_or_database_creation(self):
        variants = [
            ("[bad", ""),
            (CONFIG.replace('name = "ai-agents"', 'name = "Uppercase"'), "lens.name"),
            (CONFIG + CONFIG, "Repeated lens"),
            (CONFIG.split("[lens.categories]")[0], "categories"),
            (CONFIG.replace("123456789", '"123456789"'), "chat_id"),
            (CONFIG.replace("123456789", "true"), "chat_id"),
            (CONFIG.replace("[lens.categories]", "min_points = 9\n[lens.categories]"), "min_points"),
            (CONFIG.replace("agents =", "Bad_name ="), "category name"),
            ('[classifier]\neffort = "magic"\n' + CONFIG, "effort"),
            ('[classifier]\nprompt = "extra"\n' + CONFIG, "prompt"),
            ("bad = true\n" + CONFIG, "bad"),
        ]
        for text, error in variants:
            with self.subTest(text=text):
                self.config.write_text(text)
                with self.assertRaises(ValueError) as raised:
                    self.run_feed()
                self.assertIn(error, str(raised.exception))
                self.assertFalse(self.path.exists())

    def test_missing_token_names_variable_without_value(self):
        with patch.dict(os.environ, {}, clear=True), self.assertRaisesRegex(ValueError, "HN_FEED_TEST_TOKEN") as raised:
            load_settings(self.config, os.environ)
        self.assertNotIn(TOKEN, str(raised.exception))
