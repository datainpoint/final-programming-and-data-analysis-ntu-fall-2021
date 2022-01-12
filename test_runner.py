import unittest
import json
import ipynb.fs.full.exercises as ex
import numpy as np
import pandas as pd

class TestFinal(unittest.TestCase):
    def test_01_find_the_best_two_teams(self):
        best_team_in_west, best_team_in_east = ex.find_the_best_two_teams()
        self.assertIsInstance(best_team_in_west, dict)
        self.assertIsInstance(best_team_in_east, dict)
        self.assertEqual(best_team_in_west["teamId"], '1610612744')
        self.assertEqual(best_team_in_east["teamId"], '1610612741')
    def test_02_find_the_worst_two_teams(self):
        worst_team_in_west, worst_team_in_east = ex.find_the_worst_two_teams()
        self.assertIsInstance(worst_team_in_west, dict)
        self.assertIsInstance(worst_team_in_east, dict)
        self.assertEqual(worst_team_in_west["teamId"], '1610612745')
        self.assertEqual(worst_team_in_east["teamId"], '1610612753')
    def test_03_extract_current_standings(self):
        current_standings = ex.extract_current_standings()
        self.assertIsInstance(current_standings, pd.core.frame.DataFrame)
        self.assertEqual(current_standings.shape, (30, 7))
        win_equal = (current_standings['win'] == current_standings['homeWin'] + current_standings['awayWin']).sum()
        loss_equal = (current_standings['loss'] == current_standings['homeLoss'] + current_standings['awayLoss']).sum()
        self.assertEqual(win_equal, 30)
        self.assertEqual(loss_equal, 30)
    def test_04_find_the_best_and_worst_team_roster(self):
        the_best_and_worst_team_roster = ex.find_the_best_and_worst_team_roster()
        self.assertIsInstance(the_best_and_worst_team_roster, pd.core.frame.DataFrame)
        self.assertEqual(the_best_and_worst_team_roster.shape, (68, 5))
        self.assertIn("Orlando", the_best_and_worst_team_roster["city"].unique())
        self.assertIn("Houston", the_best_and_worst_team_roster["city"].unique())
        self.assertIn("Chicago", the_best_and_worst_team_roster["city"].unique())
        self.assertIn("Golden State", the_best_and_worst_team_roster["city"].unique())
        self.assertIn("Magic", the_best_and_worst_team_roster["nickname"].unique())
        self.assertIn("Rockets", the_best_and_worst_team_roster["nickname"].unique())
        self.assertIn("Bulls", the_best_and_worst_team_roster["nickname"].unique())
        self.assertIn("Warriors", the_best_and_worst_team_roster["nickname"].unique())
        self.assertIn("Worst in East", the_best_and_worst_team_roster["teamStanding"].unique())
        self.assertIn("Worst in West", the_best_and_worst_team_roster["teamStanding"].unique())
        self.assertIn("Best in East", the_best_and_worst_team_roster["teamStanding"].unique())
        self.assertIn("Best in West", the_best_and_worst_team_roster["teamStanding"].unique())
    def test_05_calculate_confirmed_death_rate_by_countries(self):
        confirmed_death_rate_by_countries = ex.calculate_confirmed_death_rate_by_countries()
        self.assertIsInstance(confirmed_death_rate_by_countries, pd.core.frame.DataFrame)
        self.assertEqual(confirmed_death_rate_by_countries.shape, (196, 6))
        taiwan = confirmed_death_rate_by_countries[confirmed_death_rate_by_countries["Country_Region"] == "Taiwan*"]
        self.assertEqual(taiwan.shape, (1, 6))
    def test_06_calculate_daily_cases(self):
        tw_daily_cases = ex.calculate_daily_cases("Taiwan*")
        self.assertIsInstance(type(tw_daily_cases), pd.core.frame.DataFrame)
        self.assertEqual(tw_daily_cases.shape, (720, 5))
        jp_daily_cases = ex.calculate_daily_cases("Japan")
        self.assertIsInstance(type(jp_daily_cases), pd.core.frame.DataFrame)
        self.assertEqual(jp_daily_cases.shape, (720, 5))
        us_daily_cases = ex.calculate_daily_cases("US")
        self.assertIsInstance(type(us_daily_cases), pd.core.frame.DataFrame)
        self.assertEqual(us_daily_cases.shape, (720, 5))
    def test_07_CountryCovidStatus(self):
        tw_covid_status = ex.CountryCovidStatus("Taiwan*")
        self.assertEqual(tw_covid_status.get_snapshot().shape, (1, 6))
        self.assertEqual(tw_covid_status.get_recent_two_week_trend().shape, (14, 5))
        jp_covid_status = ex.CountryCovidStatus("Japan")
        self.assertEqual(jp_covid_status.get_snapshot().shape, (1, 6))
        self.assertEqual(jp_covid_status.get_recent_two_week_trend().shape, (14, 5))
        us_covid_status = ex.CountryCovidStatus("US")
        self.assertEqual(us_covid_status.get_snapshot().shape, (1, 6))
        self.assertEqual(us_covid_status.get_recent_two_week_trend().shape, (14, 5))
    def test_08_import_all_sheets(self):
        all_sheets = ex.import_all_sheets()
        self.assertIsInstance(all_sheets, dict)
        self.assertEqual(len(all_sheets), 3)
        self.assertEqual(all_sheets["movies"].shape, (250, 6))
        self.assertEqual(all_sheets["casting"].shape, (3584, 3))
        self.assertEqual(all_sheets["actors"].shape, (3108, 2))
    def test_09_find_movie_by_actor_name(self):
        tom_hanks = ex.find_movie_by_actor_name("Tom Hanks")
        self.assertIsInstance(tom_hanks, pd.core.frame.DataFrame)
        self.assertEqual(tom_hanks.shape, (6, 6))
        leonard_dicaprio = ex.find_movie_by_actor_name("Leonardo DiCaprio")
        self.assertIsInstance(leonard_dicaprio, pd.core.frame.DataFrame)
        self.assertEqual(leonard_dicaprio.shape, (6, 6))
        tom_hanks_leonard_dicaprio = ex.find_movie_by_actor_name("Tom Hanks", "Leonardo DiCaprio")
        self.assertIsInstance(tom_hanks_leonard_dicaprio, pd.core.frame.DataFrame)
        self.assertEqual(tom_hanks_leonard_dicaprio.shape, (11, 6))
    def test_10_create_trilogy_dataframe(self):
        trilogy_dataframe = ex.create_trilogy_dataframe()
        self.assertIsInstance(trilogy_dataframe, pd.core.frame.DataFrame)
        self.assertEqual(trilogy_dataframe.shape, (90, 3))
        self.assertEqual(trilogy_dataframe["title"].nunique(), 6)
        self.assertEqual(trilogy_dataframe["director"].nunique(), 2)

suite = unittest.TestLoader().loadTestsFromTestCase(TestFinal)
runner = unittest.TextTestRunner(verbosity=2)
if __name__ == '__main__':
    test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))