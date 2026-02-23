# PET 亲子沟通完整流程

## 总览：行为窗口 → 五种情境

PET 的起点是**行为窗口**。父母观察孩子的行为后，判断落入哪个区域，每个区域对应不同的应对路径。其中**两种是非冲突情境**，**三种是冲突情境**。

```mermaid
flowchart TD
    Start([观察孩子的行为]) --> BW[/行为窗口/]
    BW --> Q1{行为是否可接受？}

    Q1 -->|可接受| Q2{孩子是否有困扰？}
    Q1 -->|不可接受| Q3{是否涉及<br>切实的需求影响？}

    Q2 -->|孩子有困扰| ChildZone["🟡 孩子拥有问题<br>（非冲突）"]
    Q2 -->|孩子也没困扰| NoProblem["🟢 无问题区<br>（非冲突）"]

    Q3 -->|行为切实影响父母需求| Q4{冲突的本质？}
    Q3 -->|不影响父母需求<br>只是信念/偏好不同| ValuesConflict["🟣 价值观冲突"]

    Q4 -->|双方需求真的矛盾| NeedsConflict["🔵 需求冲突"]
    Q4 -->|各执一个做法<br>底层需求可能不矛盾| SolutionConflict["🟠 解决方法的冲突"]

    NoProblem --> NoPPath[路径：预防技巧<br>巩固关系·减少未来冲突]
    ChildZone --> CPath[路径：积极倾听<br>帮助孩子自己解决问题]
    NeedsConflict --> NPath[路径：第三法六步骤]
    SolutionConflict --> SPath[路径：回归需求 → 第三法]
    ValuesConflict --> VPath[路径：价值观影响技巧]

    SolutionConflict -.- Note1>"⚠ 大多数表面上的冲突<br>其实是解决方法的冲突<br>而非真正的需求冲突"]

    classDef green fill:#d4edda,stroke:#28a745,color:#155724
    classDef yellow fill:#fff3cd,stroke:#ffc107,color:#856404
    classDef blue fill:#cce5ff,stroke:#004085,color:#004085
    classDef purple fill:#e8d5f5,stroke:#6f42c1,color:#6f42c1
    classDef orange fill:#fff3cd,stroke:#e67e22,color:#856404
    classDef path fill:#f0f0f0,stroke:#666,color:#333

    class NoProblem green
    class ChildZone yellow
    class NeedsConflict blue
    class ValuesConflict purple
    class SolutionConflict orange
    class NoPPath,CPath,NPath,VPath,SPath path
```

---

## 一、无问题区 → 预防与关系巩固

**定义**：孩子的行为可接受，孩子自身也没有困扰，双方需求都被满足，关系处于和谐状态。

**核心目标**：这是 PET 最理想的区域。P.E.T. 的终极目标就是**扩大这个区域**。此时不需要"解决问题"，而是**享受关系**，同时主动运用**预防技巧**，减少未来冲突的发生。

```mermaid
flowchart TD
    Start(["🟢 无问题区<br>双方需求都满足"]) --> Enjoy["自由沟通·享受关系<br>────────────<br>• 轻松对话、分享日常<br>• 不带目的地陪伴<br>• 建立情感银行存款"]

    Enjoy --> Prevent[主动运用预防技巧]

    Prevent --> P1["预防性我-信息<br>────────────<br>• 提前告知自己的计划和需求<br>• 给孩子主动体谅的机会<br>• 一条及时的我-信息<br>  可以省去九次对抗<br>────────────<br>例：「我今晚要打一个很长的电话，<br>想提前知道我们什么时候吃晚饭。」"]

    Prevent --> P2["环境调整法<br>────────────<br>• 改变环境而非改变孩子<br>• 八种策略：<br>  ① 丰富环境（提供有趣事物）<br>  ② 简化环境（适配孩子能力）<br>  ③ 限制环境（划定活动区域）<br>  ④ 安全防护（消除危险源）<br>  ⑤ 替代活动（提供替代品）<br>  ⑥ 提前预告（为变化做准备）<br>  ⑦ 使环境变单调（减少刺激）<br>  ⑧ 与大孩子共同计划"]

    Prevent --> P3["平衡三种时间<br>────────────<br>• 活动时间：全家一起做事<br>• 一对一时间：专注陪伴一个人<br>• 单独时间：独处恢复精力<br>────────────<br>三种时间失衡 → 问题和冲突<br>定期审视：哪种时间最缺？"]

    P1 & P2 & P3 --> Effect["预防的效果<br>────────────<br>• 减少「不可接受行为」的发生<br>• 扩大行为窗口的「无问题区」<br>• 让孩子感到被尊重和信任<br>• 一次调整可避免无数次对抗"]

    Effect --> Loop(["→ 持续维护<br>保持在无问题区"])

    classDef start fill:#d4edda,stroke:#28a745,color:#155724
    classDef tool fill:#cce5ff,stroke:#004085,color:#004085
    classDef effect fill:#e8f4fd,stroke:#0d6efd,color:#0d6efd
    classDef ok fill:#d4edda,stroke:#28a745,color:#155724

    class Start,Loop ok
    class P1,P2,P3 tool
    class Enjoy,Prevent start
    class Effect effect
```

