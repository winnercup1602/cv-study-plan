# CV 핵심 개념과 모델 스터디 계획

## 1. 운영계획

**주 1회, 회당 60분(방학 중에는 주 2회)** 동안 CV의 핵심 개념과 모델을 함께 공부합니다. **개념이 필요한 이유, 구조와 수식의 의미, 실제 동작 원리를 깊이 이해하는 것**을 목표로 합니다. 배운 내용을 자신의 언어와 구조도·수식·코드로 설명하고, 연구에서 설계와 활용을 판단하는 데 연결합니다.

매 세션은 **이전 내용 복습 → 이번 세션의 학습 포인트 안내 → 개념·구조·수식 학습 → 설계 이유와 근거 검토 → 구현과 확장 연결 → 개인별 학습 포인트 확인과 학습 정리** 순서로 진행합니다. 현장에서 공유 기록의 초안을 남기고, 세션 후 근거와 표현을 보완해 한 페이지로 완성합니다.

### 1. 학습 Level

| Level | 도달 기준 | 적용 기준 |
|---|---|---|
| **L1 · 직관** | 개념이 필요한 이유와 해결하는 문제를 이해하고, 핵심 아이디어를 자신의 언어와 쉬운 예·figure로 설명할 수 있습니다. | 모든 구성원의 공통 목표 |
| **L2 · 동작 원리** | 입력부터 출력까지의 계산 흐름, 구성요소·중요 수식의 역할과 가정, 학습·추론의 차이와 설계 이유를 설명할 수 있습니다. | 모든 구성원의 기본 도달 기준 |
| **L3 · 연구와 구현** | 수식·구현 수준에서 동작을 추적하고, 설계의 근거·한계·대안과 조건이 바뀔 때의 영향을 분석할 수 있습니다. | 담당자의 준비 기준. 구성원은 자신의 연구와 연결되는 부분부터 심화 |

**필수 / 중요는 학습 우선순위**, **L1 / L2 / L3는 이해의 깊이**를 나타냅니다. 구성원은 L1–L2를 공통 목표로 삼고, 담당자는 동작 원리를 수식·구현과 연결하며 설계 근거·한계·대안까지 준비합니다.

### 2. 세션 담당자 준비 안내

<!-- presenter-guidance -->

#### 준비 범위

- **기준 논문이 있는 주제**는 해당 논문을 기준으로 개념·구조·설계 의도를 공부하고, 이해에 필요한 자료를 함께 참고합니다.
- **기준 논문이 없는 주제**는 여러 논문·교재·강의·공식 문서·코드를 공부하며, 학습 포인트에 맞춰 핵심 내용과 설명 순서를 자유롭게 구성합니다.
- **준비의 중심은 개념과 구조가 작동하는 방식과 그 의미를 깊이 이해하는 것**입니다. 설명에 사용한 근거와 자신의 해석을 구분합니다.

#### 1. 학습 포인트와 필요성

- 주제·목표 Level·학습 포인트를 정하고, 이해에 필요한 개념과 자료를 골라 설명 흐름을 구성합니다.
- 해결하려는 문제와 핵심 아이디어를 쉬운 예로 연결하며, **학습 포인트는 종료 시 같은 문장·항목·순서로 확인**합니다.

#### 2. 동작 원리와 구조

- **입력 → 계산·변환 → 출력**을 따라 각 구성요소의 역할과 정보 흐름을 설명합니다. 네트워크가 없는 개념은 알고리즘·계산 과정으로 살펴봅니다.
- 중요 수식의 기호·차원·가정을 구조와 연결하고, 각 연산과 항이 무엇을 의미하며 왜 필요한지 설명합니다.
- 학습·추론, 데이터·target·loss, 고정·갱신하는 파라미터와 gradient 흐름을 연결해 혼동하기 쉬운 차이를 짚습니다.

#### 3. 설계 이유와 근거

- 구성요소가 왜 필요한지, 제거하거나 다르게 구성하면 무엇이 달라지는지 대안과 비교합니다.
- 관련 실험·ablation이 있으면 **질문 → 변경 요소·고정 조건 → 결과 → 해석**을 연결하고, 결론이 성립하는 범위를 확인합니다.
- 주제에 맞는 간단한 계산·시각화·작은 입력 예제로 원리를 살펴봅니다. 설명을 위한 예시와 실험으로 검증된 결론을 구분합니다.

#### 4. 구현과 확장

- 공식 코드나 작은 구현 예제를 구조·수식과 연결해 실제 계산을 확인하고, 이해에 필요한 학습 설정과 구현 선택을 살펴봅니다.
- 관련 개념·모델·후속 연구에서 같은 원리가 어떻게 유지·변형·활용되는지 연결하고, 유용한 조건과 한계를 비교합니다.

#### 5. 학습 확인 자료

- 시작과 **같은 학습 포인트를 담은 작성지를 인원수에 맞춰 출력**하고, 설명·수식·도식을 적을 공간을 둡니다.
- 작동 원리·구성요소의 역할·설계 이유를 자신의 언어로 설명하는 항목을 구성합니다. 주제에 따라 수식 해석·구조 그리기·대안 비교·실험 해석을 포함합니다.
- 함께 확인할 개념·혼동 지점을 준비하고, 공유 기록 틀에 학습 포인트와 참고 자료를 연결합니다.

