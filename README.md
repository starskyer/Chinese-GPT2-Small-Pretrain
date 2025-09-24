# 基于开源项目的 GPT2 Chinese Model 训练

## 1. 概述

- 本项目作为复旦大学人工智能设计与应用的课程入门作业，工程代码基本参考Github项目[lvfinn/chinese-GPT2-start-from-zero](https://github.com/lvfinn/chinese-GPT2-start-from-zero)进行复现 & 自主收集数据集尝试，基础项目配置请参阅原工程

- 在原有项目基础上收集了其它的中文小说语料共25MB，在消费级GPU（NVIDIA RTX 3060 laptop 6GB）上训练5个epoch，目标是能根据输入文本自动续写至少10句话的连贯文本，相关尝试记录如下文所述

## 2. 对原项目的增补

（1）更新了项目的库依赖，其中 `tb-nightly` 库现已弃置不用，改用 `tensorboard`库

（2）补充了`check_token_length.py`用于监测原语料库中的token数情况，防止在遇到过长的语料数据时模型处理发生indexing 错误或内存暴涨，也可用于平衡模型对不同语料数据的关注度

（3）补充了`input_gen.py`辅助文本清洗，主要应对输入文本数据来自多个不同的文本文件的情况，实现拼接

（4）对于10句话生成任务，使用context length=256-512的小规模模型已经有较好适配，同时可降低训练成本；本项目补充实现了原项目《斗破苍穹》文本以及新增其它的小说文本的5 epoch阶段性训练模型，并附带上传了模型训练的日志文件

关于训练：本项目的中文语料来自Github精简中文语料库[nlp_chinese_corpus](https://github.com/brightmart/nlp_chinese_corpus)，在该库上使用context_length=256的模型配置进行训练，在单卡3060GPU上训练5个epoch共计耗时约75分钟