### 关键洞见

- 无问题区不是"什么都不用做"的区域——它是**主动投资关系**的最佳时机
- 预防的成本远低于事后解决冲突的成本
- 环境调整是**最被忽视**的预防手段——一次布置可以避免反复对抗

> **类比**：如果你年迈的父母因半身不遂需要住进你家，你会毫不犹豫地铺防滑垫、装扶手、移走小地毯。那为什么不为孩子做同样的事？

---

## 二、孩子拥有问题 → 积极倾听

**定义**：孩子的行为可接受，但**孩子自身**不高兴、沮丧、困惑、受伤。问题属于孩子，不属于父母。

**核心工具**：积极倾听（Active Listening）——反映孩子的情绪和需求，帮助孩子**自己**解决问题。

**核心态度**：信任孩子有能力处理自己的问题；不替孩子解决，不给建议，不评判。

```mermaid
flowchart TD
    Start(["🟡 孩子拥有问题<br>孩子困扰·行为不影响父母"]) --> DoorOpen["敲门砖<br>────────────<br>• 「想说说看吗？」<br>• 「噢？」「然后呢？」<br>• 用非语言传达关注<br>• 打开沟通的大门"]

    DoorOpen --> AL1["① 暂停<br>────────────<br>• 放下自己的想法和情绪<br>• 放下「我要帮他解决」的念头<br>• 全身心关注孩子"]

    AL1 --> AL2["② 接收<br>────────────<br>• 听言语内容<br>• 观察非言语信号<br>  （表情、语气、姿态）"]

    AL2 --> AL3["③ 解码<br>────────────<br>• 理解话语背后真正的<br>  情绪和需求<br>• 「他真正想说的是什么？」"]

    AL3 --> AL4["④ 反馈<br>────────────<br>• 用自己的话表达理解<br>• 通常以「你」开头：<br>  「你觉得很不公平……」<br>  「你担心……」<br>• ⚠ 不是鹦鹉学舌"]

    AL4 --> AL5["⑤ 核实<br>────────────<br>• 孩子确认或修正你的理解<br>• 形成理解的闭环"]

    AL5 --> Check{孩子的状态？}

    Check -->|情绪释放·问题解决| Resolved(["✅ 孩子自己找到了出路"])
    Check -->|还有更深的情绪| AL1
    Check -->|情绪缓和·但问题未解| ChildSolve["孩子开始自己思考解决方案<br>────────────<br>• 当情绪被接纳后<br>  孩子的理性思考能力回来了<br>• 把解决方案的责任留给孩子<br>• 他们的方案常常令人惊喜"]

    ChildSolve --> Resolved

    Start -.- Avoid["⚠ 避免掉入绊脚石<br>────────────<br>❌ 命令：你应该去跟老师说<br>❌ 建议：你为什么不试试……<br>❌ 安慰：别担心，会好的<br>❌ 质问：你做了什么惹她的？<br>❌ 分析：你这样想是因为……"]

    classDef start fill:#fff3cd,stroke:#ffc107,color:#856404
    classDef step fill:#cce5ff,stroke:#004085,color:#004085
    classDef ok fill:#d4edda,stroke:#28a745,color:#155724
    classDef warn fill:#f8d7da,stroke:#dc3545,color:#721c24

    class Start start
    class DoorOpen,AL1,AL2,AL3,AL4,AL5,ChildSolve step
    class Resolved ok
    class Avoid warn
```

