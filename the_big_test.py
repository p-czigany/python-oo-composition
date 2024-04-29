import unittest

from boss import Boss
from has_name import HasName
from junior import Junior
from senior import Senior


class MyTestCase(unittest.TestCase):

    def test_boss_has_serfs(self):
        # arrange
        cole = HasName("Colbert Report")
        boss_bob = Boss("Robert Busy", cole)
        expected = cole

        # act
        actual = boss_bob.who_is_your_serf()

        # assert
        self.assertEqual(expected, actual)

    def test_junior_has_senior(self):
        # arrange
        bonola = HasName("Bonola Loffredo")
        junior_alice = Junior("Alice Inchains", bonola)
        expected = bonola

        # act
        actual = junior_alice.who_is_your_daddy()

        # assert
        self.assertEqual(expected, actual)

    def test_senior_has_serf(self):
        # arrange
        bob = HasName("Robert Busy")
        cole = HasName("Colbert Report")
        senior_bob = Senior("Robert Busy", cole, bob)
        expected = bob

        # act
        actual = senior_bob.who_is_your_serf()

        # assert
        self.assertEqual(expected, actual)

    def test_senior_has_senior(self):
        # arrange
        bob = HasName("Robert Busy")
        cole = HasName("Colbert Report")
        senior_bob = Senior("Robert Busy", cole, bob)
        expected = cole

        # act
        actual = senior_bob.who_is_your_daddy()

        # assert
        self.assertEqual(expected, actual)

    def test_inheritance_works_on_The_Boss(self):
        # arrange
        name = "Robert Busy"
        cole = HasName("Colbert Report")
        boss_bob = Boss(name, cole)
        expected = name

        # act
        actual = boss_bob.what_is_your_name()

        # assert
        self.assertEqual(expected, actual)

    def test_when_we_ask_the_name_of_a_junior_then_he_answers(self):
        # arrange
        name = "Dezső"
        my_junior = Junior(name, HasName("Főni"))
        expected = name

        # act
        actual = my_junior.what_is_your_name()

        # assert
        self.assertEqual(expected, actual)

    def test_when_we_ask_the_name_of_a_senior_then_he_answers(self):
        # arrange
        name = "Dezső"
        my_junior = Senior(name, HasName("Főni"), HasName("Csicska"))
        expected = name

        # act
        actual = my_junior.what_is_your_name()

        # assert
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
