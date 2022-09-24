from unittest import TestCase
import utils


class TestCleanName(TestCase):
    def test_clean_name(self):
        titre_1 = '7 peter fonDa462 579'
        titre_2 = ' 7 pETEr t  fOnDA462 57.9 - 4 - - 67Go  '
        titre_3 = ' 7 PETER t 3 FONdA462 57.9 - 4 - - 67Mo'
        res = 'Peter Fonda'
        titre_1 = utils.clean_name(titre_1)
        titre_2 = utils.clean_name(titre_2)
        titre_3 = utils.clean_name(titre_3)
        self.assertEqual(titre_1, res)
        self.assertEqual(titre_2, res)
        self.assertEqual(titre_3, res)

