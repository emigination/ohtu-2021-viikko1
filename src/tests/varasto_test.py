import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ei_voi_laittaa_liikaa_tavaraa(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ei_voi_ottaa_enemman_kuin_on(self):
        self.varasto.lisaa_varastoon(2)
        saatu_maara = self.varasto.ota_varastosta(3)
        self.assertEqual(saatu_maara, 2)

    def test_ei_negatiivista_tilavuutta(self):
        varasto = Varasto(-1)
        self.assertEqual(varasto.tilavuus, 0)

    def test_ei_negatiivista_alkusaldoa(self):
        varasto = Varasto(1, -1)
        self.assertEqual(varasto.saldo, 0)

    def test_ei_tilavuutta_suurempaa_alkusaldoa(self):
        varasto = Varasto(1, 2)
        self.assertEqual(varasto.saldo, 1)

    def test_negatiivinen_lisays_ei_vaikuta(self):
        self.varasto.lisaa_varastoon(2)
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 2)

    def test_negatiivinen_otto_ei_vaikuta(self):
        self.varasto.lisaa_varastoon(2)
        self.varasto.ota_varastosta(-1)
        self.assertEqual(self.varasto.saldo, 2)

    def test_merkkijono_oikein(self):
        merkkijono = str(self.varasto)
        self.assertEqual(merkkijono, 'saldo = 0, vielä tilaa 10')
