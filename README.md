# Shanghai_Electronic_Student_Card_QRCode
上海电子学生证二维码生成器

下载页面：https://github.com/nemoshistudio/Shanghai_Electronic_Student_Card_QRCode/releases


本项目已经进入投放环节

具体使用情况仍在调查中

未来将围绕核心算法并结合用户使用反馈进行改进

尚且缺乏 GUI 

与普通二维码生成器主要差异在于：
  
  1. 为 二维码 内 字节字符加入 UTF-8 的 BOM 头，以适配 数字哨兵 等需要 BOM 头才能正常读取的设备
  
  2.将生成的二维码规格限制于 version 4 ，纠错等级 设定为 15% ，使各项规格保持与 学生证实体卡 二维码相同

如有建议欢迎提出

谢谢！
