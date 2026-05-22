#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
为产品简介.md 中的 Acronyms and Abbreviations 表格添加中文翻译列。
正确重建三列表格结构。
"""
import re

filepath = r'D:\work\07 项目\02 文档整改_output\ss928v100-docs\docs\system-architecture\产品简介.md'

# 先还原
import os
os.system(f'git checkout -- "{filepath}"')

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

cn_map = {
    'three-dimensional noise reduction': '三维降噪',
    'advanced audio coding': '高级音频编码',
    'automatic exposure': '自动曝光',
    'acoustic echo control': '声学回声控制',
    'advanced encryption standard': '高级加密标准',
    'automatic focus': '自动对焦',
    'automatic level control': '自动电平控制',
    'adaptive noise reduction': '自适应降噪',
    'application programming interface': '应用程序编程接口',
    'adaptive variable bit rate': '自适应可变比特率',
    'any view stitching': '任意视图拼接',
    'automatic white balance': '自动白平衡',
    'chromatic aberration correction': '色差校正',
    'constant bit rate': '恒定比特率',
    'complementary metal-oxide-semiconductor': '互补金属氧化物半导体',
    'computer vision': '计算机视觉',
    'coder/decoder': '编解码器',
    'camera serial interface': '摄像头串行接口',
    'digital camera': '数字相机',
    'dynamic contrast improvement': '动态对比度增强',
    'double data rate': '双倍数据速率',
    'double data rate controller': '双倍数据速率控制器',
    'digital image stabilization': '数字图像稳定',
    'depth processing unit': '深度处理单元',
    'display serial interface': '显示串行接口',
    'digital signal processor': '数字信号处理器',
    'error-correcting code': '纠错码',
    'embedded multimedia card': '嵌入式多媒体卡',
    'endpoint': '端点',
    'flip-chip chip scale package': '倒装芯片级封装',
    'fixed pattern noise': '固定模式噪声',
    'floating-point unit': '浮点运算单元',
    'gigabit Ethernet': '千兆以太网',
    'Gigabit Ethernet Media Access Controller': '千兆以太网媒体访问控制器',
    'general-purpose input/output': '通用输入/输出',
    'graphical user interface': '图形用户界面',
    'high definition': '高清晰度',
    'high-speed serial pixel interface': '高速串行像素接口',
    'inter-integrated circuit': '内部集成电路',
    'inter-IC sound': '集成电路内置音频总线',
    'image signal processor': '图像信号处理器',
    'intelligent video engine': '智能视频引擎',
    'liquid crystal display': '液晶显示器',
    'lens geometric distortion correction': '镜头几何畸变校正',
    'low-power double data rate': '低功耗双倍数据速率',
    'low-speed analog-to-digital converter': '低速模数转换器',
    'lookup table': '查找表',
    'low-voltage differential signaling': '低压差分信号',
    'matrix arithmetic unit': '矩阵算术单元',
    'microcontroller unit': '微控制器单元',
    'microphone': '麦克风',
    'mobile industry processor interface': '移动行业处理器接口',
    'noise reduction': '降噪',
    'on-screen display': '屏幕显示',
    'one-time programming': '一次性编程',
    'peripheral component interconnect express': '外围组件互连高速',
    'picture-in-picture': '画中画',
    'power-on reset': '上电复位',
    'pulse-width modulation': '脉宽调制',
    'random access memory': '随机存取存储器',
    'root complex': '根复合体',
    'red-green-blue': '红绿蓝',
    'reduced gigabit media-independent interface': '简化千兆媒体独立接口',
    'reduced media-independent interface': '简化媒体独立接口',
    'restriction of hazardous substances': '有害物质限制指令',
    'region of interest': '感兴趣区域',
    'Rivest-Shamir-Adleman': 'RSA加密算法',
    'random number generator': '随机数生成器',
    'secure digital': '安全数字存储卡',
    'secure digital input/output': '安全数字输入/输出',
    'software development kit': '软件开发工具包',
    'synchronous dynamic random access memory': '同步动态随机存取存储器',
    'secure digital extended capacity': '安全数字扩展容量',
    'symmetric multiprocessing': '对称多处理',
    'system-on-chip': '片上系统',
    'serial peripheral interface': '串行外设接口',
    'time division multiplexing': '时分复用',
    'Tera Operations Per Second': '万亿次操作每秒',
    'TCP segmentation offload': 'TCP分段卸载',
    'transmit': '发送',
    'universal asynchronous receiver transmitter': '通用异步收发器',
    'Universal Serial Bus': '通用串行总线',
    'variable bit rate': '可变比特率',
    'video input': '视频输入',
    'video output': '视频输出',
    'voice quality enhancement': '语音质量增强',
    'wide dynamic range': '宽动态范围',
}

# 定位表格
table_start = content.index('<a name="table123mcpsimp"></a>')
table_end = content.index('</table>', table_start) + len('</table>')
old_table = content[table_start:table_end]

# 逐行解析原始表格
rows_data = []

# 用 re.DOTALL 匹配完整行（含换行）
for rm in re.finditer(r'<tr[^>]*>(.*?)</tr>', old_table, re.DOTALL):
    row_html = rm.group(1)
    # 提取所有 td 及其完整内容（含 td 标签）
    tds = re.findall(r'(<td[^>]*>.*?</td>)', row_html, re.DOTALL)
    if len(tds) >= 2:
        acro_full = tds[0]   # 完整的第一个 <td>...</td>
        eng_full = tds[1]    # 完整的第二个 <td>...</td>
        acro_text = re.sub(r'<[^>]+>', '', acro_full).strip()
        eng_text = re.sub(r'<[^>]+>', '', eng_full).strip()
        rows_data.append((acro_full, acro_text, eng_full, eng_text))

print(f'Parsed {len(rows_data)} rows from original table')

# 重建行
new_rows = []
for i, (acro_full, acro, eng_full, eng) in enumerate(rows_data):
    cn_text = cn_map.get(eng, f'[{eng}]')

    # 更新列宽
    acro_new = re.sub(r'width="[^"]*"', 'width="14%"', acro_full)
    eng_new = re.sub(r'width="[^"]*"', 'width="43%"', eng_full)
    cn_new = f'<td class="cellrowborder" valign="top" width="43%"><p id="p_cn_{i+1}"><a name="p_cn_{i+1}"></a><a name="p_cn_{i+1}"></a>{cn_text}</p></td>'

    new_row = f'<tr id="row_{i+1}">\n\t{acro_new}\n\t{eng_new}\n\t{cn_new}\n</tr>'
    new_rows.append(new_row)

# 构建新表格
new_table = '<a name="table123mcpsimp"></a>\n<table><tbody>\n' + '\n'.join(new_rows) + '\n</tbody>\n</table>'

# 替换
new_content = content[:table_start] + new_table + content[table_end:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

# 验证
print(f'Done! Table rebuilt with {len(rows_data)} rows')
with open(filepath, 'r', encoding='utf-8') as f:
    verify = f.read()

vstart = verify.index('<a name="table123mcpsimp"></a>')
vend = verify.index('</table>', vstart) + len('</table>')
vtable = verify[vstart:vend]

vrows = re.findall(r'<tr[^>]*>.*?</tr>', vtable, re.DOTALL)
ok = 0
for r in vrows:
    td_count = len(re.findall(r'<td[^>]*>', r))
    has_cn = any('一' <= c <= '鿿' for c in r)
    if td_count == 3 and has_cn:
        ok += 1
    else:
        print(f'  BAD: {td_count} tds, cn={has_cn} - {r[:80]}...')

print(f'Correctly formatted rows: {ok}/{len(vrows)}')