### 积极倾听的五大功效

1. **帮助释放情绪**——被鼓励坦诚说出困扰时，情绪会奇迹般地消失
2. **减少对负面情绪的恐惧**——传达"情绪是友好的"
3. **促进温暖的亲子关系**——被倾听和理解带给人极大的满足感
4. **帮助孩子自己解决问题**——"说出来"比"在心里想"更容易找到出路
5. **使孩子更愿意倾听父母**——被倾听的人更容易反过来倾听对方

### 必备态度（缺一不可）

| 态度 | 说明 |
|---|---|
| 真心想听 | 如果没时间，实话实说，不要假装 |
| 真诚希望帮助 | 而非急于展示你的解决方案 |
| 接受孩子的情绪 | 不论它们是什么——愤怒、悲伤、嫉妒 |
| 信任孩子的能力 | 相信他能处理自己的问题 |
| 认识到情绪是暂时的 | 不必害怕，它会流过去 |
| 视孩子为独立个体 | 他不是你的延伸 |

> **最常见的错误**：打开门后又关上——先积极倾听了两句，中途忍不住掉进12种沟通绊脚石（开始建议、评判、说教……）。

---

## 三、需求冲突的解决流程

**定义**：一方的行为**切实、具体地影响**了另一方满足自身需求。例如：孩子把音乐开到震天响，父母无法休息。

**核心工具**：第三法（没有输家的冲突解决）

**前置条件**：面质性我-信息和积极倾听都无法自然化解时，进入第三法。

```mermaid
flowchart TD
    Start([发现需求冲突]) --> IM[发送面质性我-信息<br>行为 + 感受 + 影响]

    IM --> ChildReact{孩子的反应？}
    ChildReact -->|主动改变行为| Solved([✅ 冲突解决])
    ChildReact -->|产生情绪反应<br>防御/反击/伤心| Shift[换挡技巧]
    ChildReact -->|理解但不愿改变<br>因自身需求也很重要| M3Enter[进入第三法]

    Shift --> ShiftAL[切换到积极倾听<br>接纳孩子的感受]
    ShiftAL --> ShiftOK{孩子情绪缓和？}
    ShiftOK -->|是| ShiftBack[换回：再次表达我-信息]
    ShiftOK -->|否| ShiftAL

    ShiftBack --> ChildReact2{孩子的反应？}
    ChildReact2 -->|改变行为| Solved
    ChildReact2 -->|仍有自身需求| M3Enter

    M3Enter --> S1["步骤一：界定问题<br>────────────<br>• 父母用我-信息说明自己的需求<br>• 用积极倾听了解孩子的需求<br>• ⚠ 聚焦「需求」而非「解决方案」"]

    S1 --> S2["步骤二：头脑风暴<br>────────────<br>• 双方自由提出各种可能方案<br>• 此阶段不评价任何方案<br>• 先让孩子提，父母后提<br>• 数量优先"]

    S2 --> S3["步骤三：评估方案<br>────────────<br>• 逐一讨论可行性<br>• 「你能接受这个方案吗？」<br>• 淘汰任何一方无法接受的方案"]

    S3 --> S4["步骤四：选定方案<br>────────────<br>• 找到双方都真心接受的方案<br>• 不投票，目标是共识<br>• 没有满意方案 → 回到步骤二"]

    S4 -->|无共识| S2
    S4 -->|达成共识| S5["步骤五：执行方案<br>────────────<br>• 明确：谁做什么、何时、如何<br>• 复杂方案可以写下来"]

    S5 --> S6["步骤六：检验效果<br>────────────<br>• 约定时间回顾执行情况<br>• 「方案执行得怎么样？」<br>• 效果不好 → 回到步骤一"]

    S6 --> Review{方案有效？}
    Review -->|是| Solved2([✅ 冲突解决])
    Review -->|需要调整| S1

    classDef start fill:#e8f4fd,stroke:#0d6efd,color:#0d6efd
    classDef step fill:#cce5ff,stroke:#004085,color:#004085
    classDef shift fill:#e2e3f1,stroke:#6c63ff,color:#4a44b5
    classDef ok fill:#d4edda,stroke:#28a745,color:#155724
    classDef decision fill:#fff,stroke:#666,color:#333

    class Start start
    class S1,S2,S3,S4,S5,S6,IM step
    class Shift,ShiftAL,ShiftBack shift
    class Solved,Solved2 ok
```