<!-- /presenter-guidance -->

### 3. 60분 세션 진행

각 파트의 **소요 시간**을 중심으로 읽습니다. 진행 구간은 세션 시작 후 경과 시간을 나타냅니다. 모든 시간 배분은 5분 단위입니다.

#### 시작 점검 · **10분** (0–10분)

| 소요 시간 | 진행 구간 | 단계 | 진행 내용 |
|---|---|---|---|
| **5분** | 0–5분 | 이전 내용 복습 | 이전 세션의 공유 기록을 기준으로 학습 포인트, 함께 수정한 설명과 남은 질문을 확인합니다. 첫 세션에서는 선수 개념을 점검합니다. |
| **5분** | 5–10분 | 학습 포인트와 핵심 아이디어 | 이번 주제의 목표 Level과 학습 포인트를 안내하고, 해결하려는 문제와 핵심 아이디어를 직관적으로 설명합니다. |

#### 핵심 학습 · **35분** (10–45분)

| 소요 시간 | 진행 구간 | 단계 | 진행 내용 |
|---|---|---|---|
| **15분** | 10–25분 | 개념·구조·수식의 의미 | 입력 → 계산·변환 → 출력을 따라 구성요소와 수식이 어떤 역할을 하고 왜 필요한지 살펴봅니다. 학습·추론 흐름, 가정과 혼동하기 쉬운 차이도 연결합니다. |
| **10분** | 25–35분 | 설계 이유와 근거 검토 | 대안과 비교하고, 관련 실험·ablation이나 작은 예제로 구성요소의 역할과 설계 이유를 살펴봅니다. 실험으로 확인한 사실과 설명을 위한 예시·해석을 구분합니다. |
| **10분** | 35–45분 | 구현·변형·활용 연결 | 코드나 작은 입력·출력 예제로 실제 동작을 확인합니다. 관련 개념·모델·후속 연구와 비교하며 같은 원리가 어떻게 변형·확장되는지 연결합니다. |

#### 학습 정리 · **15분** (45–60분)

| 소요 시간 | 진행 구간 | 단계 | 진행 내용 |
|---|---|---|---|
| **5분** | 45–50분 | 학습 포인트 작성 | 인쇄한 작성지의 모든 항목에 각자 짧은 설명·수식·도식을 적습니다. 먼저 자료를 덮고 작성하며, 막힌 부분과 남은 질문도 표시합니다. |
| **10분** | 50–60분 | 학습 포인트 확인·공유 기록 | 각자 적은 답을 바탕으로 학습 포인트를 함께 확인하고, 핵심 결론·수정한 설명·남은 질문과 근거 위치를 공유 페이지에 정리합니다. 문장·figure·수식 보완은 세션 후에 완성합니다. |

### 4. 학습 포인트 확인

**시작에 안내한 학습 포인트를 같은 문장·항목·순서로 다시 확인합니다.**

1. **각자 작성 · 5분.** 자료나 다른 사람의 답을 보지 않고, 인쇄된 작성지의 모든 항목에 설명·수식·도식으로 답합니다. 막힌 부분도 표시합니다.
2. **함께 확인·기록 · 10분.** 답을 비교해 헷갈린 내용을 바로잡고, 수정한 설명·남은 질문·근거를 공유 기록에 남깁니다. 이 기록을 다음 복습의 기준으로 사용합니다.

작성지에는 항목별로 **내 설명·수식·도식 / 막힌 부분·남은 질문** 공간을 둡니다.

<!-- point-example:resnet label:ResNet -->

주제: **Residual learning의 필요성과 shortcut의 작동 원리** · 목표: **L2**

- [ ] **1. 왜 층을 더 쌓는 것만으로는 충분하지 않을까요?** 더 깊은 네트워크가 학습 데이터조차 더 잘 맞추지 못할 수 있는 이유와, residual learning이 해결하려는 문제를 설명해 보세요.
- [ ] **2. Residual block은 입력을 어떻게 출력으로 바꾸나요?** 입력 `x`가 지나는 두 경로를 그리고, `F(x)`가 무엇을 학습하는지와 shortcut이 어떻게 결합되는지 수식으로 나타내 보세요.
- [ ] **3. Shortcut은 학습에 어떤 경로를 더하나요?** shortcut을 제거한 경우와 비교해, 정보와 gradient가 전달되는 흐름이 어떻게 달라지는지 설명해 보세요.
- [ ] **4. 덧셈을 다른 결합 방식으로 바꿔도 같은 구조일까요?** 덧셈과 concatenation을 비교해 출력 차원과 residual learning의 의미가 어떻게 달라지는지 설명해 보세요.

