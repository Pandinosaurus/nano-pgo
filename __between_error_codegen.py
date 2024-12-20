# -----------------------------------------------------------------------------
# This file was autogenerated by symforce from template:
#     function/FUNCTION.py.jinja
# Do NOT modify by hand.
# -----------------------------------------------------------------------------

# pylint: disable=too-many-locals,too-many-lines,too-many-statements,unused-argument,unused-import

import math
import typing as T

import numpy

import sym


def sf_between_error_with_jacobians01(Ti, Tj, Tij):
    # type: (sym.Pose3, sym.Pose3, sym.Pose3) -> T.Tuple[sym.Pose3, numpy.ndarray, numpy.ndarray]
    """
    This function was autogenerated from a symbolic function. Do not modify by hand.

    Symbolic function: sf_between_error

    Args:
        Ti: Pose3
        Tj: Pose3
        Tij: Pose3

    Outputs:
        res: Pose3
        res_D_Ti: (6x6) jacobian of res (6) wrt arg Ti (6)
        res_D_Tj: (6x6) jacobian of res (6) wrt arg Tj (6)
    """

    # Total ops: 651

    # Input arrays
    _Ti = Ti.data
    _Tj = Tj.data
    _Tij = Tij.data

    # Intermediate terms (215)
    _tmp0 = _Ti[3] * _Tj[3]
    _tmp1 = _Ti[0] * _Tj[0]
    _tmp2 = _Ti[2] * _Tj[2]
    _tmp3 = _Ti[1] * _Tj[1]
    _tmp4 = _tmp0 + _tmp1 + _tmp2 + _tmp3
    _tmp5 = _Ti[3] * _Tj[0]
    _tmp6 = _Ti[0] * _Tj[3]
    _tmp7 = _Ti[1] * _Tj[2]
    _tmp8 = _Ti[2] * _Tj[1]
    _tmp9 = _tmp5 - _tmp6 - _tmp7 + _tmp8
    _tmp10 = _Ti[2] * _Tj[0]
    _tmp11 = _Ti[1] * _Tj[3]
    _tmp12 = _Ti[0] * _Tj[2]
    _tmp13 = _Ti[3] * _Tj[1]
    _tmp14 = -_tmp10 - _tmp11 + _tmp12 + _tmp13
    _tmp15 = _Ti[1] * _Tj[0]
    _tmp16 = _Ti[2] * _Tj[3]
    _tmp17 = _Ti[3] * _Tj[2]
    _tmp18 = _Ti[0] * _Tj[1]
    _tmp19 = _tmp15 - _tmp16 + _tmp17 - _tmp18
    _tmp20 = -_Tij[0] * _tmp4 - _Tij[1] * _tmp19 + _Tij[2] * _tmp14 + _Tij[3] * _tmp9
    _tmp21 = _Tij[0] * _tmp19 - _Tij[1] * _tmp4 - _Tij[2] * _tmp9 + _Tij[3] * _tmp14
    _tmp22 = -_Tij[0] * _tmp14 + _Tij[1] * _tmp9 - _Tij[2] * _tmp4 + _Tij[3] * _tmp19
    _tmp23 = _Tij[0] * _tmp9 + _Tij[1] * _tmp14 + _Tij[2] * _tmp19 + _Tij[3] * _tmp4
    _tmp24 = -2 * _Tij[1] ** 2
    _tmp25 = 1 - 2 * _Tij[2] ** 2
    _tmp26 = _tmp24 + _tmp25
    _tmp27 = _Ti[2] ** 2
    _tmp28 = 2 * _tmp27
    _tmp29 = -_tmp28
    _tmp30 = _Ti[1] ** 2
    _tmp31 = 2 * _tmp30
    _tmp32 = 1 - _tmp31
    _tmp33 = _tmp29 + _tmp32
    _tmp34 = 2 * _Ti[2]
    _tmp35 = _Ti[0] * _tmp34
    _tmp36 = 2 * _Ti[1]
    _tmp37 = _Ti[3] * _tmp36
    _tmp38 = -_tmp37
    _tmp39 = _tmp35 + _tmp38
    _tmp40 = _Ti[6] * _tmp39
    _tmp41 = _Ti[3] * _tmp34
    _tmp42 = _Ti[0] * _tmp36
    _tmp43 = _tmp41 + _tmp42
    _tmp44 = _Ti[5] * _tmp43
    _tmp45 = _Tj[5] * _tmp43 + _Tj[6] * _tmp39
    _tmp46 = -_Ti[4] * _tmp33 + _Tj[4] * _tmp33 - _tmp40 - _tmp44 + _tmp45
    _tmp47 = 2 * _Tij[2]
    _tmp48 = _Tij[3] * _tmp47
    _tmp49 = 2 * _Tij[0]
    _tmp50 = _Tij[1] * _tmp49
    _tmp51 = _tmp48 + _tmp50
    _tmp52 = _Ti[0] ** 2
    _tmp53 = 2 * _tmp52
    _tmp54 = -_tmp53
    _tmp55 = _tmp29 + _tmp54 + 1
    _tmp56 = _Ti[2] * _tmp36
    _tmp57 = 2 * _Ti[0] * _Ti[3]
    _tmp58 = _tmp56 + _tmp57
    _tmp59 = _Ti[6] * _tmp58
    _tmp60 = -_tmp41
    _tmp61 = _tmp42 + _tmp60
    _tmp62 = _Ti[4] * _tmp61
    _tmp63 = _Tj[4] * _tmp61 + _Tj[6] * _tmp58
    _tmp64 = -_Ti[5] * _tmp55 + _Tj[5] * _tmp55 - _tmp59 - _tmp62 + _tmp63
    _tmp65 = _Tij[2] * _tmp49
    _tmp66 = 2 * _Tij[1] * _Tij[3]
    _tmp67 = _tmp65 - _tmp66
    _tmp68 = _tmp32 + _tmp54
    _tmp69 = -_tmp57
    _tmp70 = _tmp56 + _tmp69
    _tmp71 = _Ti[5] * _tmp70
    _tmp72 = _tmp35 + _tmp37
    _tmp73 = _Ti[4] * _tmp72
    _tmp74 = _Tj[4] * _tmp72 + _Tj[5] * _tmp70
    _tmp75 = -_Ti[6] * _tmp68 + _Tj[6] * _tmp68 - _tmp71 - _tmp73 + _tmp74
    _tmp76 = -_tmp48 + _tmp50
    _tmp77 = -2 * _Tij[0] ** 2
    _tmp78 = _tmp25 + _tmp77
    _tmp79 = _Tij[1] * _tmp47
    _tmp80 = _Tij[3] * _tmp49
    _tmp81 = _tmp79 + _tmp80
    _tmp82 = _tmp65 + _tmp66
    _tmp83 = _tmp79 - _tmp80
    _tmp84 = _tmp24 + _tmp77 + 1
    _tmp85 = (1.0 / 2.0) * _tmp5
    _tmp86 = (1.0 / 2.0) * _tmp6
    _tmp87 = (1.0 / 2.0) * _tmp7
    _tmp88 = (1.0 / 2.0) * _tmp8
    _tmp89 = _tmp85 - _tmp86 - _tmp87 + _tmp88
    _tmp90 = -_Tij[1] * _tmp89
    _tmp91 = (1.0 / 2.0) * _tmp1
    _tmp92 = (1.0 / 2.0) * _tmp0
    _tmp93 = (1.0 / 2.0) * _tmp2
    _tmp94 = (1.0 / 2.0) * _tmp3
    _tmp95 = -_tmp91 - _tmp92 - _tmp93 - _tmp94
    _tmp96 = _Tij[2] * _tmp95
    _tmp97 = (1.0 / 2.0) * _tmp15
    _tmp98 = (1.0 / 2.0) * _tmp16
    _tmp99 = (1.0 / 2.0) * _tmp17
    _tmp100 = (1.0 / 2.0) * _tmp18
    _tmp101 = -_tmp100 + _tmp97 - _tmp98 + _tmp99
    _tmp102 = _Tij[3] * _tmp101
    _tmp103 = (1.0 / 2.0) * _tmp10
    _tmp104 = (1.0 / 2.0) * _tmp11
    _tmp105 = (1.0 / 2.0) * _tmp12
    _tmp106 = (1.0 / 2.0) * _tmp13
    _tmp107 = _tmp103 + _tmp104 - _tmp105 - _tmp106
    _tmp108 = _Tij[0] * _tmp107
    _tmp109 = _tmp102 + _tmp108
    _tmp110 = _tmp109 + _tmp90 - _tmp96
    _tmp111 = 2 * _tmp22
    _tmp112 = _Tij[3] * _tmp89
    _tmp113 = _Tij[0] * _tmp95
    _tmp114 = _Tij[1] * _tmp101
    _tmp115 = _Tij[2] * _tmp107
    _tmp116 = _tmp114 + _tmp115
    _tmp117 = _tmp112 + _tmp113 + _tmp116
    _tmp118 = 2 * _tmp20
    _tmp119 = -_Tij[0] * _tmp101
    _tmp120 = _Tij[1] * _tmp95
    _tmp121 = _Tij[3] * _tmp107
    _tmp122 = _Tij[2] * _tmp89
    _tmp123 = _tmp119 + _tmp120 + _tmp121 - _tmp122
    _tmp124 = 2 * _tmp21
    _tmp125 = _Tij[2] * _tmp101
    _tmp126 = _Tij[3] * _tmp95
    _tmp127 = -_Tij[1] * _tmp107
    _tmp128 = _Tij[0] * _tmp89
    _tmp129 = _tmp125 + _tmp126 + _tmp127 - _tmp128
    _tmp130 = 2 * _tmp23
    _tmp131 = -_tmp30
    _tmp132 = _Ti[3] ** 2
    _tmp133 = -_tmp52
    _tmp134 = _tmp131 + _tmp132 + _tmp133 + _tmp27
    _tmp135 = -_Ti[6] * _tmp134 + _Tj[6] * _tmp134 - _tmp71 - _tmp73 + _tmp74
    _tmp136 = -_tmp56
    _tmp137 = _tmp136 + _tmp69
    _tmp138 = _tmp131 + _tmp52
    _tmp139 = -_tmp132
    _tmp140 = _tmp139 + _tmp27
    _tmp141 = _tmp138 + _tmp140
    _tmp142 = -_tmp42
    _tmp143 = _tmp142 + _tmp41
    _tmp144 = (
        -_Ti[4] * _tmp143
        - _Ti[5] * _tmp141
        - _Ti[6] * _tmp137
        + _Tj[4] * _tmp143
        + _Tj[5] * _tmp141
        + _Tj[6] * _tmp137
    )
    _tmp145 = -_tmp103 - _tmp104 + _tmp105 + _tmp106
    _tmp146 = _Tij[3] * _tmp145
    _tmp147 = _tmp100 - _tmp97 + _tmp98 - _tmp99
    _tmp148 = _Tij[0] * _tmp147
    _tmp149 = _tmp122 + _tmp148
    _tmp150 = _tmp120 + _tmp146 + _tmp149
    _tmp151 = _Tij[1] * _tmp145
    _tmp152 = -_Tij[2] * _tmp147
    _tmp153 = _tmp128 + _tmp152
    _tmp154 = _tmp126 - _tmp151 + _tmp153
    _tmp155 = -_Tij[2] * _tmp145
    _tmp156 = _Tij[1] * _tmp147
    _tmp157 = _tmp112 + _tmp156
    _tmp158 = -_tmp113 + _tmp155 + _tmp157
    _tmp159 = _Tij[3] * _tmp147
    _tmp160 = _Tij[0] * _tmp145
    _tmp161 = _tmp159 - _tmp160 + _tmp90 + _tmp96
    _tmp162 = -_tmp27
    _tmp163 = _tmp132 + _tmp162
    _tmp164 = _tmp138 + _tmp163
    _tmp165 = -_Ti[4] * _tmp164 + _Tj[4] * _tmp164 - _tmp40 - _tmp44 + _tmp45
    _tmp166 = _tmp136 + _tmp57
    _tmp167 = -_tmp35
    _tmp168 = _tmp167 + _tmp38
    _tmp169 = _tmp139 + _tmp162 + _tmp30 + _tmp52
    _tmp170 = (
        -_Ti[4] * _tmp168
        - _Ti[5] * _tmp166
        - _Ti[6] * _tmp169
        + _Tj[4] * _tmp168
        + _Tj[5] * _tmp166
        + _Tj[6] * _tmp169
    )
    _tmp171 = -_tmp85 + _tmp86 + _tmp87 - _tmp88
    _tmp172 = _Tij[2] * _tmp171
    _tmp173 = _tmp146 + _tmp172
    _tmp174 = _tmp119 - _tmp120 + _tmp173
    _tmp175 = _Tij[1] * _tmp171
    _tmp176 = _tmp160 + _tmp175
    _tmp177 = _tmp102 + _tmp176 + _tmp96
    _tmp178 = -_Tij[0] * _tmp171
    _tmp179 = _tmp151 + _tmp178
    _tmp180 = -_tmp125 + _tmp126 + _tmp179
    _tmp181 = _Tij[3] * _tmp171
    _tmp182 = _tmp113 - _tmp114 + _tmp155 + _tmp181
    _tmp183 = _tmp167 + _tmp37
    _tmp184 = _tmp133 + _tmp30
    _tmp185 = _tmp140 + _tmp184
    _tmp186 = _tmp142 + _tmp60
    _tmp187 = (
        -_Ti[4] * _tmp185
        - _Ti[5] * _tmp186
        - _Ti[6] * _tmp183
        + _Tj[4] * _tmp185
        + _Tj[5] * _tmp186
        + _Tj[6] * _tmp183
    )
    _tmp188 = _tmp163 + _tmp184
    _tmp189 = -_Ti[5] * _tmp188 + _Tj[5] * _tmp188 - _tmp59 - _tmp62 + _tmp63
    _tmp190 = _tmp28 - 1
    _tmp191 = _tmp190 + _tmp31
    _tmp192 = _tmp190 + _tmp53
    _tmp193 = _tmp31 + _tmp53 - 1
    _tmp194 = _tmp91 + _tmp92 + _tmp93 + _tmp94
    _tmp195 = _Tij[1] * _tmp194
    _tmp196 = _tmp121 + _tmp195
    _tmp197 = _tmp119 - _tmp172 + _tmp196
    _tmp198 = _Tij[0] * _tmp194
    _tmp199 = _tmp181 + _tmp198
    _tmp200 = _tmp116 + _tmp199
    _tmp201 = _Tij[2] * _tmp194
    _tmp202 = _tmp109 - _tmp175 - _tmp201
    _tmp203 = _Tij[3] * _tmp194
    _tmp204 = _tmp127 + _tmp203
    _tmp205 = _tmp125 + _tmp178 + _tmp204
    _tmp206 = _tmp153 + _tmp204
    _tmp207 = -_tmp115 + _tmp157 - _tmp198
    _tmp208 = _tmp149 + _tmp196
    _tmp209 = _tmp159 + _tmp201
    _tmp210 = -_tmp108 + _tmp209 + _tmp90
    _tmp211 = -_tmp148 + _tmp173 - _tmp195
    _tmp212 = _tmp155 - _tmp156 + _tmp199
    _tmp213 = _tmp152 + _tmp179 + _tmp203
    _tmp214 = _tmp176 + _tmp209

    # Output terms
    _res = [0.0] * 7
    _res[0] = _tmp20
    _res[1] = _tmp21
    _res[2] = _tmp22
    _res[3] = _tmp23
    _res[4] = (
        -_Tij[4] * _tmp26
        - _Tij[5] * _tmp51
        - _Tij[6] * _tmp67
        + _tmp26 * _tmp46
        + _tmp51 * _tmp64
        + _tmp67 * _tmp75
    )
    _res[5] = (
        -_Tij[4] * _tmp76
        - _Tij[5] * _tmp78
        - _Tij[6] * _tmp81
        + _tmp46 * _tmp76
        + _tmp64 * _tmp78
        + _tmp75 * _tmp81
    )
    _res[6] = (
        -_Tij[4] * _tmp82
        - _Tij[5] * _tmp83
        - _Tij[6] * _tmp84
        + _tmp46 * _tmp82
        + _tmp64 * _tmp83
        + _tmp75 * _tmp84
    )
    _res_D_Ti = numpy.zeros((6, 6))
    _res_D_Ti[0, 0] = (
        _tmp110 * _tmp111 - _tmp117 * _tmp118 - _tmp123 * _tmp124 + _tmp129 * _tmp130
    )
    _res_D_Ti[1, 0] = (
        _tmp110 * _tmp130 - _tmp111 * _tmp129 - _tmp117 * _tmp124 + _tmp118 * _tmp123
    )
    _res_D_Ti[2, 0] = (
        -_tmp110 * _tmp118 - _tmp111 * _tmp117 + _tmp123 * _tmp130 + _tmp124 * _tmp129
    )
    _res_D_Ti[3, 0] = _tmp135 * _tmp51 + _tmp144 * _tmp67
    _res_D_Ti[4, 0] = _tmp135 * _tmp78 + _tmp144 * _tmp81
    _res_D_Ti[5, 0] = _tmp135 * _tmp83 + _tmp144 * _tmp84
    _res_D_Ti[0, 1] = (
        _tmp111 * _tmp154 - _tmp118 * _tmp150 - _tmp124 * _tmp158 + _tmp130 * _tmp161
    )
    _res_D_Ti[1, 1] = (
        -_tmp111 * _tmp161 + _tmp118 * _tmp158 - _tmp124 * _tmp150 + _tmp130 * _tmp154
    )
    _res_D_Ti[2, 1] = (
        -_tmp111 * _tmp150 - _tmp118 * _tmp154 + _tmp124 * _tmp161 + _tmp130 * _tmp158
    )
    _res_D_Ti[3, 1] = _tmp165 * _tmp67 + _tmp170 * _tmp26
    _res_D_Ti[4, 1] = _tmp165 * _tmp81 + _tmp170 * _tmp76
    _res_D_Ti[5, 1] = _tmp165 * _tmp84 + _tmp170 * _tmp82
    _res_D_Ti[0, 2] = (
        _tmp111 * _tmp182 - _tmp118 * _tmp177 - _tmp124 * _tmp180 + _tmp130 * _tmp174
    )
    _res_D_Ti[1, 2] = (
        -_tmp111 * _tmp174 + _tmp118 * _tmp180 - _tmp124 * _tmp177 + _tmp130 * _tmp182
    )
    _res_D_Ti[2, 2] = (
        -_tmp111 * _tmp177 - _tmp118 * _tmp182 + _tmp124 * _tmp174 + _tmp130 * _tmp180
    )
    _res_D_Ti[3, 2] = _tmp187 * _tmp51 + _tmp189 * _tmp26
    _res_D_Ti[4, 2] = _tmp187 * _tmp78 + _tmp189 * _tmp76
    _res_D_Ti[5, 2] = _tmp187 * _tmp83 + _tmp189 * _tmp82
    _res_D_Ti[0, 3] = 0
    _res_D_Ti[1, 3] = 0
    _res_D_Ti[2, 3] = 0
    _res_D_Ti[3, 3] = _tmp143 * _tmp51 + _tmp168 * _tmp67 + _tmp191 * _tmp26
    _res_D_Ti[4, 3] = _tmp143 * _tmp78 + _tmp168 * _tmp81 + _tmp191 * _tmp76
    _res_D_Ti[5, 3] = _tmp143 * _tmp83 + _tmp168 * _tmp84 + _tmp191 * _tmp82
    _res_D_Ti[0, 4] = 0
    _res_D_Ti[1, 4] = 0
    _res_D_Ti[2, 4] = 0
    _res_D_Ti[3, 4] = _tmp166 * _tmp67 + _tmp186 * _tmp26 + _tmp192 * _tmp51
    _res_D_Ti[4, 4] = _tmp166 * _tmp81 + _tmp186 * _tmp76 + _tmp192 * _tmp78
    _res_D_Ti[5, 4] = _tmp166 * _tmp84 + _tmp186 * _tmp82 + _tmp192 * _tmp83
    _res_D_Ti[0, 5] = 0
    _res_D_Ti[1, 5] = 0
    _res_D_Ti[2, 5] = 0
    _res_D_Ti[3, 5] = _tmp137 * _tmp51 + _tmp183 * _tmp26 + _tmp193 * _tmp67
    _res_D_Ti[4, 5] = _tmp137 * _tmp78 + _tmp183 * _tmp76 + _tmp193 * _tmp81
    _res_D_Ti[5, 5] = _tmp137 * _tmp83 + _tmp183 * _tmp82 + _tmp193 * _tmp84
    _res_D_Tj = numpy.zeros((6, 6))
    _res_D_Tj[0, 0] = (
        _tmp111 * _tmp202 - _tmp118 * _tmp200 - _tmp124 * _tmp197 + _tmp130 * _tmp205
    )
    _res_D_Tj[1, 0] = (
        -_tmp111 * _tmp205 + _tmp118 * _tmp197 - _tmp124 * _tmp200 + _tmp130 * _tmp202
    )
    _res_D_Tj[2, 0] = (
        -_tmp111 * _tmp200 - _tmp118 * _tmp202 + _tmp124 * _tmp205 + _tmp130 * _tmp197
    )
    _res_D_Tj[3, 0] = 0
    _res_D_Tj[4, 0] = 0
    _res_D_Tj[5, 0] = 0
    _res_D_Tj[0, 1] = (
        _tmp111 * _tmp206 - _tmp118 * _tmp208 - _tmp124 * _tmp207 + _tmp130 * _tmp210
    )
    _res_D_Tj[1, 1] = (
        -_tmp111 * _tmp210 + _tmp118 * _tmp207 - _tmp124 * _tmp208 + _tmp130 * _tmp206
    )
    _res_D_Tj[2, 1] = (
        -_tmp111 * _tmp208 - _tmp118 * _tmp206 + _tmp124 * _tmp210 + _tmp130 * _tmp207
    )
    _res_D_Tj[3, 1] = 0
    _res_D_Tj[4, 1] = 0
    _res_D_Tj[5, 1] = 0
    _res_D_Tj[0, 2] = (
        _tmp111 * _tmp212 - _tmp118 * _tmp214 - _tmp124 * _tmp213 + _tmp130 * _tmp211
    )
    _res_D_Tj[1, 2] = (
        -_tmp111 * _tmp211 + _tmp118 * _tmp213 - _tmp124 * _tmp214 + _tmp130 * _tmp212
    )
    _res_D_Tj[2, 2] = (
        -_tmp111 * _tmp214 - _tmp118 * _tmp212 + _tmp124 * _tmp211 + _tmp130 * _tmp213
    )
    _res_D_Tj[3, 2] = 0
    _res_D_Tj[4, 2] = 0
    _res_D_Tj[5, 2] = 0
    _res_D_Tj[0, 3] = 0
    _res_D_Tj[1, 3] = 0
    _res_D_Tj[2, 3] = 0
    _res_D_Tj[3, 3] = _tmp26 * _tmp33 + _tmp51 * _tmp61 + _tmp67 * _tmp72
    _res_D_Tj[4, 3] = _tmp33 * _tmp76 + _tmp61 * _tmp78 + _tmp72 * _tmp81
    _res_D_Tj[5, 3] = _tmp33 * _tmp82 + _tmp61 * _tmp83 + _tmp72 * _tmp84
    _res_D_Tj[0, 4] = 0
    _res_D_Tj[1, 4] = 0
    _res_D_Tj[2, 4] = 0
    _res_D_Tj[3, 4] = _tmp26 * _tmp43 + _tmp51 * _tmp55 + _tmp67 * _tmp70
    _res_D_Tj[4, 4] = _tmp43 * _tmp76 + _tmp55 * _tmp78 + _tmp70 * _tmp81
    _res_D_Tj[5, 4] = _tmp43 * _tmp82 + _tmp55 * _tmp83 + _tmp70 * _tmp84
    _res_D_Tj[0, 5] = 0
    _res_D_Tj[1, 5] = 0
    _res_D_Tj[2, 5] = 0
    _res_D_Tj[3, 5] = _tmp26 * _tmp39 + _tmp51 * _tmp58 + _tmp67 * _tmp68
    _res_D_Tj[4, 5] = _tmp39 * _tmp76 + _tmp58 * _tmp78 + _tmp68 * _tmp81
    _res_D_Tj[5, 5] = _tmp39 * _tmp82 + _tmp58 * _tmp83 + _tmp68 * _tmp84
    return sym.Pose3.from_storage(_res), _res_D_Ti, _res_D_Tj