### 第三法的五大优势

1. **孩子有动力执行**——参与制定的决策，执行意愿远高于被强加的
2. **更高质量的方案**——两个脑袋比一个好，常产出意想不到的创造性方案
3. **培养思考能力**——孩子在参与中练习分析和解决问题
4. **更少敌意，更多爱**——共同解决问题拉近关系
5. **几乎不需要强制执行**——孩子既然同意了，通常自觉执行

---

## 四、解决方法的冲突

**定义**：表面上双方各执一个做法（你坚持 A，孩子坚持 B），但**底层需求可以同时满足**。戈登指出，亲子之间的大多数冲突其实是解决方法的冲突，而非真正的需求冲突。

**经典案例**：

| | 表面的解决方法 | 真正的需求 |
|---|---|---|
| 父亲 | 简**必须穿**雨衣 | 简不要被淋湿、不要感冒 |
| 简 | **不穿**雨衣 | 不想穿难看的衣服在同学面前丢脸 |

两个做法冲突了，但两个需求完全可以同时满足——借妈妈那件好看的旧雨衣。

```mermaid
flowchart TD
    Start([发现分歧：双方各执一个做法]) --> Trap{⚠ 常见陷阱}

    Trap -->|❌ 直接争论做法<br>各不相让| Deadlock[僵局<br>父母用权力 → 方法I<br>或 父母投降 → 方法II]

    Trap -->|✅ 先停下来<br>识别这是「做法之争」| Step1[用积极倾听<br>探索孩子的真正需求]

    Step1 --> Q1["问自己：<br>「我的真正需求是什么？」<br>而不是「我要孩子怎么做？」"]

    Q1 --> Compare{双方的「需求」<br>是否真的矛盾？}

    Compare -->|需求不矛盾<br>只是做法冲突| Creative["回到第三法步骤二<br>基于双方需求<br>头脑风暴新的做法"]
    Compare -->|需求确实矛盾| RealNeed[确认为真正的需求冲突<br>→ 走完整第三法六步骤]

    Creative --> NewSolution["创造性方案浮现<br>────────────<br>• 满足父母需求 ✓<br>• 满足孩子需求 ✓<br>• 往往出乎意料"]

    NewSolution --> Execute["执行 + 检验效果"]
    Execute --> Solved([✅ 冲突解决])

    Deadlock --> Lose["方法I → 孩子怨恨、叛逆<br>方法II → 孩子自私、不体谅"]

    classDef start fill:#fff3cd,stroke:#e67e22,color:#856404
    classDef trap fill:#f8d7da,stroke:#dc3545,color:#721c24
    classDef good fill:#cce5ff,stroke:#004085,color:#004085
    classDef ok fill:#d4edda,stroke:#28a745,color:#155724
    classDef bad fill:#f5c6cb,stroke:#dc3545,color:#721c24

    class Start start
    class Deadlock,Lose bad
    class Step1,Q1,Creative,NewSolution,Execute good
    class Solved ok
```

### 关键口诀

> **分清「需求」和「做法」，是打开死锁的钥匙。**
>
> 当你发现自己在想"孩子必须……"时，问一句：**"我真正需要的是什么？"**

---

## 五、价值观冲突的解决流程

**定义**：分歧涉及孩子的信念、价值观、风格、偏好或生活态度，但孩子的行为**没有切实影响**父母满足自身需求。

**判断**：问自己——"孩子的行为有没有**直接、具体地**影响到我？"如果没有，多半是价值观冲突。

**核心原则**：不使用第三法（孩子不愿把价值观摆上谈判桌），也绝不使用权力。用**价值观影响技巧**。

