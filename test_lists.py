from mahjong.constants import CHUN, EAST, HAKU, HATSU, NORTH, SOUTH, WEST
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules

option_config = OptionalRules(
    # ,kazoe_limit = HandConstants.KAZOE_LIMITED
    has_open_tanyao=False,
    has_aka_dora=False,
    has_double_yakuman=True,
    kiriage=False,
    fu_for_open_pinfu=True,
    fu_for_pinfu_tsumo=False,
    renhou_as_yakuman=False,
    has_daisharin=False,
    has_daisharin_other_suits=False
)


test_list = 
    # Case1
    [
        HandConfig(
            is_tsumo=True,
            is_riichi=False,
            is_ippatsu=False,
            is_rinshan=False,
            is_chankan=False,
            is_haitei=False,
            is_houtei=False,
            is_daburu_riichi=False,
            is_nagashi_mangan=False,
            is_tenhou=False,
            is_renhou=False,
            is_chiihou=False,
            player_wind=None,
            round_wind=None,
            options=option_config
        ),
        {
            'list_pi_name': ['3m', '3m', '6m', '7m', '4p', '5p',
                             '6p', '9p', '9p', '9p', '5s', '6s', '7s', '8m'],
            'win_pi': '8m',
            'dora_pi': ['2m'],
            'list_meld_pi': []
        }],
    # Case2
    [
        HandConfig(
            is_tsumo=True,
            is_riichi=False,
            is_ippatsu=False,
            is_rinshan=False,
            is_chankan=False,
            is_haitei=False,
            is_houtei=False,
            is_daburu_riichi=False,
            is_nagashi_mangan=False,
            is_tenhou=False,
            is_renhou=False,
            is_chiihou=False,
            player_wind=WEST,
            round_wind=SOUTH,
            options=option_config
        ),
        {
            'list_pi_name': ['4s', '4s', '4s', '1m', '2m', '3m', '4m', '5m', '6m', '8p', '8p', 's', 's', 's'],
            'win_pi': '4m',
            'dora_pi': ['9s'],
            'list_meld_pi': [{'pis': ['1m', '2m', '3m'],
                              'opened': True},
                             {'pis': ['s', 's', 's'],
                              'opened': True},
                             {'pis': ['4s', '4s', '4s'],
                              'opened': True}
                             ]
        }],
    # Case3
    [
        HandConfig(
            is_tsumo=False,
            is_riichi=False,
            is_ippatsu=False,
            is_rinshan=False,
            is_chankan=False,
            is_haitei=False,
            is_houtei=False,
            is_daburu_riichi=False,
            is_nagashi_mangan=False,
            is_tenhou=False,
            is_renhou=False,
            is_chiihou=False,
            player_wind=NORTH,
            round_wind=SOUTH,
            options=option_config
        ),
        {
            'list_pi_name': ['3s', '4s', '5s', '2m', '2m', '2m', '7p', '7p', '9p', '9p', '9p', 'h', 'h', 'h'],
            'win_pi': 'h',
            'dora_pi': ['2p', '1s'],
            'list_meld_pi': [{'pis': ['9p', '9p', '9p', '9p'],
                              'opened': False},
                             {'pis': ['3s', '4s', '5s'],
                              'opened': True}
                             ]
        }],
    # Case4
    [
        HandConfig(
            is_tsumo=False,
            is_riichi=False,
            is_ippatsu=False,
            is_rinshan=False,
            is_chankan=False,
            is_haitei=False,
            is_houtei=False,
            is_daburu_riichi=False,
            is_nagashi_mangan=False,
            is_tenhou=False,
            is_renhou=False,
            is_chiihou=False,
            player_wind=NORTH,
            round_wind=SOUTH,
            options=option_config
        ),
        {
            'list_pi_name': ['7s', '7s', '8s', '8s', '9s', '9s', '3m', '4m', '5m', '7m', '7m', '7m', 'f', 'f'],
            'win_pi': '9s',
            'dora_pi': ['6s', '3p'],
            'list_meld_pi': [{'pis': ['7m', '7m', '7m', '7m'],
                              'opened': False}
                             ]
        }],
    # Case5
    [
        HandConfig(
            is_tsumo=True,
            is_riichi=False,
            is_ippatsu=False,
            is_rinshan=False,
            is_chankan=False,
            is_haitei=False,
            is_houtei=False,
            is_daburu_riichi=False,
            is_nagashi_mangan=False,
            is_tenhou=False,
            is_renhou=False,
            is_chiihou=False,
            player_wind=EAST,
            round_wind=SOUTH,
            options=option_config
        ),
        {
            'list_pi_name': ['4s', '4s', '4s', '5s', '5s', '2m', '2m', '2m', 'c', 'c', 'c', 'h', 'h', 'h'],
            'win_pi': '4s',
            'dora_pi': ['3m', '7m', '6s', '6m'],
            'list_meld_pi': [{'pis': ['h', 'h', 'h', 'h'],
                              'opened': False}
                             ]
        }],
]
