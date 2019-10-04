import re
from mahjong.meld import Meld
import numpy as np

from mahjong.tile import TilesConverter


class PiName2IntList:
    def __init__(self):
        self.man_pttn = re.compile('^[1-9]m')
        self.pin_pttn = re.compile('^[1-9]p')
        self.sou_pttn = re.compile('^[1-9]s')
        self.honors_pttn = re.compile('^[a-z]$')
        self.dict_honors = {'e': 1, 's': 2,
                            'w': 3, 'n': 4, 'h': 5, 'f': 6, 'c': 7}

    def _get_int_list(self, pttn, list_pi_name):
        list_int_tmp = [pttn.findall(pi_name) for pi_name in list_pi_name]
        list_int = [pi_name[0][0:1]
                    for pi_name in list_int_tmp if len(pi_name) == 1]
        list_int = ''.join(list_int)
        return list_int

    def _get_int_list_honors(self, list_pi_name):
        list_int_tmp = [self.honors_pttn.findall(
            pi_name) for pi_name in list_pi_name]
        list_int = [pi_name[0][0:1]
                    for pi_name in list_int_tmp if len(pi_name) == 1]
        list_int = [str(self.dict_honors[i]) for i in list_int]
        list_int = ''.join(list_int)
        return list_int

    def pinames2list(self, list_pi_name):
        pttns = [self.man_pttn, self.pin_pttn, self.sou_pttn]
        list_man, list_pin, list_sou = [
            self._get_int_list(pttn, list_pi_name) for pttn in pttns]
        list_honors = self._get_int_list_honors(list_pi_name)
        return list_man, list_pin, list_sou, list_honors

    # 鳴きロジック　# TODO:チャンカン対応
    def get_melds(self, meld_pis):
        def _get_meld(meld_pi):
            melds_uq = np.unique(meld_pi)
            list_man, list_pin, list_sou, list_honors = self.pinames2list(
                meld_pi)

            if len(melds_uq) == 1:
                if len(meld_pi) == 3:
                    meld_type = Meld.PON
                elif len(meld_pi) == 4:
                    meld_type = Meld.KAN
                else:
                    raise ValueError(
                        '{} is unsupported melds tile.'.format(meld_pi))
            else:
                meld_type = Meld.CHI
            return meld_type, list_man, list_pin, list_sou, list_honors

        melds = []
        for dict_meld_pi in meld_pis:
            meld_type, list_man, list_pin, list_sou, list_honors = \
                _get_meld(dict_meld_pi['pis'])
            melds.extend([Meld(meld_type=meld_type,
                               tiles=TilesConverter.string_to_136_array(
                                   man=list_man,
                                   pin=list_pin,
                                   sou=list_sou,
                                   honors=list_honors),
                               opened=dict_meld_pi['opened']
                               )
                          ])
        return melds

    def piname2int(self, pi):
        if len(pi) == 2:
            if pi[1] == 's':
                pi = TilesConverter.string_to_136_array(sou=pi[0])[0]
            elif pi[1] == 'p':
                pi = TilesConverter.string_to_136_array(pin=pi[0])[0]
            elif pi[1] == 'm':
                pi = TilesConverter.string_to_136_array(man=pi[0])[0]
            else:
                raise ValueError('{} is unsupported tile.'.format(pi))
        elif len(pi) == 1:
            pi = TilesConverter.string_to_136_array(
                honors=[self.dict_honors[pi]])[0]
        else:
            raise ValueError('{} is unsupported tile.'.format(pi))
        return pi


class ResultConverter:
    def __init__(self, result):
        self.result = result

    def _get_han(self, yaku, list_meld_pi):
        if len(list_meld_pi) == 0 or not all([x['opened'] for x in list_meld_pi]):
            han = yaku.han_closed
        else:
            han = yaku.han_open
        return han

    def _update_dict(self, result_dict, list_meld_pi):
        han_by_yaku = [(x, self._get_han(x, list_meld_pi))
                       for x in self.result.yaku]
        for yaku_name, han in han_by_yaku:
            result_dict['han'][yaku_name] = han

        return result_dict

    def result2dict(self, is_tsumo, list_meld_pi):
        if is_tsumo:
            result_dict = {
                'oya_point': self.result.cost['main'],
                'ko_point': self.result.cost['additional'],
                'total_han': self.result.han,
                'han': {},
                'fu': self.result.fu
            }
        else:
            result_dict = {
                'oya_point': self.result.cost['main'],
                'ko_point': None,
                'total_han': self.result.han,
                'han': {},
                'fu': self.result.fu
            }
        result_dict = self._update_dict(result_dict, list_meld_pi)
        return result_dict