PET 归纳了 7 个等级的应对方式，**从低风险到高风险**排列。推荐使用等级 1~4（绿色区），慎用等级 5（黄色区），不推荐等级 6~7（红色区）。

```mermaid
flowchart TD
    Start([发现价值观分歧]) --> Verify{确认：孩子的行为<br>是否切实影响<br>父母的需求？}

    Verify -->|是| NotValue["这不是价值观冲突<br>→ 按需求冲突处理"]
    Verify -->|否| Confirm[确认为价值观冲突]

    Confirm --> Explore["先用积极倾听 + 我-信息<br>深入探索<br>────────────<br>许多表面的「价值观冲突」<br>其实是需求冲突"]

    Explore --> ReallyValue{探索后确认<br>确实是价值观冲突？}
    ReallyValue -->|其实是需求冲突| NotValue
    ReallyValue -->|确实是价值观冲突| Ladder[选择价值观影响技巧<br>从低风险开始]

    Ladder --> L1["等级1：自我调整 🟢<br>────────────<br>• 审视自己的价值观来源和意义<br>• 问3个问题：<br>  ① 我的价值观是什么？<br>  ② 它来自哪里？<br>  ③ 为什么要保留它？<br>• 必要时降低接纳线<br>• 接受「孩子不是我的延伸」"]

    Ladder --> L2["等级2：树立榜样 🟢<br>────────────<br>• 用自己的行为示范价值观<br>• 「按我做的去做」而非<br>  「按我说的去做」<br>• 对大孩子小孩子都有效<br>• 耐心——效果可能数年后才显现"]

    Ladder --> L3["等级3：面质与积极倾听 🟢<br>────────────<br>• 发送一条我-信息<br>  （描述行为对孩子自身的潜在影响）<br>• 然后换挡到积极倾听<br>• 只说一次，不反复唠叨<br>• 帮助孩子深层探索自己的信念"]

    Ladder --> L4["等级4：担任顾问 🟢<br>────────────<br>• 原则①：被「聘用」而非强行上岗<br>  （孩子愿意听才说）<br>• 原则②：事先准备好事实<br>  （不夸大、不恐吓）<br>• 原则③：把改变的责任留给孩子<br>  （说完后优雅地后退）<br>• 少说多听、分享而非说教"]

    Ladder --> L5["等级5：运用第三法 🟡<br>────────────<br>• 孩子可能愿意改变行为<br>  （但不放弃价值观）<br>• 风险：孩子可能过「双重生活」<br>• 慎用"]

    Ladder --> L6["等级6：威胁使用权威 🔴<br>────────────<br>• 不推荐<br>• 引发孩子逃跑、反抗<br>• 削弱父母说话的可信度"]

    Ladder --> L7["等级7：使用权威 🔴<br>────────────<br>• 不推荐<br>• 仅在极端情况使用<br>  （如孩子深陷毒瘾危及生命）<br>• 会严重损害亲子关系"]

    L1 & L2 & L3 & L4 --> Accept["最终心态<br>────────────<br>「虽然我们是两个完全不同的<br>独特个体，但仍可以彼此喜欢，<br>相互尊重。」"]

    Accept --> Resolved([🕊 与差异和平共处])

    classDef start fill:#e8d5f5,stroke:#6f42c1,color:#6f42c1
    classDef green fill:#d4edda,stroke:#28a745,color:#155724
    classDef yellow fill:#fff3cd,stroke:#ffc107,color:#856404
    classDef red fill:#f8d7da,stroke:#dc3545,color:#721c24
    classDef ok fill:#e8d5f5,stroke:#6f42c1,color:#6f42c1
    classDef neutral fill:#f0f0f0,stroke:#666,color:#333

    class Start,Resolved ok
    class L1,L2,L3,L4 green
    class L5 yellow
    class L6,L7 red
    class Accept neutral
```

### 价值观冲突的常见领域

| 领域 | 典型表现 |
|---|---|
| 外表 | 发型、着装、文身、穿环 |
| 社交 | 交友选择 |
| 娱乐 | 音乐/影视偏好 |
| 信仰 | 宗教观、道德观 |
| 学业 | 学习态度、读书选择 |
| 生活 | 饮食习惯、性观念、职业选择 |