참고자료: [Deep Residual Learning for Image Recognition — 원문](https://arxiv.org/pdf/1512.03385), §1·§3.1–3.3, Figure 2·3 및 Eq. (1)–(2).
<!-- /point-example -->

<!-- point-example:transformer label:Transformer -->

주제: **토큰 사이의 정보 교환과 encoder–decoder의 작동 원리** · 목표: **L2**

- [ ] **1. 왜 토큰 사이에 정보를 주고받아야 할까요?** “고양이가 우유를 마신다”에서 각 토큰을 따로 처리하는 경우와 문맥을 함께 반영하는 경우를 비교하고, self-attention을 사용하는 이유를 설명해 보세요.
- [ ] **2. 다른 토큰의 정보가 내 표현에 어떻게 섞이나요?** 한 토큰의 표현을 갱신하는 과정을 수식과 그림으로 나타내고, Q·K·V·softmax와 여러 head의 역할을 설명해 보세요.
- [ ] **3. 입력 문장이 출력 문장으로 바뀌는 구조는 어떻게 작동하나요?** encoder와 decoder의 정보 흐름을 그리고, positional encoding·self-attention·cross-attention·FFN이 각각 어떤 역할을 하는지 짚어 보세요.
- [ ] **4. 왜 학습은 병렬로 계산하고 생성은 순차적으로 하나요?** decoder 입력과 정답의 관계, causal mask, 생성 시 이용할 수 있는 정보를 기준으로 설명해 보세요.

참고자료: [Attention Is All You Need — 원문](https://arxiv.org/pdf/1706.03762), §3.1–3.5, Figure 1·2 및 Eq. (1). 문장은 원리 설명을 위한 예시입니다.
<!-- /point-example -->

<!-- /운영계획 -->

---

## 2. 학습 항목

신경망 기초부터 생성 모델까지 0–4장의 학습 항목을 정리합니다. 각 모델의 구조·수식·학습·구현을 함께 살펴보며, 원리가 밀접하게 연결된 후속 모델은 주요 변화를 비교합니다.


### 개념 유형 구분

학습 항목 옆의 유형은 해당 항목의 성격과 세션에서 중점적으로 다루는 역할을 나타냅니다. 둘 이상의 관점으로 다루면 **모델 · 학습 방법**처럼 함께 표기합니다.

| 유형 | 의미 | 예시 |
|---|---|---|
| 기초 개념 | 텐서 표현과 layer의 동작, 초기화 등 모델 이해의 바탕 | Tensor / Linear / MLP, Activation / Initialization |
| 기초 연산 | 모델을 구성하는 기본 계산과 변환 | Convolution / Pooling, Normalization |
| 학습 원리 | 오차를 정의하고 gradient를 계산하는 원리 | Loss / Backpropagation |
| 학습 방법 | 학습 신호·목표·업데이트·전이 방식을 정하는 방법 | Optimization, Regularization, SimCLR, DINO, MAE |
| 모델 구조 | 여러 모델에서 활용하는 블록 구성과 정보 흐름 | Transformer |
| 모델 | 구조와 학습 목표를 특정 작업에 맞게 구성한 전체 | U-Net, CLIP, DETR, DPT, SAM |
| 구성 요소 | 모델 안에서 feature 결합 등 특정 역할을 맡는 구조 | FPN |
| 적응 방법 | 사전학습 모델을 새로운 작업에 맞게 조정하는 기법 | LoRA |
| 생성 모델 | 데이터 분포를 학습해 새 샘플을 만드는 모델 계열과 시스템 | VAE, GAN, DDPM, Latent Diffusion |
| 생성 방법 | 생성 경로·sampling 절차 또는 이를 위한 학습 목표를 정의하는 방법 | DDIM, Flow Matching, Rectified Flow |

**Backbone·Neck·Denoiser·조건 제어**는 모델이나 구성 요소의 역할을 덧붙이는 표기입니다. 각각 feature 추출, 다중 해상도 feature 결합, 노이즈 제거를 위한 예측, 조건 입력 반영을 뜻합니다. 예를 들어 ResNet은 **모델 · Backbone**, FPN은 **구성 요소 · Neck**, DiT는 **모델 · Denoiser**, ControlNet은 **모델 · 조건 제어**로 표시합니다.

유형과 함께 구조·학습 목표·데이터·학습과 추론의 흐름을 살펴보고, 설계의 효과와 한계를 설명할 수 있는 것을 목표로 합니다.

---

### 0. 신경망 연산과 최적화 기초

#### 학습 목표

모델 전반에서 사용하는 텐서 연산과 학습 과정을 이해하고, 구조·수식·코드의 입력과 출력, gradient와 파라미터 갱신을 연결한다.

#### 학습 내용

| 항목 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Tensor / Linear / MLP | 기초 개념 | 필수 | **텐서와 차원:** batch·채널·공간·토큰 축을 구분하고, reshape·transpose 전후의 shape를 추적한다.<br>**기본 연산:** 행렬 곱과 broadcasting의 조건을 확인하고, Linear layer의 입력·출력 shape와 파라미터 수를 계산한다.<br>**MLP 구성:** Linear와 activation을 조합해 정보를 변환하는 과정을 수식과 작은 코드로 연결한다. |
| Activation / Initialization | 기초 개념 | 필수 | **비선형성:** activation이 필요한 이유를 이해하고, ReLU·GELU·SiLU의 출력과 gradient, Sigmoid·Tanh의 saturation을 비교한다.<br>**초기화:** 가중치 크기가 activation·gradient의 크기에 미치는 영향을 살펴보고, Xavier·He 초기화의 가정과 적용 대상을 구분한다.<br>**직접 확인:** 작은 네트워크와 그래프로 출력 분포, gradient 소실·폭주, 초기화에 따른 차이를 확인한다. |
| Loss / Backpropagation | 학습 원리 | 필수 | **예측과 정답:** logits·확률·target을 구분하고, 분류의 cross-entropy와 회귀의 MSE를 비교한다.<br>**미분과 갱신:** chain rule로 loss의 gradient를 계산하는 backpropagation과, 파라미터를 바꾸는 optimizer의 역할을 구분한다.<br>**코드 연결:** 간단한 forward·backward를 추적한다. PyTorch CrossEntropyLoss에는 softmax 전 logits를 넣는 이유도 확인한다. |
| Optimization | 학습 방법 | 필수 | **Gradient descent:** full-batch·stochastic·mini-batch 방식을 구분하고, SGD·Momentum·Adam·AdamW의 갱신식과 상태 변수를 비교한다.<br>**학습률:** learning rate가 갱신 크기를 조절하는 방식과 warmup·step·cosine schedule의 역할을 이해한다.<br>**Weight decay:** L2 penalty와 파라미터 감쇠의 관계를 살펴보고, Adam에서 L2 regularization과 AdamW의 decoupled weight decay가 다른 이유를 확인한다. |
| Normalization | 기초 연산 | 필수 | **정규화 축:** BN·LN·GroupNorm이 평균·분산을 계산하는 축과 batch 의존성을 비교한다.<br>**학습과 추론:** 일반적인 BN 설정에서 학습 시 batch 통계, 추론 시 누적 통계를 사용하는 차이를 확인한다.<br>**변형과 배치:** 평균을 빼지 않는 RMSNorm의 연산을 비교하고, 각 모델에서 normalization을 선택하고 배치한 이유를 연결한다. |
| Regularization | 학습 방법 | 필수 | **일반화:** 학습·검증 성능의 차이로 overfitting을 살펴보고, dropout과 weight decay가 학습에 개입하는 위치를 구분한다.<br>**적용 방식:** dropout의 학습·추론 차이를 확인하고, weight decay는 optimizer의 갱신식과 연결한다.<br>**데이터 증강:** Mixup의 입력·label 혼합과 CutMix의 영역 교체·면적 비례 label 혼합을 비교한다. |

### 1. CNN 구조와 활용 모델

#### 학습 목표

Convolution·pooling의 연산에서 출발해 CNN 블록과 다중 해상도 feature 구성을 이해하고, 이를 검출·분할의 출력과 학습 구조로 연결한다.

#### 학습 내용

| 모델 / 구조 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Convolution / Pooling | 기초 연산 | 필수 | **공간 연산:** locality·weight sharing을 이해하고, kernel·stride·padding·dilation에 따른 출력 shape와 receptive field를 계산한다.<br>**연산 비용:** 일반·1×1·group·depthwise convolution의 채널 연결, 파라미터 수와 연산량을 비교한다.<br>**Pooling:** max·average·global average pooling이 공간 해상도와 정보에 미치는 영향을 확인한다. |
| ResNet | 모델 · Backbone | 필수 | **Residual learning:** plain network의 degradation 문제와, residual branch에 shortcut을 더하는 구조를 연결한다.<br>**블록과 stage:** basic block·bottleneck, stage별 해상도·채널 변화, identity·projection shortcut의 조건과 gradient 흐름을 추적한다.<br>**설계 비교:** shortcut ablation을 해석하고, pre-activation은 원 ResNet과 구분되는 후속 변형으로 비교한다. |
| MobileNetV2 | 모델 · Backbone | 중요 | **효율적인 연산:** depthwise와 pointwise convolution이 공간 처리와 채널 결합을 나누는 방식을 이해한다.<br>**블록 구조:** 채널 확장 → depthwise convolution → 선형 projection의 흐름과 residual 연결의 적용 조건을 추적한다.<br>**설계 이유:** inverted residual·linear bottleneck을 ResNet bottleneck과 비교하고, 좁은 출력에 비선형 활성화를 두지 않는 이유를 설명한다. |
| ConvNeXt | 모델 · Backbone | 중요 | **CNN 현대화:** ResNet에서 출발해 stage 구성·큰 kernel·depthwise convolution·normalization·activation이 바뀌는 과정을 살펴본다.<br>**설계 근거:** 구조 변경과 학습 레시피 변경을 구분하고, 단계별 ablation이 뒷받침하는 결론을 읽는다.<br>**비교:** CNN 구조 자체를 먼저 이해한 뒤, ViT·Swin의 블록 구성과 계층적 feature 처리에 연결한다. |
| U-Net | 모델 | 필수 | **Encoder–decoder:** 해상도를 줄이며 문맥을 얻는 경로와, 해상도를 높여 픽셀별 출력을 만드는 경로를 추적한다.<br>**Skip connection:** encoder feature를 decoder에 concatenation하는 이유와 채널·공간 크기 변화를 확인한다.<br>**해상도 정렬:** 원 논문의 up-convolution·crop을 확인하고, interpolation 등 후속 구현의 선택과 구분한다. |
| FPN | 구성 요소 · Neck | 필수 | **다중 해상도:** backbone의 여러 stage에서 나온 feature를 활용해 크기가 다른 대상을 다루는 이유를 이해한다.<br>**Feature fusion:** top-down upsampling과 lateral 1×1 convolution, addition 전 해상도·채널 정렬을 추적한다.<br>**Neck의 역할:** 각 pyramid level의 출력을 확인하고, U-Net의 concatenation과 FPN의 addition을 비교한다. |
| Faster R-CNN | 모델 | 필수 | **Two-stage 검출:** 공유 backbone → RPN의 proposal 생성 → RoIPool → 분류·box 보정의 흐름을 추적한다.<br>**학습 신호:** anchor·proposal의 정답 할당, objectness·class target, box regression target과 loss를 구분한다.<br>**학습과 추론:** proposal 선택·NMS와 두 단계의 역할을 확인하고, 원 논문의 학습 절차와 후속 구현을 구분한다. |
| Mask R-CNN | 모델 | 중요 | **Instance segmentation:** Faster R-CNN의 분류·box 예측에 병렬 mask branch를 더하는 구조를 이해한다.<br>**공간 정렬:** RoIPool의 좌표 양자화 문제와 RoIAlign의 bilinear sampling을 비교한다.<br>**Mask 학습:** RoI별 mask target·픽셀별 binary loss·추론 시 class 선택을 연결하고, 원 논문의 ablation으로 설계를 검토한다. |
| YOLO | 모델 | 중요 | **One-stage 검출:** 대표 버전 한 편을 정해 backbone·neck·head와 box·class 출력, 정답 할당과 loss를 추적한다.<br>**추론과 비용:** 선택한 버전의 후처리를 확인하고, Faster R-CNN과 예측 구조·속도·정확도를 비교한다.<br>**버전 구분:** anchor 사용 여부와 NMS 필요 여부는 버전별로 확인한다. 다른 버전의 전체 구조는 별도 심화로 다룬다. |

### 2. Transformer 구조와 활용 모델

#### 학습 목표

Attention·encoder·decoder와 이미지 토큰 구성을 이해하고, 이를 검출·dense prediction·prompt 기반 분할의 구조로 연결한다.

#### 학습 내용

| 모델 / 구조 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Transformer | 모델 구조 | 필수 | **Attention:** self/cross-attention의 Q·K·V shape, √d_k 스케일링, softmax 축, multi-head 결합과 토큰 수에 따른 계산 비용을 추적한다.<br>**전체 구조:** attention·FFN·residual·normalization이 encoder와 decoder에서 연결되는 방식과 causal mask를 설명한다.<br>**순서 정보:** sinusoidal positional encoding의 역할을 확인한다. 위치 정보와 순서 의존 mask가 없을 때 self-attention의 permutation equivariance를 이해한다. |
| GPT | 모델 | 중요 | **Decoder-only 구조:** 원 GPT의 causal self-attention과 next-token prediction을 입력·target·loss에 연결한다.<br>**학습과 활용:** 언어 모델 사전학습과 downstream fine-tuning을 구분하고, 학습의 병렬 계산과 생성의 순차 처리를 비교한다.<br>**후속 확장:** KV cache·RoPE는 원 GPT와 구분해 소개한다. 여러 세대의 GPT 전체 구조를 한 세션에 묶지 않는다. |
| BERT | 모델 | 중요 | **Encoder 구조:** 원 BERT의 양방향 self-attention과 token·segment·position embedding을 이해한다.<br>**사전학습 목표:** masked language modeling·next sentence prediction의 입력과 target을 확인하고, downstream fine-tuning의 head를 구분한다.<br>**GPT와 비교:** 정보를 볼 수 있는 범위, 학습 목표, 학습 시 입력 구성과 활용 방식의 차이를 설명한다. |
| ViT | 모델 · Backbone | 필수 | **이미지 토큰화:** 이미지를 patch로 나누고 Linear projection한 뒤, CLS token·learned positional embedding과 함께 encoder에 넣는 흐름을 추적한다.<br>**출력과 해상도:** 원 모델의 CLS 기반 분류와 해상도 변경 시 positional embedding 보간을 확인하고, pooling 등 readout 변형과 구분한다.<br>**CNN과 비교:** 국소 연결·계층 구조 등 inductive bias, receptive field, 데이터 규모와 사전학습의 영향을 비교한다. |
| Swin Transformer | 모델 · Backbone | 중요 | **국소 Attention:** window attention의 비용을 확인하고, shifted window가 이웃 window 사이의 정보를 연결하는 방식을 이해한다.<br>**계층 구조:** patch merging에 따른 해상도·채널 변화, relative position bias와 다중 해상도 출력을 추적한다.<br>**비교:** ViT의 전역 attention, CNN의 계층적 feature 구성과 비교해 dense prediction에 활용되는 이유를 설명한다. |
| DETR | 모델 | 필수 | **Set prediction:** CNN backbone과 Transformer encoder–decoder, learned object query가 고정 개수의 예측을 만드는 흐름을 이해한다.<br>**Matching과 loss:** Hungarian matching의 비용과, matching 후 계산하는 class·box loss 및 no-object 처리를 구분한다.<br>**추론 비교:** 원 DETR의 NMS 없는 출력을 확인하고, Faster R-CNN·선택한 YOLO 버전의 예측·정답 할당 방식과 비교한다. |
| DPT | 모델 | 필수 | **Dense prediction:** ViT 또는 hybrid backbone의 여러 층에서 얻은 토큰을 깊이·분할 출력에 활용하는 전체 흐름을 이해한다.<br>**Reassemble과 fusion:** 토큰을 공간 feature로 재배열하고 여러 해상도로 변환한 뒤, decoder에서 융합하는 과정을 추적한다.<br>**구조 비교:** vanilla ViT의 중간 층이 처음부터 해상도 pyramid인 것은 아님을 확인하고, Swin·FPN·U-Net과 비교한다. |
| SAM | 모델 | 중요 | **Promptable segmentation:** 원 SAM의 image encoder·prompt encoder·mask decoder가 이미지와 point·box·mask prompt를 결합하는 흐름을 이해한다.<br>**학습과 추론:** 학습 데이터·prompt sampling·mask loss, 모호한 prompt에 대한 복수 mask와 품질 예측, image embedding 재사용을 확인한다.<br>**후속 비교:** SAM 2의 streaming memory와 프레임별 prompt·mask 처리를 비교한다. 버전별 전체 구조·평가는 별도 심화로 다룬다. |

### 3. 표현 학습과 모델 적응

#### 학습 목표

표현을 얻는 학습 목표와 teacher·target의 역할을 이해하고, pretraining 모델을 활용·적응하는 방법을 구분한다.

#### 학습 내용

| 개념 / 모델 / 기법 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| Pretraining / Transfer Learning | 학습 방법 | 필수 | **학습 단계:** pretraining과 downstream task에서 데이터·target·head가 어떻게 달라지는지 구분한다.<br>**적응 범위:** frozen feature·linear probing·부분 및 전체 fine-tuning에서 고정·갱신하는 파라미터를 비교한다.<br>**실험 해석:** 사전학습 데이터와 학습 조건을 확인하고, 증강·regularization·평가 시 데이터 누수를 기초 원리와 연결한다. |
| SimCLR | 학습 방법 | 필수 | **학습 쌍:** 같은 이미지의 두 augmentation을 positive로, batch의 다른 이미지에서 얻은 view를 negative로 사용하는 구성을 이해한다.<br>**목표와 구조:** NT-Xent·temperature, encoder representation과 projection head 출력의 차이를 추적한다.<br>**비교와 주의:** 증강·batch 크기의 영향을 확인한다. 여기서 view는 증강한 이미지이며, 다른 카메라에서 촬영한 multi-view와 구분한다. |
| CLIP | 모델 | 필수 | **이미지–텍스트 정렬:** 두 encoder가 paired image·text를 공통 embedding 공간으로 보내는 흐름을 이해한다.<br>**학습 목표:** batch 내 정답 pair와 나머지 pair, 정규화된 embedding·temperature·양방향 contrastive loss를 연결한다.<br>**Zero-shot 추론:** class 이름을 prompt 문장으로 바꿔 text embedding을 만들고, image embedding과의 유사도로 분류하는 과정을 추적한다. |
| SigLIP | 모델 · 학습 방법 | 중요 | **Pairwise 목표:** image–text pair의 일치 여부를 sigmoid loss로 학습하는 방식을 이해한다.<br>**CLIP과 비교:** batch 전체 유사도의 softmax 정규화와 pairwise sigmoid의 차이, positive·negative pair 구성과 bias·scale을 확인한다.<br>**설계 근거:** batch 크기·pair 비율·학습 조건을 확인하며 원 논문의 ablation을 읽는다. |
| Knowledge distillation | 학습 방법 | 필수 | **Teacher와 student:** teacher의 soft target으로 student를 학습시키는 목적과 temperature의 역할을 이해한다.<br>**Loss와 gradient:** soft-target loss·hard-label loss의 결합, teacher 고정과 student 업데이트를 수식·코드로 추적한다.<br>**후속 비교:** 원 논문의 목표·실험을 기준으로 feature distillation, DINO의 self-distillation·EMA teacher와 차이를 연결한다. |
| DINO | 학습 방법 | 필수 | **원 DINO:** 같은 이미지의 서로 다른 crop에서 teacher·student의 출력 분포를 맞추는 self-distillation을 이해한다.<br>**학습 안정화:** multi-crop, EMA teacher·stop-gradient, centering·sharpening과 collapse 방지의 관계를 추적한다.<br>**후속 비교:** DINOv2의 image·patch-level 목표와 데이터·학습 레시피, DINOv3의 Gram anchoring을 비교한다. 버전별 전체 구조·목표는 별도 심화로 다룬다. |
| MAE | 학습 방법 | 필수 | **Masked reconstruction:** 일부 patch를 가리고, 보이는 patch만 encoder에 넣어 가린 영역의 픽셀을 복원하는 목표를 이해한다.<br>**비대칭 구조:** encoder 출력을 원래 위치에 놓고 mask token을 더해 작은 decoder로 보내는 과정과, masked 영역의 pixel 복원 loss를 추적한다.<br>**학습과 전이:** pretraining의 decoder와 downstream head를 구분하고, masking 비율·연산량·표현 학습의 관계를 살펴본다. |
| SimMIM | 학습 방법 | 중요 | **단순한 복원 목표:** 가린 위치를 mask token으로 대체한 입력에서 원래 RGB 값을 회귀하는 학습을 이해한다.<br>**구조와 loss:** encoder 뒤의 가벼운 prediction head, masked 영역의 L1 loss와 patch·mask 크기를 확인한다.<br>**MAE와 비교:** mask token의 encoder 통과 여부, decoder·head의 크기, pixel 복원 목표의 차이를 비교한다. |
| BEiT | 학습 방법 | 중요 | **Discrete target:** 별도로 사전학습한 visual tokenizer가 만든 discrete token을 가린 위치의 정답으로 사용하는 원 BEiT를 이해한다.<br>**학습 흐름:** mask token을 포함한 입력, Transformer·prediction head, token 분류 loss와 tokenizer의 역할을 구분한다.<br>**비교:** MAE·SimMIM의 pixel 회귀와 target·head의 차이를 비교한다. 후속 BEiT 버전의 전체 재현은 선택 심화로 둔다. |
| LoRA | 적응 방법 | 중요 | **Low-rank update:** 사전학습 가중치는 고정하고, 가중치 변화량을 두 작은 행렬의 곱으로 학습하는 원리를 이해한다.<br>**파라미터와 gradient:** 적용 위치·rank·scale, 두 행렬의 초기화와 gradient 흐름을 전체 fine-tuning과 비교한다.<br>**학습과 배포:** 가중치에 update를 합치는 조건과 비용을 확인하고, 원 논문의 ablation 및 PEFT 안에서의 역할을 살펴본다. |

---

### 4. 생성 모델

#### 학습 목표

생성 목표, latent 표현, 네트워크 구조와 sampling 과정을 연결해 이해한다.

#### 학습 내용

#### 4.1 VAE · GAN · Autoregressive · VQ

| 모델 / 방법 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| VAE | 생성 모델 | 필수 | **잠재변수 모델:** encoder가 근사 posterior를, decoder가 관측 데이터의 분포를 나타내는 구조를 이해한다.<br>**학습 목표:** ELBO의 reconstruction·KL 항, prior와 posterior, reparameterization을 통한 gradient 흐름을 연결한다.<br>**복원과 생성:** 입력을 encoding한 뒤 복원하는 과정과, prior에서 latent를 뽑아 새 샘플을 만드는 과정을 구분한다. |
| GAN | 생성 모델 | 중요 | **적대적 학습:** noise를 데이터로 바꾸는 generator와, 실제·생성 데이터를 구분하는 discriminator의 역할을 이해한다.<br>**두 모델의 갱신:** 원 minimax 목표와 generator의 non-saturating 목표를 구분하고, 번갈아 학습할 때의 gradient 흐름을 추적한다.<br>**학습과 추론:** 불안정성·mode collapse의 의미를 살펴보고, 생성 시에는 generator를 사용하는 흐름을 확인한다. |
| Autoregressive Models | 생성 모델 | 중요 | **순차 확률 분해:** 앞선 픽셀·토큰을 조건으로 다음 값을 예측하며 이미지의 확률을 구성하는 원리를 이해한다.<br>**대표 모델:** PixelCNN의 masked convolution·학습 target을 확인하고, 정답 문맥을 쓰는 학습과 생성 문맥을 쓰는 순차 sampling을 비교한다.<br>**확장과 비용:** 순차 추론의 비용을 확인하고, pixel 공간에서 latent token 공간으로 옮기는 연결을 VQ-VAE·VQGAN에서 살펴본다. |
| VQ-VAE | 생성 모델 | 중요 | **이산 latent:** encoder 출력을 codebook의 가까운 벡터로 치환해 decoder에 전달하는 vector quantization을 이해한다.<br>**학습과 gradient:** reconstruction·codebook·commitment loss, stop-gradient와 straight-through 추정의 역할을 추적한다.<br>**생성의 두 단계:** autoencoder 학습과 code index의 prior 학습을 구분한다. 생성 시 prior → codebook → decoder의 흐름을 연속 latent VAE와 비교한다. |
| VQGAN | 생성 모델 | 중요 | **Tokenizer 학습:** encoder·codebook·decoder와 discriminator를 확인하고, reconstruction·perceptual·adversarial 목표의 역할을 구분한다.<br>**Prior 학습:** tokenizer를 학습한 뒤, 이미지 code의 배열을 예측하는 autoregressive Transformer를 별도로 학습하는 두 단계를 추적한다.<br>**생성과 비교:** token sampling → codebook → decoder의 흐름을 확인하고, VQ-VAE와 구조·목표·이미지 표현을 비교한다. |

#### 4.2 Diffusion · Flow Matching

| 모델 / 방법 | 유형 | 등급 | 깊게 봐야 할 포인트 |
|---|---|---|---|
| DDPM | 생성 모델 | 필수 | **Noising과 denoising:** forward에서 noise를 더하는 과정과, 학습한 역방향 전이로 noise에서 이미지를 생성하는 과정을 구분한다.<br>**학습 목표:** 임의의 timestep에서 noisy 입력을 만들고 ε를 예측하는 목표, noise schedule과 시간 조건을 수식·코드로 연결한다.<br>**Sampling:** ε 예측으로 역방향 평균을 계산하고 noise를 주입하는 반복 절차를 추적한다. 학습에 쓰는 정답 이미지와 생성 시 입력을 구분한다. |
| DDIM | 생성 방법 | 필수 | **학습과 sampling 분리:** DDPM의 ε-prediction 목표로 학습한 denoiser를 활용하면서 sampling 갱신식을 바꾸는 방법을 이해한다.<br>**갱신식과 경로:** 현재 noisy sample → 원본 추정 → 다음 sample의 계산과, η가 추가 noise를 조절하는 역할을 추적한다.<br>**속도와 결과:** 같은 초기 noise에서 η=0일 때의 결정적 sampling을 확인하고, timestep 부분집합·sampling 단계 수에 따른 비용과 품질을 비교한다. |
| Score-based Generative Models | 생성 모델 | 필수 | **Score의 의미:** noise가 섞인 데이터 분포의 log-density를 입력으로 미분한 gradient를 학습한다는 관점을 이해한다.<br>**원 방법:** noise-conditioned score network와 denoising score matching, 여러 noise 수준을 거치는 annealed Langevin sampling을 추적한다.<br>**Diffusion과 연결:** Gaussian perturbation에서 score와 ε-prediction의 관계를 확인한다. SDE·probability flow ODE 정식화는 후속 심화로 구분한다. |
| Latent Diffusion | 생성 모델 | 필수 | **학습 단계:** 먼저 학습한 autoencoder로 이미지를 압축한 뒤, latent 공간에서 denoiser를 학습하는 두 단계를 구분한다.<br>**조건과 생성:** condition·cross-attention·classifier-free guidance의 역할과 noise latent → denoising → 이미지 decoder의 흐름을 추적한다.<br>**Autoencoder 비교:** KL·VQ regularization 및 perceptual·adversarial reconstruction을 VAE·VQGAN과 연결한다. Stable Diffusion은 후속 활용으로 살펴본다. |
| ControlNet | 모델 · 조건 제어 | 중요 | **공간 조건:** edge·depth·pose 등의 조건을 사전학습 text-to-image diffusion 모델에 추가하는 구조를 이해한다.<br>**학습 구조:** 고정된 backbone, trainable branch와 zero-initialized convolution이 연결되는 위치와 gradient 흐름을 추적한다.<br>**설계 이유:** 초기에는 원 모델의 출력을 유지하며 조건 제어를 학습하는 원리와, 추론 시 조건의 영향을 확인한다. |
| DiT | 모델 · Denoiser | 필수 | **Transformer denoiser:** 원 DiT에서 autoencoder latent를 patch token으로 바꿔 Transformer로 처리하는 흐름을 이해한다.<br>**조건 주입:** timestep·class embedding, adaLN-Zero와 출력 head를 추적하고, ε와 역방향 분산을 예측하는 원 모델을 확인한다.<br>**구조 비교:** U-Net denoiser와 비교하고, latent patch 크기·모델 규모·계산량을 바꾼 ablation으로 설계를 검토한다. |
| Flow Matching | 생성 방법 | 필수 | **Probability path:** noise 분포와 data 분포를 잇는 경로를 정하고, 그 분포의 변화를 만드는 시간 의존 velocity field를 학습하는 관점을 이해한다.<br>**학습과 생성:** conditional path에서 만든 velocity target의 회귀와, 학습한 field를 ODE로 적분하는 sampling을 구분한다.<br>**비교와 연결:** 경로 선택과 학습 target을 DDPM의 noise 예측과 비교하고, 다음 Rectified Flow의 직선 보간 목표에 연결한다. |
| Rectified Flow | 생성 방법 | 필수 | **직선 보간 학습:** noise–data pair를 잇는 직선 위에서 두 끝점의 차이를 velocity target으로 회귀하는 방법을 이해한다.<br>**실제 생성 경로:** 학습에 쓴 직선 보간과, 학습한 field를 적분해 얻는 ODE 경로가 항상 같거나 직선인 것은 아님을 구분한다.<br>**Coupling과 reflow:** 생성한 pair로 다시 학습하는 reflow, 경로의 직선성·sampling 단계 수의 관계를 확인하고 Flow Matching과 비교한다. |
| Video Diffusion | 생성 모델 | 중요 | **시간 축 확장:** 대표 논문 한 편을 정해 video tensor·조건 입력·학습 target과 생성 과정을 추적한다.<br>**공간·시간 처리:** spatial·temporal 연산 또는 attention이 프레임 내부와 프레임 사이 정보를 결합하는 방식을 이해한다.<br>**평가와 범위:** 이미지 품질과 시간적 일관성을 구분해 평가한다. 다른 영상 모델의 구조·조건 방식은 후속 비교로 다룬다. |

