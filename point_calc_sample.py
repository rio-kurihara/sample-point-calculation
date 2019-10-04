import sys

from lib import util_point_calc
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.tile import TilesConverter

sys.path.append('./')


def main(config, agari_info):
    # ライブラリに渡す用に整形
    p2l = util_point_calc.PiName2IntList()
    list_man, list_pin, list_sou, list_honors = \
        p2l.pinames2list(agari_info['list_pi_name'])

    calculator = HandCalculator()

    # we had to use all 14 tiles in that array
    tiles = TilesConverter.string_to_136_array(
        man=list_man, pin=list_pin, sou=list_sou, honors=list_honors)

    win_tile = p2l.piname2int(agari_info['win_pi'])
    dora_indicators = [p2l.piname2int(x) for x in agari_info['dora_pi']]

    # 鳴き牌
    if len(agari_info['list_meld_pi']) == 0:
        result = calculator.estimate_hand_value(
            tiles, win_tile, dora_indicators=dora_indicators, config=config)
    else:
        melds = p2l.get_melds(agari_info['list_meld_pi'])
        result = calculator.estimate_hand_value(
            tiles, win_tile, melds=melds, dora_indicators=dora_indicators, config=config)

    if result.error is not None:
        result_dict = result.error
    else:
        rc = util_point_calc.ResultConverter(result)
        result_dict = rc.result2dict(
            config.is_tsumo, agari_info['list_meld_pi'])
    return result_dict


if __name__ == "__main__":
    # Test
    import test_lists
    for x in test_lists.test_list:
        result_dict = main(x[0], x[1])
        print(result_dict)