### 孩子的典型回应（说明这是价值观冲突）

- "这是**我的**头发。"
- "别管我的事。"
- "这又没碍**你**的事。"
- "我有权做我喜欢的。"

---

## 六、五种情境对比总结

```mermaid
flowchart LR
    subgraph NP ["🟢 无问题区"]
        NP1[双方需求都满足]
        NP2[工具：预防技巧]
        NP3[目标：巩固关系<br>减少未来冲突]
        NP1 --> NP2 --> NP3
    end

    subgraph CO ["🟡 孩子拥有问题"]
        CO1[孩子困扰<br>不影响父母]
        CO2[工具：积极倾听]
        CO3[目标：帮孩子<br>自己解决]
        CO1 --> CO2 --> CO3
    end

    subgraph NC ["🔵 需求冲突"]
        NC1[行为切实影响<br>父母需求]
        NC2[工具：第三法六步骤]
        NC3[目标：双赢方案]
        NC1 --> NC2 --> NC3
    end

    subgraph SC ["🟠 解决方法的冲突"]
        SC1[做法对立<br>需求不矛盾]
        SC2[关键：回归需求层面]
        SC3[目标：创造性方案]
        SC1 --> SC2 --> SC3
    end

    subgraph VC ["🟣 价值观冲突"]
        VC1[信念/偏好不同<br>不影响父母需求]
        VC2[工具：价值观影响技巧]
        VC3[目标：尊重差异<br>维护关系]
        VC1 --> VC2 --> VC3
    end

    classDef green fill:#d4edda,stroke:#28a745,color:#155724
    classDef yellow fill:#fff3cd,stroke:#ffc107,color:#856404
    classDef blue fill:#cce5ff,stroke:#004085,color:#004085
    classDef orange fill:#fff3cd,stroke:#e67e22,color:#856404
    classDef purple fill:#e8d5f5,stroke:#6f42c1,color:#6f42c1

    class NP1,NP2,NP3 green
    class CO1,CO2,CO3 yellow
    class NC1,NC2,NC3 blue
    class SC1,SC2,SC3 orange
    class VC1,VC2,VC3 purple
```

| | 🟢 无问题区 | 🟡 孩子拥有问题 | 🔵 需求冲突 | 🟠 解决方法的冲突 | 🟣 价值观冲突 |
|---|---|---|---|---|---|
| **本质** | 双方需求都满足 | 孩子困扰，不影响父母 | 双方需求真的矛盾 | 做法对立，需求可共存 | 信念/偏好不同 |
| **问题归属** | 无问题 | 孩子 | 双方 | 双方 | 无（或父母自认的） |
| **核心工具** | 预防性我-信息、环境调整、三种时间 | 积极倾听五步法 | 第三法六步骤 | 回归需求 + 第三法 | 价值观影响技巧 |
| **父母角色** | 同伴、预防者 | 倾听者、帮助者 | 协商者 | 需求探索者 | 咨询者、榜样 |
| **目标** | 巩固关系、防患未然 | 帮孩子自己找到出路 | 双赢方案 | 满足双方需求的新做法 | 尊重差异，维护关系 |
| **禁忌** | 忽视这个区域（不投资关系） | 替孩子解决、给建议、评判 | 方法I或方法II | 在做法层面僵持不下 | 用权力或第三法强改价值观 |

### PET 的终极目标

```
┌──────────────────────────────┐
│  孩子拥有问题  →  积极倾听     │ ↑ 缩小
├──────────────────────────────┤
│                              │
│        没 有 问 题            │ ← 扩大这个区域！
│                              │
├──────────────────────────────┤
│  父母拥有问题  →  我-信息/第三法│ ↓ 缩小
└──────────────────────────────┘
```

> **一句话总结**：先通过行为窗口判断情境，再选择对应的工具。无问题时主动预防；孩子有困扰时倾听而不替他解决；有冲突时分清冲突类型再行动。用错工具比不用工具更危险——拿第三法去改变价值观，或拿权力去解决需求冲突，都会适得其反。
