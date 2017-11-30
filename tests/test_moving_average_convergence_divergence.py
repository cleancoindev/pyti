from __future__ import absolute_import
import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import moving_average_convergence_divergence


class TestStandardVariance(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.macd_period_6_period_12_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        2.7330916437261976, 1.9752084449276026, 0.28489861686296081,
        -0.43901806349049366, -2.8323254378504998, -5.0185265681711826,
        -8.542389164178644, -9.8668992878021982, -11.940718734879283,
        -12.766685325756384, -10.365848920970961, -5.9988568174347847,
        -2.7610061066208118, -1.3965468953550726, -0.014796994450989587,
        2.0694822166211679, 2.6669600935603057, 1.0206013628395567,
        1.3351518731763008, 0.75688611991108701, -0.64753314017843877,
        -5.1603671883692641, -4.7030739786239337, -2.2731003655889026,
        2.6912432256771126, 6.6744206684292067, 7.4594085033218107,
        5.5584399376898546, 3.7292626833934719, 2.9076972675294428,
        3.9774410104337221, 4.5589887044490069, 6.2764539666637802,
        6.9079359733273122, 7.9077070177647784, 8.998728755620391,
        10.152488113772165, 8.5890174354948385, 6.2496106654776895,
        4.8643496144911751, 2.5330250493486801, -1.6154536136899651,
        -4.5697336562969895, -5.8199541288457795, -4.9103647765524556,
        -4.7833716062679059, -3.504553687722364, -3.8186259196990022,
        -3.06166496883543, -2.7939090744181385, -2.5303093163888661,
        -2.3297984823307161, -1.7625339791999295, -1.2682751507309149,
        0.09600728618067933, 1.0960977781371639, 0.56120109202004187,
        2.194589746762972, 3.245908195691527, 1.8899766895515313,
        -0.090299164988209668, -2.0692999024313394, -2.4555027276334158,
        -2.6814220218944911, -4.3870661493868965, -5.1237376013945095,
        -3.4189476686231046, -3.5280199812840465, -1.4614894542015691,
        0.81654592442191642, 2.7502181666093293, 2.0939329838561207,
        0.31859059681096369, -0.64881788629588755, -1.4104571649409081,
        -1.3966414955448272, -2.0254214763848495, -2.2799390038646834,
        -1.5585981024242983, -0.72989989383802367, 0.10087674048054396,
        1.0349412528433959, 2.2215267644170353, 3.1631985392447177,
        2.7566099631934549, 2.9293330230932497, 3.0569514516447498,
        3.1138578105827719, 2.8302867584027354, 2.1526291860873243,
        1.4504935468157782, 1.0307177965310075, -0.83981100875598713,
        -1.7338183328604373, -2.0118501749313964, -1.8972910034302686,
        -3.2169593455835184, -7.7271083067281552, -10.252745888979234,
        -11.958343859834031, -12.460749066883523, -11.94778810016544,
        -11.435671557863316, -8.9628332835274023, -7.4112842989063665,
        -5.7082142532883609, -6.7755665272891292, -6.8604855544505199,
        -7.2979731464128008, -7.2541118666791817, -7.5835575029062738,
        -8.9108944553156562, -10.116973472857012, -9.9541953682828535,
        -9.7135367824123477, -8.2234453078966681]

        self.macd_period_8_period_16_expected = [np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, -1.3162539905129051, -3.5589643396778001,
        -6.6468158284825449, -8.5419377933840224, -11.300735561407237,
        -12.896232600029634, -12.000048665319696, -9.4347983125483097,
        -7.3100622276219838, -6.1751973164587071, -4.8168509718806263,
        -2.8614710343068737, -0.80246194622327494, -0.25827103704966703,
        1.0248472956704973, 0.82621114062101242, 0.032350903937754083,
        -2.9959748961307469, -2.9540803119009524, -1.9983127943504542,
        1.4872600675569174, 4.8282090435536702, 5.6081056492757853,
        3.891771858736206, 2.8807473360916447, 3.557173305482479,
        5.4354694337007459, 6.9603772699570072, 8.1347959925748228,
        7.9946082747653691, 8.644002043035357, 10.181654117336734,
        11.705406909918565, 10.38921888471873, 8.5303795470990735,
        7.5567441977746057, 6.0268594345852762, 3.1890845306658093,
        0.52072048665900184, -2.0739258849731641, -3.2928175213949089,
        -4.010356738371911, -3.5914474679511841, -5.0051322028151617,
        -5.2580677844124466, -5.061620483225056, -4.3991142372063905,
        -3.9122974984435359, -3.0644751150657612, -2.6144957833257649,
        -1.4859449539270599, 0.0015168731961239246, -0.028984050351709811,
        1.3049033428892471, 2.2332244651028077, 1.5753673669764794,
        0.47932110877866307, -0.77472023424627423, -1.4459643837209342,
        -1.728643386528347, -2.8954496220776491, -4.2850554591677792,
        -3.969255887361328, -4.6176076721264963, -2.9807262360614004,
        -1.0163438798711013, 0.43862607017058508, 0.030449268186657719,
        -0.64937478614388056, -0.9503638377907464, -1.1043513640321407,
        -0.48593532097220304, -0.88490027549516981, -1.636758007611661,
        -1.8370680110078865, -1.1634635156129889, -0.61932413216277382,
        0.11313436670138799, 1.0959546318792945, 1.7676433084419614,
        1.9950119612949493, 2.87352144439933, 3.5217902243446133,
        3.7641654621068028, 3.7549809432213124, 3.3844224208402238,
        2.6615444200652973, 2.2364297858268856, 0.77741394315296475,
        -0.2743514657470314, -0.89906081481592537, -1.2446421699432904,
        -2.6572702228741036, -6.5941697707436333, -9.4863800949095776,
        -11.762030123505269, -12.781289719803112, -12.886679438662441,
        -13.200348488365648, -12.725657191037158, -12.143274266298931,
        -10.522398244741453, -10.991482084131349, -10.648431808966848,
        -10.868057521370702, -10.235990376295831, -9.8228020650484495,
        -10.307487410385647, -11.508865572968716, -12.130736032815093,
        -12.146432665244674, -11.16990255153371]

        self.macd_period_10_period_20_expected = [np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
        -9.3510987321908488, -11.481561538741403, -11.675560755091851,
        -10.204597597959605, -9.0426736038627951, -8.6542515622219298,
        -7.9095851272228401, -6.4402574550654208, -4.7284729401343384,
        -4.2542630806233319, -2.3694213907235735, -1.3382274140785739,
        -1.1876618394392153, -3.555525704792899, -3.3318895533857358,
        -2.014215290281868, 1.4251284553831738, 4.4039250649744872,
        5.3335886047939312, 4.0937765003485538, 2.7275842111515658,
        2.4055843836556505, 4.0960266106873178, 6.5409569177755884,
        8.7225339216416842, 9.6784689551305974, 9.9601337405936192,
        10.477423682709286, 11.602246927500232, 11.479213793719964,
        11.052780800329401, 10.833646719154444, 9.3472806007747522,
        6.0875027902354759, 3.1947742183220953, 1.0064826061415033,
        0.27992671361153043, -0.61419381766995684, -1.2013027211322651,
        -3.0327300276834421, -4.1300951046210912, -5.2236898165339198,
        -5.4791248681809748, -5.3777609066814875, -4.6264727739544469,
        -4.1098478038708208, -3.0252499667919892, -1.9169659333550726,
        -1.8424725807616369, -0.26031760500370638, 0.97419863728873679,
        0.96329201204559922, 0.3563771354012033, -0.63708007069953965,
        -1.2233075198216738, -1.2763617810660435, -2.4610909605212328,
        -3.5160951978048161, -2.9329817162091558, -4.0005633893456434,
        -3.3172599300802403, -1.9930761385335245, -0.81419283780155638,
        -0.9456273112909912, -1.5778514767800971, -2.2700523563127035,
        -2.1177675517296848, -1.4665005666710158, -1.5648339423555626,
        -1.3168415651889518, -1.1997809365294643, -1.0658104719661878,
        -0.99898633568750483, -0.43495688101006635, 0.48871740771164696,
        1.540718462742575, 1.681898972775798, 2.093890742881058,
        2.6758673289742774, 3.0905897712896149, 3.5138608776975389,
        3.6823548562355199, 3.5394016557726218, 3.3298752795999462,
        1.9731352789137873, 0.97245722295417636, 0.44301307615273799,
        0.023635734440176748, -1.3434609199487113, -4.9788864186062938,
        -7.9896204956727388, -10.478282465507959, -12.111872722315638,
        -12.965012604508615, -13.558244754189332, -13.487658548009449,
        -13.647213499338591, -13.498558292260327, -14.609095561117329,
        -14.380671453926539, -14.365532870884181, -13.569443127350155,
        -13.170461737722803, -13.483363581811318, -14.409837221095927,
        -14.609174792788281, -14.676099492783123, -13.790585278138337]

    def test_macd_period_6_period_12(self):
        short_period = 6
        long_period = 12
        macd = moving_average_convergence_divergence.moving_average_convergence_divergence(self.data, short_period, long_period)
        np.testing.assert_array_equal(macd, self.macd_period_6_period_12_expected)

    def test_macd_period_8_period_16(self):
        short_period = 8
        long_period = 16
        macd = moving_average_convergence_divergence.moving_average_convergence_divergence(self.data, short_period, long_period)
        np.testing.assert_array_equal(macd, self.macd_period_8_period_16_expected)

    def test_macd_period_10_period_20(self):
        short_period = 10
        long_period = 20
        macd = moving_average_convergence_divergence.moving_average_convergence_divergence(self.data, short_period, long_period)
        np.testing.assert_array_equal(macd, self.macd_period_10_period_20_expected)

    def test_macd_invalid_period_short(self):
        short_period = 128
        long_period = 1
        with self.assertRaises(Exception) as cm:
            moving_average_convergence_divergence.moving_average_convergence_divergence(self.data, short_period, long_period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)

    def test_macd_invalid_period_long(self):
        short_period = 1
        long_period = 128
        with self.assertRaises(Exception) as cm:
            moving_average_convergence_divergence.moving_average_convergence_divergence(self.data, short_period, long_period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
