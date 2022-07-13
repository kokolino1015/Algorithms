from main import Cat
import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat('test')

    def test_cat_increase_size_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cat_cant_eat_after_eating(self):
        self.cat.eat()
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_if_cat_cant_sleep_before_eat(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))
    def test_if_cat_is_sleepy_after_sleep(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy)


if __name__ == '__main__':
    unittest.main()
