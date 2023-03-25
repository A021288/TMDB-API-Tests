import requests
from unittest import TestCase
import random

from config import BASE_URI, API_KEY, VALID_LANGUAGES


class TestTopRatedMoviesTopLevelResponse(TestCase):
    def setUp(self):
        self.resource_url = BASE_URI + "movie/top_rated"
        self.payload = {
            "api_key": API_KEY,
            "page": 1
        }

    def test_success_status_code(self):
        response = requests.get(self.resource_url, params=self.payload)
        self.assertEqual(response.status_code, 200)

    def test_invalid_api_key(self):
        self.payload["api_key"] = None
        response = requests.get(self.resource_url, params=self.payload)
        resp_json = response.json()
        self.assertEqual(response.status_code, 401)
        self.assertEqual(resp_json["status_message"], "Invalid API key: You must be granted a valid key.")
        self.assertFalse(resp_json["success"])

    def test_complete_object(self):
        response = requests.get(self.resource_url, params=self.payload)
        resp_json = response.json()
        self.assertIsInstance(resp_json["results"], list)

        self.assertIsInstance(resp_json["page"], int)
        self.assertGreaterEqual(resp_json["page"], 0)

        self.assertIsInstance(resp_json["total_pages"], int)
        self.assertGreaterEqual(resp_json["total_pages"], 0)

        self.assertIsInstance(resp_json["total_results"], int)
        self.assertGreaterEqual(resp_json["total_results"], 0)


class TestSingleMovieObject(TestCase):
    def setUp(self):
        self.resource_url = BASE_URI + "movie/top_rated"
        self.payload = {
            "api_key": API_KEY,
            "page": 1
        }
        response = requests.get(self.resource_url, params=self.payload)
        resp_json = response.json()
        # Pick any random movie object from the list.
        self.random_movie_object = resp_json.get("results", [])[random.randrange(0, 19, 2)]

    def test_adult_key(self):
        # adult must be present
        self.assertIsInstance(self.random_movie_object["adult"], bool)
        # adult must be of type boolean
        self.assertIn("id", self.random_movie_object.keys())

    def test_id_key(self):
        # id must be present
        self.assertIn("id", self.random_movie_object.keys())
        # id must be of type integer
        self.assertIsInstance(self.random_movie_object["id"], int)
        # id must be greater than 0
        self.assertGreater(self.random_movie_object["id"], 0)

    def test_backdrop_path(self):
        # backdrop_path must be present
        self.assertIn("backdrop_path", self.random_movie_object.keys())
        # id must be of type stringing
        self.assertIsInstance(self.random_movie_object["backdrop_path"], str)

    def test_genre_ids(self):
        # genre_ids must be present
        self.assertIn("genre_ids", self.random_movie_object.keys())
        # genre_ids must be of type stringing
        self.assertIsInstance(self.random_movie_object["genre_ids"], list)
        # genre_ids length must be greater than zero
        self.assertGreater(len(self.random_movie_object["genre_ids"]), 0)

    def test_original_language(self):
        # original_language must be present
        self.assertIn("original_language", self.random_movie_object.keys())
        # original_language must be of type stringing
        self.assertIsInstance(self.random_movie_object["original_language"], str)
        # original_language must be a valid language
        self.assertIn(self.random_movie_object["original_language"], VALID_LANGUAGES)

    def test_original_title(self):
        # original_title must be present
        self.assertIn("original_title", self.random_movie_object.keys())
        # original_title must be of type stringing
        self.assertIsInstance(self.random_movie_object["original_title"], str)

    def test_popularity(self):
        # popularity must be present
        self.assertIn("popularity", self.random_movie_object.keys())
        # popularity must be of type float
        self.assertIsInstance(self.random_movie_object["popularity"], float)

    def test_poster_path(self):
        # poster_path must be present
        self.assertIn("poster_path", self.random_movie_object.keys())
        # poster_path must be of type string
        self.assertIsInstance(self.random_movie_object["poster_path"], str)

    def test_release_date(self):
        # release_date must be present
        self.assertIn("release_date", self.random_movie_object.keys())
        # release_date must be of type string
        self.assertIsInstance(self.random_movie_object["release_date"], str)

    def test_title(self):
        # title must be present
        self.assertIn("title", self.random_movie_object.keys())
        # title must be of type string
        self.assertIsInstance(self.random_movie_object["title"], str)

    def test_video(self):
        # video must be present
        self.assertIn("video", self.random_movie_object.keys())
        # video must be of type boolean
        self.assertIsInstance(self.random_movie_object["video"], bool)

    def test_vote_average(self):
        # vote_average must be present
        self.assertIn("vote_average", self.random_movie_object.keys())
        # vote_average must be of type float
        self.assertIsInstance(self.random_movie_object["vote_average"], float)
        # vote_average must be of type float
        self.assertGreaterEqual(self.random_movie_object["vote_average"], 0)
        self.assertLessEqual(self.random_movie_object["vote_average"], 10)
