from __future__ import absolute_import
import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import relative_strength_index


class TestRelativeStrengthIndex(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.rsi_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, 91.128696376509808, 92.285403839188717, 80.894025017461274,
        70.592511652751313, 77.951770109884649, 80.239605929360266,
        70.277707266920117, 48.985014949691646, 52.57705771185794,
        29.56369140946228, 26.022225467384374, 16.324760280103618,
        21.03611935582866, 14.450447899471271, 14.399340568284714,
        37.838548007732264, 55.142917715980929, 50.59361566108123,
        43.932577726393127, 42.491462993376658, 51.948772620890892,
        51.609285637335049, 38.336269106131539, 54.530400068283633,
        45.780486043398241, 39.802974309817188, 23.233126351199488,
        46.011558572428697, 53.622238465968238, 69.105150494992742,
        71.943927752634877, 61.401768306657985, 44.82267986085872,
        45.738292422095121, 51.282952118549289, 63.529113661498116,
        66.172797931315301, 71.576348726382349, 68.569307930673602,
        71.64205694415736, 75.538772783985877, 79.336902977248528,
        60.902733049554506, 57.563547365591383, 63.029070885613358,
        54.405071613499608, 38.057877659724475, 36.069340676148251,
        35.551867201277034, 48.630430960266096, 45.463148398801508,
        53.123523689152051, 35.576818846625244, 39.779600801796533,
        37.488732721794584, 40.930916165630222, 37.139626791998928,
        46.260584259310058, 43.348151988222661, 59.382590313669397,
        60.591197175338664, 42.3532081852956, 62.815591971052257,
        64.047199117793127, 44.526399707555605, 37.867766944276163,
        32.926883858681308, 38.578727318762738, 45.537296891112497,
        31.423697245000028, 29.642545839858357, 49.557967472745197,
        36.771050674724215, 55.783922272827709, 60.850265479188977,
        60.881597670697779, 44.866787790759361, 38.850530452564023,
        37.156348420849575, 41.261293848032722, 48.819610310127324,
        44.263098553227302, 40.881844554211057, 46.731306039053081,
        53.854133357002794, 54.728745404768361, 61.325753528491738,
        67.792188074305614, 72.537957869691667, 56.664633742766149,
        66.56520901272998, 68.536344606136481, 70.721673114559167,
        71.324374049055464, 65.674281500057276, 54.197082940262945,
        60.461845412582441, 31.25312253767251, 37.503538994748723,
        42.046913819284043, 45.307280972084463, 25.306147643535695,
        10.512959368525003, 9.5014336746420298, 8.4166453804807304,
        8.3820873579604438, 14.111318591298641, 11.685025961279209,
        20.65996515862561, 17.694039794502245, 17.521324009591709,
        8.8490257823457767, 9.3698586066620919, 7.4665597738277256,
        17.148873648403978, 14.055923198144484, 10.156378730298115,
        7.4037283218177805, 12.053100590713569, 10.53811332066924,
        25.333373455819356]

        self.rsi_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, 83.74284752608537, 75.96946564885495,
        80.490137054219588, 81.983526674546667, 74.55846637012155,
        57.264837834932379, 59.501394660820722, 38.362259492388972,
        34.710619925495479, 23.945731338271358, 27.379877500246252,
        20.310320855359052, 20.253855087073887, 37.809698498673697,
        51.990703125851546, 48.582765106851404, 43.582541362843514,
        42.50916707089258, 49.601916414104501, 49.369883919182122,
        39.942200405447721, 52.024905041825861, 45.658135197528608,
        41.167452613422348, 27.233397029554069, 45.152340120725469,
        51.449547166103386, 65.039593582662647, 67.653150302178176,
        59.709613911194225, 46.565572793708569, 47.256610740681815,
        51.365100917086565, 60.897490376517084, 63.042323966087459,
        67.495584787282723, 65.434078964944788, 67.846384422099959,
        70.988436326409783, 74.200314568068876, 61.549503024941693,
        59.151584620311134, 62.866539861761467, 56.81042956236201,
        44.106947788205488, 42.448288369054524, 42.028967758173984,
        50.322846355738633, 48.074072207880782, 53.083971350819432,
        40.134731954707448, 42.93589935749435, 41.215459072106583,
        43.401066237392961, 40.727556785126616, 46.480811088913121,
        44.572874835377384, 55.484893235337545, 56.37126957702457,
        44.232367090010179, 59.439912681746065, 60.431643962144456,
        46.193449615658309, 40.898881381607907, 36.861327848228875,
        40.787483517743432, 45.666472255959192, 34.830534792309251,
        33.368585479985455, 47.880807749553838, 38.15728800508743,
        53.231675938448284, 57.479746680396758, 57.505443490007785,
        45.759020349263054, 41.056963100268781, 39.734701257792807,
        42.558210405522132, 47.821966983512596, 44.701022921450722,
        42.367504358881497, 46.211656127421485, 51.061411550381976,
        51.661135467303595, 56.255989673528305, 61.107043819371263,
        64.934729239492214, 55.11391303791622, 62.435681938638261,
        63.970519220630983, 65.66221548791998, 66.12066484831152,
        62.784212880382157, 55.636595393895853, 59.60733748851144,
        37.667545161264741, 41.885033057845654, 44.944174880919768,
        47.118093459179086, 30.8301816428866, 15.043559705306762,
        13.816478713123985, 12.514236683060346, 12.473802863884089,
        16.641092414477271, 14.463409950597409, 20.945479375484567,
        18.717292910371967, 18.587980971319979, 11.193518363714105,
        11.582457766777452, 9.7653340846728298, 16.90800205206591,
        14.594269077494857, 11.424620834757548, 8.945086851889954,
        12.473974212697996, 11.281727789650006, 22.415284637880248]

        self.rsi_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, 80.382399161864811,
        81.58297360799952, 75.721434246783815, 61.416457310356634,
        63.033041416747935, 44.113161156152088, 40.604396885470429,
        29.742114212280526, 32.422102432320955, 25.21394366994187,
        25.155236117171285, 39.143302960913552, 51.071910062341495,
        48.243694050081899, 44.089016517558669, 43.201607970756832,
        48.914054247164799, 48.732527235700935, 41.227053752801318,
        50.919606399372469, 45.826854315089811, 42.171708191280061,
        30.049752911709177, 44.909852138547663, 50.314889030321169,
        62.443899229961993, 64.851807409862261, 58.376274499138454,
        47.330458997163682, 47.900894356054458, 51.25369437632294,
        59.235604904143777, 61.070635039058558, 64.906801937622419,
        63.320673549928046, 65.343205295182088, 68.005029130114806,
        70.78431754824166, 61.190196581873671, 59.331226550164423,
        62.198342414125172, 57.572881550264221, 47.339736611786314,
        45.952135181740232, 45.607320085790207, 51.577755174521243,
        49.83880562787823, 53.482434731949304, 43.264888695398618,
        45.30903418461596, 43.93606152736691, 45.483853514142019,
        43.425935322167604, 47.459192056993352, 46.051586106621635,
        53.976794157654723, 54.645265825608782, 45.742583508406462,
        57.471387533431276, 58.277325091890276, 47.293233939087905,
        42.967147461659778, 39.601486397034741, 42.540543643550443,
        46.215041647309448, 37.428884268109378, 36.193678284783815,
        47.391170320790039, 39.50500571954332, 51.865056655425036,
        55.488977253711553, 55.51065657697405, 46.215140099782296,
        42.349549102920783, 41.262890464938629, 43.417280351603608,
        47.452054449078041, 45.071367075450659, 43.289342419501764,
        46.124569379604779, 49.753119249271819, 50.201807527824464,
        53.65083228388503, 57.413613311765189, 60.483698025569829,
        53.672576817758376, 59.400953966546119, 60.636758883775606,
        61.992968663776942, 62.35636887763178, 60.131501419424886,
        55.251850141024732, 58.105911946540154, 41.399935060427609,
        44.460837486574761, 46.684294876443616, 48.257083944192289,
        34.874539878819078, 19.177931796772313, 17.825060113615422,
        16.390929545473469, 16.346953960508898, 19.592095128093803,
        17.504375219974605, 22.53298531123572, 20.613919308674014,
        20.502900337132814, 13.662549952743703, 13.971111646021569,
        12.173903805406653, 17.806248012431396, 15.829536909459037,
        12.98760468233867, 10.621412075858444, 13.468704666819292,
        12.419802813127859, 21.359400151132036]

    def test_relative_strength_index_period_6(self):
        period = 6
        rsi = relative_strength_index.relative_strength_index(self.data, period)
        np.testing.assert_array_equal(rsi, self.rsi_period_6_expected)

    def test_relative_strength_index_period_8(self):
        period = 8
        rsi = relative_strength_index.relative_strength_index(self.data, period)
        np.testing.assert_array_equal(rsi, self.rsi_period_8_expected)

    def test_relative_strength_index_period_10(self):
        period = 10
        rsi = relative_strength_index.relative_strength_index(self.data, period)
        np.testing.assert_array_equal(rsi, self.rsi_period_10_expected)

    def test_relative_strength_index_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            relative_strength_index.relative_strength_index(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
