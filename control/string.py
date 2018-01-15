# **coding: utf-8**
"""
从机-主机通讯码
"""

"""
步骤完成码
"""
RESET_FINISHED = 0b1000110000000000             # 复位完成
MATERIAL_FINISHED = 0b1001110000000000          # 取料完成
PRINTING_FINISHED = 0b1010110000000000          # 打印完成
BALE_FINISHED = 0b1011110000000000              # 包装完成


"""
运行状态码
"""
READY_STATE = 0b00                              # 就绪状态
RUNNING_STATE = 0b01                            # 执行状态
FINISHED_STATE = 0b10                           # 完成状态
EXCEPTION_STATE = 0b11                          # 异常状态


"""
步骤码
"""
RESET_STEP = 0b00                               # 复位
MATERIAL_STEP = 0b01                            # 取料
PRINTING_STEP = 0b10                            # 打印
BALE_STEP = 0b11                                # 包装


"""
复位活动码
"""
START_RESET_ACTIVE = 0b00                       # 开始复位
ROBOT_RESET_FINISHED_ACTIVE = 0b01              # 工业机器人复位
PRINTING_RESET_FINISHED_ACTIVE = 0b10           # 打印机复位
FINISHED_RESET_ACTIVE = 0b11                    # 复位完毕


"""
取料活动码
"""
START_MATERIAL_ACTIVE = 0b00                    # 开始取料
TAKE_PHONE_CASE_ACTIVE = 0b01                   # 取出手机壳
CLEAR_PHONE_CASE_ACTIVE = 0b10                  # 清理手机壳
FINISHED_MATERIAL_ACTIVE = 0b11                 # 取料完毕


"""
打印活动码
"""
READY_PRINTING_ACTIVE = 0b00                    # 准备打印
START_PRINTING_ACTIVE = 0b01                    # 开始打印
RUNNING_PRINTING_ACTIVE = 0b10                  # 打印中
FINISHED_PRINTING_ACTIVE = 0b11                 # 打印完毕


"""
包装活动码
"""
START_BALE_ACTIVE = 0b00                        # 开始包装
PUT_INTI_PHONE_CASE_ACTIVE = 0b01               # 放入手机壳
PASTE_WAYBILL_ACTIVE = 0b10                     # 贴货运单
FINISHED_BALE_ACTIVE = 0b11                     # 包装完毕


class ResolveData(object):

    """
    解析得到的字符串
    """

    def __init__(self, code):
        self.code = code

    def get_state(self):
        state = (0xC000 & self.code) >> 14
        semantic = ''
        msg = ''
        if READY_STATE == state:
            semantic = 'READY_STATE'
            msg = u'准备状态'
        elif RUNNING_STATE == state:
            semantic = u'RUNNING_STATE'
            msg = u'运行状态'
        elif FINISHED_STATE == state:
            semantic = 'FINISHED_STATE'
            msg = u'完成状态'
        elif EXCEPTION_STATE == state:
            semantic = 'EXCEPTION_STATE'
            msg = u'异常状态'

        return bin(state), semantic, msg

    def get_step(self):
        step = (0x3000 & self.code) >> 12
        semantic = ''
        msg = ''
        if RESET_STEP == step:
            semantic = 'RESET_STEP'
            msg = u'复位'
        elif MATERIAL_STEP == step:
            semantic = u'MATERIAL_STEP'
            msg = u'上料'
        elif PRINTING_STEP == step:
            semantic = 'PRINTING_STEP'
            msg = u'打印'
        elif BALE_STEP == step:
            semantic = 'BALE_STEP'
            msg = u'包装'

        return bin(step), semantic, msg

    def get_active(self):
        step = (0x3000 & self.code) >> 12
        active = (0x0C00 & self.code) >> 10
        semantic = ''
        msg = ''
        if RESET_STEP == step:
            if START_RESET_ACTIVE == active:
                semantic = 'START_RESET_ACTIVE'
                msg = u'开始复位'
            elif ROBOT_RESET_FINISHED_ACTIVE == active:
                semantic = 'ROBOT_RESET_FINISHED_ACTIVE'
                msg = u'工业机器人复位'
            elif PRINTING_RESET_FINISHED_ACTIVE == active:
                semantic = 'PRINTING_RESET_FINISHED_ACTIVE'
                msg = u'打印机复位'
            elif FINISHED_RESET_ACTIVE == active:
                semantic = 'FINISHED_RESET_ACTIVE'
                msg = u'复位完成'
        elif MATERIAL_STEP == step:
            if START_MATERIAL_ACTIVE == active:
                semantic = 'START_MATERIAL_ACTIVE'
                msg = u'开始取料'
            elif TAKE_PHONE_CASE_ACTIVE == active:
                semantic = 'TAKE_PHONE_CASE_ACTIVE'
                msg = u'取出手机壳'
            elif CLEAR_PHONE_CASE_ACTIVE == active:
                semantic = 'CLEAR_PHONE_CASE_ACTIVE'
                msg = u'清理手机壳'
            elif FINISHED_MATERIAL_ACTIVE == active:
                semantic = 'FINISHED_MATERIAL_ACTIVE'
                msg = u'清理完毕'
        elif PRINTING_STEP == step:
            if READY_PRINTING_ACTIVE == active:
                semantic = 'READY_PRINTING_ACTIVE'
                msg = u'准备打印'
            elif START_PRINTING_ACTIVE == active:
                semantic = 'START_PRINTING_ACTIVE'
                msg = u'开始打印'
            elif RUNNING_PRINTING_ACTIVE == active:
                semantic = 'RUNNING_PRINTING_ACTIVE'
                msg = u'打印中'
            elif FINISHED_PRINTING_ACTIVE == active:
                semantic = 'FINISHED_PRINTING_ACTIVE'
                msg = u'打印完毕'
        elif BALE_STEP == step:
            if START_BALE_ACTIVE == active:
                semantic = 'READY_STATE'
                msg = u'开始包装'
            elif PUT_INTI_PHONE_CASE_ACTIVE == active:
                semantic = 'READY_STATE'
                msg = u'放入手机壳'
            elif PASTE_WAYBILL_ACTIVE == active:
                semantic = 'READY_STATE'
                msg = u'贴货运单'
            elif FINISHED_PRINTING_ACTIVE == active:
                semantic = 'READY_STATE'
                msg = u'包装完毕'
        return bin(active), semantic, msg
